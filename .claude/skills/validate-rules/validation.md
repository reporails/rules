# Validation Reference

Rule validation checks schema and contract compliance.

## Validation Levels

| Level | Name | Description |
|-------|------|-------------|
| 1 | Schema | Frontmatter fields, types, format |
| 2 | Contract | .md <-> .yml pairing and ID matching |

## Schema Validation

Required fields:
- `id` matches coordinate pattern (`CORE:S:0001`, `CLAUDE:S:0001`, etc.)
- `slug` matches directory name
- `title` <= 64 characters
- `category` is valid
- `type` is mechanical, deterministic, or semantic
- `level` is L1-L6
- `checks[]` array exists and non-empty
- `checks[].id` follows `NAMESPACE.CATEGORY.SLOT.descriptive-name` format

Type-specific:
- Semantic: must have `question` + `criteria` (required — drives LLM evaluation)
- Mechanical/Deterministic: `question` + `criteria` optional (documentation only)

## Contract Validation

Every rule .md file must have a matching .yml file:

- [ ] .yml file exists (named `rule.yml` in same directory)
- [ ] Every `checks[].id` in .md has matching `rules[].id` in .yml (deterministic/semantic)
- [ ] Every `rules[].id` in .yml has matching `checks[].id` in .md
- [ ] Severity mapping is consistent between .md and .yml
- [ ] Mechanical rules have `rules: []` in .yml

## Auto-fixable vs Manual Issues

| Issue | Auto-fixable | Action |
|-------|--------------|--------|
| Title > 64 chars | Yes | Truncate with "..." |
| Missing .yml severity | Yes | Add based on mapping |
| Wrong check ID prefix | Yes | Rename to match coordinate |
| Type mismatch | No | Change mechanical/deterministic/semantic |

## Output Format

```
Rules: 47 | Schema errors: 0 | Contract errors: 0
CORE:S:0001: ok  CORE:S:0002: ok  CORE:C:0001: ok  ...
```