---
id: CORE:S:0021
slug: the-name-field-in-skill-md-frontmatter-matches-the-containin
title: The Name Field In Skill.Md Frontmatter Matches The Containing Directory 
  Name (Kebab Case)
category: structure
type: deterministic
level: L2
backed_by:
- building-skills-for-claude
targets: '{{skills_dir}}/**/*.md'
checks:
- id: CORE.S.0021.skill_file_exists
  type: mechanical
  severity: medium
  name: skill_file_exists
  check: file_exists
- id: CORE.S.0021.name_matches_dir
  type: deterministic
  severity: medium
  name: name_matches_dir
---

# The Name Field In Skill.Md Frontmatter Matches The Containing Directory Name (Kebab Case)

Skill frontmatter name field SHOULD match the skill directory name

## Pass / Fail

### Pass

````
name: commit-helper
````

### Fail

````
# Instruction file content
````

## Limitations


