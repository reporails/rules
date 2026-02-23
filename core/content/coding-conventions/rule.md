---
id: CORE:C:0012
slug: coding-conventions
title: Coding Conventions
category: content
type: semantic
level: L3
backed_by:
- agent-readmes-empirical-study
- agentic-coding-adoption-github
- agents-md-impact-efficiency
- agents-md-spec
- awesome-copilot-meta-instructions
- building-skills-for-claude
- claude-4-best-practices
- claude-code-memory
- claude-md-guide
- claude-md-optimization-study
- codex-introducing
- codex-prompting-guide
- codex-skills-shell-compaction
- copilot-cli-best-practices
- copilot-coding-agent-best-practices
- copilot-coding-agent-results
- copilot-coding-agent-tasks
- copilot-custom-instructions-vscode
- developer-context-cursor-study
- dometrain-claude-md-guide
- enterprise-claude-usage
- evaluating-agents-md
- fowler-assessing-quality-agents
- fowler-context-engineering-agents
- fowler-pushing-ai-autonomy
- microsoft-awesome-copilot-blog
- openai-community-agents-md-optimization
- osmani-ai-coding-workflow
- prompthub-cursor-rules-analysis
- sewell-agents-md-tips
- spec-writing-for-agents
- using-claude-md-files
targets: '{{instruction_files}}'
checks:
- id: CORE.C.0012.file_in_scope
  type: mechanical
  severity: high
  name: file_in_scope
  check: file_exists
- id: CORE.C.0012.extract_convention_content
  type: deterministic
  severity: high
  name: extract_convention_content
- id: CORE.C.0012.conventions_are_project_specific
  type: semantic
  severity: high
  name: conventions_are_project_specific
question: Are these conventions specific to this project rather than generic 
  best practices any developer would know?
criteria:
- Conventions reference project-specific tools, patterns, or decisions
- Following these conventions would produce different code than default behavior
- At least some conventions mention concrete patterns, not just 'follow best 
  practices'
choices:
- value: pass
  label: Passes
- value: fail
  label: Fails
pass_value: pass
---

# Coding Conventions

Instruction files MUST without project conventions agents apply generic defaults — explicit conventions maintain codebase consistency

## Pass / Fail

### Pass

````
## Conventions

Naming: use snake_case for Python, camelCase for TypeScript.
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


