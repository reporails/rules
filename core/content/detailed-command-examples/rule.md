---
id: CORE:C:0020
slug: detailed-command-examples
title: Detailed Command Examples
category: content
type: deterministic
level: L4
backed_by:
- agent-readmes-empirical-study
- builder-ai-instruction-best-practices
- building-skills-for-claude
- claude-4-best-practices
- claude-md-guide
- claude-md-optimization-study
- codex-exec-plans
- codex-prompting-guide
- copilot-coding-agent-best-practices
- copilot-coding-agent-results
- copilot-coding-agent-tasks
- copilot-custom-instructions
- dometrain-claude-md-guide
- openai-community-agents-md-optimization
- sewell-agents-md-tips
- spec-writing-for-agents
- using-claude-md-files
targets: '{{main_instruction_file}}'
checks:
- id: CORE.C.0020.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.C.0020.mentions_tools
  type: deterministic
  severity: medium
  name: mentions_tools
- id: CORE.C.0020.has_detailed_commands
  type: deterministic
  severity: medium
  name: has_detailed_commands
---

# Detailed Command Examples

Instruction files SHOULD tool names alone cause agents to guess at flags — full invocations prevent argument errors

## Pass / Fail

### Pass

````
Include full executable commands with flags, not just tool names
npm install --save-dev
git commit --no-verify
docker build --no-cache
````

### Fail

````
# Tools
Use npm for package management.
Use docker for containers.
````

## Limitations


