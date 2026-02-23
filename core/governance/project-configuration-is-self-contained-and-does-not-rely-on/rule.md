---
id: CORE:G:0008
slug: project-configuration-is-self-contained-and-does-not-rely-on
title: Project Configuration Is Self Contained And Does Not Rely On User Level 
  Settings
category: governance
type: semantic
level: L2
backed_by:
- claude-code-settings
targets: '{{main_instruction_file}}'
checks:
- id: CORE.G.0008.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.G.0008.extract_settings_refs
  type: deterministic
  severity: medium
  name: extract_settings_refs
- id: CORE.G.0008.no_user_dependency
  type: semantic
  severity: medium
  name: no_user_dependency
question: Does the project configuration avoid depending on user-level or 
  personal settings?
criteria:
- No references to user home directory configurations as requirements
- Project works out of the box without personal configuration
choices:
- value: pass
  label: Passes
- value: fail
  label: Fails
pass_value: pass
---

# Project Configuration Is Self Contained And Does Not Rely On User Level Settings

Instruction files SHOULD instructions that depend on user-level settings break for team members who haven't configured them — project config should be self-contained

## Pass / Fail

### Pass

````
Don't rely on user-level settings — keep project config self-contained
# === SEMANTIC JUDGMENT REQUIRED ===
# Write content satisfying all prior M/D checks,
# but testing the specific semantic question at this stage.
# One judgment call per rule — do not generate.
````

### Fail

````
(File does not exist at expected path)
````

## Limitations


