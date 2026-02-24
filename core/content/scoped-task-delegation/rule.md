---
id: CORE:C:0006
slug: scoped-task-delegation
title: Scoped Task Delegation
category: content
type: semantic
level: L6
backed_by:
- advanced-context-engineering
- claude-4-best-practices
- claude-code-hooks
- claude-code-issue-13579
- claude-code-settings
- codex-introducing
- copilot-ai-best-practices-vscode
- enterprise-claude-usage
- fowler-context-engineering-agents
- fowler-pushing-ai-autonomy
- spec-writing-for-agents
- using-claude-md-files
targets: '{{main_instruction_file}}'
checks:
- id: CORE.C.0006.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.C.0006.discusses_delegation
  type: deterministic
  severity: medium
  name: discusses_delegation
- id: CORE.C.0006.extract_delegation_content
  type: deterministic
  severity: medium
  name: extract_delegation_content
- id: CORE.C.0006.delegation_is_scoped
  type: semantic
  severity: medium
  name: delegation_is_scoped
question: Do delegation directives include explicit scope boundaries for 
  sub-tasks?
criteria:
- Specifies what directories or files sub-agents can modify
- Includes completion criteria or output expectations
choices:
- value: pass
  label: Passes
- value: fail
  label: Fails
pass_value: pass
---

# Scoped Task Delegation

Instruction files SHOULD unbounded sub-agent delegation causes runaway operations — explicit scope prevents overreach

## Pass / Fail

### Pass

````
Scope sub-agent tasks to specific directories or concerns
# === SEMANTIC JUDGMENT REQUIRED ===
# Write content satisfying all prior M/D checks,
# but testing the specific semantic question at this stage.
# One judgment call per rule — do not generate.
````

### Fail

````
# Architecture
The system uses autonomous components for reliability.
````

## Limitations


