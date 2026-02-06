---
name: validate-rules
description: Validate rules against schema and contracts
---

# /validate-rules

Validate rules against their schema and rule.md/rule.yml contracts.

## Usage

```
/validate-rules [coordinate] [options]
```

**Options:**
- `--category <cat>`: Validate only rules in category (structure, content, efficiency, maintenance, governance)

## Examples

```
/validate-rules                        # All rules
/validate-rules CORE:S:0001            # Single rule
/validate-rules --category structure   # Category filter
```

## Workflow

1. Load rule schema from `backbone.schemas.rule`
2. Load coordinate map from `backbone.registry.coordinate_map`
3. Resolve rule directories via `backbone.rules.patterns`
4. For each rule:
   - Validate rule.md frontmatter against schema
   - Validate rule.yml patterns match check IDs in rule.md
   - Verify coordinate exists in coordinate-map.yml
   - Verify check types don't exceed declared rule type ceiling
   - Verify supersedes target is at a strictly lower level

## Quick Reference

| Level | Check |
|-------|-------|
| 1 | Schema: fields, types, format, coordinate pattern |
| 2 | Contract: rule.md ↔ rule.yml check ID matching |
| 3 | Cross-reference: coordinate-map, tombstones, supersession |
