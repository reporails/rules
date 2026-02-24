---
id: CORE:C:0023
slug: error-handling-guidance
title: Error Handling Guidance
category: content
type: semantic
level: L3
backed_by:
- agent-readmes-empirical-study
- awesome-copilot-meta-instructions
- building-skills-for-claude
- claude-code-issue-13579
- claude-md-optimization-study
- codex-exec-plans
- copilot-custom-instructions
- copilot-custom-instructions-vscode
- developer-context-cursor-study
- fowler-pushing-ai-autonomy
- openai-community-agents-md-optimization
- prompthub-cursor-rules-analysis
- spec-writing-for-agents
targets: '{{main_instruction_file}}'
checks:
- id: CORE.C.0023.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.C.0023.discusses_fallible_operations
  type: deterministic
  severity: medium
  name: discusses_fallible_operations
- id: CORE.C.0023.extract_error_content
  type: deterministic
  severity: medium
  name: extract_error_content
- id: CORE.C.0023.error_guidance_is_actionable
  type: semantic
  severity: medium
  name: error_guidance_is_actionable
question: Does the error handling guidance give the agent concrete actions to 
  take when things go wrong?
criteria:
- Specifies what to do when a specific operation fails
- Provides fallback behavior or escalation path
- Goes beyond 'handle errors gracefully' to name concrete error types or 
  responses
choices:
- value: pass
  label: Passes
- value: fail
  label: Fails
pass_value: pass
---

# Error Handling Guidance

Instruction files SHOULD agents without error guidance either crash silently or retry endlessly — explicit error handling prevents both

## Pass / Fail

### Pass

````
Include error handling directives for agent behavior
# === SEMANTIC JUDGMENT REQUIRED ===
# Write content satisfying all prior M/D checks,
# but testing the specific semantic question at this stage.
# One judgment call per rule — do not generate.
````

### Fail

````
# Operations
Monitor for error conditions and timeout events.
````

## Limitations


