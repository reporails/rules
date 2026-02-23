---
id: CORE:X:0003
slug: directory-layout-documented
title: Directory Layout Documented
category: context_quality
type: deterministic
level: L2
backed_by:
- agent-readmes-empirical-study
- agentic-coding-adoption-github
- agents-md-impact-efficiency
- awesome-copilot-meta-instructions
- building-skills-for-claude
- claude-md-optimization-study
- claudemd-best-practices-backbone-yml-pattern
- codex-exec-plans
- codex-introducing
- copilot-coding-agent-best-practices
- copilot-coding-agent-results
- copilot-coding-agent-tasks
- copilot-custom-instructions
- developer-context-cursor-study
- dometrain-claude-md-guide
- evaluating-agents-md
- fowler-pushing-ai-autonomy
- instruction-limits-principles
- sewell-agents-md-tips
- spec-writing-for-agents
- using-claude-md-files
targets: '{{main_instruction_file}}'
checks:
- id: CORE.X.0003.file_in_scope
  type: mechanical
  severity: high
  name: file_in_scope
  check: file_exists
- id: CORE.X.0003.has_directory_notation
  type: deterministic
  severity: high
  name: has_directory_notation
---

# Directory Layout Documented

Instruction files MUST agents waste time exploring when a directory map is provided — explicit structure prevents wrong file placement

## Pass / Fail

### Pass

````
```
src/
  components/
  utils/
tests/
  unit/
```
````

### Fail

````
(File does not exist at expected path)
````

## Limitations


