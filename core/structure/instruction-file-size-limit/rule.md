---
id: "CORE:S:0005"
slug: instruction-file-size-limit
title: Instruction File Size Limit
category: structure
type: mechanical
level: L2
backed_by:
- claude-md-guide
- instruction-limits-principles
- using-claude-md-files
targets: '{{instruction_files}}'
checks:
- id: "CORE:S:0005:check:0001"
  type: mechanical
  check: line_count
  args:
    max: 300
  severity: high
question: "Is every instruction file at most 300 lines long?"
criteria:
- Every instruction file has a line count of 300 or fewer
- Line count includes all lines (blank lines, comments, content)
- Each file is evaluated independently, not as a sum
---

# Instruction File Size Limit

Each instruction file must be at most 300 lines.

## Pass / Fail

**Pass:** A CLAUDE.md file contains 180 lines of concise project guidance. A
supplementary .claude/rules/testing.md file contains 45 lines. Each
individual file is well under the 300-line threshold.
**Fail:** A CLAUDE.md file contains 420 lines, including extensive inline code
examples, duplicated style guides, and verbose explanations that could be
moved to imported files. The single file exceeds the 300-line limit.

## Limitations

Line count is a coarse proxy for context consumption. A file with 290 lines
of dense technical content may consume more context than a 310-line file
with generous whitespace. Does not account for line length variation. Also
does not distinguish between the root instruction file and supplementary
files, though the threshold applies equally to both.
