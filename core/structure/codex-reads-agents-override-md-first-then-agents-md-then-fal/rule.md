---
id: CORE:S:0034
slug: codex-reads-agents-override-md-first-then-agents-md-then-fal
title: Codex Reads Agents.Override.Md First, Then Agents.Md, Then Fallback 
  Filenames Per Directory Root To Cwd
category: structure
type: deterministic
level: L2
backed_by:
- codex-agent-loop
- codex-agents-md
- codex-prompting-guide
- codex-skills-guide
- openai-codex-own-agents-md
targets: '{{main_instruction_file}}'
checks:
- id: CORE.S.0034.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.S.0034.discovery_chain_documented
  type: deterministic
  severity: medium
  name: discovery_chain_documented
---

# Codex Reads Agents.Override.Md First, Then Agents.Md, Then Fallback Filenames Per Directory Root To Cwd

Codex instruction file discovery SHOULD follow the override-then-fallback chain per directory

## Pass / Fail

### Pass

````
Codex checks AGENTS.override.md first, then AGENTS.md, then fallback filenames
````

### Fail

````
# Instruction file content
````

## Limitations


