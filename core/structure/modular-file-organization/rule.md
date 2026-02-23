---
id: CORE:S:0010
slug: modular-file-organization
title: Modular File Organization
category: structure
type: mechanical
level: L1
backed_by:
- agents-md-impact-efficiency
- builder-ai-instruction-best-practices
- claude-code-memory
- claude-md-guide
- claudemd-best-practices-mermaid-for-workflows
- copilot-ai-best-practices-vscode
- copilot-coding-agent-best-practices
- copilot-coding-agent-tasks
- copilot-custom-instructions
- copilot-custom-instructions-vscode
- fowler-context-engineering-agents
- instruction-limits-principles
- rules-directory-mechanics
- spec-writing-for-agents
targets: '{{main_instruction_file}}'
checks:
- id: CORE.S.0010.multiple_files_present
  type: mechanical
  severity: medium
  name: multiple_files_present
  check: glob_count
  args:
    pattern: '{{instruction_files}}'
    min: 2
---

# Modular File Organization

Instruction files SHOULD splitting concerns across multiple dedicated files is better than one large file

## Pass / Fail

### Pass

````

````

### Fail

````
(File does not exist at expected path)
````

## Limitations


