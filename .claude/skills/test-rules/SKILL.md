---
name: test-rules
description: Run rules against pass/fail fixtures using the local CLI test harness
---

# /test-rules

Run rules against their pass/fail test fixtures via the local docker test harness. This verifies that patterns fire correctly — pass fixtures produce zero violations, fail fixtures trigger at least one.

**This is not `/validate-rules`.** That skill checks schema and contracts (are fields correct? do files agree?). This skill runs the runtime harness (do patterns actually catch violations?).

## Usage

```
/test-rules [coordinate|path] [options]
```

**Options:**
- `--rule <coordinate>`: Run a single rule by coordinate
- `--agent <name>`: Agent config for template var resolution (default: `claude`)
- `--verbose`: Show per-check details for passing rules
- `--format json`: JSON output

## Examples

```
/test-rules                            # All rules
/test-rules --rule CORE:S:0001         # Single rule by coordinate
/test-rules core/structure/            # Category filter by path
/test-rules --agent codex              # Use codex agent vars
/test-rules --verbose                  # Show check-level detail
```

## Two harnesses

| Harness | Compose files | CLI source | When to use |
|---------|--------------|------------|-------------|
| Local | `docker-compose.yml` + `docker-compose.dev.yml` | `../../cli` (mounted) | Development — uses your local CLI source |
| CI | `docker-compose.yml` only | PyPI (`reporails-cli>=0.4.0`) | CI pipeline — uses published release |

**This skill always uses the local harness.** The local harness mounts the sibling `cli/` repo and installs it from source, so you test against the latest local CLI code.

## Workflow

### 1. Run the harness

From the rules repo root:

```bash
# All rules (local CLI)
docker compose -f runtime/docker-compose.yml -f runtime/docker-compose.dev.yml run --rm test

# Single rule
docker compose -f runtime/docker-compose.yml -f runtime/docker-compose.dev.yml run --rm test --rule CORE:S:0001

# Category
docker compose -f runtime/docker-compose.yml -f runtime/docker-compose.dev.yml run --rm test core/structure/

# With agent
docker compose -f runtime/docker-compose.yml -f runtime/docker-compose.dev.yml run --rm test --agent codex

# Verbose
docker compose -f runtime/docker-compose.yml -f runtime/docker-compose.dev.yml run --rm test --verbose
```

### 2. Read the results

The harness reports per-rule outcomes:

| Symbol | Meaning |
|--------|---------|
| `.` | Passed — all checks behave correctly on both fixtures |
| `F` | Failed — either pass fixture triggered a violation, or fail fixture was not caught |

Exit code 0 = all pass, exit code 1 = failures exist.

### 3. Diagnose failures

Each failure reports the reason:

| Failure | Meaning | Fix |
|---------|---------|-----|
| "Fail fixture: no check detected a violation" | Deterministic patterns don't match `tests/fail/` content | Fix pattern in rule.yml or fix fail fixture content |
| "Unknown mechanical check: X" | Check function name not registered in CLI | Add to CLI mechanical checks or fix name in rule.md |
| "[FAIL] ... (mechanical, pass): ..." | Pass fixture violates a mechanical check | Fix pass fixture or adjust check args |
| "no pattern specified" | Mechanical check missing required args | Add `args` to check in rule.md |

### 4. Fix and re-run

After fixing, re-run the specific failing rule:

```bash
docker compose -f runtime/docker-compose.yml -f runtime/docker-compose.dev.yml run --rm test --rule <coordinate> --verbose
```

## What the harness does

1. **Discovers** rules by walking `core/*/` and `agents/*/rules/` for directories with `rule.md`
2. **Loads** agent config for template var resolution
3. **Runs each rule** against its fixtures with asymmetric contract:
   - **Pass fixture** (`tests/pass/`): ALL checks must produce zero violations
   - **Fail fixture** (`tests/fail/`): AT LEAST ONE check must detect a violation
4. **Dispatches by check type:**
   - `mechanical` → built-in check functions
   - `deterministic` → regex engine
   - `semantic` → always skipped (no LLM in harness mode)

## Quick Reference

| Concern | Use |
|---------|-----|
| Do patterns fire correctly? | `/test-rules` (this skill) |
| Are rule definitions valid? | `/validate-rules` |
| Full QA before merge? | Both, in order: `/validate-rules` then `/test-rules` |
