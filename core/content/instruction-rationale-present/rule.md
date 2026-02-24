---
id: CORE:C:0002
slug: instruction-rationale-present
title: Instruction Rationale Present
category: content
type: semantic
level: L3
backed_by:
- advanced-context-engineering
- agent-readmes-empirical-study
- agentic-coding-adoption-github
- awesome-copilot-meta-instructions
- building-skills-for-claude
- claude-4-best-practices
- claude-code-issue-13579
- claude-md-guide
- claude-md-optimization-study
- claudemd-best-practices-mermaid-for-workflows
- codex-exec-plans
- codex-prompting-guide
- copilot-coding-agent-results
- copilot-coding-agent-tasks
- copilot-custom-instructions
- copilot-custom-instructions-vscode
- developer-context-cursor-study
- dometrain-claude-md-guide
- enterprise-claude-usage
- fowler-assessing-quality-agents
- fowler-pushing-ai-autonomy
- instruction-limits-principles
- openai-community-agents-md-optimization
- osmani-ai-coding-workflow
- prompthub-cursor-rules-analysis
- rules-directory-mechanics
- sewell-agents-md-tips
- spec-writing-for-agents
targets: '{{main_instruction_file}}'
checks:
- id: CORE.C.0002.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.C.0002.extract_rationale_content
  type: deterministic
  severity: medium
  name: extract_rationale_content
- id: CORE.C.0002.rationale_adds_understanding
  type: semantic
  severity: medium
  name: rationale_adds_understanding
question: Do the rationale statements explain WHY rules exist, not just WHAT the
  rules are?
criteria:
- Explains consequences of not following the rule
- Connects the rule to a project-specific concern or past incident
- Helps an agent decide how to apply the rule in ambiguous cases
choices:
- value: pass
  label: Passes
- value: fail
  label: Fails
pass_value: pass
---

# Instruction Rationale Present

Instruction files SHOULD agents that understand why a rule exists apply it correctly in novel situations — without rationale they follow rules blindly

## Pass / Fail

### Pass

````
Include context or motivation behind instructions to help the model understand goals
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


