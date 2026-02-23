---
id: CORE:S:0005
slug: identity-fields-in-frontmatter
title: Identity Fields in Frontmatter
category: structure
type: deterministic
level: L2
backed_by:
- agent-readmes-empirical-study
- awesome-copilot-meta-instructions
- building-skills-for-claude
- codex-eval-skills
- codex-skills-guide
- codex-skills-shell-compaction
- copilot-custom-instructions-vscode
targets: '{{supplementary_files}}'
checks:
- id: CORE.S.0005.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.S.0005.has_frontmatter_block
  type: deterministic
  severity: medium
  name: has_frontmatter_block
- id: CORE.S.0005.identity_field_present
  type: deterministic
  severity: medium
  name: identity_field_present
---

# Identity Fields in Frontmatter

Instruction files SHOULD identity fields in frontmatter make files discoverable and self-documenting

## Pass / Fail

### Pass

````
---
description: Example rule
---
Skill frontmatter must include a name field in kebab-case
````

### Fail

````
---
scope: project
---
# Rule Content
This rule has frontmatter.
````

## Limitations


