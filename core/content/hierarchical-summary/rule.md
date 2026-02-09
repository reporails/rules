---
id: "CORE:C:0019"
slug: hierarchical-summary
title: Hierarchical Summary
category: content
type: semantic
level: L3
backed_by:
- spec-writing-for-agents
targets: '{{instruction_files}}'
checks:
- id: "CORE:C:0019:check:0001"
  type: deterministic
  negate: true
  severity: medium
- id: "CORE:C:0019:check:0002"
  type: semantic
  prompt: "Does the instruction file provide a hierarchical summary or table of contents for navigating the instruction system?"
  severity: medium
question: "Does this instruction file include a summary or table of contents near
  the top for quick orientation?"
criteria:
- File exceeding 100 lines contains a summary, overview, or table of contents 
  within the first 20 lines
- The summary references or links to detailed sections later in the file
- The summary covers the major topics addressed in the file (not just one 
  section)
- Files under 100 lines are exempt from this rule
---

# Hierarchical Summary

Instruction files exceeding 100 lines must include a summary section or table of
contents near the top of the file.

## Pass / Fail

**Pass:** A 250-line CLAUDE.md opens with a 10-line summary:
"## Overview\n- Commands: build, test, lint (see ##Commands)\n- Structure: monorepo
with packages/ (see ##Structure)\n- Key constraints: ESM only, no require()
(see ##Constraints)\n- Testing: pytest with fixtures in tests/conftest.py
(see ##Testing)"
**Fail:** A 250-line CLAUDE.md jumps directly into a detailed `## Commands` section with no
overview, summary, or table of contents. The agent must read all 250 lines to
understand the file's scope before finding the relevant section.

## Limitations

Only applies to files exceeding 100 lines — short files are exempt. Cannot assess
whether the summary accurately reflects the file's content. A stale or incomplete
summary would pass the structural check. Cannot distinguish between a true summary
(condensed key points) and a table of contents (just section links) — both are
accepted as valid.
