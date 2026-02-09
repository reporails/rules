---
id: "CLAUDE:S:0012"
slug: memory-file-within-200-lines
title: MEMORY.md Within 200-Line Limit
category: structure
type: mechanical
level: L6
backed_by:
- claude-code-memory
targets: '{{instruction_files}}'
checks:
- id: "CLAUDE:S:0012:check:0001"
  type: mechanical
  check: line_count
  args:
    path: ".claude/memory/MEMORY.md"
    max: 200
  severity: medium
question: "Does the MEMORY.md file stay within the 200-line auto-load limit?"
criteria:
- The total line count of MEMORY.md does not exceed 200 lines
- The check applies to all MEMORY.md files at any scope (user, project)
- Blank lines and comment lines are included in the line count
---

# MEMORY.md Within 200-Line Limit

MEMORY.md files must not exceed 200 lines, as content beyond that limit is not loaded into the system prompt.

## Pass / Fail

**Pass:** ~/.claude/MEMORY.md contains 147 lines of key architectural decisions, common mistakes,
and project conventions. All content is within the 200-line limit and fully loaded at
session start.
**Fail:** ~/.claude/MEMORY.md contains 283 lines. The first 200 lines cover general conventions,
but lines 201-283 contain critical security constraints and deployment procedures that
are silently dropped and never seen by the agent.

## Limitations

This check counts physical lines including blank lines and comments. If Claude Code's
line-counting behavior differs (e.g., ignoring trailing blank lines), the check may
report false positives near the boundary. The check does not evaluate whether the most
important content is placed within the first 200 lines — only that the file does not
exceed the limit.
