# Validation Reference

Multi-level rule validation process.

## Validation Levels

| Level | Name | Description |
|-------|------|-------------|
| 1 | Schema | Frontmatter fields, types, format |
| 2 | Contract | .md <-> .yml pairing and ID matching |
| 3 | OpenGrep | Pattern syntax, positive patterns present |
| 4 | Source | URL validity, content drift |
| 5 | Evidence Chain | backed_by integrity, tier derivation |

## Schema Validation

Required fields:
- `id` matches pattern (core: `^[SCEGM][0-9]+$`, agent: `^[A-Z]+_[SCEGM][0-9]+$`)
- `title` <= 64 characters
- `category` is valid
- `type` is deterministic or semantic
- `backed_by` sources exist in sources.yml
- `checks[]` array exists and non-empty
- `checks[].id` starts with `{rule.id}-`
- `checks[].pattern_confidence` is valid enum (if set)

Type-specific:
- Semantic: must have `question` + `criteria`
- Deterministic: must NOT have `question`/`criteria`

## Contract Validation

Every rule .md file must have a matching .yml file:

- [ ] .yml file exists (same name, different extension)
- [ ] Every `checks[].id` in .md has matching `rules[].id` in .yml
- [ ] Every `rules[].id` in .yml has matching `checks[].id` in .md
- [ ] OpenGrep severity matches rule severity mapping

## Source Drift Detection

Flag for review if:
- Source page returns 404 (broken link)
- Source content changed significantly (hash mismatch)
- Source mentions different thresholds than rule
- Source no longer mentions the pattern rule enforces

## Auto-fixable vs Manual Issues

| Issue | Auto-fixable | Action |
|-------|--------------|--------|
| Title > 64 chars | Yes | Truncate with "..." |
| Missing .yml severity | Yes | Add based on mapping |
| Wrong check ID prefix | Yes | Rename to match rule ID |
| Missing rule in claim.rules | Yes | Add rule ID to array |
| Source drift | No | Review and update rule |
| Missing source support | No | Find source or reconsider |
| Type mismatch | No | Change deterministic <-> semantic |
| Invalid pattern_confidence | Yes | Set to valid enum value |

## Output Format

```
Rules: 42 | Schema errors: 3 | Contract: 1 | Drift: 5
S1: ok  S2: schema error  C1: contract error  E3: drift warning
```
