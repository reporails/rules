---
id: CORE:X:0002
slug: tech-stack-declared
title: Tech Stack Declared
category: context_quality
type: deterministic
level: L4
backed_by:
- agent-readmes-empirical-study
- agentic-coding-adoption-github
- agents-md-impact-efficiency
- awesome-copilot-meta-instructions
- claude-md-optimization-study
- codex-exec-plans
- copilot-ai-best-practices-vscode
- copilot-coding-agent-best-practices
- copilot-coding-agent-results
- copilot-coding-agent-tasks
- copilot-custom-instructions
- copilot-custom-instructions-vscode
- developer-context-cursor-study
- dometrain-claude-md-guide
- fowler-context-engineering-agents
- fowler-pushing-ai-autonomy
- instruction-limits-principles
- microsoft-awesome-copilot-blog
- openai-community-agents-md-optimization
- osmani-ai-coding-workflow
- prompthub-cursor-rules-analysis
- sewell-agents-md-tips
- spec-writing-for-agents
- using-claude-md-files
targets: '{{main_instruction_file}}'
checks:
- id: CORE.X.0002.file_in_scope
  type: mechanical
  severity: high
  name: file_in_scope
  check: file_exists
- id: CORE.X.0002.has_tech_declarations
  type: deterministic
  severity: high
  name: has_tech_declarations
- id: CORE.X.0002.has_version_specifics
  type: deterministic
  severity: high
  name: has_version_specifics
---

# Tech Stack Declared

Instruction files MUST agents need to know which languages and frameworks are in use to generate correct code

## Pass / Fail

### Pass

````
This project uses Python and FastAPI.
Built with PostgreSQL and Redis.
Python 3.12, Node 20, React 18.2.0
````

### Fail

````
# Tech Stack
This project uses a modern web framework.
Built with a SQL database and caching layer.
````

## Limitations


