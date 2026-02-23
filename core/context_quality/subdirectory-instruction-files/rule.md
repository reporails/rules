---
id: CORE:X:0004
slug: subdirectory-instruction-files
title: Subdirectory Instruction Files
category: context_quality
type: mechanical
level: L3
backed_by:
- agents-md-impact-efficiency
- agents-md-spec
- builder-ai-instruction-best-practices
- claude-code-memory
- claude-md-guide
- codex-agent-loop
- codex-agents-md
- codex-eval-skills
- codex-introducing
- copilot-cli-best-practices
- copilot-coding-agent-best-practices
- copilot-coding-agent-results
- copilot-coding-agent-tasks
- copilot-custom-instructions
- copilot-custom-instructions-vscode
- instruction-limits-principles
- monorepo-claude-md-organization
- openai-codex-own-agents-md
- openai-community-agents-md-optimization
- sewell-agents-md-tips
- spec-writing-for-agents
- using-claude-md-files
targets: '{{instruction_files}}'
checks:
- id: CORE.X.0004.subdir_instruction_exists
  type: mechanical
  severity: low
  name: subdir_instruction_exists
  check: glob_match
---

# Subdirectory Instruction Files

Instruction files MAY monorepos require subdirectory-level instruction files for subproject-specific context

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


