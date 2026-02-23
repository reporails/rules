---
id: CORE:E:0001
slug: total-instruction-file-size-including-imports-stays-within-r
title: Total Instruction File Size (Including Imports) Stays Within Reasonable 
  Limits
category: efficiency
type: mechanical
level: L1
backed_by:
- advanced-context-engineering
- agents-md-impact-efficiency
- building-skills-for-claude
- claude-4-best-practices
- claude-context-windows
- codex-agent-loop
- codex-agents-md
- codex-prompting-guide
- developer-context-cursor-study
- fowler-context-engineering-agents
- lost-in-the-middle-long-contexts
- openai-codex-own-agents-md
- osmani-ai-coding-workflow
- spec-writing-for-agents
targets: '{{instruction_files}}'
checks:
- id: CORE.E.0001.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.E.0001.total_size_check
  type: mechanical
  severity: medium
  name: total_size_check
  check: aggregate_byte_size
  args:
    pattern: '{{instruction_files}}'
---

# Total Instruction File Size (Including Imports) Stays Within Reasonable Limits

Instruction files SHOULD agents have finite context windows — instruction files that consume too much context leave less room for code and conversation

## Pass / Fail

### Pass

````
# Instruction file
````

### Fail

````
(File does not exist at expected path)
````

## Limitations


