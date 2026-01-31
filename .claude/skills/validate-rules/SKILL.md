---
name: validate-rules
description: Validate rules against schema and contracts
---

# /validate-rules

Validate rules against their schema and .md/.yml contracts.

## Usage

```
/validate-rules [id] [options]
```

**Options:**
- `--category <cat>`: Validate only rules in category

## Examples

```
/validate-rules                        # All rules
/validate-rules S1                     # Single rule
/validate-rules --category structure   # Category filter
```

## Workflow

Follow: [workflow.md](workflow.md)

## Reference

- [Validation](validation.md) — Validation levels

## Path Resolution

Resolve all rule and artifact paths from `.reporails/backbone.yml` instead of hardcoding.
See [@.shared/knowledge/backbone-resolution.md](../../../.shared/knowledge/backbone-resolution.md) for the resolution table and ID-to-path algorithm.

## Quick Reference

| Level | Check |
|-------|-------|
| 1 | Schema: fields, types, format |
| 2 | Contract: .md <-> .yml matching |
