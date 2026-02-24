---
id: CLAUDE:G:0001
slug: hook-shell-commands-reference-claude-project-dir-instead-of-
title: Hook Shell Commands Reference $Claude Project Dir Instead Of Hardcoded 
  Paths
category: governance
type: deterministic
level: L2
backed_by:
- claude-code-hooks
- claude-code-settings
targets: '{{settings_file}}'
checks:
- id: CLAUDE.G.0001.settings_file_exists
  type: mechanical
  severity: medium
  name: settings_file_exists
  check: file_exists
- id: CLAUDE.G.0001.uses_project_dir_var
  type: deterministic
  severity: medium
  name: uses_project_dir_var
---

# Hook Shell Commands Reference $Claude Project Dir Instead Of Hardcoded Paths

Hook commands SHOULD use $CLAUDE_PROJECT_DIR for project-relative paths

## Pass / Fail

### Pass

````
Use $CLAUDE_PROJECT_DIR in hook commands for portable paths
````

### Fail

````
# Instruction file content
````

## Limitations


