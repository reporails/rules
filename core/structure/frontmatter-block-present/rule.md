---
id: CORE:S:0006
slug: frontmatter-block-present
title: Frontmatter Block Present
category: structure
type: deterministic
level: L2
backed_by:
- agent-readmes-empirical-study
- awesome-copilot-meta-instructions
- building-skills-for-claude
- claude-code-memory
- claude-code-settings
- codex-skills-shell-compaction
- copilot-coding-agent-best-practices
- copilot-coding-agent-results
- copilot-custom-instructions
- copilot-custom-instructions-vscode
- rules-directory-mechanics
targets: '{{supplementary_files}}'
checks:
- id: CORE.S.0006.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.S.0006.has_frontmatter_block
  type: deterministic
  severity: medium
  name: has_frontmatter_block
---

# Frontmatter Block Present

Instruction files SHOULD rule files should include machine-readable frontmatter for tooling and discoverability

## Pass / Fail

### Pass

````
---
description: Example rule
---
````

### Fail

````
# Instruction file content
````

## Limitations


