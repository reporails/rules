---
id: CORE:G:0003
slug: permissions-ordered
title: Permissions Ordered
category: governance
type: deterministic
level: L5
backed_by:
- building-skills-for-claude
- claude-code-settings
- copilot-cli-best-practices
- enterprise-claude-usage
targets: '{{main_instruction_file}}'
checks:
- id: CORE.G.0003.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.G.0003.has_permission_section
  type: deterministic
  severity: medium
  name: has_permission_section
---

# Permissions Ordered

Instruction files SHOULD ordered permissions help agents and reviewers quickly find the most relevant entries

## Pass / Fail

### Pass

````
Order allowed tools by how frequently they are used
````

### Fail

````
# Instruction file content
````

## Limitations


