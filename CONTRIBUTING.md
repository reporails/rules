# Contributing Rules

## Setup

1. Clone this repo
2. Use Claude Code — skills guide you through everything

## Adding a rule
```
/generate-rule S5 core "My New Rule"
```

Claude will:
1. Ask what it checks and why it matters
2. Determine if it's deterministic or semantic
3. Create .md and .yml files
4. Validate the OpenGrep pattern
5. Save only if validation passes

## Updating a rule
```
/update-rule S1 "increase line limit to 250"
```

## Before submitting
```
/validate-rules
```

This checks:
- Schema compliance
- .md <> .yml contract
- OpenGrep pattern validity

## After changes
```
/add-changelog-entry
```

## Rule structure
```
core/
  structure/     # S1-S4
  content/       # C1-C5
  efficiency/    # E1-E2
  maintenance/   # M1-M4

agents/
  claude/rules/  # CLAUDE_* rules
  codex/rules/   # CODEX_* rules
```

Opinionated rules (governance, process, style guidance) live in [reporails/recommended](https://github.com/reporails/recommended) with the `AILS_` prefix.

## Quick reference

| Task | Skill |
|------|-------|
| New rule | `/generate-rule <id> <scope> <title>` |
| Fix pattern | `/update-rule <id> <instruction>` |
| Validate all | `/validate-rules` |
| Validate one | `/validate-rules <id>` |
| Log change | `/add-changelog-entry` |

## Advanced: Agent configs
```
/manage-agent-config create cursor
/manage-agent-config audit claude
```

See `.claude/skills/manage-agent-config/` for details.

## Questions?

Open an issue.
