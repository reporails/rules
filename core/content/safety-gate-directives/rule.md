---
id: CORE:C:0022
slug: safety-gate-directives
title: Safety Gate Directives
category: content
type: deterministic
level: L3
backed_by:
- agent-readmes-empirical-study
- agentic-coding-adoption-github
- claude-4-best-practices
- claude-code-hooks
- claude-code-issue-13579
- codex-agents-md
- codex-exec-plans
- codex-introducing
- codex-prompting-guide
- codex-skills-shell-compaction
- copilot-about-coding-agent
- copilot-cli-best-practices
- copilot-coding-agent-tasks
- developer-context-cursor-study
- enterprise-claude-usage
- fowler-pushing-ai-autonomy
- openai-codex-own-agents-md
- openai-community-agents-md-optimization
- osmani-ai-coding-workflow
- sewell-agents-md-tips
- spec-writing-for-agents
targets: '{{main_instruction_file}}'
checks:
- id: CORE.C.0022.file_in_scope
  type: mechanical
  severity: high
  name: file_in_scope
  check: file_exists
- id: CORE.C.0022.discusses_risky_operations
  type: deterministic
  severity: high
  name: discusses_risky_operations
- id: CORE.C.0022.has_safety_directives
  type: deterministic
  severity: high
  name: has_safety_directives
---

# Safety Gate Directives

Instruction files MUST agents must ask before destructive operations — without safety gates they delete, overwrite, or push without checking

## Pass / Fail

### Pass

````
Require confirmation before risky actions like deletions or force-pushes
````

### Fail

````
# Operations
Use git push to deploy changes.
Use rm to clean artifacts.
````

## Limitations


