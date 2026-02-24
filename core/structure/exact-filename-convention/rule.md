---
id: CORE:S:0004
slug: exact-filename-convention
title: Exact Filename Convention
category: structure
type: mechanical
level: L1
backed_by:
- agent-readmes-empirical-study
- agentic-coding-adoption-github
- agents-md-spec
- builder-ai-instruction-best-practices
- building-skills-for-claude
- claude-code-settings
- claude-md-guide
- claude-md-optimization-study
- codex-agent-loop
- codex-agents-md
- codex-developers-2025
- codex-exec-plans
- codex-introducing
- codex-skills-guide
- copilot-cli-best-practices
- copilot-coding-agent-best-practices
- copilot-coding-agent-results
- copilot-coding-agent-tasks
- copilot-custom-instructions
- copilot-custom-instructions-vscode
- enterprise-claude-usage
- evaluating-agents-md
- fowler-context-engineering-agents
- instruction-limits-principles
- microsoft-awesome-copilot-blog
- openai-codex-own-agents-md
- osmani-ai-coding-workflow
- sewell-agents-md-tips
- sewell-codex-vs-claude
- spec-writing-for-agents
- using-claude-md-files
targets: '{{main_instruction_file}}'
checks:
- id: CORE.S.0004.filename_matches_convention
  type: mechanical
  severity: high
  name: filename_matches_convention
  check: filename_matches_pattern
  args:
    pattern: (?i)^(CLAUDE|AGENTS)\.md$
---

# Exact Filename Convention

Instruction files MUST agent discovery depends on exact filenames — wrong case or name means the agent never reads it

## Pass / Fail

### Pass

````

````

### Fail

````
(File does not exist at expected path)
````

## Limitations


