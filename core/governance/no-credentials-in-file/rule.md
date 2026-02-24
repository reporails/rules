---
id: CORE:G:0002
slug: no-credentials-in-file
title: No Credentials in File
category: governance
type: deterministic
level: L1
backed_by:
- advanced-context-engineering
- agent-readmes-empirical-study
- building-skills-for-claude
- claude-code-settings
- codex-skills-shell-compaction
- copilot-about-coding-agent
- copilot-ai-best-practices-vscode
- copilot-cli-best-practices
- dometrain-claude-md-guide
- openai-community-agents-md-optimization
- spec-writing-for-agents
- using-claude-md-files
targets: '{{instruction_files}}'
checks:
- id: CORE.G.0002.file_in_scope
  type: mechanical
  severity: high
  name: file_in_scope
  check: file_exists
- id: CORE.G.0002.no_secret_patterns
  type: deterministic
  severity: high
  name: no_secret_patterns
- id: CORE.G.0002.no_token_strings
  type: deterministic
  severity: high
  name: no_token_strings
---

# No Credentials in File

Instruction files MUST instruction files are committed to version control and must never contain secrets

## Pass / Fail

### Pass

````
# Instruction file
````

### Fail

````
# Instruction file content
api_key = AKIAIOSFODNN7EXAMPLE1
ghp_ABCDEFGHIJKLMNOPQRSTuvwxyz1234
````

## Limitations


