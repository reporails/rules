---
id: "CODEX:S:0001"
slug: agents-md-file-placement
title: AGENTS.md File Placement
category: structure
type: mechanical
level: L1
backed_by:
- agents-md-spec
- codex-agent-loop
targets: '{{instruction_files}}'
checks:
- id: "CODEX:S:0001:check:0001"
  type: mechanical
  check: file_exists
  args:
    path: "AGENTS.md"
  severity: critical
question: "Does an AGENTS.md file with exact case-sensitive naming exist at the project
  root?"
criteria:
- A file named exactly AGENTS.md exists at the Git/project root
- The filename uses uppercase AGENTS and lowercase .md extension
- The file is not empty (Codex skips empty instruction files)
---

# AGENTS.md File Placement

An AGENTS.md file must exist at the project root with exact case-sensitive naming.

## Pass / Fail

**Pass:** The repository root contains a file named exactly AGENTS.md (uppercase AGENTS, uppercase
.MD extension not required — standard .md). Codex discovers it during the instruction walk
from Git root.
**Fail:** The repository has no AGENTS.md at the root. Variants such as agents.md, Agents.md, or
AGENTS.txt are not recognized by Codex's instruction discovery. The agent receives zero
project-level guidance.

## Limitations

This check verifies file existence and exact filename only. It does not validate the content
of the AGENTS.md file. An empty AGENTS.md is detected by Codex and skipped, but this rule
only checks for file presence, not content. The check does not verify Git root detection —
it assumes the project root is the Git root.
