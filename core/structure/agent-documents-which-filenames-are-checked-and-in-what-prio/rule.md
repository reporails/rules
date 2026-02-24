---
id: CORE:S:0012
slug: agent-documents-which-filenames-are-checked-and-in-what-prio
title: Agent Documents Which Filenames Are Checked And In What Priority Order
category: structure
type: deterministic
level: L2
backed_by:
- agents-md-spec
- claude-code-memory
- codex-agents-md
- codex-prompting-guide
- copilot-custom-instructions-vscode
- openai-codex-own-agents-md
targets: '{{main_instruction_file}}'
checks:
- id: CORE.S.0012.discovery_documented
  type: deterministic
  severity: medium
  name: discovery_documented
---

# Agent Documents Which Filenames Are Checked And In What Priority Order

Instruction files SHOULD when agents support multiple instruction filenames (instruction file, TEAM_GUIDE.md, .agents.md), authors need to know which file takes priority to avoid configuration confusion

## Pass / Fail

### Pass

````
## Discovery Order

1. Root instruction file
2. Scoped rules
3. Skills
````

### Fail

````
# Instruction file content
````

## Limitations


