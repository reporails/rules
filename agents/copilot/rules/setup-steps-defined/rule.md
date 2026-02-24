---
id: COPILOT:S:0002
slug: setup-steps-defined
title: Setup Steps Defined
category: structure
type: deterministic
level: L6
backed_by:
- copilot-coding-agent-best-practices
- copilot-coding-agent-results
- copilot-coding-agent-tasks
targets: '{{main_instruction_file}}'
checks:
- id: COPILOT.S.0002.setup_file_exists
  type: mechanical
  severity: low
  name: setup_file_exists
  check: file_exists
- id: COPILOT.S.0002.has_steps_array
  type: deterministic
  severity: low
  name: has_steps_array
---

# Setup Steps Defined

A setup steps file MAY define workspace environment setup commands for reproducible bootstrapping

## Pass / Fail

### Pass

````
steps:
  - name: setup
    command: npm install
````

### Fail

````
# Instruction file content
````

## Limitations


