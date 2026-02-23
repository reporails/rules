---
id: CORE:C:0013
slug: project-description-present
title: Project Description Present
category: content
type: deterministic
level: L2
backed_by:
- agent-readmes-empirical-study
- agentic-coding-adoption-github
- agents-md-impact-efficiency
- agents-md-spec
- awesome-copilot-meta-instructions
- building-skills-for-claude
- claude-md-guide
- codex-exec-plans
- copilot-about-coding-agent
- copilot-coding-agent-best-practices
- copilot-coding-agent-results
- copilot-coding-agent-tasks
- copilot-custom-instructions
- copilot-custom-instructions-vscode
- developer-context-cursor-study
- evaluating-agents-md
- instruction-limits-principles
- microsoft-awesome-copilot-blog
- openai-community-agents-md-optimization
- osmani-ai-coding-workflow
- spec-writing-for-agents
targets: '{{main_instruction_file}}'
checks:
- id: CORE.C.0013.file_in_scope
  type: mechanical
  severity: high
  name: file_in_scope
  check: file_exists
- id: CORE.C.0013.has_project_description
  type: deterministic
  severity: high
  name: has_project_description
---

# Project Description Present

Instruction files MUST agents need to understand the project's purpose and scope before making changes

## Pass / Fail

### Pass

````
## Project Overview

This project is a REST API for user management.
````

### Fail

````
# Instruction file content
````

## Limitations


