# Rule Creation Workflow

```mermaid
flowchart TD
    START([/generate-rule coordinate scope title]) --> GATHER[Gather: what, why, type, patterns]
    GATHER --> TYPE{OpenGrep fully decides?}
    TYPE -->|Yes| DET[type: deterministic]
    TYPE -->|No - needs judgment| SEM[type: semantic<br/>Add question + criteria]
    TYPE -->|No - structural only| MECH[type: mechanical]
    DET --> SOURCES[Find backing sources in docs/sources.yml]
    SEM --> SOURCES
    MECH --> SOURCES
    SOURCES --> GEN[Generate rule.md + rule.yml + tests/pass/ + tests/fail/]
    GEN --> RESOLVE[Resolve templates for validation]
    RESOLVE --> VALID{OpenGrep exit code?}
    VALID -->|0 or 1| SAVE[Save files with templates intact]
    VALID -->|2| FIX2[Fix syntax error] --> RESOLVE
    VALID -->|7| FIX7[Add positive pattern] --> RESOLVE
    SAVE --> REFS[Update coordinate-map, capability-levels if needed]
    REFS --> CHANGELOG[/add-changelog-entry]
```

## Edge Cases

**No existing source backs the rule:**
- Add a new source entry to `docs/sources.yml` with the URL, type, and weight
- Then reference its ID in the rule's `backed_by` list

**Core vs Agent rules:**
- Core rules use only `{{instruction_files}}`
- Agent rules can use `{{rules_dir}}`, `{{skills_dir}}`, etc.

**Path resolution:** Resolve rule paths from `.reporails/backbone.yml` using `rules.categories`, `rules.agent_rules`, and `rules.patterns`.
See [@.shared/knowledge/backbone-resolution.md](../knowledge/backbone-resolution.md) for the coordinate-to-path algorithm and directory structure.
