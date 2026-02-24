---
id: CODEX:S:0002
slug: codex-skill-directory-contains-agents-openai-yaml-with-displ
title: Codex Skill Directory Contains Agents/Openai.Yaml With Display Name, 
  Icon, And Policy Fields
category: structure
type: deterministic
level: L2
backed_by:
- codex-skills-guide
targets: '{{skills_dir}}/**/*.md'
checks:
- id: CODEX.S.0002.skill_dir_exists
  type: mechanical
  severity: low
  name: skill_dir_exists
  check: glob_match
- id: CODEX.S.0002.has_openai_yaml
  type: deterministic
  severity: low
  name: has_openai_yaml
---

# Codex Skill Directory Contains Agents/Openai.Yaml With Display Name, Icon, And Policy Fields

Codex skills MAY include agents/openai.yaml for UI metadata and invocation policy

## Pass / Fail

### Pass

````
display_name: Code Review
allow_implicit_invocation: true
````

### Fail

````
# Instruction file content
````

## Limitations


