---
id: CORE:S:0025
slug: rules-directory-structure
title: Rules Directory Structure
category: structure
type: deterministic
level: L5
backed_by:
- claude-code-memory
- claude-md-guide
targets: '{{rules_dir}}/**/*.md'
checks:
- id: CORE.S.0025.rules_dir_exists
  type: mechanical
  severity: medium
  name: rules_dir_exists
  check: glob_match
- id: CORE.S.0025.has_markdown_rule_files
  type: deterministic
  severity: medium
  name: has_markdown_rule_files
---

# Rules Directory Structure

Instruction files SHOULD modular rules should be organized in a dedicated directory with one concern per file

## Pass / Fail

### Pass

````
rules/style.md
rules/testing.md
````

### Fail

````
# Instruction file content
````

## Limitations


