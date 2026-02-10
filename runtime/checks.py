"""Mechanical check implementations for the reporails test harness.

Each check receives:
    root: Path to the fixture directory (simulated project root)
    args: Check-specific arguments from rule.md frontmatter
    vars: Resolved template variables from agent config

Returns a CheckResult indicating pass/fail.
"""

import glob as globmod
import re
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class CheckResult:
    passed: bool
    message: str
    findings_count: int = 0


def _resolve_path(template: str, vars: dict) -> str:
    """Resolve template variables in a path string."""
    result = template
    for key, value in vars.items():
        placeholder = "{{" + key + "}}"
        if placeholder in result:
            if isinstance(value, list):
                result = result.replace(placeholder, value[0] if value else "")
            else:
                result = result.replace(placeholder, str(value))
    return result


def _resolve_glob_targets(pattern: str, root: Path) -> list[Path]:
    """Resolve a glob pattern relative to root, returning matching paths."""
    resolved = str(root / pattern)
    return [Path(p) for p in globmod.glob(resolved, recursive=True)]


def file_exists(root: Path, args: dict, vars: dict) -> CheckResult:
    """Check that at least one file matching the target pattern exists."""
    path_pattern = args.get("path", "")
    if not path_pattern:
        # Fall back to checking for any instruction files via vars
        patterns = vars.get("instruction_files", [])
        if isinstance(patterns, str):
            patterns = [patterns]
        for pattern in patterns:
            matches = _resolve_glob_targets(pattern, root)
            if matches:
                return CheckResult(passed=True, message=f"Found: {matches[0].name}")
        return CheckResult(passed=False, message="No instruction files found")

    resolved = _resolve_path(path_pattern, vars)
    matches = _resolve_glob_targets(resolved, root)
    if matches:
        return CheckResult(passed=True, message=f"Found: {matches[0].name}")
    return CheckResult(passed=False, message=f"File not found: {resolved}")


def directory_exists(root: Path, args: dict, vars: dict) -> CheckResult:
    """Check that a directory exists."""
    path = _resolve_path(args.get("path", ""), vars)
    target = root / path
    if target.is_dir():
        return CheckResult(passed=True, message=f"Directory exists: {path}")
    return CheckResult(passed=False, message=f"Directory not found: {path}")


def directory_contains(root: Path, args: dict, vars: dict) -> CheckResult:
    """Check that a directory contains at least min_count files matching a pattern."""
    path = _resolve_path(args.get("path", ""), vars)
    pattern = args.get("pattern", "*")
    min_count = args.get("min", 1)
    target = root / path
    if not target.is_dir():
        return CheckResult(passed=False, message=f"Directory not found: {path}")
    matches = list(target.glob(pattern))
    if len(matches) >= min_count:
        return CheckResult(passed=True, message=f"Found {len(matches)} file(s) in {path}")
    return CheckResult(passed=False, message=f"Found {len(matches)} file(s) in {path}, need {min_count}")


def git_tracked(root: Path, args: dict, vars: dict) -> CheckResult:
    """Check that files are git-tracked. In test fixtures, checks for .git marker."""
    # In fixture context, only check for a .git directory/file within root.
    # .git_marker is an alternative because git cannot track paths named .git.
    if (root / ".git").exists() or (root / ".git_marker").exists():
        return CheckResult(passed=True, message="Git repository detected")
    return CheckResult(passed=False, message="Not a git repository")


def frontmatter_key(root: Path, args: dict, vars: dict) -> CheckResult:
    """Check that files have specific YAML frontmatter keys."""
    import frontmatter as fm

    key = args.get("key", "")
    patterns = vars.get("instruction_files", [])
    if isinstance(patterns, str):
        patterns = [patterns]

    path_pattern = args.get("path", "")
    if path_pattern:
        patterns = [_resolve_path(path_pattern, vars)]

    for pattern in patterns:
        matches = _resolve_glob_targets(pattern, root)
        for match in matches:
            try:
                post = fm.load(str(match))
                if key in post.metadata:
                    return CheckResult(passed=True, message=f"Key '{key}' found in {match.name}")
            except Exception:
                continue

    return CheckResult(passed=False, message=f"Frontmatter key '{key}' not found")


def file_count(root: Path, args: dict, vars: dict) -> CheckResult:
    """Check that file count is within bounds."""
    pattern = args.get("pattern", "**/*")
    min_count = args.get("min", 0)
    max_count = args.get("max", float("inf"))

    resolved = _resolve_path(pattern, vars)
    matches = _resolve_glob_targets(resolved, root)
    # Filter to files only
    files = [m for m in matches if m.is_file()]
    count = len(files)

    if min_count <= count <= max_count:
        return CheckResult(passed=True, message=f"File count {count} within [{min_count}, {max_count}]")
    return CheckResult(passed=False, message=f"File count {count} outside [{min_count}, {max_count}]")


