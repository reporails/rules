---
id: CORE:S:0035
slug: setup-steps-defined
title: Setup Steps Defined
category: structure
type: deterministic
level: L6
backed_by:
- codex-introducing
- copilot-coding-agent-best-practices
- copilot-coding-agent-results
- copilot-coding-agent-tasks
targets: '{{main_instruction_file}}'
checks:
- id: CORE.S.0035.setup_file_exists
  type: mechanical
  severity: low
  name: setup_file_exists
  check: file_exists
- id: CORE.S.0035.has_steps_array
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


