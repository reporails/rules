---
id: CORE:C:0011
slug: file-includes-security-requirements-constraints-or-patterns-
title: File Includes Security Requirements, Constraints, Or Patterns For 
  Generated Code
category: content
type: deterministic
level: L2
backed_by:
- agent-readmes-empirical-study
- agents-md-spec
- awesome-copilot-meta-instructions
- claude-code-hooks
- codex-skills-shell-compaction
- copilot-about-coding-agent
- copilot-ai-best-practices-vscode
- copilot-custom-instructions-vscode
- developer-context-cursor-study
- evaluating-agents-md
- fowler-pushing-ai-autonomy
- openai-community-agents-md-optimization
- prompthub-cursor-rules-analysis
targets: '{{main_instruction_file}}'
checks:
- id: CORE.C.0011.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.C.0011.has_security_content
  type: deterministic
  severity: medium
  name: has_security_content
---

# File Includes Security Requirements, Constraints, Or Patterns For Generated Code

Instruction files SHOULD 45% of AI-generated code contains OWASP vulnerabilities — without explicit security requirements agents produce insecure code by default

## Pass / Fail

### Pass

````
Document security requirements: input validation, auth checks, no eval()
````

### Fail

````
(File does not exist at expected path)
````

## Limitations


