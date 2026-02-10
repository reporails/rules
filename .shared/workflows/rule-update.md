# Rule Update Workflow

```mermaid
flowchart TD
    START([/update-rule coordinate instruction]) --> LOCATE[Locate rule.md + rule.yml]
    LOCATE --> READ[Read current state<br/>frontmatter, patterns]
    READ --> APPLY[Apply instruction to patterns]
    APPLY --> RESOLVE[Resolve templates for validation]
    RESOLVE --> VALID{OpenGrep exit code?}
    VALID -->|0 or 1| CONFLICT[Check for ID conflicts]
    VALID -->|2| FIX2[Fix syntax error] --> RESOLVE
    VALID -->|7| FIX7[Add positive pattern] --> RESOLVE
    CONFLICT --> SAVE[Save with templates intact]
    SAVE --> SYNC{rule.md needs update?}
    SYNC -->|yes| UPDATEMD[Update rule.md if checks changed]
    SYNC -->|no| REPORT
    UPDATEMD --> REPORT[Report changes]
```

## Constraints

**NEVER change:**
- Rule coordinate (e.g., `CORE:S:0005` stays `CORE:S:0005`)
- Directory slug (e.g., `instruction-file-size-limit/` stays `instruction-file-size-limit/`)
- Category or type

**Save with templates:**
- Write `{{instruction_files}}` not resolved values
- Resolution is only for validation

## Path Resolution

Resolve rule paths from `.reporails/backbone.yml` using `rules.categories` and `rules.patterns`.
See [@.shared/knowledge/backbone-resolution.md](../knowledge/backbone-resolution.md) for the coordinate-to-path algorithm.
