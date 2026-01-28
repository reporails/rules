# Rule Validation Workflow

```mermaid
flowchart TD
    START([/validate-rules options]) --> COLLECT[Collect rules from paths]
    COLLECT --> LOOP[For each rule]
    LOOP --> SCHEMA[1. Schema validation<br/>Fields, types, format]
    SCHEMA -->|fail| REPORT
    SCHEMA -->|pass| CONTRACT[2. Contract validation<br/>.md and .yml matching]
    CONTRACT -->|fail| REPORT
    CONTRACT -->|pass| RESOLVE[Resolve template variables]
    RESOLVE --> OPENGREP[3. OpenGrep validation<br/>Pattern syntax]
    OPENGREP -->|exit 2 or 7| REPORT
    OPENGREP -->|exit 0 or 1| SOURCE{--source-check?}
    SOURCE -->|yes| EVIDENCE[4. Evidence chain validation<br/>backed_by integrity]
    SOURCE -->|no| REPORT
    EVIDENCE --> REPORT[Report results]
    REPORT --> NEXT{More rules?}
    NEXT -->|yes| LOOP
    NEXT -->|no| SUMMARY[Summary output]
```

## Template Resolution

Before OpenGrep validation:

1. Load agent config: `agents/{agent}/config.yml`
2. Replace variables from `vars:` section
3. Create temp resolved file for validation

| Template | Example Value (claude) |
|----------|------------------------|
| `{{instruction_files}}` | `**/CLAUDE.md`, `.claude/rules/**/*.md` |
| `{{rules_dir}}` | `.claude/rules` |
| `{{skills_dir}}` | `.claude/skills` |

## Output Format

```
Rules: 42 | Schema errors: 3 | Contract: 1 | Drift: 5
S1: ok  S2: schema error  C1: contract error  E3: drift warning
```
