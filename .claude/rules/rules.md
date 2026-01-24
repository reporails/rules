---
paths: ["rules/**/*.md"]
---

# Rule File Instructions

When editing files in `rules/`:

## Frontmatter

Required fields: id, title, category, type, detection, level, sources

Optional fields: antipatterns, see_also, validation

**Type values:** deterministic, heuristic, semantic, behavioral

**Severity values:** critical (5.5), high (4.0), medium (2.5), low (1.0)

## Constraints

- MUST keep rule under 40 lines (M7)
- MUST update `see_also` when adding cross-references
- MUST update `.reporails/backbone.yml` rule_index if type changes
- MUST update `.reporails/capability-levels.yml` if level changes
- MUST update `capability-levels.md` Capability Matrix if rule added/removed

## Format
- One-line summary after title
- Pattern section with Good/Bad examples
- No code blocks over 10 lines (E6)
