---
id: CORE:S:0003
slug: shallow-heading-hierarchy
title: Shallow Heading Hierarchy
category: structure
type: deterministic
level: L2
backed_by:
- agent-readmes-empirical-study
- building-skills-for-claude
- codex-exec-plans
targets: '{{instruction_files}}'
checks:
- id: CORE.S.0003.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.S.0003.no_deeply_nested_headings
  type: deterministic
  severity: medium
  name: no_deeply_nested_headings
---

# Shallow Heading Hierarchy

Instruction files SHOULD deeply nested heading structures (H5+) are rare and less maintainable — prefer shallow hierarchy

## Pass / Fail

### Pass

````
# Instruction file
````

### Fail

````
# Instruction file content
##### Deeply Nested Heading
````

## Limitations


