---
id: CORE:S:0013
slug: scope-fields-in-frontmatter
title: Scope Fields in Frontmatter
category: structure
type: deterministic
level: L4
backed_by:
- awesome-copilot-meta-instructions
- claude-code-memory
- copilot-coding-agent-best-practices
- copilot-coding-agent-results
- copilot-coding-agent-tasks
- copilot-custom-instructions
- copilot-custom-instructions-vscode
- rules-directory-mechanics
targets: '{{supplementary_files}}'
checks:
- id: CORE.S.0013.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.S.0013.has_frontmatter_block
  type: deterministic
  severity: medium
  name: has_frontmatter_block
- id: CORE.S.0013.scope_field_present
  type: deterministic
  severity: medium
  name: scope_field_present
---

# Scope Fields in Frontmatter

Instruction files SHOULD scope fields in frontmatter control which files a rule applies to

## Pass / Fail

### Pass

````
---
description: Example rule
---
applyTo: '**/*.ts'
globs: ['src/**/*.ts']
````

### Fail

````
---
scope: project
---
# Rule Content
This rule has frontmatter.
````

## Limitations


