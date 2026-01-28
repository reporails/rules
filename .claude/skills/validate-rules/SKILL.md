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

Follow: [@.shared/workflows/rule-validation.md](../../../.shared/workflows/rule-validation.md)

## Reference

- [@.shared/knowledge/validation.md](../../../.shared/knowledge/validation.md) - Validation levels
- [@.shared/knowledge/opengrep-patterns.md](../../../.shared/knowledge/opengrep-patterns.md) - Pattern validation
- [@.shared/knowledge/evidence-chain.md](../../../.shared/knowledge/evidence-chain.md) - Evidence checks

## Quick Reference

| Level | Check |
|-------|-------|
| 1 | Schema: fields, types, format |
| 2 | Contract: .md <-> .yml matching |
| 3 | OpenGrep: pattern syntax (exit 0/1 = ok) |
| 4 | Source: URL validity, drift (with --source-check) |
| 5 | Evidence: backed_by integrity (with --source-check) |
