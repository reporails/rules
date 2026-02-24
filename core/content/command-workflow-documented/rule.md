---
id: CORE:C:0021
slug: command-workflow-documented
title: Command Workflow Documented
category: content
type: deterministic
level: L4
backed_by:
- agent-readmes-empirical-study
- building-skills-for-claude
- copilot-coding-agent-best-practices
- copilot-coding-agent-results
- copilot-coding-agent-tasks
- copilot-custom-instructions
- developer-context-cursor-study
- dometrain-claude-md-guide
- osmani-ai-coding-workflow
targets: '{{main_instruction_file}}'
checks:
- id: CORE.C.0021.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.C.0021.mentions_commands
  type: deterministic
  severity: medium
  name: mentions_commands
- id: CORE.C.0021.has_workflow_sequence
  type: deterministic
  severity: medium
  name: has_workflow_sequence
---

# Command Workflow Documented

Instruction files SHOULD agents need to know command sequencing — running steps out of order causes failures

## Pass / Fail

### Pass

````
Document the sequence of steps for bootstrap, build, test, run, lint
1. Run tests first
2. Execute the build
3. Then run deployment
````

### Fail

````
# Commands
Run npm test to execute the test suite.
````

## Limitations


