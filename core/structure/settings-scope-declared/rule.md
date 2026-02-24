---
id: CORE:S:0021
slug: settings-scope-declared
title: Settings Scope Declared
category: structure
type: deterministic
level: L5
backed_by:
- claude-code-hooks
- claude-code-settings
- enterprise-claude-usage
targets: '{{settings_file}}'
checks:
- id: CORE.S.0021.settings_file_exists
  type: mechanical
  severity: medium
  name: settings_file_exists
  check: file_exists
- id: CORE.S.0021.has_config_keys
  type: deterministic
  severity: medium
  name: has_config_keys
---

# Settings Scope Declared

Instruction files SHOULD agent settings should declare scope (project, user, enterprise) to prevent config leaks

## Pass / Fail

### Pass

````
permissions:
  allow:
    - Read
hooks:
  PreToolUse:
    - command: lint
````

### Fail

````
# Instruction file content
````

## Limitations


