# Rule Skeleton Workflow

```mermaid
flowchart TD
    START([/generate-rule id scope title]) --> GATHER[Gather: what, why, type]
    GATHER --> TYPE{OpenGrep fully decides?}
    TYPE -->|Yes| DET[type: deterministic]
    TYPE -->|No| SEM[type: semantic<br/>Add question + criteria]
    DET --> GEN[Generate skeleton files]
    SEM --> GEN
    GEN --> MD[Create .md with frontmatter<br/>+ Good/Bad examples]
    MD --> YML[Create .yml with placeholder pattern]
    YML --> TESTS[Create tests/pass.md + tests/fail.md]
    TESTS --> INDEX[Update backbone rules.index]
    INDEX --> CHANGELOG[/add-changelog-entry]
```

## What Gets Generated

| File | Content |
|------|---------|
| `{id}-{slug}.md` | Frontmatter + heading + Pattern section (Good/Bad) |
| `{id}-{slug}.yml` | Placeholder with TODO pattern |
| `tests/pass.md` | Empty file with TODO comment |
| `tests/fail.md` | Empty file with TODO comment |

## Placeholder .yml

```yaml
rules:
  - id: {ID}-{check-slug}
    message: "TODO: {description}"
    severity: WARNING
    languages: [generic]
    pattern-regex: "TODO"  # placeholder — to be filled by tooling or contributor
    paths:
      include:
        - "{{instruction_files}}"
```

## Edge Cases

**Core vs Agent rules:**
- Core rules use only `{{instruction_files}}`
- Agent rules can use `{{rules_dir}}`, `{{skills_dir}}`, etc.

**Path resolution:** Resolve rule paths from `.reporails/backbone.yml` using `rules.index`, `rules.categories`, and `rules.patterns`.
See [@.shared/knowledge/backbone-resolution.md](../../../.shared/knowledge/backbone-resolution.md) for the ID-to-path algorithm and directory structure.
