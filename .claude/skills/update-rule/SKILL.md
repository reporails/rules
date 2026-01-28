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

- `<id>`: Rule ID (e.g., S6, C1, CLAUDE_S4)
- `<instruction>`: What to change (e.g., "fix invalid pattern", "more aggressive")
- `--agent <name>`: Agent name for template resolution (default: `claude`)

## Examples

```
/update-rule S1 "increase threshold to 400 lines"
/update-rule C7 "fix regex syntax error"
/update-rule CLAUDE_S4 "add detection for nested rules"
```

## Workflow

Follow: [@.shared/workflows/rule-update.md](../../../.shared/workflows/rule-update.md)

## Reference

- [@.shared/knowledge/opengrep-patterns.md](../../../.shared/knowledge/opengrep-patterns.md) - Pattern syntax
- [@.shared/knowledge/rule-authoring.md](../../../.shared/knowledge/rule-authoring.md) - Validation

## Quick Reference

**NEVER change:**
- Rule ID
- Filenames
- Category or type

**File locations:**

| Scope | Path |
|-------|------|
| Core | `core/{category}/{ID}-*.md` and `.yml` |
| Agent | `agents/{agent}/rules/{ID}-*.md` and `.yml` |

**Save with `{{templates}}` intact - resolution is only for validation.**
