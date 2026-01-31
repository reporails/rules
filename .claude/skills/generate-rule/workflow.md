# Rule Creation Workflow

```mermaid
flowchart TD
    START([/generate-rule id scope title]) --> GATHER[Gather: what, why, type, patterns, sources]
    GATHER --> TYPE{OpenGrep fully decides?}
    TYPE -->|Yes| DET[type: deterministic]
    TYPE -->|No| SEM[type: semantic<br/>Add question + criteria]
    DET --> SOURCES[Find backing claims in sources.yml]
    SEM --> SOURCES
    SOURCES --> CONF{Confidence decision tree}
    CONF -->|max weight >= 0.8| CORE[tier: core]
    CONF -->|max weight < 0.8 or none| EXPERIMENTAL[tier: experimental]
    CONFIRMED --> GEN[Generate .md + .yml from templates]
    HIGH --> GEN
    MEDIUM --> GEN
    LOW --> GEN
    GEN --> RESOLVE[Resolve templates for validation]
    RESOLVE --> VALID{OpenGrep exit code?}
    VALID -->|0 or 1| SAVE[Save files with templates intact]
    VALID -->|2| FIX2[Fix syntax error] --> RESOLVE
    VALID -->|7| FIX7[Add positive pattern] --> RESOLVE
    SAVE --> BIDIR[Update claim.rules bidirectionally]
    BIDIR --> REFS[Update see_also, capability-levels if needed]
    REFS --> CHANGELOG[/add-changelog-entry]
```

## Edge Cases

**No existing claim backs the rule:**
- Run `/extract-claims <url>` first to create claim
- Then reference in rule's `backed_by`

**Core vs Agent rules:**
- Core rules use only `{{instruction_files}}`
- Agent rules can use `{{rules_dir}}`, `{{skills_dir}}`, etc.

**Path resolution:** Resolve rule paths from `.reporails/backbone.yml` using `rules.index`, `rules.categories`, and `rules.patterns`.
See [@.shared/knowledge/backbone-resolution.md](../../../.shared/knowledge/backbone-resolution.md) for the ID-to-path algorithm and directory structure.
