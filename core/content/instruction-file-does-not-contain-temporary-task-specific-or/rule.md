---
id: CORE:C:0029
slug: instruction-file-does-not-contain-temporary-task-specific-or
title: Instruction File Does Not Contain Temporary, Task Specific, Or Session 
  Bound Instructions
category: content
type: deterministic
level: L2
backed_by:
- claude-code-issue-13579
- copilot-custom-instructions
- openai-codex-own-agents-md
- spec-writing-for-agents
targets: '{{instruction_files}}'
checks:
- id: CORE.C.0029.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.C.0029.no_ephemeral_markers
  type: deterministic
  severity: medium
  name: no_ephemeral_markers
---

# Instruction File Does Not Contain Temporary, Task Specific, Or Session Bound Instructions

Instruction files SHOULD persistent instruction files should contain stable guidance — ephemeral tasks belong in conversations or task trackers, not in committed files

## Pass / Fail

### Pass

````
# Instruction file
````

### Fail

````
# Instruction file content
TODO: fill this in
FIXME: broken implementation
````

## Limitations


