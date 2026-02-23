---
id: CORE:S:0025
slug: hook-handlers-with-type-command-contain-a-command-field-with
title: Hook Handlers With Type Command Contain A Command Field With The Shell 
  Command To Execute
category: structure
type: deterministic
level: L2
backed_by:
- claude-code-hooks
- claude-code-settings
targets: '{{settings_file}}'
checks:
- id: CORE.S.0025.settings_file_exists
  type: mechanical
  severity: high
  name: settings_file_exists
  check: file_exists
- id: CORE.S.0025.command_hook_has_command
  type: deterministic
  severity: high
  name: command_hook_has_command
---

# Hook Handlers With Type Command Contain A Command Field With The Shell Command To Execute

Command-type hook handlers MUST include a command field

## Pass / Fail

### Pass

````
"command": "/bin/bash .claude/hooks/lint.sh"
````

### Fail

````
# Instruction file content
````

## Limitations


