---
id: CORE:C:0025
slug: output-format-specified
title: Output Format Specified
category: content
type: deterministic
level: L3
backed_by:
- agent-readmes-empirical-study
- building-skills-for-claude
- claude-4-best-practices
- claude-code-issue-13579
- codex-introducing
- codex-prompting-guide
- developer-context-cursor-study
- fowler-pushing-ai-autonomy
- prompthub-cursor-rules-analysis
targets: '{{instruction_files}}'
checks:
- id: CORE.C.0025.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.C.0025.discusses_agent_output
  type: deterministic
  severity: medium
  name: discusses_agent_output
- id: CORE.C.0025.has_format_directives
  type: deterministic
  severity: medium
  name: has_format_directives
---

# Output Format Specified

Instruction files SHOULD agents without output guidance produce inconsistent formatting — explicit format specs ensure predictable responses

## Pass / Fail

### Pass

````
Specify output formatting requirements like templates and response languages
Output format as JSON.
Response should use bullet points.
````

### Fail

````
# Data
Support both json and yaml configuration files.
````

## Limitations


