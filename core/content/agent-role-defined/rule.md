---
id: CORE:C:0014
slug: agent-role-defined
title: Agent Role Defined
category: content
type: semantic
level: L3
backed_by:
- agent-readmes-empirical-study
- building-skills-for-claude
- claude-4-best-practices
- copilot-coding-agent-best-practices
- copilot-coding-agent-results
- copilot-coding-agent-tasks
- developer-context-cursor-study
- fowler-pushing-ai-autonomy
- microsoft-awesome-copilot-blog
- openai-community-agents-md-optimization
- osmani-ai-coding-workflow
- spec-writing-for-agents
targets: '{{main_instruction_file}}'
checks:
- id: CORE.C.0014.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.C.0014.addresses_agent_identity
  type: deterministic
  severity: medium
  name: addresses_agent_identity
- id: CORE.C.0014.extract_role_content
  type: deterministic
  severity: medium
  name: extract_role_content
- id: CORE.C.0014.role_is_meaningful
  type: semantic
  severity: medium
  name: role_is_meaningful
question: Does the role definition give the agent a specific perspective that 
  shapes its decision-making?
criteria:
- Names a concrete role or persona, not just 'be helpful'
- The role implies specific expertise or judgment criteria
- Following the role would produce different behavior than default
choices:
- value: pass
  label: Passes
- value: fail
  label: Fails
pass_value: pass
---

# Agent Role Defined

Instruction files SHOULD agents with an explicit role produce more focused output — without one they oscillate between approaches

## Pass / Fail

### Pass

````
Specify the persona or expert role the agent should adopt
You are a senior backend engineer specializing in Python APIs.
# === SEMANTIC JUDGMENT REQUIRED ===
# Write content satisfying all prior M/D checks,
# but testing the specific semantic question at this stage.
# One judgment call per rule — do not generate.
````

### Fail

````
# Project
Seek expert guidance when needed for identity verification.
````

## Limitations


