---
id: CORE:C:0016
slug: code-block-examples-present
title: Code Block Examples Present
category: content
type: deterministic
level: L2
backed_by:
- agent-readmes-empirical-study
- awesome-copilot-meta-instructions
- builder-ai-instruction-best-practices
- building-skills-for-claude
- claude-4-best-practices
- claudemd-best-practices-mermaid-for-workflows
- codex-exec-plans
- codex-prompting-guide
- codex-skills-shell-compaction
- copilot-ai-best-practices-vscode
- copilot-custom-instructions
- copilot-custom-instructions-vscode
- developer-context-cursor-study
- dometrain-claude-md-guide
- flowbench-workflow-format-benchmark
- fowler-pushing-ai-autonomy
- openai-community-agents-md-optimization
- osmani-ai-coding-workflow
- sewell-agents-md-tips
- spec-writing-for-agents
- using-claude-md-files
targets: '{{main_instruction_file}}'
checks:
- id: CORE.C.0016.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.C.0016.has_technical_content
  type: deterministic
  severity: medium
  name: has_technical_content
- id: CORE.C.0016.has_code_fences
  type: deterministic
  severity: medium
  name: has_code_fences
---

# Code Block Examples Present

Instruction files SHOULD instruction files should include concrete code or command examples for complex workflows

## Pass / Fail

### Pass

````
Include code block examples for CLI commands
```bash
npm test
```
````

### Fail

````
# Project Setup
Install dependencies with `npm install`.
````

## Limitations


