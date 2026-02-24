---
id: CORE:X:0005
slug: path-scope-declared
title: Path Scope Declared
category: context_quality
type: deterministic
level: L4
backed_by:
- awesome-copilot-meta-instructions
- claude-code-memory
- copilot-coding-agent-results
- copilot-custom-instructions
- copilot-custom-instructions-vscode
- fowler-context-engineering-agents
- rules-directory-mechanics
targets: '{{supplementary_files}}'
checks:
- id: CORE.X.0005.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.X.0005.has_globs_frontmatter_field
  type: deterministic
  severity: medium
  name: has_globs_frontmatter_field
---

# Path Scope Declared

Instruction files SHOULD path-scoped rules must declare their applicable paths so they are applied selectively

## Pass / Fail

### Pass

````
globs: ['**/*.md']
````

### Fail

````
# Instruction file content
````

## Limitations


