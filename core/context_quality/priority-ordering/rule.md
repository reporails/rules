---
id: CORE:X:0006
slug: priority-ordering
title: Priority Ordering
category: context_quality
type: semantic
level: L5
backed_by:
- builder-ai-instruction-best-practices
- building-skills-for-claude
- claude-md-guide
- claudemd-best-practices-mermaid-for-workflows
- codex-agent-loop
- copilot-custom-instructions
- copilot-custom-instructions-vscode
- enterprise-claude-usage
- fowler-context-engineering-agents
- instruction-limits-principles
- lost-in-the-middle-long-contexts
- rules-directory-mechanics
- sewell-agents-md-tips
- spec-writing-for-agents
- using-claude-md-files
targets: '{{instruction_files}}'
checks:
- id: CORE.X.0006.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.X.0006.extract_early_content
  type: deterministic
  severity: medium
  name: extract_early_content
- id: CORE.X.0006.critical_content_leads
  type: semantic
  severity: medium
  name: critical_content_leads
question: Does the file place its most critical instructions and hard 
  constraints at the top, before supporting details and examples?
criteria:
- Hard constraints (MUST/NEVER/prohibited) appear before optional guidance
- Project-critical context appears in the first third of the file
- The file does not lead with boilerplate, background, or optional features
choices:
- value: pass
  label: Passes
- value: fail
  label: Fails
pass_value: pass
---

# Priority Ordering

Instruction files SHOULD agents scan from top — placing critical rules first ensures they are not missed

## Pass / Fail

### Pass

````
## Critical Rules

NEVER commit secrets.
MUST run tests first.
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


