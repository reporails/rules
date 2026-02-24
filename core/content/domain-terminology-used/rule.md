---
id: CORE:C:0024
slug: domain-terminology-used
title: Domain Terminology Used
category: content
type: deterministic
level: L5
backed_by:
- agent-readmes-empirical-study
- building-skills-for-claude
- codex-exec-plans
- developer-context-cursor-study
- dometrain-claude-md-guide
- sewell-agents-md-tips
- spec-writing-for-agents
targets: '{{main_instruction_file}}'
checks:
- id: CORE.C.0024.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.C.0024.has_domain_terms
  type: deterministic
  severity: medium
  name: has_domain_terms
---

# Domain Terminology Used

Instruction files SHOULD domain-specific terms help agents generate contextually appropriate code and communication

## Pass / Fail

### Pass

````
## Terminology

We call the deployment unit a 'service'.
In our system, 'shard' means...
````

### Fail

````
# Instruction file content
````

## Limitations


