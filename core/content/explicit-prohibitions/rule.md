---
id: CORE:C:0019
slug: explicit-prohibitions
title: Explicit Prohibitions
category: content
type: deterministic
level: L3
backed_by:
- agent-readmes-empirical-study
- agents-md-impact-efficiency
- builder-ai-instruction-best-practices
- building-skills-for-claude
- claude-4-best-practices
- claude-code-issue-13579
- claude-md-guide
- claudemd-best-practices-backbone-yml-pattern
- codex-agents-md
- codex-introducing
- codex-prompting-guide
- codex-skills-shell-compaction
- copilot-about-coding-agent
- copilot-coding-agent-tasks
- developer-context-cursor-study
- enterprise-claude-usage
- fowler-pushing-ai-autonomy
- openai-codex-own-agents-md
- openai-community-agents-md-optimization
- osmani-ai-coding-workflow
- prompthub-cursor-rules-analysis
- sewell-agents-md-tips
- spec-writing-for-agents
- using-claude-md-files
targets: '{{instruction_files}}'
checks:
- id: CORE.C.0019.file_in_scope
  type: mechanical
  severity: high
  name: file_in_scope
  check: file_exists
- id: CORE.C.0019.has_negative_directives
  type: deterministic
  severity: high
  name: has_negative_directives
---

# Explicit Prohibitions

Instruction files MUST agents without prohibitions repeat common mistakes — explicit don'ts prevent known failure modes

## Pass / Fail

### Pass

````
Don't commit directly to main.
Never force-push to shared branches.
MUST NOT deploy without passing CI.
````

### Fail

````
# Project Guidelines
Follow the coding standards.
Review all pull requests before merging.
````

## Limitations


