---
id: C4
title: Links Are Valid
category: content
type: semantic
backed_by:
  - source: claude-code-memory
    claim: imports-syntax
checks:
  - id: C4-broken-import
    name: "@import references non-existent file"
    severity: high
    pattern_confidence: very_high
question: "Do all @import references point to files that exist?"
criteria:
  - Each @path/to/file reference resolves to an existing file
  - Paths are relative to the project root
  - Verify using filesystem, not text matching
sources:
  - "https://code.claude.com/docs/en/memory"
see_also: [S2, M3]
---

# Links Are Valid

All @imports and file references resolve to existing files.

## Pattern

**Good:** @docs/api.md where docs/api.md exists
**Bad:** @docs/old-api.md where file was deleted
