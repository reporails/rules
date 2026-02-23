---
id: CORE:S:0030
slug: local-override-file-present
title: Local Override File Present
category: structure
type: deterministic
level: L5
backed_by:
- claude-code-memory
- claude-code-settings
- claude-md-guide
- codex-agent-loop
- codex-agents-md
- codex-prompting-guide
- openai-codex-own-agents-md
targets: '{{local_file}}'
checks:
- id: CORE.S.0030.local_override_exists
  type: mechanical
  severity: medium
  name: local_override_exists
  check: file_exists
- id: CORE.S.0030.gitignore_has_local_override
  type: deterministic
  severity: medium
  name: gitignore_has_local_override
---

# Local Override File Present

Instruction files SHOULD local overrides allow developer-specific customization without polluting shared config

## Pass / Fail

### Pass

````
CLAUDE.local.md provides developer-specific overrides
````

### Fail

````
# Instruction file content
````

## Limitations


