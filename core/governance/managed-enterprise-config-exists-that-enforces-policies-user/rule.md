---
id: CORE:G:0007
slug: managed-enterprise-config-exists-that-enforces-policies-user
title: Managed/Enterprise Config Exists That Enforces Policies Users Cannot 
  Override
category: governance
type: mechanical
level: L2
backed_by:
- claude-code-memory
- claude-code-settings
- copilot-custom-instructions-vscode
targets: '{{managed_config}}'
checks:
- id: CORE.G.0007.managed_config_exists
  type: mechanical
  severity: low
  name: managed_config_exists
  check: file_exists
---

# Managed/Enterprise Config Exists That Enforces Policies Users Cannot Override

Instruction files MAY organizations need to enforce security baselines, sandbox policies, and approved tools across all agent users

## Pass / Fail

### Pass

````

````

### Fail

````
(File does not exist at expected path)
````

## Limitations


