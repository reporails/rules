---
id: CORE:S:0032
slug: import-targets-resolve
title: Import Targets Resolve
category: structure
type: deterministic
level: L4
backed_by:
- claude-code-memory
- developer-context-cursor-study
targets: '{{supplementary_files}}'
checks:
- id: CORE.S.0032.file_in_scope
  type: mechanical
  severity: high
  name: file_in_scope
  check: file_exists
- id: CORE.S.0032.extract_import_refs
  type: deterministic
  severity: high
  name: extract_import_refs
- id: CORE.S.0032.all_imports_resolve
  type: mechanical
  severity: high
  name: all_imports_resolve
  check: extract_imports
---

# Import Targets Resolve

Instruction files MUST broken @import references silently omit instructions the agent needs

## Pass / Fail

### Pass

````
@import .claude/rules/style.md
@import .claude/skills/commit/SKILL.md
````

### Fail

````
(File does not exist at expected path)
````

## Limitations


