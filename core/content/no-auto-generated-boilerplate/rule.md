---
id: CORE:C:0030
slug: no-auto-generated-boilerplate
title: No Auto-Generated Boilerplate
category: content
type: deterministic
level: L1
backed_by:
- claude-md-guide
- codex-agents-md
- developer-context-cursor-study
- dometrain-claude-md-guide
- fowler-context-engineering-agents
- instruction-limits-principles
- openai-codex-own-agents-md
- openai-community-agents-md-optimization
- using-claude-md-files
targets: '{{instruction_files}}'
checks:
- id: CORE.C.0030.file_in_scope
  type: mechanical
  severity: high
  name: file_in_scope
  check: file_exists
- id: CORE.C.0030.no_boilerplate_markers
  type: deterministic
  severity: high
  name: no_boilerplate_markers
---

# No Auto-Generated Boilerplate

Instruction files MUST auto-generated boilerplate wastes context tokens and may conflict with actual instructions

## Pass / Fail

### Pass

````
# Instruction file
````

### Fail

````
# Instruction file content
TODO: fill in your project description.
YOUR NAME here.
````

## Limitations


