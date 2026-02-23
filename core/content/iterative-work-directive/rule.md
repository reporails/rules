---
id: CORE:C:0003
slug: iterative-work-directive
title: Iterative Work Directive
category: content
type: semantic
level: L3
backed_by:
- advanced-context-engineering
- agent-readmes-empirical-study
- builder-ai-instruction-best-practices
- building-skills-for-claude
- claude-4-best-practices
- claude-code-issue-13579
- claude-md-guide
- codex-eval-skills
- codex-exec-plans
- codex-prompting-guide
- copilot-ai-best-practices-vscode
- developer-context-cursor-study
- fowler-assessing-quality-agents
- fowler-pushing-ai-autonomy
- openai-community-agents-md-optimization
- osmani-ai-coding-workflow
- sewell-agents-md-tips
- spec-writing-for-agents
targets: '{{instruction_files}}'
checks:
- id: CORE.C.0003.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.C.0003.discusses_implementation_approach
  type: deterministic
  severity: medium
  name: discusses_implementation_approach
- id: CORE.C.0003.extract_iteration_directives
  type: deterministic
  severity: medium
  name: extract_iteration_directives
- id: CORE.C.0003.iteration_is_actionable
  type: semantic
  severity: medium
  name: iteration_is_actionable
question: Do these directives give the agent concrete guidance on how to scope 
  its work iteratively?
criteria:
- Specifies a unit of work (one function, one file, one test)
- Provides a workflow for iteration (implement, test, commit, repeat)
- Goes beyond just saying 'work incrementally' — gives actionable scope
choices:
- value: pass
  label: Passes
- value: fail
  label: Fails
pass_value: pass
---

# Iterative Work Directive

Instruction files SHOULD agents that attempt too much at once produce more errors — iterative work reduces catastrophic failures

## Pass / Fail

### Pass

````
Implement one function, fix one bug, or add one feature at a time
# === SEMANTIC JUDGMENT REQUIRED ===
# Write content satisfying all prior M/D checks,
# but testing the specific semantic question at this stage.
# One judgment call per rule — do not generate.
````

### Fail

````
# Implementation Approach
Build the feature using the provided module.
````

## Limitations


