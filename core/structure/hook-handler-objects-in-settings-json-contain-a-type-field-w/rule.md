---
id: CORE:S:0028
slug: hook-handler-objects-in-settings-json-contain-a-type-field-w
title: Hook Handler Objects In Settings Json Contain A Type Field With Value 
  Command, Prompt, Or Agent
category: structure
type: deterministic
level: L2
backed_by:
- claude-code-hooks
targets: '{{settings_file}}'
checks:
- id: CORE.S.0028.settings_file_exists
  type: mechanical
  severity: high
  name: settings_file_exists
  check: file_exists
- id: CORE.S.0028.handler_has_type
  type: deterministic
  severity: high
  name: handler_has_type
---

# Hook Handler Objects In Settings Json Contain A Type Field With Value Command, Prompt, Or Agent

Hook handlers MUST declare a type field (command, prompt, or agent)

## Pass / Fail

### Pass

````
"type": "command"
````

### Fail

````
# Instruction file content
````

## Limitations


