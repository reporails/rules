---
id: COPILOT:S:0001
slug: copilot-instructions-placement
title: Copilot Instructions File Placement
category: structure
type: mechanical
level: L1
backed_by:
- copilot-cli-best-practices
- copilot-coding-agent-best-practices
- copilot-custom-instructions
targets: '{{instruction_files}}'
checks:
- id: COPILOT.S.0001.file-exists
  type: mechanical
  severity: medium
  name: file-exists
  check: file_exists
---

# Copilot Instructions File Placement

Copilot projects SHOULD place repository-wide custom instructions in .github/copilot-instructions.md for automatic discovery by Copilot Chat, code review, and coding agent

## Pass / Fail

### Pass

~~~~markdown
A repository with .github/copilot-instructions.md containing project-specific build commands and conventions
~~~~

### Fail

~~~~markdown
A repository relying solely on AGENTS.md for Copilot instructions, missing Copilot-specific features like code review integration
~~~~

## Limitations

Cannot verify whether the team actually uses Copilot. Projects not using Copilot have no obligation to create this file. Checks file existence only, not content quality.
