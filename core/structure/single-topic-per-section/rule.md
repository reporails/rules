---
id: CORE:S:0023
slug: single-topic-per-section
title: Single Topic Per Section
category: structure
type: semantic
level: L2
backed_by:
- building-skills-for-claude
- claude-code-memory
- codex-exec-plans
- codex-skills-guide
- copilot-custom-instructions-vscode
- developer-context-cursor-study
- lost-in-the-middle-long-contexts
- openai-community-agents-md-optimization
- rules-directory-mechanics
- spec-writing-for-agents
targets: '{{instruction_files}}'
checks:
- id: CORE.S.0023.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.S.0023.extract_sections
  type: deterministic
  severity: medium
  name: extract_sections
- id: CORE.S.0023.sections_are_focused
  type: semantic
  severity: medium
  name: sections_are_focused
question: Does each section heading describe a single coherent topic, and does 
  the content under it stay on that topic?
criteria:
- Section headings name a specific concern (commands, testing, architecture) not
  vague labels
- Content under each heading relates to that heading's topic
- No section mixes unrelated concerns (e.g., build commands mixed with coding 
  style)
choices:
- value: pass
  label: Passes
- value: fail
  label: Fails
pass_value: pass
---

# Single Topic Per Section

Instruction files SHOULD mixed-concern sections confuse agents about which instruction applies to which context

## Pass / Fail

### Pass

````
Rule files should focus on one topic per file
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


