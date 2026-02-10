# Contributing

Rules define what Reporails checks in AI instruction files (CLAUDE.md, AGENTS.md, .cursorrules). This repo is where those rules live.

## Prerequisites

- **Docker** — for running the test harness
- **A coding agent** — rules are created and validated through agent skills

Currently supported: **Claude Code**. Codex and Copilot support is planned.

## Rule anatomy

Each rule lives in its own directory with three parts:

```
core/structure/instruction-file-size-limit/
  rule.md          # Definition: frontmatter (id, type, level, checks) + prose
  rule.yml         # OpenGrep patterns (or empty `rules: []` for mechanical)
  tests/
    pass/          # Fixture that should pass the rule
    fail/          # Fixture that should fail the rule
```

## Coordinates

Every rule has a coordinate like `CORE:S:0005` — three parts:

| Part | Meaning | Values |
|------|---------|--------|
| Namespace | Who owns it | `CORE`, `CLAUDE`, `CODEX` |
| Category | What it checks | `S` (structure), `C` (content) |
| Slot | Sequence number | `0001`–`9999` |

Check `registry/coordinate-map.yml` to see which slots are taken before picking a new one.

## Rule types

| Type | How it detects | Example |
|------|---------------|---------|
| **mechanical** | Python structural checks (file exists, line count, byte size) | CORE:S:0001 — instruction file exists |
| **deterministic** | OpenGrep pattern matching on file content | CORE:C:0006 — specificity over vagueness |
| **semantic** | OpenGrep pre-filter + LLM evaluation | CORE:C:0017 — repo-specific content |

Mechanical rules have `rules: []` in their rule.yml. Deterministic and semantic rules have OpenGrep patterns.

## Creating a rule

```
/generate-rule CORE:C:0026 core "My New Rule"
```

The skill creates the directory, rule.md, rule.yml, and test fixtures. It walks you through choosing the type, writing patterns, and finding backing sources.

To implement checks and wire up an existing skeleton:

```
/implement-rule CORE:C:0026
```

## Testing

Build and run the Docker test harness:

```bash
# Build the test image (first time, or after runtime/ changes)
docker compose -f runtime/docker-compose.yml build

# Run all rules
docker compose -f runtime/docker-compose.yml run test

# Run one rule
docker compose -f runtime/docker-compose.yml run test --rule CORE:S:0001

# Run one category
docker compose -f runtime/docker-compose.yml run test core/structure/

# Verbose output (shows OpenGrep matches)
docker compose -f runtime/docker-compose.yml run test --verbose
```

All tests must pass before submitting.

## Submitting changes

1. Create a branch from `main`
2. Make your changes
3. Run the test harness — all rules must pass
4. Open a pull request

## Rule layout

```
core/
  structure/       # 12 rules — file existence, size, format
  content/         # 18 rules — what instruction files should contain

agents/
  claude/rules/    # 10 rules — CLAUDE.md-specific patterns
  codex/rules/     #  7 rules — AGENTS.md-specific patterns
```

Opinionated rules (governance, style) live in [reporails/recommended](https://github.com/reporails/recommended) with the `RRAILS_` namespace.

## Skills

| Task | Skill | Example |
|------|-------|---------|
| Create a rule | `/generate-rule` | `/generate-rule CORE:C:0026 core "My Rule"` |
| Implement checks | `/implement-rule` | `/implement-rule CORE:C:0026` |
| Validate all rules | `/validate-rules` | `/validate-rules` |
| Validate one rule | `/validate-rules` | `/validate-rules CORE:C:0026` |
| Level mappings | `/manage-levels` | `/manage-levels diff` |
| Log a change | `/add-changelog-entry` | `/add-changelog-entry` |

## Questions?

[Open an issue](https://github.com/reporails/rules/issues).
