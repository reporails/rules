---
id: CORE:S:0015
slug: skill-entry-point-present
title: Skill Entry Point Present
category: structure
type: deterministic
level: L6
backed_by:
- building-skills-for-claude
- claude-code-settings
- codex-eval-skills
- codex-skills-guide
- codex-skills-shell-compaction
- enterprise-claude-usage
- fowler-context-engineering-agents
targets: '{{skill_entry_file}}'
checks:
- id: CORE.S.0015.skill_file_exists
  type: mechanical
  severity: medium
  name: skill_file_exists
  check: file_exists
- id: CORE.S.0015.has_required_sections
  type: deterministic
  severity: medium
  name: has_required_sections
---

# Skill Entry Point Present

Instruction files SHOULD skills should have a SKILL.md entry point with name, description, and process sections

## Pass / Fail

### Pass

````
## Name

commit

## Description

Create a git commit

## Process

1. Stage files
````

### Fail

````
# Instruction file content
````

## Limitations


