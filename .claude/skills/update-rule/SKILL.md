---
name: update-rule
description: Update an existing rule based on user intent
---

# /update-rule

Update an existing rule's OpenGrep patterns based on user instruction.

## Usage

```
/update-rule <id> <instruction> [--agent <name>]
```

- `<id>`: Rule ID (e.g., S4, C1, CLAUDE_S2)
- `<instruction>`: What to change (e.g., "fix invalid pattern", "more aggressive")
- `--agent <name>`: Agent name for template resolution (default: `claude`)

## Examples

```
/update-rule S1 "increase threshold to 400 lines"
/update-rule C7 "fix regex syntax error"
/update-rule CLAUDE_S2 "add detection for nested rules"
```

## Workflow

Follow: [workflow.md](workflow.md)

## Reference

- [OpenGrep patterns](opengrep-patterns.md) - Pattern syntax
- [Rule authoring](rule-authoring.md) - Validation

## Quick Reference

**NEVER change:**
- Rule ID
- Filenames
- Category or type

**Path resolution:** Resolve rule paths from `.reporails/backbone.yml` using `rules.index`, `rules.categories`, and `rules.patterns`.
See [@.shared/knowledge/backbone-resolution.md](../../../.shared/knowledge/backbone-resolution.md) for the ID-to-path algorithm.

**Save with `{{templates}}` intact - resolution is only for validation.**
