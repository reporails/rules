#!/usr/bin/env python3
"""Contributor test harness for reporails rules.

Discovers rules, runs their checks against test fixtures, reports pass/fail.
Does NOT compute scores, levels, or invoke LLMs.
"""

import argparse
import json
import os
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

import frontmatter
import yaml

from checks import MECHANICAL_CHECKS, CheckResult


@dataclass
class RuleInfo:
    id: str
    slug: str
    title: str
    category: str
    rule_type: str
    level: str
    targets: str
    checks: list
    rule_dir: Path
    rule_yml: Path

    @property
    def has_checks(self) -> bool:
        return len(self.checks) > 0

    @property
    def has_pass_fixture(self) -> bool:
        return (self.rule_dir / "tests" / "pass").is_dir() and any(
            (self.rule_dir / "tests" / "pass").iterdir()
        )

    @property
    def has_fail_fixture(self) -> bool:
        return (self.rule_dir / "tests" / "fail").is_dir() and any(
            (self.rule_dir / "tests" / "fail").iterdir()
        )


@dataclass
class CheckRun:
    check_id: str
    check_type: str
    fixture: str  # "pass" or "fail"
    passed: bool
    message: str


@dataclass
class RuleResult:
    rule: RuleInfo
    status: str  # "passed", "failed", "not_implemented", "no_fixtures", "skipped"
    check_runs: list = field(default_factory=list)
    messages: list = field(default_factory=list)


def load_agent_config(rules_root: Path, agent: str) -> tuple[dict, list]:
    """Load agent config and build template var map.
    
    Returns:
        (vars_dict, excludes_list)
    """
    config_path = rules_root / "agents" / agent / "config.yml"
    if not config_path.exists():
        print(f"Warning: agent config not found: {config_path}", file=sys.stderr)
        return {}, []
    with open(config_path) as f:
        config = yaml.safe_load(f)
    return config.get("vars", {}), config.get("excludes", [])


def resolve_var(template: str, agent_vars: dict) -> list[str]:
    """Resolve a template variable like {{instruction_files}} to its values."""
    if not template.startswith("{{") or not template.endswith("}}"):
        return [template]
    var_name = template[2:-2]
    value = agent_vars.get(var_name, template)
    if isinstance(value, list):
        return value
    return [value]


def rule_matches_exclude(rule_id: str, exclude_patterns: list[str]) -> bool:
    """Check if a rule ID matches any exclude pattern.
    
    Patterns support:
    - Exact match: "CORE:S:0010"
    - Wildcard: "CLAUDE:*" (all CLAUDE rules)
    - Namespace wildcard: "NAMESPACE:*"
    """
    for pattern in exclude_patterns:
        if pattern == rule_id:
            return True
        if pattern.endswith(":*"):
            prefix = pattern[:-1]  # Remove trailing *
            if rule_id.startswith(prefix):
                return True
    return False


def _scan_root(root: Path) -> list[Path]:
    """Find all rule directories under a single root (core/ + agents/*/rules/)."""
    dirs = []

    core_dir = root / "core"
    if core_dir.exists():
        for category_dir in sorted(core_dir.iterdir()):
            if category_dir.is_dir():
                for slug_dir in sorted(category_dir.iterdir()):
                    if slug_dir.is_dir():
                        dirs.append(slug_dir)

    agents_dir = root / "agents"
    if agents_dir.exists():
        for agent_dir in sorted(agents_dir.iterdir()):
            rules_subdir = agent_dir / "rules"
            if rules_subdir.is_dir():
                for slug_dir in sorted(rules_subdir.iterdir()):
                    if slug_dir.is_dir():
                        dirs.append(slug_dir)

    return dirs


