---
id: CORE:S:0011
slug: child-nested-instruction-files-extend-parent-scope-without-c
title: Child/Nested Instruction Files Extend Parent Scope Without Creating 
  Contradictions
category: structure
type: semantic
level: L2
backed_by:
- agents-md-spec
- claude-code-memory
- claude-code-settings
- codex-agents-md
- codex-introducing
- codex-prompting-guide
- codex-skills-guide
- copilot-custom-instructions
- copilot-custom-instructions-vscode
- openai-codex-own-agents-md
- openai-community-agents-md-optimization
- rules-directory-mechanics
- sewell-agents-md-tips
targets: '{{supplementary_files}}'
checks:
- id: CORE.S.0011.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.S.0011.extract_override_content
  type: deterministic
  severity: medium
  name: extract_override_content
- id: CORE.S.0011.no_contradictions
  type: semantic
  severity: medium
  name: no_contradictions
question: Do nested instruction files extend parent scope without contradicting 
  parent rules?
criteria:
- Child files add specificity, they don't reverse parent directives
- No conflicting MUST/MUST NOT between parent and child scopes
choices:
- value: pass
  label: Passes
- value: fail
  label: Fails
pass_value: pass
---

# Child/Nested Instruction Files Extend Parent Scope Without Creating Contradictions

Instruction files SHOULD instruction file inheritance should be additive — child files that contradict parents create unpredictable behavior

## Pass / Fail

### Pass

````
Child CLAUDE.md files add to parent rules, they don't override them
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


