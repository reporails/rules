---
id: CORE:C:0001
slug: actionable-instructions
title: Actionable Instructions
category: content
type: semantic
level: L5
backed_by:
- advanced-context-engineering
- agent-readmes-empirical-study
- agents-md-impact-efficiency
- agents-md-spec
- awesome-copilot-meta-instructions
- builder-ai-instruction-best-practices
- building-skills-for-claude
- claude-4-best-practices
- claude-code-memory
- claude-md-guide
- claude-md-optimization-study
- claudemd-best-practices-backbone-yml-pattern
- codex-eval-skills
- codex-exec-plans
- codex-skills-guide
- codex-skills-shell-compaction
- copilot-ai-best-practices-vscode
- copilot-cli-best-practices
- copilot-custom-instructions-vscode
- developer-context-cursor-study
- dometrain-claude-md-guide
- enterprise-claude-usage
- evaluating-agents-md
- fowler-context-engineering-agents
- fowler-pushing-ai-autonomy
- instruction-limits-principles
- microsoft-awesome-copilot-blog
- openai-community-agents-md-optimization
- osmani-ai-coding-workflow
- sewell-agents-md-tips
- sewell-codex-vs-claude
- spec-writing-for-agents
- using-claude-md-files
targets: '{{instruction_files}}'
checks:
- id: CORE.C.0001.file_in_scope
  type: mechanical
  severity: high
  name: file_in_scope
  check: file_exists
- id: CORE.C.0001.extract_instruction_sentences
  type: deterministic
  severity: high
  name: extract_instruction_sentences
- id: CORE.C.0001.flag_vague_language
  type: deterministic
  severity: high
  name: flag_vague_language
- id: CORE.C.0001.specificity_evaluation
  type: semantic
  severity: high
  name: specificity_evaluation
question: Are the flagged instructions specific enough for an agent to follow 
  without asking for clarification?
criteria:
- Each instruction names a specific action or condition the agent can test for
- Instructions do not rely on agent judgment about what counts as 'appropriate' 
  or 'proper'
- At least 80% of instructions contain a concrete, testable action verb
choices:
- value: pass
  label: Passes
- value: fail
  label: Fails
pass_value: pass
---

# Actionable Instructions

Instruction files MUST vague instructions cause the agent to guess or apply incorrect defaults

## Pass / Fail

### Pass

````
Always use TypeScript for new files.
Never bypass the linter.
Must write tests for new features.
Use best practices when writing code.
Be careful with edge cases.
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