def discover_rules(rules_root: Path, filter_path: str = None, filter_rule: str = None,
                   package_roots: list[Path] = None, excludes: list[str] = None) -> list[RuleInfo]:
    """Walk core/ and agents/*/rules/ for rule.md files across all roots.
    
    Args:
        rules_root: Primary rules repository root
        filter_path: Optional path prefix filter
        filter_rule: Optional rule ID filter
        package_roots: Additional package roots to scan
        excludes: List of rule ID patterns to exclude (supports wildcards)
    """
    rules = []
    excludes = excludes or []

    # Build (root, slug_dir) pairs from primary root + any package roots
    all_roots = [rules_root] + (package_roots or [])
    search_pairs = []
    for root in all_roots:
        for slug_dir in _scan_root(root):
            search_pairs.append((root, slug_dir))

    for root, slug_dir in search_pairs:
        rule_md = slug_dir / "rule.md"
        rule_yml = slug_dir / "rule.yml"
        if not rule_md.exists():
            continue

        # Apply path filter (relative to the owning root)
        if filter_path:
            rel = str(slug_dir.relative_to(root))
            if not rel.startswith(filter_path.rstrip("/")):
                continue

        post = frontmatter.load(str(rule_md))
        meta = post.metadata

        rule_id = meta.get("id", "")

        # Apply rule ID filter
        if filter_rule and rule_id != filter_rule:
            continue
        
        # Apply excludes from agent config
        if rule_matches_exclude(rule_id, excludes):
            continue

        rules.append(RuleInfo(
            id=rule_id,
            slug=meta.get("slug", ""),
            title=meta.get("title", ""),
            category=meta.get("category", ""),
            rule_type=meta.get("type", ""),
            level=meta.get("level", ""),
            targets=meta.get("targets", ""),
            checks=meta.get("checks", []),
            rule_dir=slug_dir,
            rule_yml=rule_yml,
        ))

    return rules


def run_mechanical_check(check: dict, fixture_root: Path, agent_vars: dict) -> CheckResult:
    """Run a single mechanical check against a fixture directory."""
    check_name = check.get("check", "")
    args = check.get("args", {})

    if check_name not in MECHANICAL_CHECKS:
        return CheckResult(passed=False, message=f"Unknown mechanical check: {check_name}")

    result = MECHANICAL_CHECKS[check_name](fixture_root, args, agent_vars)
    if args.get("negate"):
        result = CheckResult(passed=not result.passed, message=result.message)
    return result


def _resolve_vars_in_rule(rule: dict, agent_vars: dict) -> dict:
    """Recursively resolve {{var}} placeholders in an OpenGrep rule dict."""
    import copy
    rule = copy.deepcopy(rule)

    def resolve(value):
        if isinstance(value, str):
            for key, val in agent_vars.items():
                placeholder = "{{" + key + "}}"
                if placeholder in value:
                    # If the entire string is a placeholder and val is a list,
                    # return the list (for paths.include expansion)
                    if value == placeholder and isinstance(val, list):
                        return val
                    if isinstance(val, list):
                        value = value.replace(placeholder, val[0] if val else "")
                    else:
                        value = value.replace(placeholder, str(val))
            return value
        if isinstance(value, list):
            expanded = []
            for item in value:
                resolved = resolve(item)
                if isinstance(resolved, list):
                    expanded.extend(resolved)
                else:
                    expanded.append(resolved)
            return expanded
        if isinstance(value, dict):
            return {k: resolve(v) for k, v in value.items()}
        return value

    return resolve(rule)


def run_opengrep_check(rule_yml: Path, fixture_root: Path, check: dict, verbose: bool = False, agent_vars: dict = None) -> CheckResult:
    """Run OpenGrep against a fixture directory for a deterministic check."""
    if not rule_yml.exists():
        return CheckResult(passed=False, message=f"rule.yml not found: {rule_yml}")

    with open(rule_yml) as f:
        yml_content = yaml.safe_load(f)

    yml_rules = yml_content.get("rules", [])
    if not yml_rules:
        return CheckResult(passed=False, message="rule.yml has no patterns (rules: [])")

    # Find the matching rule entry by check ID
    # rule.md uses colon format (CORE:S:0001:check:0001)
    # rule.yml uses dot format (CORE.S.0001.check.0001) for OpenGrep compatibility
    check_id = check.get("id", "")
    check_id_dotted = check_id.replace(":", ".")
    matching_rule = None
    for r in yml_rules:
        if r.get("id") == check_id_dotted:
            matching_rule = r
            break

    # If no exact match, use first rule (single-pattern rules)
    if matching_rule is None and len(yml_rules) == 1:
        matching_rule = yml_rules[0]

    if matching_rule is None:
        return CheckResult(
            passed=False,
            message=f"No OpenGrep pattern found for check {check_id} in rule.yml",
        )

    # Resolve template variables in the rule
    if agent_vars:
        matching_rule = _resolve_vars_in_rule(matching_rule, agent_vars)

    # Write a temp rule file with just this pattern
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as tmp:
        yaml.dump({"rules": [matching_rule]}, tmp)
        tmp_path = tmp.name

    try:
        result = subprocess.run(
            ["opengrep", "scan", "--config", tmp_path, "--json", str(fixture_root)],
            capture_output=True,
            text=True,
            timeout=30,
        )

        if verbose:
            print(f"    opengrep stdout: {result.stdout[:500]}", file=sys.stderr)
            if result.stderr:
                print(f"    opengrep stderr: {result.stderr[:500]}", file=sys.stderr)

        # Parse JSON output for findings
        try:
            output = json.loads(result.stdout) if result.stdout.strip() else {}
        except json.JSONDecodeError:
            # opengrep may output non-JSON on error
            if result.returncode != 0:
                return CheckResult(
                    passed=False,
                    message=f"OpenGrep error (exit {result.returncode}): {result.stderr[:200]}",
                )
            output = {}

        findings = output.get("results", [])
        return CheckResult(
            passed=True,
            message=f"{len(findings)} finding(s)",
            findings_count=len(findings),
        )
    except FileNotFoundError:
        return CheckResult(passed=False, message="opengrep not found — run inside Docker")
    except subprocess.TimeoutExpired:
        return CheckResult(passed=False, message="OpenGrep timed out (30s)")
    finally:
        os.unlink(tmp_path)


