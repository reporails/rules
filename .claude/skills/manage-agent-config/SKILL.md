---
name: manage-agent-config
description: Create, update, and validate agent configurations
---

# /manage-agent-config

Manage agent configuration files. Config paths resolved from `backbone.agents.{agent}.config`.

## Usage

```
/manage-agent-config <action> <agent> [options]
```

**Actions:**
- `validate` — Check config against schema
- `create` — Create new agent config interactively
- `audit` — Audit: which vars are defined, which are missing
- `sync` — Update config based on audit findings

**Examples:**
```
/manage-agent-config validate claude
/manage-agent-config create cursor
/manage-agent-config audit claude
/manage-agent-config sync copilot
```

## Process

### Validate

1. Load agent config from `backbone.agents.{agent}.config`
2. Check against schema from `backbone.schemas.agent`
3. Verify required vars exist (main_instruction_file, instruction_files)
4. Report issues

### Create

1. Prompt for agent details (name, file patterns)
2. Determine feature support (rules dir, skills, etc.)
3. Generate config with appropriate vars and excludes
4. Validate and save

### Audit

1. Load agent config
2. Check all vars resolve to existing paths
3. Verify excludes patterns are valid
4. Generate recommendations

### Sync

1. Run audit
2. Apply recommended changes
3. Validate result

## Path Resolution

Resolve agent config and schema paths from `.reporails/backbone.yml`:
- Agent config: `backbone.agents.{agent}.config`
- Agent schema: `backbone.schemas.agent`