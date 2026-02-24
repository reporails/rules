---
id: CORE:S:0008
slug: expected-directories-exist
title: Expected Directories Exist
category: structure
type: mechanical
level: L2
backed_by:
- agentic-coding-adoption-github
- awesome-copilot-meta-instructions
- builder-ai-instruction-best-practices
- building-skills-for-claude
- claude-code-memory
- claude-code-settings
- claude-md-guide
- codex-eval-skills
- codex-skills-guide
- copilot-coding-agent-best-practices
- copilot-coding-agent-results
- copilot-coding-agent-tasks
- copilot-custom-instructions
- copilot-custom-instructions-vscode
- developer-context-cursor-study
- fowler-context-engineering-agents
- microsoft-awesome-copilot-blog
- rules-directory-mechanics
- using-claude-md-files
targets: '{{main_instruction_file}}'
checks:
- id: CORE.S.0008.expected_directory_exists
  type: mechanical
  severity: medium
  name: expected_directory_exists
  check: glob_match
---

# Expected Directories Exist

Instruction files SHOULD modular files (rules, skills, hooks) must be organized in specific named directories

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


