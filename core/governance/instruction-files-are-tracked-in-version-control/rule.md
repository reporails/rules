---
id: CORE:G:0001
slug: instruction-files-are-tracked-in-version-control
title: Instruction Files Are Tracked In Version Control
category: governance
type: mechanical
level: L1
backed_by:
- advanced-context-engineering
- agent-readmes-empirical-study
- agentic-coding-adoption-github
- agents-md-impact-efficiency
- agents-md-spec
- building-skills-for-claude
- claude-code-issue-13579
- claude-code-memory
- claude-code-settings
- claude-md-guide
- copilot-custom-instructions-vscode
- dometrain-claude-md-guide
- openai-codex-own-agents-md
- openai-community-agents-md-optimization
- rules-directory-mechanics
- spec-writing-for-agents
- using-claude-md-files
targets: '{{instruction_files}}'
checks:
- id: CORE.G.0001.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.G.0001.file_tracked
  type: mechanical
  severity: medium
  name: file_tracked
  check: git_tracked
---

# Instruction Files Are Tracked In Version Control

Instruction files SHOULD instruction files should be committed to the repository so all team members and CI systems use the same agent configuration

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


