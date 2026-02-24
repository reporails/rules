---
id: CLAUDE:S:0005
slug: hook-configuration-uses-recognized-event-type-names-as-keys
title: Hook Configuration Uses Recognized Event Type Names As Keys
category: structure
type: deterministic
level: L2
backed_by:
- claude-code-hooks
- claude-code-settings
targets: '{{settings_file}}'
checks:
- id: CLAUDE.S.0005.settings_file_exists
  type: mechanical
  severity: high
  name: settings_file_exists
  check: file_exists
- id: CLAUDE.S.0005.valid_event_types
  type: deterministic
  severity: high
  name: valid_event_types
---

# Hook Configuration Uses Recognized Event Type Names As Keys

Hook event names MUST use valid Claude Code event types

## Pass / Fail

### Pass

````
Valid hook events: PreToolUse, PostToolUse, SessionStart, Stop, etc.
````

### Fail

````
# Instruction file content
````

## Limitations