def run_rule(rule: RuleInfo, agent_vars: dict, verbose: bool = False) -> RuleResult:
    """Run all checks for a rule against its fixtures."""
    result = RuleResult(rule=rule, status="passed")

    if not rule.has_checks:
        result.status = "not_implemented"
        result.messages.append("checks: [] — not implemented")
        return result

    if not rule.has_pass_fixture and not rule.has_fail_fixture:
        result.status = "no_fixtures"
        result.messages.append("No test fixtures (tests/pass/ or tests/fail/ empty)")
        return result

    pass_dir = rule.rule_dir / "tests" / "pass"
    fail_dir = rule.rule_dir / "tests" / "fail"

    # Track whether at least one check detects a violation on the fail fixture.
    # Multi-check rules may have some checks pass and others fail on the fail
    # fixture — that's expected. Only require at least one violation detected.
    fail_violation_found = False

    for check in rule.checks:
        check_id = check.get("id", "unknown")
        check_type = check.get("type", "unknown")
        negate = check.get("negate", False)

        # === Pass fixture: ALL checks must pass (no violations) ===
        if rule.has_pass_fixture:
            if check_type == "mechanical":
                cr = run_mechanical_check(check, pass_dir, agent_vars)
                passed = cr.passed
                run = CheckRun(check_id, check_type, "pass", passed, cr.message)
            elif check_type == "deterministic":
                cr = run_opengrep_check(rule.rule_yml, pass_dir, check, verbose, agent_vars)
                if negate:
                    # Negated: findings = desired content exists = pass
                    passed = cr.passed and cr.findings_count > 0
                else:
                    # Normal: 0 findings = no violations = pass
                    passed = cr.passed and cr.findings_count == 0
                run = CheckRun(check_id, check_type, "pass", passed, cr.message)
            elif check_type == "semantic":
                # Semantic checks: only validate that pre-checks ran
                run = CheckRun(check_id, check_type, "pass", True, "semantic — skipped (no LLM)")
                passed = True
            else:
                run = CheckRun(check_id, check_type, "pass", False, f"unknown check type: {check_type}")
                passed = False

            result.check_runs.append(run)
            if not passed:
                result.status = "failed"

        # === Fail fixture: at least ONE check must detect a violation ===
        if rule.has_fail_fixture:
            if check_type == "mechanical":
                cr = run_mechanical_check(check, fail_dir, agent_vars)
                violation = not cr.passed
                msg = cr.message
                run = CheckRun(check_id, check_type, "fail", True, msg)
            elif check_type == "deterministic":
                cr = run_opengrep_check(rule.rule_yml, fail_dir, check, verbose, agent_vars)
                if negate:
                    # Negated: 0 findings = desired content missing = violation
                    violation = cr.passed and cr.findings_count == 0
                    msg = cr.message
                else:
                    # Normal: 1+ findings = violations found
                    violation = cr.passed and cr.findings_count > 0
                    msg = cr.message
                run = CheckRun(check_id, check_type, "fail", True, msg)
            elif check_type == "semantic":
                run = CheckRun(check_id, check_type, "fail", True, "semantic — skipped (no LLM)")
                violation = False
            else:
                run = CheckRun(check_id, check_type, "fail", False, f"unknown check type: {check_type}")
                violation = False

            if violation:
                fail_violation_found = True
            result.check_runs.append(run)

    # After all checks: fail fixture must have triggered at least one violation
    if rule.has_fail_fixture and not fail_violation_found:
        result.status = "failed"
        result.messages.append("Fail fixture: no check detected a violation")

    return result


