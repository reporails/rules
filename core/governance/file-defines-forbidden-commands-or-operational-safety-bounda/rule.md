---
id: CORE:G:0004
slug: file-defines-forbidden-commands-or-operational-safety-bounda
title: File Defines Forbidden Commands Or Operational Safety Boundaries
category: governance
type: deterministic
level: L2
backed_by:
- claude-4-best-practices
- claude-code-hooks
- claude-code-issue-13579
- codex-prompting-guide
- codex-skills-shell-compaction
- copilot-about-coding-agent
- spec-writing-for-agents
targets: '{{main_instruction_file}}'
checks:
- id: CORE.G.0004.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.G.0004.has_command_boundaries
  type: deterministic
  severity: medium
  name: has_command_boundaries
---

# File Defines Forbidden Commands Or Operational Safety Boundaries

Instruction files SHOULD aI agents have deleted production databases and wiped drives — explicit command boundaries prevent catastrophic irreversible actions

## Pass / Fail

### Pass

````
Define forbidden commands: rm -rf, DROP TABLE, force push to main
````

### Fail

````
(File does not exist at expected path)
````

## Limitations


