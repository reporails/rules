---
id: COPILOT:S:0001
slug: applyto-scope-declared
title: ApplyTo Scope Declared
category: structure
type: deterministic
level: L6
backed_by:
- awesome-copilot-meta-instructions
- copilot-ai-best-practices-vscode
- copilot-coding-agent-best-practices
- copilot-coding-agent-results
- copilot-coding-agent-tasks
- copilot-custom-instructions
- copilot-custom-instructions-vscode
targets: '{{supplementary_files}}'
checks:
- id: COPILOT.S.0001.instruction_file_exists
  type: mechanical
  severity: high
  name: instruction_file_exists
  check: file_exists
- id: COPILOT.S.0001.has_applyto_frontmatter
  type: deterministic
  severity: high
  name: has_applyto_frontmatter
---

# ApplyTo Scope Declared

Scoped .github/copilot-instructions.md files MUST use applyTo frontmatter to declare their target file patterns

## Pass / Fail

### Pass

````
applyTo: '**/*.py'
````

### Fail

````
# Instruction file content
````

## Limitations


