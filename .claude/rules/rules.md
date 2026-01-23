---
paths: ["rules/**/*.md"]
---

# Rule File Instructions

When editing files in `rules/`:

## Frontmatter

Required fields: id, title, category, type, detection, level, sources

Optional fields: scoring, antipatterns, see_also, validation

## Constraints

- MUST keep rule under 40 lines (M7)
- MUST update `see_also` when adding cross-references
- MUST update `.reporails/backbone.yml` rule_index if type changes
- MUST update `.reporails/capability-levels.yml` if level changes
- MUST update `capability-model.md` Capability Matrix if rule added/removed

## Format
- One-line summary after title
- Pattern section with Good/Bad examples
- No code blocks over 10 lines (E6)
