---
id: CORE:C:0017
slug: no-inline-style-rules
title: No Inline Style Rules
category: content
type: deterministic
level: L3
backed_by:
- agent-readmes-empirical-study
- agentic-coding-adoption-github
- claude-md-optimization-study
- copilot-custom-instructions-vscode
- developer-context-cursor-study
- dometrain-claude-md-guide
- instruction-limits-principles
- spec-writing-for-agents
targets: '{{instruction_files}}'
checks:
- id: CORE.C.0017.file_in_scope
  type: mechanical
  severity: high
  name: file_in_scope
  check: file_exists
- id: CORE.C.0017.extract_inline_style_rules
  type: deterministic
  severity: high
  name: extract_inline_style_rules
- id: CORE.C.0017.no_style_ruleset_embedded
  type: mechanical
  severity: high
  name: no_style_ruleset_embedded
  check: count_at_most
---

# No Inline Style Rules

Instruction files MUST code style belongs in linter config files, not instruction files — duplicating it causes drift

## Pass / Fail

### Pass

````
Indentation with 4 spaces.
````

### Fail

````
# Project Setup
Run npm install to set up the project.
Use the provided Makefile for builds.
````

## Limitations


