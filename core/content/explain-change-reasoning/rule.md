---
id: CORE:C:0028
slug: explain-change-reasoning
title: Explain Change Reasoning
category: content
type: semantic
level: L3
backed_by:
- building-skills-for-claude
- developer-context-cursor-study
- fowler-assessing-quality-agents
- osmani-ai-coding-workflow
targets: '{{main_instruction_file}}'
checks:
- id: CORE.C.0028.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.C.0028.extract_reasoning_directives
  type: deterministic
  severity: medium
  name: extract_reasoning_directives
- id: CORE.C.0028.reasoning_guidance_is_actionable
  type: semantic
  severity: medium
  name: reasoning_guidance_is_actionable
question: Does the file specify when and how agents should explain their 
  reasoning?
criteria:
- Specifies contexts where explanation is required (design decisions, 
  non-obvious changes)
- Goes beyond 'explain your reasoning' to describe what good explanation looks 
  like
choices:
- value: pass
  label: Passes
- value: fail
  label: Fails
pass_value: pass
---

# Explain Change Reasoning

Instruction files SHOULD agents that explain reasoning produce reviewable output — silent changes are harder to verify

## Pass / Fail

### Pass

````
Explain your reasoning when making changes
# === SEMANTIC JUDGMENT REQUIRED ===
# Write content satisfying all prior M/D checks,
# but testing the specific semantic question at this stage.
# One judgment call per rule — do not generate.
````

### Fail

````
(File does not exist at expected path)
````

## Limitations


