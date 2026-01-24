# Schema Validation Checks

## Required Fields

- [ ] Frontmatter parses as valid YAML
- [ ] `id` matches pattern (core/agent/custom)
- [ ] `title` ≤ 64 characters
- [ ] `category` is valid (structure, content, efficiency, governance, maintenance)
- [ ] `type` is valid (deterministic/semantic)
- [ ] `checks` array exists and non-empty
- [ ] `checks[].id` starts with rule ID + hyphen
- [ ] `checks[].severity` is valid (critical, high, medium, low)
- [ ] If semantic: `question` and `criteria` exist
- [ ] If deterministic: NO `question` or `criteria`
- [ ] `sources` are valid URLs (if present)
- [ ] `see_also` references valid rule IDs (if present)
- [ ] Body ≤ 40 lines

## Validation Logic

For each rule: validate required fields, type-specific fields, and check ID prefixes.

Key checks:
- Required: id, title (≤64), category, type, checks[]
- Semantic: must have question + criteria
- Deterministic: must NOT have question/criteria
- All check IDs must start with `{rule.id}-`

## ID Patterns

| Scope | Pattern | Example |
|-------|---------|---------|
| Core | `^[SCEGM][0-9]+$` | S1, C12, E3 |
| Agent | `^[A-Z]+_[SCEGM][0-9]+$` | CLAUDE_S4 |

## Valid Categories

- structure
- content
- efficiency
- governance
- maintenance
