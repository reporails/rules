---
name: generate-rule
description: Generate a rule skeleton with proper schema and directory structure
---

# /generate-rule

Generate a rule skeleton with coordinate-based ID, directory structure, and placeholder files.

## Usage

```
/generate-rule <coordinate> <scope> <title> [--agent <name>]
```

- `<coordinate>`: Rule coordinate (e.g., CORE:C:0001, CLAUDE:S:0001)
- `<scope>`: `core` or agent name (e.g., `claude`)
- `<title>`: Short title for the rule
- `--agent <name>`: Agent for path resolution (default: `claude`)

## Examples

```
/generate-rule CORE:C:0006 core "My New Rule"
/generate-rule CLAUDE:C:0002 claude "Some Agent Rule"
```

## Workflow

1. Validate coordinate is not in `registry/tombstones.yml`
2. Validate coordinate slot is not already taken in `registry/coordinate-map.yml`
3. Determine category from coordinate letter (S/C/E/M/G)
4. Resolve directory path from `backbone.rules.patterns` and `backbone.rules.categories`
5. Create directory: `{category_path}/{slug}/`
6. Generate `rule.md` with frontmatter (id, slug, title, category, type, level, targets, checks)
7. Generate `rule.yml` with regex patterns (if deterministic/semantic)
8. Create `tests/pass/` and `tests/fail/` directories with `.gitkeep`
9. Update `registry/coordinate-map.yml` with new slug→coordinate entry

## Reference

- Schema: `schemas/rule.schema.yml` — field definitions and validation rules
- Registry: `registry/coordinate-map.yml` — existing coordinates
- Registry: `registry/tombstones.yml` — dead slots

## Quick Reference

| Decision | Result |
|----------|--------|
| Structural/file checks only | type: mechanical |
| Regex pattern matching | type: deterministic |
| LLM evaluation needed | type: semantic (prompt field on terminal check) |
| Has backing sources | Add to backed_by with source IDs from docs/sources.yml |
| No backing sources | Omit backed_by (optional field) |