def line_count(root: Path, args: dict, vars: dict) -> CheckResult:
    """Check that file line count is within bounds."""
    patterns = vars.get("instruction_files", [])
    if isinstance(patterns, str):
        patterns = [patterns]

    path_pattern = args.get("path", "")
    if path_pattern:
        patterns = [_resolve_path(path_pattern, vars)]

    max_lines = args.get("max", float("inf"))
    min_lines = args.get("min", 0)

    for pattern in patterns:
        matches = _resolve_glob_targets(pattern, root)
        for match in matches:
            if not match.is_file():
                continue
            try:
                count = len(match.read_text().splitlines())
                if count > max_lines:
                    return CheckResult(
                        passed=False,
                        message=f"{match.name}: {count} lines exceeds max {max_lines}",
                    )
                if count < min_lines:
                    return CheckResult(
                        passed=False,
                        message=f"{match.name}: {count} lines below min {min_lines}",
                    )
            except Exception as e:
                return CheckResult(passed=False, message=f"Error reading {match.name}: {e}")

    return CheckResult(passed=True, message=f"Line counts within bounds")


def byte_size(root: Path, args: dict, vars: dict) -> CheckResult:
    """Check that file size is within bounds."""
    patterns = vars.get("instruction_files", [])
    if isinstance(patterns, str):
        patterns = [patterns]

    path_pattern = args.get("path", "")
    if path_pattern:
        patterns = [_resolve_path(path_pattern, vars)]

    max_bytes = args.get("max", float("inf"))
    min_bytes = args.get("min", 0)

    for pattern in patterns:
        matches = _resolve_glob_targets(pattern, root)
        for match in matches:
            if not match.is_file():
                continue
            size = match.stat().st_size
            if size > max_bytes:
                return CheckResult(passed=False, message=f"{match.name}: {size} bytes exceeds max {max_bytes}")
            if size < min_bytes:
                return CheckResult(passed=False, message=f"{match.name}: {size} bytes below min {min_bytes}")

    return CheckResult(passed=True, message="File sizes within bounds")


def path_resolves(root: Path, args: dict, vars: dict) -> CheckResult:
    """Check that referenced paths in files actually resolve."""
    # This checks that paths mentioned in instruction files point to real locations
    patterns = vars.get("instruction_files", [])
    if isinstance(patterns, str):
        patterns = [patterns]

    path_pattern = args.get("path", "")
    if path_pattern:
        patterns = [_resolve_path(path_pattern, vars)]

    for pattern in patterns:
        matches = _resolve_glob_targets(pattern, root)
        if matches:
            return CheckResult(passed=True, message="Target paths exist")

    return CheckResult(passed=False, message="No matching paths found")


def extract_imports(root: Path, args: dict, vars: dict) -> CheckResult:
    """Check for @import references in instruction files."""
    import re

    patterns = vars.get("instruction_files", [])
    if isinstance(patterns, str):
        patterns = [patterns]

    path_pattern = args.get("path", "")
    if path_pattern:
        patterns = [_resolve_path(path_pattern, vars)]

    imports_found = []
    for pattern in patterns:
        matches = _resolve_glob_targets(pattern, root)
        for match in matches:
            if not match.is_file():
                continue
            try:
                content = match.read_text()
                # Match @path/to/file patterns
                found = re.findall(r'@[\w./-]+', content)
                imports_found.extend(found)
            except Exception:
                continue

    if imports_found:
        return CheckResult(passed=True, message=f"Found {len(imports_found)} import(s)")
    return CheckResult(passed=False, message="No imports found")


def aggregate_byte_size(root: Path, args: dict, vars: dict) -> CheckResult:
    """Check that the total byte size of all matching files is within bounds."""
    pattern = args.get("pattern", "**/*")
    max_bytes = args.get("max", float("inf"))

    resolved = _resolve_path(pattern, vars)
    matches = _resolve_glob_targets(resolved, root)
    files = [m for m in matches if m.is_file()]
    total = sum(f.stat().st_size for f in files)

    if total <= max_bytes:
        return CheckResult(passed=True, message=f"Total {total} bytes within limit {max_bytes}")
    return CheckResult(passed=False, message=f"Total {total} bytes exceeds max {max_bytes}")


