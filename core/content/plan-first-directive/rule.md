---
id: CORE:C:0004
slug: plan-first-directive
title: Plan-First Directive
category: content
type: semantic
level: L3
backed_by:
- advanced-context-engineering
- agent-readmes-empirical-study
- agentic-coding-adoption-github
- building-skills-for-claude
- claude-4-best-practices
- claude-code-issue-13579
- claudemd-best-practices-backbone-yml-pattern
- codex-eval-skills
- codex-exec-plans
- codex-prompting-guide
- copilot-ai-best-practices-vscode
- copilot-cli-best-practices
- developer-context-cursor-study
- dometrain-claude-md-guide
- enterprise-claude-usage
- fowler-assessing-quality-agents
- fowler-pushing-ai-autonomy
- instruction-limits-principles
- openai-community-agents-md-optimization
- osmani-ai-coding-workflow
- sewell-agents-md-tips
- spec-writing-for-agents
- using-claude-md-files
targets: '{{instruction_files}}'
checks:
- id: CORE.C.0004.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.C.0004.discusses_task_execution
  type: deterministic
  severity: medium
  name: discusses_task_execution
- id: CORE.C.0004.extract_plan_directives
  type: deterministic
  severity: medium
  name: extract_plan_directives
- id: CORE.C.0004.plan_directives_are_substantive
  type: semantic
  severity: medium
  name: plan_directives_are_substantive
question: Do these directives give the agent a concrete planning workflow rather
  than just saying 'think first'?
criteria:
- Specifies what to investigate (requirements, existing code, dependencies)
- Provides a planning structure (outline, questions, scope definition)
- Distinguishes planning from implementation with clear transition criteria
choices:
- value: pass
  label: Passes
- value: fail
  label: Fails
pass_value: pass
---

# Plan-First Directive

Instruction files SHOULD agents that jump straight to coding miss requirements — plan-first reduces rework

## Pass / Fail

### Pass

````
Begin by defining the problem and planning a solution before code generation
Plan before coding.
Investigate first, then implement.
Read the spec before making changes.
# === SEMANTIC JUDGMENT REQUIRED ===
# Write content satisfying all prior M/D checks,
# but testing the specific semantic question at this stage.
# One judgment call per rule — do not generate.
````

### Fail

````
# Task Management
Complete the task according to requirements.
````

## Limitations


