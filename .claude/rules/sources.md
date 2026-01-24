---
paths:
  - "core/**/*.md"
  - "agents/**/rules/*.md"
---

# Sources Reference

Instructions for citing sources when writing or updating rules.

## Source Registry

Location: `docs/sources.yml`
Schema: `schemas/sources.schema.yml`

## Finding Sources

Sources are grouped by agent:

| Writing rule for | Read sections |
|------------------|---------------|
| Core rule | `generic` |
| Claude rule | `generic` + `claude` |
| Copilot rule | `generic` + `copilot` |
| Codex rule | `generic` + `codex` |

## Selection Priority

1. **Prefer official** over community sources
2. **Prefer research** (empirical data) for measurable claims
3. **Match description** to rule topic

## Citing in Rules

Put actual URLs in the rule's `sources` field:

```yaml
sources:
  - "https://www.anthropic.com/engineering/claude-code-best-practices"
  - "https://code.claude.com/docs/en/memory"
```

Do NOT use source IDs. Use full URLs.

## When No Source Exists

If no existing source covers the rule topic:

1. Check if rule is based on established practice (may not need source)
2. Leave `sources` empty rather than cite irrelevant sources
3. Note in PR that source is needed

## Adding New Sources

If you find a valuable source not in the registry:

1. Add to appropriate section in `docs/sources.yml`
2. Follow schema in `schemas/sources.schema.yml`
3. Use `id` that reflects content, not title