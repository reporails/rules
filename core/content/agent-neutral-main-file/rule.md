---
id: CORE:C:0032
slug: agent-neutral-main-file
title: Agent-Neutral Main File
category: content
type: deterministic
level: L3
backed_by:
- copilot-custom-instructions-vscode
- enterprise-claude-usage
- instruction-limits-principles
- rules-directory-mechanics
targets: '{{main_instruction_file}}'
checks:
- id: CORE.C.0032.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.C.0032.no_agent_specific_directives
  type: deterministic
  severity: medium
  name: no_agent_specific_directives
---

# Agent-Neutral Main File

Instruction files SHOULD agent-specific content in the main file reduces portability across coding agents

## Pass / Fail

### Pass

````
# Instruction file
````

### Fail

````
# Instruction file content
## Claude Specific Settings

This only works with Claude.
````

## Limitations


