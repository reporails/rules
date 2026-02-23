---
id: CLAUDE:S:0007
slug: hook-handlers-with-type-prompt-or-agent-contain-a-prompt-fie
title: Hook Handlers With Type Prompt Or Agent Contain A Prompt Field
category: structure
type: deterministic
level: L2
backed_by:
- claude-code-hooks
targets: '{{settings_file}}'
checks:
- id: CLAUDE.S.0007.settings_file_exists
  type: mechanical
  severity: high
  name: settings_file_exists
  check: file_exists
- id: CLAUDE.S.0007.prompt_hook_has_prompt
  type: deterministic
  severity: high
  name: prompt_hook_has_prompt
---

# Hook Handlers With Type Prompt Or Agent Contain A Prompt Field

Prompt-type and agent-type hook handlers MUST include a prompt field

## Pass / Fail

### Pass

````
"prompt": "Check for security issues before proceeding"
````

### Fail

````
# Instruction file content
````

## Limitations


