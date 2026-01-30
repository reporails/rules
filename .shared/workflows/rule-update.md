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
- Rule ID (e.g., S4 stays S4)
- Filenames (e.g., S4-yaml-backbone.yml stays S4-yaml-backbone.yml)
- Category or type

**Re-assess when patterns change:**
- Re-evaluate `pattern_confidence` for any check whose pattern was modified

**Save with templates:**
- Write `{{instruction_files}}` not resolved values
- Resolution is only for validation

## File Locations

```
Core rules:    core/{category}/{ID}-{slug}/{ID}-{slug}.md and .yml
Agent rules:   agents/{agent}/rules/{ID}-{slug}/{ID}-{slug}.md and .yml
```

**Directory structure:**
```
{rule-id}/
├── {rule-id}.md
├── {rule-id}.yml
└── tests/
    ├── fail.md   # Should trigger
    └── pass.md   # Should not trigger
```
