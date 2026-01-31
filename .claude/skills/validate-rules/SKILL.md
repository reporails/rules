---
name: validate-rules
description: Validate rules against schema, contracts, and sources
---

# /validate-rules

Validate rules against their sources and schema.

## Usage

```
/validate-rules [id] [options]
```

**Options:**
- `--agent <name>`: Agent for template resolution (default: `claude`)
- `--category <cat>`: Validate only rules in category
- `--source-check`: Deep source and evidence chain validation

## Examples

```
/validate-rules                        # All rules, claude agent
/validate-rules S1                     # Single rule
/validate-rules --agent cursor         # All rules, cursor agent
/validate-rules --category structure   # Category filter
/validate-rules --source-check         # Deep source validation
```

## Workflow

Follow: [workflow.md](workflow.md)

## Reference

- [Validation](validation.md) - Validation levels
- [OpenGrep patterns](opengrep-patterns.md) - Pattern validation
- [Evidence chain](evidence-chain.md) - Evidence checks

## Path Resolution

Resolve all rule and artifact paths from `.reporails/backbone.yml` instead of hardcoding.
See [@.shared/knowledge/backbone-resolution.md](../../../.shared/knowledge/backbone-resolution.md) for the resolution table and ID-to-path algorithm.

## Quick Reference

| Level | Check |
|-------|-------|
| 1 | Schema: fields, types, format |
| 2 | Contract: .md <-> .yml matching |
| 3 | OpenGrep: pattern syntax (exit 0/1 = ok) |
| 4 | Source: URL validity, drift (with --source-check) |
| 5 | Evidence: backed_by integrity (with --source-check) |
