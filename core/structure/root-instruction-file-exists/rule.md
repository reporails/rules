---
id: CORE:S:0007
slug: root-instruction-file-exists
title: Root Instruction File Exists
category: structure
type: mechanical
level: L1
backed_by:
- agentic-coding-adoption-github
- agents-md-impact-efficiency
- agents-md-spec
- builder-ai-instruction-best-practices
- claude-code-memory
- claude-code-settings
- claude-md-guide
- claude-md-optimization-study
- claudemd-best-practices-backbone-yml-pattern
- codex-agents-md
- codex-developers-2025
- codex-exec-plans
- codex-introducing
- copilot-cli-best-practices
- copilot-coding-agent-best-practices
- copilot-coding-agent-results
- copilot-coding-agent-tasks
- copilot-custom-instructions
- copilot-custom-instructions-vscode
- dometrain-claude-md-guide
- enterprise-claude-usage
- evaluating-agents-md
- fowler-context-engineering-agents
- instruction-limits-principles
- microsoft-awesome-copilot-blog
- openai-codex-own-agents-md
- openai-community-agents-md-optimization
- prompthub-cursor-rules-analysis
- rules-directory-mechanics
- sewell-agents-md-tips
- spec-writing-for-agents
- using-claude-md-files
targets: '{{main_instruction_file}}'
checks:
- id: CORE.S.0007.file_exists_at_root
  type: mechanical
  severity: high
  name: file_exists_at_root
  check: file_exists
---

# Root Instruction File Exists

Instruction files MUST instruction files must be placed at the repository root so the agent discovers them

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


