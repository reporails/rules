---
paths:
  - "core/**/*.md"
  - "core/**/*.yml"
  - "agents/**/rules/*.md"
  - "agents/**/rules/*.yml"
---

# OpenGrep Quick Reference

## Type Decision

| Question | Type |
|----------|------|
| Can OpenGrep fully decide? | `deterministic` |
| OpenGrep partial, LLM fills gaps? | `semantic` |

**Default to deterministic.** Both types need .yml files with patterns.

## Use Deterministic When

- File/directory exists → path glob
- Line count threshold → `(?s)(?:[^\\n]*\\n){N,}`
- Keyword presence → `pattern-regex: "KEYWORD"`
- YAML key presence → `pattern: key: $VALUE`

## Use Semantic When

- Subjective judgment needed (quality, intent)
- Context-dependent evaluation
- Still write patterns for what OpenGrep CAN detect

## Severity Mapping

| Rule | OpenGrep |
|------|----------|
| critical | ERROR |
| high/medium/low | WARNING |

## Limitations

- Metavariables capture single words only
- Cannot assess semantic meaning or quality

For pattern examples → `.claude/skills/generate-rule/opengrep-patterns.md`
For full schema → `schemas/rule.schema.yml`
