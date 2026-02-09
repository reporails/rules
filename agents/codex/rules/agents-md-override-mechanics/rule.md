---
id: "CODEX:S:0002"
slug: agents-md-override-mechanics
title: AGENTS.md Override Mechanics
category: structure
type: mechanical
level: L3
backed_by:
- codex-agent-loop
- codex-agents-md
targets: '{{instruction_files}}'
checks:
- id: "CODEX:S:0002:check:0001"
  type: mechanical
  check: file_count
  args:
    pattern: "**/AGENTS.override.md"
    max: 0
  severity: medium
question: "Do any directories contain both AGENTS.md and AGENTS.override.md, risking
  content shadowing?"
criteria:
- No directory in the repository contains both AGENTS.md and AGENTS.override.md 
  simultaneously
- If both files exist, AGENTS.override.md fully subsumes the content of 
  AGENTS.md
- The override relationship is intentional and documented, not accidental
---

# AGENTS.md Override Mechanics

Directories containing both AGENTS.md and AGENTS.override.md must not have conflicting content, as only one is loaded.

## Pass / Fail

**Pass:** A directory contains only AGENTS.md with project conventions. No AGENTS.override.md exists,
so there is no ambiguity about which file is loaded. Alternatively, AGENTS.override.md
exists alone and fully replaces the guidance that would have been in AGENTS.md.
**Fail:** A directory contains both AGENTS.md (with coding standards) and AGENTS.override.md (with
deployment overrides). The developer expects both to load, but Codex loads only
AGENTS.override.md. The coding standards in AGENTS.md are silently ignored.

## Limitations

This check detects coexistence of both files but cannot determine developer intent. In
some workflows, AGENTS.override.md intentionally replaces AGENTS.md (e.g., for CI
environments). The check flags all coexistence as a warning; the developer must confirm
whether the override is intentional and complete. Content comparison between the two files
is not performed.
