---
id: CORE:C:0005
slug: instruction-file-documents-testing-framework-test-commands-a
title: Instruction File Documents Testing Framework, Test Commands, And Testing 
  Patterns
category: content
type: deterministic
level: L2
backed_by:
- advanced-context-engineering
- agent-readmes-empirical-study
- agentic-coding-adoption-github
- agents-md-impact-efficiency
- agents-md-spec
- awesome-copilot-meta-instructions
- claude-md-optimization-study
- codex-exec-plans
- codex-introducing
- copilot-coding-agent-best-practices
- copilot-coding-agent-results
- copilot-coding-agent-tasks
- copilot-custom-instructions
- copilot-custom-instructions-vscode
- developer-context-cursor-study
- openai-community-agents-md-optimization
- osmani-ai-coding-workflow
- prompthub-cursor-rules-analysis
- spec-writing-for-agents
- using-claude-md-files
targets: '{{main_instruction_file}}'
checks:
- id: CORE.C.0005.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.C.0005.has_testing_content
  type: deterministic
  severity: medium
  name: has_testing_content
---

# Instruction File Documents Testing Framework, Test Commands, And Testing Patterns

Instruction files SHOULD agents need to know the testing framework and conventions to write correct tests and run them properly

## Pass / Fail

### Pass

````
Document which test framework the project uses (pytest, jest, etc.)
````

### Fail

````
# Instruction file content
````

## Limitations


