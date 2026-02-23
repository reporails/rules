---
id: CORE:X:0007
slug: a-structured-project-manifest-file-exists-that-maps-director
title: A Structured Project Manifest File Exists That Maps Directories, Repos, 
  Ownership, And Key Paths
category: context_quality
type: mechanical
level: L1
backed_by:
- claudemd-best-practices-backbone-yml-pattern
targets: '{{main_instruction_file}}'
checks:
- id: CORE.X.0007.manifest_file_exists
  type: mechanical
  severity: medium
  name: manifest_file_exists
  check: file_exists
---

# A Structured Project Manifest File Exists That Maps Directories, Repos, Ownership, And Key Paths

Instruction files SHOULD agents waste tokens exploring project structure when a manifest provides direct path construction — the exploration tax

## Pass / Fail

### Pass

````
# Instruction file
````

### Fail

````
(File does not exist at expected path)
````

## Limitations


