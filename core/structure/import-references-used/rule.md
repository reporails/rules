---
id: CORE:S:0001
slug: import-references-used
title: Import References Used
category: structure
type: deterministic
level: L4
backed_by:
- advanced-context-engineering
- building-skills-for-claude
- claude-code-memory
- claude-md-guide
- claudemd-best-practices-backbone-yml-pattern
- copilot-custom-instructions-vscode
- developer-context-cursor-study
- dometrain-claude-md-guide
- instruction-limits-principles
- monorepo-claude-md-organization
- sewell-agents-md-tips
- spec-writing-for-agents
- using-claude-md-files
targets: '{{supplementary_files}}'
checks:
- id: CORE.S.0001.file_in_scope
  type: mechanical
  severity: low
  name: file_in_scope
  check: file_exists
- id: CORE.S.0001.has_import_references
  type: deterministic
  severity: low
  name: has_import_references
---

# Import References Used

Instruction files MAY instruction files should use @imports for modular organization and progressive disclosure

## Pass / Fail

### Pass

````
@import .claude/rules/style.md
````

### Fail

````
# Instruction file content
````

## Limitations


