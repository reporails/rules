---
id: CORE:G:0005
slug: permission-configuration-explicitly-denies-access-to-sensiti
title: Permission Configuration Explicitly Denies Access To Sensitive Files
category: governance
type: deterministic
level: L2
backed_by:
- claude-code-hooks
- claude-code-settings
- codex-skills-shell-compaction
- copilot-coding-agent-best-practices
- copilot-coding-agent-results
- copilot-coding-agent-tasks
targets: '{{settings_file}}'
checks:
- id: CORE.G.0005.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.G.0005.mentions_deny_policy
  type: deterministic
  severity: medium
  name: mentions_deny_policy
---

# Permission Configuration Explicitly Denies Access To Sensitive Files

Instruction files SHOULD agents should not read or modify credentials, secrets, or sensitive configuration — explicit deny rules prevent accidental exposure

## Pass / Fail

### Pass

````
Add .env and credentials files to permissions.deny
````

### Fail

````
# Instruction file content
````

## Limitations


