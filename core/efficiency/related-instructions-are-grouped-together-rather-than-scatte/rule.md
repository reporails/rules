---
id: CORE:E:0005
slug: related-instructions-are-grouped-together-rather-than-scatte
title: Related Instructions Are Grouped Together Rather Than Scattered 
  Throughout The File
category: efficiency
type: semantic
level: L2
backed_by:
- claude-md-guide
- spec-writing-for-agents
targets: '{{main_instruction_file}}'
checks:
- id: CORE.E.0005.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.E.0005.extract_all_content
  type: deterministic
  severity: medium
  name: extract_all_content
- id: CORE.E.0005.instructions_consolidated
  type: semantic
  severity: medium
  name: instructions_consolidated
question: Are related instructions grouped together rather than scattered across
  unrelated sections?
criteria:
- Testing instructions appear in one place, not scattered
- Style/formatting rules are consolidated, not repeated in multiple sections
choices:
- value: pass
  label: Passes
- value: fail
  label: Fails
pass_value: pass
---

# Related Instructions Are Grouped Together Rather Than Scattered Throughout The File

Instruction files SHOULD scattered discrete instructions increase cognitive load and context consumption — consolidating related guidance improves comprehension

## Pass / Fail

### Pass

````
Group related instructions together rather than scattering them
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


