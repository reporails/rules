---
id: CORE:S:0018
slug: skill-directory-names-follow-kebab-case-convention
title: Skill Directory Names Follow Kebab Case Convention
category: structure
type: deterministic
level: L2
backed_by:
- building-skills-for-claude
targets: '{{skill_entry_file}}'
checks:
- id: CORE.S.0018.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.S.0018.kebab_case_names
  type: deterministic
  severity: medium
  name: kebab_case_names
---

# Skill Directory Names Follow Kebab Case Convention

Instruction files SHOULD consistent naming conventions prevent lookup failures and improve discoverability across the skill system

## Pass / Fail

### Pass

````
Name skill directories in kebab-case (e.g., extract-claims, admit-source)
````

### Fail

````
# Instruction file content
````

## Limitations


