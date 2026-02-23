---
id: CORE:C:0010
slug: build-and-test-commands
title: Build and Test Commands
category: content
type: deterministic
level: L4
backed_by:
- agent-readmes-empirical-study
- agentic-coding-adoption-github
- agents-md-impact-efficiency
- agents-md-spec
- awesome-copilot-meta-instructions
- builder-ai-instruction-best-practices
- claude-code-memory
- claude-code-settings
- claude-md-guide
- claude-md-optimization-study
- codex-exec-plans
- codex-introducing
- copilot-about-coding-agent
- copilot-cli-best-practices
- copilot-coding-agent-best-practices
- copilot-coding-agent-results
- copilot-coding-agent-tasks
- copilot-custom-instructions
- developer-context-cursor-study
- dometrain-claude-md-guide
- evaluating-agents-md
- fowler-pushing-ai-autonomy
- instruction-limits-principles
- openai-community-agents-md-optimization
- osmani-ai-coding-workflow
- prompthub-cursor-rules-analysis
- sewell-agents-md-tips
- spec-writing-for-agents
- using-claude-md-files
targets: '{{main_instruction_file}}'
checks:
- id: CORE.C.0010.file_in_scope
  type: mechanical
  severity: high
  name: file_in_scope
  check: file_exists
- id: CORE.C.0010.has_command_invocations
  type: deterministic
  severity: high
  name: has_command_invocations
- id: CORE.C.0010.commands_in_code_blocks
  type: deterministic
  severity: high
  name: commands_in_code_blocks
---

# Build and Test Commands

Instruction files MUST agents need exact commands to verify their work — without them they guess or run wrong commands

## Pass / Fail

### Pass

````
npm run build
git push origin main
docker build -t app .
```
npm run build
```
````

### Fail

````
(File does not exist at expected path)
````

## Limitations


