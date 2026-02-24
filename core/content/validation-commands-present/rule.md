---
id: CORE:C:0008
slug: validation-commands-present
title: Validation Commands Present
category: content
type: deterministic
level: L4
backed_by:
- advanced-context-engineering
- agent-readmes-empirical-study
- agents-md-spec
- awesome-copilot-meta-instructions
- builder-ai-instruction-best-practices
- building-skills-for-claude
- claude-4-best-practices
- claude-code-hooks
- claude-code-issue-13579
- codex-agents-md
- codex-eval-skills
- codex-exec-plans
- codex-introducing
- copilot-ai-best-practices-vscode
- copilot-cli-best-practices
- copilot-coding-agent-best-practices
- copilot-coding-agent-results
- copilot-coding-agent-tasks
- copilot-custom-instructions
- developer-context-cursor-study
- enterprise-claude-usage
- fowler-pushing-ai-autonomy
- instruction-limits-principles
- openai-codex-own-agents-md
- openai-community-agents-md-optimization
- osmani-ai-coding-workflow
- prompthub-cursor-rules-analysis
- sewell-agents-md-tips
- spec-writing-for-agents
targets: '{{main_instruction_file}}'
checks:
- id: CORE.C.0008.file_in_scope
  type: mechanical
  severity: high
  name: file_in_scope
  check: file_exists
- id: CORE.C.0008.mentions_checking
  type: deterministic
  severity: high
  name: mentions_checking
- id: CORE.C.0008.has_validation_section
  type: deterministic
  severity: high
  name: has_validation_section
---

# Validation Commands Present

Instruction files MUST agents need self-check commands to validate work — without them they skip verification

## Pass / Fail

### Pass

````
Run these checks before pushing code
````

### Fail

````
# Quality Assurance
Run tests regularly during development.
````

## Limitations


