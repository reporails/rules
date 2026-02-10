---
id: "CLAUDE:S:0002"
slug: import-depth-within-limit
title: Import Depth Within Limit
category: structure
type: mechanical
level: L3
backed_by:
- claude-code-memory
targets: '{{instruction_files}}'
checks:
- id: "CLAUDE:S:0002:check:0001"
  type: mechanical
  check: import_depth
  args:
    max: 5
  severity: medium
question: "Do all @import chains from CLAUDE.md files stay within the 5-hop recursion
  limit?"
criteria:
- Every @import reference outside of code blocks is followed recursively
- The maximum chain depth from any root CLAUDE.md to any leaf import does not 
  exceed 5
- Relative paths are resolved from the importing file's directory, not the 
  project root
- "@import references inside markdown code spans and code blocks are excluded from
  traversal"
---

# Import Depth Within Limit

@import chains in CLAUDE.md files must not exceed 5 levels of recursion.

## Pass / Fail

**Pass:** CLAUDE.md imports @.claude/rules/style.md, which imports @.claude/rules/shared/naming.md.
The chain depth is 2 hops, well within the 5-hop limit.
**Fail:** CLAUDE.md -> @imports/a.md -> @imports/b.md -> @imports/c.md -> @imports/d.md -> @imports/e.md
-> @imports/f.md. The chain is 6 hops deep. The content of imports/f.md is silently dropped
by Claude Code.

## Limitations

This check follows @import references statically and counts maximum depth. It does not
evaluate whether imports inside code blocks are correctly ignored at runtime. Circular
import detection is a separate concern not covered by this rule. The check cannot verify
runtime behavior if Claude Code changes its import resolution algorithm.
