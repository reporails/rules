---
id: CORE:S:0009
slug: instruction-file-uses-valid-markdown-syntax-without-structur
title: Instruction File Uses Valid Markdown Syntax Without Structural Errors
category: structure
type: deterministic
level: L2
backed_by:
- agentic-coding-adoption-github
- agents-md-spec
- codex-exec-plans
- copilot-custom-instructions
- copilot-custom-instructions-vscode
targets: '{{instruction_files}}'
checks:
- id: CORE.S.0009.file_in_scope
  type: mechanical
  severity: high
  name: file_in_scope
  check: file_exists
- id: CORE.S.0009.no_broken_headings
  type: deterministic
  severity: high
  name: no_broken_headings
---

# Instruction File Uses Valid Markdown Syntax Without Structural Errors

Instruction files MUST agents parse Markdown for structure — broken syntax causes misinterpretation of sections, lists, and code blocks

## Pass / Fail

### Pass

````
```bash
npm test
```
````

### Fail

````
# Instruction file content
##Broken heading without space
````

## Limitations


