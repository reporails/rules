---
id: CLAUDE:S:0003
slug: skill-yaml-frontmatter-description-field-is-under-1024-chara
title: Skill Yaml Frontmatter Description Field Is Under 1024 Characters And 
  Contains No Xml Angle Brackets
category: structure
type: mechanical
level: L1
backed_by:
- building-skills-for-claude
targets: '{{skill_entry_file}}'
checks:
- id: CLAUDE.S.0003.skill_file_exists
  type: mechanical
  severity: high
  name: skill_file_exists
  check: file_exists
- id: CLAUDE.S.0003.description_length
  type: mechanical
  severity: high
  name: description_length
  check: byte_size
---

# Skill Yaml Frontmatter Description Field Is Under 1024 Characters And Contains No Xml Angle Brackets

Skill description in SKILL.md frontmatter MUST be under 1024 characters

## Pass / Fail

### Pass

````
# Instruction file
````

### Fail

````
(File does not exist at expected path)
````

## Limitations


