---
id: CORE:S:0024
slug: hook-event-handlers-defined
title: Hook Event Handlers Defined
category: structure
type: deterministic
level: L6
backed_by:
- claude-code-hooks
- claude-code-settings
- enterprise-claude-usage
- fowler-context-engineering-agents
- instruction-limits-principles
targets: '{{settings_file}}'
checks:
- id: CORE.S.0024.settings_file_exists
  type: mechanical
  severity: medium
  name: settings_file_exists
  check: file_exists
- id: CORE.S.0024.has_hook_event_types
  type: deterministic
  severity: medium
  name: has_hook_event_types
---

# Hook Event Handlers Defined

Instruction files SHOULD hooks should define explicit event-handler mappings with validated command arrays

## Pass / Fail

### Pass

````
PreToolUse:
  - command: lint
PostToolUse:
  - command: format
````

### Fail

````
# Instruction file content
````

## Limitations


