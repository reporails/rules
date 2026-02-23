---
id: CORE:C:0007
slug: workflow-definitions
title: Workflow Definitions
category: content
type: deterministic
level: L3
backed_by:
- advanced-context-engineering
- agent-readmes-empirical-study
- agentic-coding-adoption-github
- agents-md-impact-efficiency
- agents-md-spec
- building-skills-for-claude
- claude-4-best-practices
- claude-code-issue-13579
- claudemd-best-practices-mermaid-for-workflows
- codex-eval-skills
- codex-exec-plans
- codex-prompting-guide
- codex-skills-shell-compaction
- copilot-ai-best-practices-vscode
- copilot-cli-best-practices
- developer-context-cursor-study
- dometrain-claude-md-guide
- enterprise-claude-usage
- flowbench-workflow-format-benchmark
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
- id: CORE.C.0007.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.C.0007.discusses_development_activities
  type: deterministic
  severity: medium
  name: discusses_development_activities
- id: CORE.C.0007.has_workflow_content
  type: deterministic
  severity: medium
  name: has_workflow_content
---

# Workflow Definitions

Instruction files SHOULD agents without workflow definitions improvise processes — defined workflows ensure consistent execution

## Pass / Fail

### Pass

````
Document specific workflows for different task types (features, TDD, UI changes)
## Workflow

When you receive a feature request:
1. Read the spec
2. Write tests first
````

### Fail

````
# Development
Fix bugs and deploy changes regularly.
````

## Limitations


