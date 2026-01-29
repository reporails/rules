---
name: generate-rule
description: Generate a new rule with proper schema and OpenGrep patterns
---

# /generate-rule

Generate a new rule with proper schema and OpenGrep patterns.

## Usage

```
/generate-rule <id> <scope> <title> [--agent <name>]
```

- `<id>`: Rule ID (e.g., S1, C1, CLAUDE_S1)
- `<scope>`: `core` or agent name (e.g., `claude`)
- `<title>`: Short title for the rule
- `--agent <name>`: Agent for template resolution (default: `claude`)

## Examples

```
/generate-rule S1 core "Size Limits"
/generate-rule CLAUDE_S2 claude "Hierarchical Memory"
/generate-rule S1 core "Size Limits" --agent cursor
```

## Workflow

Follow: [workflow.md](workflow.md)

## Reference

- [Rule authoring](rule-authoring.md) - Templates and validation
- [OpenGrep patterns](opengrep-patterns.md) - Pattern syntax
- [Evidence chain](evidence-chain.md) - Source linking

## Quick Reference

| Decision | Result |
|----------|--------|
| OpenGrep fully decides | type: deterministic |
| LLM needed | type: semantic (add question + criteria) |
| max(source_weights) >= 0.8 | tier: core |
| max(source_weights) < 0.8 or none | tier: experimental |
