---
id: CLAUDE:S:0001
slug: skill-folder-does-not-contain-readme-md-all-documentation-go
title: Skill Folder Does Not Contain Readme.Md — All Documentation Goes In 
  Skill.Md
category: structure
type: mechanical
level: L1
backed_by:
- building-skills-for-claude
targets: '{{skills_dir}}/**/*.md'
checks:
- id: CLAUDE.S.0001.skill_dir_exists
  type: mechanical
  severity: high
  name: skill_dir_exists
  check: glob_match
- id: CLAUDE.S.0001.no_readme
  type: mechanical
  severity: high
  name: no_readme
  check: file_absent
  args:
    pattern: README.md
---

# Skill Folder Does Not Contain Readme.Md — All Documentation Goes In Skill.Md

Skill directories MUST NOT contain a README.md file

## Pass / Fail

### Pass

````

````

### Fail

````
(File does not exist at expected path)
````

## Limitations


