---
id: CORE:C:0009
slug: ask-rather-than-guess
title: Ask Rather Than Guess
category: content
type: semantic
level: L3
backed_by:
- advanced-context-engineering
- agent-readmes-empirical-study
- claude-code-issue-13579
- codex-exec-plans
- codex-prompting-guide
- copilot-ai-best-practices-vscode
- developer-context-cursor-study
- fowler-assessing-quality-agents
- fowler-pushing-ai-autonomy
- instruction-limits-principles
- osmani-ai-coding-workflow
- sewell-agents-md-tips
- spec-writing-for-agents
targets: '{{main_instruction_file}}'
checks:
- id: CORE.C.0009.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.C.0009.extract_ask_directives
  type: deterministic
  severity: medium
  name: extract_ask_directives
- id: CORE.C.0009.ask_guidance_is_actionable
  type: semantic
  severity: medium
  name: ask_guidance_is_actionable
question: Does the file give concrete guidance on when to ask vs. proceed?
criteria:
- Specifies conditions that should trigger asking (ambiguous requirements, 
  missing info)
- Distinguishes between situations where proceeding is OK vs. asking is required
choices:
- value: pass
  label: Passes
- value: fail
  label: Fails
pass_value: pass
---

# Ask Rather Than Guess

Instruction files SHOULD agents that guess when uncertain produce incorrect output — asking reduces costly rework

## Pass / Fail

### Pass

````
Ask for clarification when requirements are ambiguous
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


