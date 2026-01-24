---
paths:
  - "core/**/*.md"
  - "core/**/*.yml"
  - "agents/**/rules/*.md"
  - "agents/**/rules/*.yml"
---

# Rule File Instructions

## References

- **Schema:** `schemas/rule.schema.yml` (fields, validation, examples)
- **OpenGrep:** `.claude/rules/opengrep.md` (patterns, type decision)
- **Agent config:** `schemas/agent.schema.yml` (template variables)
- **Sources:** `.claude/rules/sources.md` (how to cite)

## File Pairing

Every rule needs TWO files:

```
{id}-{slug}.md    →  Rule definition (frontmatter + body)
{id}-{slug}.yml   →  OpenGrep patterns
```

**Contract:** `checks[].id` in .md must match `rules[].id` in .yml

## Type Decision

| Question | Type |
|----------|------|
| Can OpenGrep fully decide? | deterministic |
| OpenGrep partial, LLM fills gaps? | semantic |

Default to deterministic. See `opengrep.md` for decision guide.

## Constraints

When creating or editing rules:

- MUST create matching .yml file — OpenGrep needs patterns to run
- MUST keep body under 40 lines — prevents context bloat
- MUST update `see_also` when cross-referencing — enables navigation
- MUST update `docs/capability-levels.md` if affects detection — keeps assessment accurate
- MUST NOT duplicate schema info — reference `schemas/` instead

## Body Format

After frontmatter:

```markdown
# {Title}

{One sentence: why this matters}

## Pattern

**Good:** {example}
**Bad:** {example}
```

No code blocks over 10 lines.

## Quick Frontmatter

```yaml
id: S1                    # Required
title: Size Limits        # ≤64 chars
category: structure       # structure|content|efficiency|governance|maintenance
type: deterministic       # deterministic|semantic
checks:
  - id: S1-check-name     # Must start with rule ID
    name: Description
    severity: critical    # critical|high|medium|low
```

Semantic adds: `question: "..."` and `criteria: [...]`

For full field reference → `schemas/rule.schema.yml`