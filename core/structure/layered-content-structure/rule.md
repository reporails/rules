---
id: CORE:S:0017
slug: layered-content-structure
title: Layered Content Structure
category: structure
type: deterministic
level: L5
backed_by:
- building-skills-for-claude
- developer-context-cursor-study
- lost-in-the-middle-long-contexts
- spec-writing-for-agents
targets: '{{instruction_files}}'
checks:
- id: CORE.S.0017.file_in_scope
  type: mechanical
  severity: medium
  name: file_in_scope
  check: file_exists
- id: CORE.S.0017.has_overview_section
  type: deterministic
  severity: medium
  name: has_overview_section
---

# Layered Content Structure

Instruction files SHOULD agents benefit from progressive disclosure — high-level context first enables better navigation of details

## Pass / Fail

### Pass

````
## Overview

This tool validates instruction files.
````

### Fail

````
# Instruction file content
````

## Limitations


