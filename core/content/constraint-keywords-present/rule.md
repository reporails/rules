---
id: CORE:C:0018
slug: constraint-keywords-present
title: Constraint Keywords Present
category: content
type: deterministic
level: L3
backed_by:
- agent-readmes-empirical-study
- awesome-copilot-meta-instructions
- building-skills-for-claude
- claude-4-best-practices
- claude-md-guide
- codex-eval-skills
- codex-skills-shell-compaction
- copilot-custom-instructions
- developer-context-cursor-study
- fowler-pushing-ai-autonomy
- openai-community-agents-md-optimization
- osmani-ai-coding-workflow
- spec-writing-for-agents
targets: '{{instruction_files}}'
checks:
- id: CORE.C.0018.file_in_scope
  type: mechanical
  severity: high
  name: file_in_scope
  check: file_exists
- id: CORE.C.0018.has_constraint_keywords
  type: deterministic
  severity: high
  name: has_constraint_keywords
---

# Constraint Keywords Present

Instruction files MUST critical constraints should be stated in explicit mandatory language so the agent treats them as non-negotiable

## Pass / Fail

### Pass

````
MUST NOT commit credentials to version control.
NEVER deploy without passing tests.
````

### Fail

````
# Instruction file content
````

## Limitations


