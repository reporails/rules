---
id: CORE:C:0015
slug: standard-named-sections
title: Standard Named Sections
category: content
type: deterministic
level: L2
backed_by:
- agent-readmes-empirical-study
- awesome-copilot-meta-instructions
- building-skills-for-claude
- codex-exec-plans
- copilot-coding-agent-best-practices
- copilot-coding-agent-results
- copilot-coding-agent-tasks
- spec-writing-for-agents
targets: '{{main_instruction_file}}'
checks:
- id: CORE.C.0015.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.C.0015.has_named_section
  type: deterministic
  severity: medium
  name: has_named_section
---

# Standard Named Sections

Instruction files SHOULD standard sections provide predictable structure agents can navigate

## Pass / Fail

### Pass

````
## Commands

Run `npm test` to verify.
````

### Fail

````
# Instruction file content
````

## Limitations


