# Reporails Rule Test Harness

Contributor-facing test harness for validating rule implementations against test fixtures.

## Quick Start

```bash
# Build the test image
docker compose -f runtime/docker-compose.yml build

# Run all rules
docker compose -f runtime/docker-compose.yml run test

# Run one rule by coordinate
docker compose -f runtime/docker-compose.yml run test --rule CORE:S:0001

# Run one category
docker compose -f runtime/docker-compose.yml run test core/structure/

# Use a different agent's config for var resolution
docker compose -f runtime/docker-compose.yml run test --agent codex

# Verbose output (shows OpenGrep output)
docker compose -f runtime/docker-compose.yml run test --verbose
```

## Fixture Format

Each rule has `tests/pass/` and `tests/fail/` directories that simulate mini project roots:

```
{rule-dir}/tests/
  pass/                  # Simulated project that PASSES this rule
    CLAUDE.md            # (or whatever files the rule targets)
  fail/                  # Simulated project that FAILS this rule
    CLAUDE.md            # (content/structure that triggers violation)
```

### Writing Fixtures

1. Look at the rule's `targets:` field — it tells you what files the rule scans
2. Resolve template vars: `{{main_instruction_file}}` → `CLAUDE.md` (for claude agent)
3. Create those files inside `tests/pass/` and `tests/fail/`
4. Pass fixture: content that should NOT trigger the rule
5. Fail fixture: content that SHOULD trigger the rule

### Example: Mechanical Rule (file_exists)

```
instruction-file-exists/tests/
  pass/
    CLAUDE.md            # File exists → check passes
  fail/
    .gitkeep             # No instruction file → check fails
```

### Example: Deterministic Rule (OpenGrep pattern)

```
has-project-description/tests/
  pass/
    CLAUDE.md            # Starts with heading + description → 0 findings
  fail/
    CLAUDE.md            # Starts with commands, no description → 1+ findings
```

## Check Types

| Type | Engine | Pass fixture | Fail fixture |
|------|--------|-------------|-------------|
| Mechanical | Python (`checks.py`) | Check passes | Check fails |
| Deterministic | OpenGrep via `rule.yml` | 0 findings | 1+ findings |
| Semantic | Pre-checks only | Skipped (no LLM) | Skipped (no LLM) |

## Template Variables

Variables like `{{instruction_files}}` resolve from agent config files (`agents/{agent}/config.yml`). Default agent is `claude`.

| Variable | Claude value | Codex value |
|----------|-------------|-------------|
| `{{main_instruction_file}}` | `**/CLAUDE.md` | `**/AGENTS.md` |
| `{{instruction_files}}` | `**/CLAUDE.md`, `.claude/rules/**/*.md` | `**/AGENTS.md`, `**/AGENTS.override.md` |
| `{{rules_dir}}` | `.claude/rules` | — |
| `{{skills_dir}}` | `.claude/skills` | — |

## Graceful Degradation

- `checks: []` → reported as "not implemented" (skipped)
- `rules: []` in rule.yml → deterministic checks fail (no patterns)
- Empty fixture directories → reported as "no fixtures" (skipped)
- Unknown check type → warning, skipped

## Exit Codes

- `0` — all implemented rules passed
- `1` — one or more rules failed
