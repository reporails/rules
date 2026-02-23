---
id: CORE:S:0031
slug: agent-memory-learned-context-is-stored-in-a-dedicated-direct
title: Agent Memory/Learned Context Is Stored In A Dedicated Directory, Not 
  Mixed Into Instruction Files
category: structure
type: deterministic
level: L2
backed_by:
- claude-code-memory
- copilot-about-coding-agent
targets: '{{memory_dir}}'
checks:
- id: CORE.S.0031.memory_dir_exists
  type: mechanical
  severity: medium
  name: memory_dir_exists
  check: directory_exists
- id: CORE.S.0031.memory_content_present
  type: deterministic
  severity: medium
  name: memory_content_present
---

# Agent Memory/Learned Context Is Stored In A Dedicated Directory, Not Mixed Into Instruction Files

Instruction files SHOULD mixing learned context with authored instructions makes files unstable — memory should persist in a separate directory agents can update without modifying instruction files

## Pass / Fail

### Pass

````
## Memory

Store patterns and conventions here.
````

### Fail

````
(File does not exist at expected path)
````

## Limitations


