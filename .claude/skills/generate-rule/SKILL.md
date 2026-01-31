---
name: generate-rule
description: Generate a rule skeleton with proper schema and directory structure
---

# /generate-rule

Generate a rule skeleton with proper directory structure, frontmatter, and placeholder files.

## Usage

```
/generate-rule <id> <scope> <title> [--agent <name>]
```

- `<id>`: Rule ID (e.g., S5, C6, CLAUDE_S3)
- `<scope>`: `core` or agent name (e.g., `claude`)
- `<title>`: Short title for the rule
- `--agent <name>`: Agent for path resolution (default: `claude`)

## Examples

```
/generate-rule S5 core "My New Rule"
/generate-rule CLAUDE_S3 claude "Some Agent Rule"
```

## Workflow

Follow: [workflow.md](workflow.md)

## Reference

- [Rule authoring](rule-authoring.md) — Templates and validation

## Path Resolution

Resolve all rule and artifact paths from `.reporails/backbone.yml` instead of hardcoding.
See [@.shared/knowledge/backbone-resolution.md](../../../.shared/knowledge/backbone-resolution.md) for the resolution table and ID-to-path algorithm.

## Quick Reference

| Decision | Result |
|----------|--------|
| OpenGrep fully decides | type: deterministic |
| LLM needed | type: semantic (add question + criteria) |
| Has backing sources | Add to backed_by (optional) |
| No backing sources | `backed_by: []` (valid default) |