def print_results(results: list[RuleResult], verbose: bool = False):
    """Print test results summary."""
    passed = [r for r in results if r.status == "passed"]
    failed = [r for r in results if r.status == "failed"]
    not_impl = [r for r in results if r.status == "not_implemented"]
    no_fix = [r for r in results if r.status == "no_fixtures"]
    skipped = [r for r in results if r.status == "skipped"]

    print()
    print("=" * 60)
    print("REPORAILS RULE TEST RESULTS")
    print("=" * 60)
    print()

    # Print failures first
    if failed:
        print("FAILURES:")
        print("-" * 40)
        for r in failed:
            print(f"  FAIL  {r.rule.id} ({r.rule.slug})")
            for run in r.check_runs:
                status = "PASS" if run.passed else "FAIL"
                print(f"        [{status}] {run.check_id} ({run.check_type}, {run.fixture} fixture): {run.message}")
        print()

    # Print passes
    if passed and verbose:
        print("PASSES:")
        print("-" * 40)
        for r in passed:
            print(f"  PASS  {r.rule.id} ({r.rule.slug})")
            for run in r.check_runs:
                print(f"        [PASS] {run.check_id} ({run.check_type}, {run.fixture} fixture): {run.message}")
        print()

    # Summary
    print("SUMMARY:")
    print("-" * 40)
    print(f"  Passed:          {len(passed)}")
    print(f"  Failed:          {len(failed)}")
    print(f"  Not implemented: {len(not_impl)}")
    print(f"  No fixtures:     {len(no_fix)}")
    if skipped:
        print(f"  Skipped:         {len(skipped)}")
    print(f"  Total:           {len(results)}")
    print()

    if not_impl:
        print(f"Not implemented ({len(not_impl)}):")
        for r in not_impl:
            print(f"  - {r.rule.id} {r.rule.slug}")
        print()

    return len(failed)


def main():
    parser = argparse.ArgumentParser(
        description="Test harness for reporails rules",
        epilog="Examples:\n"
               "  python test-runner.py                     # All rules\n"
               "  python test-runner.py core/structure/     # One category\n"
               "  python test-runner.py --rule CORE:S:0001  # One rule by coordinate\n"
               "  python test-runner.py --agent codex       # Use codex vars\n"
               "  python test-runner.py --verbose           # Show OpenGrep output\n",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("path", nargs="?", default=None, help="Filter by path prefix (e.g., core/structure/)")
    parser.add_argument("--rule", "-r", default=None, help="Filter by rule coordinate (e.g., CORE:S:0001)")
    parser.add_argument("--agent", "-a", default="claude", help="Agent config for var resolution (default: claude)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show detailed output")
    parser.add_argument("--rules-root", default=".", help="Path to rules repo root (default: .)")
    parser.add_argument("--package", "-p", action="append", default=[], help="Additional package root(s) to scan (e.g., /recommended)")

    args = parser.parse_args()
    rules_root = Path(args.rules_root).resolve()
    package_roots = [Path(p).resolve() for p in args.package]

    # Load agent config (always from primary rules root)
    agent_vars, excludes = load_agent_config(rules_root, args.agent)
    if args.verbose:
        print(f"Agent: {args.agent}", file=sys.stderr)
        print(f"Vars: {agent_vars}", file=sys.stderr)
        if excludes:
            print(f"Excludes: {excludes}", file=sys.stderr)
        if package_roots:
            print(f"Packages: {[str(p) for p in package_roots]}", file=sys.stderr)

    # Discover rules
    rules = discover_rules(rules_root, filter_path=args.path, filter_rule=args.rule,
                           package_roots=package_roots, excludes=excludes)
    if not rules:
        print("No rules found.", file=sys.stderr)
        sys.exit(1)

    print(f"Discovered {len(rules)} rule(s)")

    # Run checks
    results = []
    for rule in rules:
        result = run_rule(rule, agent_vars, verbose=args.verbose)
        results.append(result)

        # Progress indicator
        icon = {"passed": ".", "failed": "F", "not_implemented": "-", "no_fixtures": "?", "skipped": "S"}
        print(icon.get(result.status, "?"), end="", flush=True)

    # Print results
    fail_count = print_results(results, verbose=args.verbose)
    sys.exit(1 if fail_count > 0 else 0)


if __name__ == "__main__":
    main()
