---
id: CORE:E:0003
slug: non-redundant-content
title: Non-Redundant Content
category: efficiency
type: semantic
level: L5
backed_by:
- agent-readmes-empirical-study
- agents-md-spec
- awesome-copilot-meta-instructions
- builder-ai-instruction-best-practices
- building-skills-for-claude
- claude-4-best-practices
- claude-md-guide
- codex-exec-plans
- codex-introducing
- codex-prompting-guide
- codex-skills-shell-compaction
- copilot-ai-best-practices-vscode
- copilot-custom-instructions-vscode
- developer-context-cursor-study
- dometrain-claude-md-guide
- enterprise-claude-usage
- evaluating-agents-md
- fowler-assessing-quality-agents
- fowler-context-engineering-agents
- fowler-pushing-ai-autonomy
- instruction-limits-principles
- microsoft-awesome-copilot-blog
- openai-community-agents-md-optimization
- prompthub-cursor-rules-analysis
- sewell-agents-md-tips
- spec-writing-for-agents
- using-claude-md-files
targets: '{{instruction_files}}'
checks:
- id: CORE.E.0003.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.E.0003.extract_potentially_redundant
  type: deterministic
  severity: medium
  name: extract_potentially_redundant
- id: CORE.E.0003.no_large_dependency_block
  type: mechanical
  severity: medium
  name: no_large_dependency_block
  check: count_at_most
- id: CORE.E.0003.redundancy_judgment
  type: semantic
  severity: medium
  name: redundancy_judgment
question: Does the file avoid duplicating information that would be in README, 
  package.json, or similar project configuration files?
criteria:
- Content provides agent-specific context that enhances behavior beyond what 
  generic docs say
- Dependency or installation information is referenced, not copy-pasted
- References to external docs use @imports rather than inlining their content
choices:
- value: pass
  label: Passes
- value: fail
  label: Fails
pass_value: pass
---

# Non-Redundant Content

Instruction files SHOULD duplicated content causes drift when one copy is updated and the other is not

## Pass / Fail

### Pass

````
This project uses numpy and pandas.
# === SEMANTIC JUDGMENT REQUIRED ===
# Write content satisfying all prior M/D checks,
# but testing the specific semantic question at this stage.
# One judgment call per rule — do not generate.
````

### Fail

````
# Project Guidelines
Write clean code with good variable names.
Add tests for new features.
````

## Limitations


