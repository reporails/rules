---
id: CORE:S:0002
slug: section-headers-present
title: 'Section Headers Present'
category: structure
type: deterministic
level: L2
backed_by:
- agent-readmes-empirical-study
- agents-md-spec
- awesome-copilot-meta-instructions
- building-skills-for-claude
- claude-code-memory
- claude-md-guide
- codex-agents-md
- codex-exec-plans
- copilot-coding-agent-best-practices
- copilot-coding-agent-results
- copilot-coding-agent-tasks
- openai-codex-own-agents-md
- spec-writing-for-agents
targets: '{{instruction_files}}'
checks:
- id: CORE.S.0002.file_in_scope
  type: mechanical
  severity: high
  name: file_in_scope
  check: file_exists
- id: CORE.S.0002.has_h2_sections
  type: deterministic
  severity: high
  name: has_h2_sections
---

# Section Headers Present

Instruction files MUST instruction files should be organized with clear section headers for agent navigation

## Pass / Fail

### Pass

````
## Project Context

Project description here.
````

### Fail

````
# Instruction file content
````

## Limitations


