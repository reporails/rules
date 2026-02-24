---
id: CORE:E:0004
slug: static-stable-content-appears-before-dynamic-variable-conten
title: Static/Stable Content Appears Before Dynamic/Variable Content In The 
  Instruction File
category: efficiency
type: semantic
level: L2
backed_by:
- building-skills-for-claude
- claudemd-best-practices-backbone-yml-pattern
- codex-agent-loop
- codex-prompting-guide
- codex-skills-guide
- codex-skills-shell-compaction
- fowler-pushing-ai-autonomy
- lost-in-the-middle-long-contexts
- monorepo-claude-md-organization
- spec-writing-for-agents
targets: '{{main_instruction_file}}'
checks:
- id: CORE.E.0004.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.E.0004.extract_sections
  type: deterministic
  severity: medium
  name: extract_sections
- id: CORE.E.0004.static_before_dynamic
  type: semantic
  severity: medium
  name: static_before_dynamic
question: Is stable/static content placed before dynamic/frequently-changing 
  content?
criteria:
- Project description, tech stack, and style guides appear early
- Session-specific, variable, or frequently-updated content appears later
choices:
- value: pass
  label: Passes
- value: fail
  label: Fails
pass_value: pass
---

# Static/Stable Content Appears Before Dynamic/Variable Content In The Instruction File

Instruction files SHOULD placing static content first maximizes prompt cache hit rates — content that changes frequently should be near the end

## Pass / Fail

### Pass

````
Put stable instructions at the top — they get cached across sessions
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


