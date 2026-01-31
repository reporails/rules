# Validation Reference

Rule validation checks schema and contract compliance.

## Validation Levels

| Level | Name | Description |
|-------|------|-------------|
| 1 | Schema | Frontmatter fields, types, format |
| 2 | Contract | .md <-> .yml pairing and ID matching |

## Schema Validation

Required fields:
- `id` matches pattern (core: `^[SCEGM][0-9]+$`, agent: `^[A-Z]+_[SCEGM][0-9]+$`)
- `title` <= 64 characters
- `category` is valid
- `type` is deterministic or semantic
- `checks[]` array exists and non-empty
- `checks[].id` starts with `{rule.id}-`

Type-specific:
- Semantic: must have `question` + `criteria`
- Deterministic: must NOT have `question`/`criteria`

## Contract Validation

Every rule .md file must have a matching .yml file:

- [ ] .yml file exists (same name, different extension)
- [ ] Every `checks[].id` in .md has matching `rules[].id` in .yml
- [ ] Every `rules[].id` in .yml has matching `checks[].id` in .md
- [ ] Severity mapping is consistent between .md and .yml

## Auto-fixable vs Manual Issues

| Issue | Auto-fixable | Action |
|-------|--------------|--------|
| Title > 64 chars | Yes | Truncate with "..." |
| Missing .yml severity | Yes | Add based on mapping |
| Wrong check ID prefix | Yes | Rename to match rule ID |
| Type mismatch | No | Change deterministic <-> semantic |

## Output Format

```
Rules: 18 | Schema errors: 0 | Contract errors: 0
S1: ok  S2: ok  C1: ok  ...
```
