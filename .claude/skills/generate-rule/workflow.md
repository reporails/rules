# Rule Skeleton Workflow

```mermaid
flowchart TD
    START([/generate-rule coordinate scope title]) --> GATHER[Gather: what, why, type]
    GATHER --> TYPE{Detection method?}
    TYPE -->|Structural checks only| MECH[type: mechanical]
    TYPE -->|Regex fully decides| DET[type: deterministic]
    TYPE -->|Needs LLM judgment| SEM[type: semantic<br/>Add question + criteria]
    MECH --> GEN[Generate skeleton files]
    DET --> GEN
    SEM --> GEN
    GEN --> MD[Create rule.md with frontmatter<br/>+ Pass/Fail examples]
    MD --> YML[Create rule.yml<br/>patterns or empty rules list]
    YML --> TESTS[Create tests/pass/ + tests/fail/]
    TESTS --> COORDMAP[Update registry/coordinate-map.yml]
    COORDMAP --> CHANGELOG[/add-changelog-entry]
```

## What Gets Generated

| File | Content |
|------|---------|
| `rule.md` | Frontmatter (id, slug, title, category, type, level, checks, backed_by) + prose |
| `rule.yml` | Regex patterns (deterministic/semantic) or `rules: []` (mechanical) |
| `tests/pass/` | Empty — populated by `/implement-rule` |
| `tests/fail/` | Empty — populated by `/implement-rule` |

## Placeholder .yml (deterministic/semantic)

```yaml
rules:
  - id: NAMESPACE.CATEGORY.SLOT.descriptive-name
    message: "{description}"
    severity: WARNING
    languages: [generic]
    pattern-regex: "TODO"  # placeholder — to be filled by /implement-rule
    paths:
      include:
        - "{{instruction_files}}"
```

Mechanical rules get `rules: []` — no regex patterns needed.

## Edge Cases

**Core vs Agent rules:**
- Core rules use only `{{instruction_files}}`
- Agent rules can use `{{rules_dir}}`, `{{skills_dir}}`, etc.

**Path resolution:** Resolve rule paths from `.reporails/backbone.yml` using `rules.categories` and `rules.patterns`.
See [@.shared/knowledge/backbone-resolution.md](../../../.shared/knowledge/backbone-resolution.md) for the coordinate-to-path algorithm.