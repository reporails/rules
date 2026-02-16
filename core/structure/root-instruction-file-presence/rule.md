---
id: CORE:S:0001
slug: root-instruction-file-presence
title: Root Instruction File Presence
category: structure
type: mechanical
level: L1
backed_by:
- agents-md-spec
- claude-md-guide
- copilot-custom-instructions
- instruction-limits-principles
targets: '{{instruction_files}}'
checks:
- id: CORE.S.0001.file-exists
  type: mechanical
  severity: high
  name: file-exists
  check: file_exists
---

# Root Instruction File Presence

Every project MUST have a root-level instruction file that agents discover automatically at session start

## Pass / Fail

### Pass

~~~~markdown
A repository containing any of: CLAUDE.md, AGENTS.md, .github/copilot-instructions.md, or GEMINI.md at the project root
~~~~

### Fail

~~~~markdown
(File does not exist at expected path)
~~~~

## Limitations

Cannot verify the file contains useful content (that is covered by other rules). Only checks for file existence.