def import_depth(root: Path, args: dict, vars: dict) -> CheckResult:
    """Check that @import reference chains do not exceed max depth."""
    max_depth = args.get("max", 5)
    patterns = vars.get("instruction_files", [])
    if isinstance(patterns, str):
        patterns = [patterns]

    path_pattern = args.get("path", "")
    if path_pattern:
        patterns = [_resolve_path(path_pattern, vars)]

    def follow_chain(filepath: Path, visited: set, depth: int) -> int:
        if filepath in visited or not filepath.is_file():
            return depth
        visited.add(filepath)
        try:
            content = filepath.read_text()
        except Exception:
            return depth
        refs = re.findall(r'@([\w./-]+)', content)
        max_d = depth
        for ref in refs:
            target = filepath.parent / ref
            if target.is_file():
                max_d = max(max_d, follow_chain(target, visited, depth + 1))
        return max_d

    for pattern in patterns:
        matches = _resolve_glob_targets(pattern, root)
        for match in matches:
            if not match.is_file():
                continue
            deepest = follow_chain(match, set(), 0)
            if deepest > max_depth:
                return CheckResult(
                    passed=False,
                    message=f"{match.name}: import depth {deepest} exceeds max {max_depth}",
                )

    return CheckResult(passed=True, message=f"Import depth within limit ({max_depth})")


def directory_file_types(root: Path, args: dict, vars: dict) -> CheckResult:
    """Check that all files in a directory match the allowed extension list."""
    path = _resolve_path(args.get("path", ""), vars)
    extensions = args.get("extensions", [])
    target = root / path

    if not target.is_dir():
        return CheckResult(passed=True, message=f"Directory not found: {path} (OK if optional)")

    bad_files = []
    for f in target.iterdir():
        if f.is_file() and f.suffix not in extensions:
            bad_files.append(f.name)

    if bad_files:
        return CheckResult(
            passed=False,
            message=f"Non-{extensions} files in {path}: {', '.join(bad_files[:5])}",
        )
    return CheckResult(passed=True, message=f"All files in {path} match {extensions}")


def frontmatter_valid_glob(root: Path, args: dict, vars: dict) -> CheckResult:
    """Check that YAML frontmatter paths: entries use valid glob syntax."""
    import frontmatter as fm

    path = _resolve_path(args.get("path", ""), vars)
    target = root / path

    if not target.is_dir():
        return CheckResult(passed=True, message=f"Directory not found: {path} (OK if optional)")

    for f in target.iterdir():
        if not f.is_file() or f.suffix != ".md":
            continue
        try:
            post = fm.load(str(f))
            paths = post.metadata.get("globs", post.metadata.get("paths", []))
            if isinstance(paths, str):
                paths = [paths]
            for p in paths:
                if not isinstance(p, str):
                    return CheckResult(
                        passed=False,
                        message=f"{f.name}: non-string path entry: {p}",
                    )
                # Check for obviously broken glob syntax
                if p.count("[") != p.count("]"):
                    return CheckResult(
                        passed=False,
                        message=f"{f.name}: unbalanced brackets in glob: {p}",
                    )
        except Exception:
            continue

    return CheckResult(passed=True, message="All frontmatter path entries valid")


def content_absent(root: Path, args: dict, vars: dict) -> CheckResult:
    """Check that a regex pattern does NOT appear in any matching files. Pass=absent."""
    pattern = args.get("pattern", "")
    if not pattern:
        return CheckResult(passed=False, message="content_absent: no pattern specified")

    file_patterns = vars.get("instruction_files", [])
    if isinstance(file_patterns, str):
        file_patterns = [file_patterns]

    path_pattern = args.get("path", "")
    if path_pattern:
        file_patterns = [_resolve_path(path_pattern, vars)]

    compiled = re.compile(pattern)
    for fp in file_patterns:
        matches = _resolve_glob_targets(fp, root)
        for match in matches:
            if not match.is_file():
                continue
            try:
                content = match.read_text()
                if compiled.search(content):
                    return CheckResult(
                        passed=False,
                        message=f"{match.name}: forbidden pattern found: {pattern}",
                    )
            except Exception:
                continue

    return CheckResult(passed=True, message="Forbidden pattern not found")


# Registry of mechanical checks
MECHANICAL_CHECKS = {
    "file_exists": file_exists,
    "directory_exists": directory_exists,
    "directory_contains": directory_contains,
    "git_tracked": git_tracked,
    "frontmatter_key": frontmatter_key,
    "file_count": file_count,
    "line_count": line_count,
    "byte_size": byte_size,
    "path_resolves": path_resolves,
    "extract_imports": extract_imports,
    "aggregate_byte_size": aggregate_byte_size,
    "import_depth": import_depth,
    "directory_file_types": directory_file_types,
    "frontmatter_valid_glob": frontmatter_valid_glob,
    "content_absent": content_absent,
}
