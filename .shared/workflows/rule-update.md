# Rule Update Workflow

```mermaid
flowchart TD
    START([/update-rule id instruction]) --> LOCATE[Locate rule .md + .yml]
    LOCATE --> READ[Read current state<br/>frontmatter, patterns]
    READ --> APPLY[Apply instruction to patterns]
    APPLY --> RESOLVE[Resolve templates for validation]
    RESOLVE --> VALID{OpenGrep exit code?}
    VALID -->|0 or 1| CONFLICT[Check for ID conflicts]
    VALID -->|2| FIX2[Fix syntax error] --> RESOLVE
    VALID -->|7| FIX7[Add positive pattern] --> RESOLVE
    CONFLICT --> SAVE[Save with templates intact]
    SAVE --> SYNC{.md needs update?}
    SYNC -->|yes| UPDATEMD[Update .md if checks changed]
    SYNC -->|no| REPORT
    UPDATEMD --> REPORT[Report changes]
```

## Constraints

**NEVER change:**
- Rule ID (e.g., S6 stays S6)
- Filenames (e.g., S6-yaml-backbone.yml stays S6-yaml-backbone.yml)
- Category or type

**Save with templates:**
- Write `{{instruction_files}}` not resolved values
- Resolution is only for validation

## File Locations

```
Core rules:    core/{category}/{ID}-*.md and .yml
Agent rules:   agents/{agent}/rules/{ID}-*.md and .yml
```
