---
id: CORE:C:0026
slug: cross-agent-compatibility
title: Cross-Agent Compatibility
category: content
type: semantic
level: L5
backed_by:
- agentic-coding-adoption-github
- agents-md-spec
- building-skills-for-claude
- claude-md-guide
- claude-md-optimization-study
- claudemd-best-practices-backbone-yml-pattern
- codex-developers-2025
- copilot-coding-agent-results
- copilot-custom-instructions-vscode
- enterprise-claude-usage
- fowler-pushing-ai-autonomy
- microsoft-awesome-copilot-blog
- osmani-ai-coding-workflow
- sewell-codex-vs-claude
targets: '{{main_instruction_file}}'
checks:
- id: CORE.C.0026.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.C.0026.extract_compat_content
  type: deterministic
  severity: medium
  name: extract_compat_content
- id: CORE.C.0026.compat_is_substantive
  type: semantic
  severity: medium
  name: compat_is_substantive
question: Does the file take concrete steps toward cross-agent compatibility?
criteria:
- Uses agent-neutral terminology or provides agent-specific sections separately
- Instructions could be followed by multiple different coding agents
choices:
- value: pass
  label: Passes
- value: fail
  label: Fails
pass_value: pass
---

# Cross-Agent Compatibility

Instruction files SHOULD portable instructions reduce maintenance burden when switching or using multiple coding agents

## Pass / Fail

### Pass

````
Cross-agent compatible: avoid agent-specific syntax.
AGENT_NAME should be parameterized.
# === SEMANTIC JUDGMENT REQUIRED ===
# Write content satisfying all prior M/D checks,
# but testing the specific semantic question at this stage.
# One judgment call per rule — do not generate.
````

### Fail

````
(File does not exist at expected path)
````

## Limitations


