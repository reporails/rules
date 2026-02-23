---
id: CORE:S:0018
slug: self-contained-skills
title: Self-Contained Skills
category: structure
type: deterministic
level: L6
backed_by:
- building-skills-for-claude
- claude-code-settings
- codex-agent-loop
- codex-developers-2025
- codex-eval-skills
- codex-skills-guide
- codex-skills-shell-compaction
- enterprise-claude-usage
- fowler-context-engineering-agents
- fowler-pushing-ai-autonomy
- microsoft-awesome-copilot-blog
- osmani-ai-coding-workflow
targets: '{{skills_dir}}/**/*.md'
checks:
- id: CORE.S.0018.skill_dir_exists
  type: mechanical
  severity: medium
  name: skill_dir_exists
  check: glob_match
- id: CORE.S.0018.has_skill_entry_point
  type: deterministic
  severity: medium
  name: has_skill_entry_point
---

# Self-Contained Skills

Instruction files SHOULD reusable skills reduce duplication and ensure consistent behavior across invocations

## Pass / Fail

### Pass

````
## Process

1. Read the input
2. Validate format

## Inputs

File path
````

### Fail

````
# Instruction file content
````

## Limitations


