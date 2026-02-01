# Contributing

Reporails validates AI agent instruction files (CLAUDE.md, .cursorrules, copilot-instructions.md). Rules define what to check — this repo is where those rules live.

## Setup

1. Clone this repo
2. Open in Claude Code — slash commands handle the rest

## Create a rule

```
/generate-rule S5 core "My New Rule"
```

The skill walks you through it: what the rule checks, whether detection is deterministic or semantic, and generates the .md, .yml, and test files.

## Validate

```
/validate-rules
```

Checks schema compliance, .md/.yml consistency, and OpenGrep pattern validity. Run before submitting.

## Log changes

```
/add-changelog-entry
```

Run after any rule change.

## Rule layout

```
core/
  structure/     # S1-S4
  content/       # C1-C5
  efficiency/    # E1-E2
  maintenance/   # M1-M4

agents/
  claude/rules/  # CLAUDE_M1, CLAUDE_S1, CLAUDE_S2
  codex/rules/   # (no rules yet)
```

Opinionated rules (governance, process, style) live in [reporails/recommended](https://github.com/reporails/recommended) with the `AILS_` prefix.

Schemas live in `schemas/` — single source of truth, never duplicated across repos.

## Quick reference

| Task | Command |
|------|---------|
| New rule | `/generate-rule <id> <scope> <title>` |
| Validate all | `/validate-rules` |
| Validate one | `/validate-rules <id>` |
| Level mappings | `/manage-levels <sync\|diff\|list> [level]` |
| Agent config | `/manage-agent-config <create\|audit> <agent>` |
| Log change | `/add-changelog-entry` |

## Questions?

Open an issue.
