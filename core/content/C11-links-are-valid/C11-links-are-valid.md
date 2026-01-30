---
id: C11
title: Links Are Valid
category: content
type: deterministic
backed_by:
  - source: claude-code-memory
    claim: imports-syntax
checks:
  - id: C11-broken-import
    name: "@import references non-existent file"
    severity: high
    pattern_confidence: very_high
sources:
  - "https://code.claude.com/docs/en/memory"
see_also: [S2, M5]
---

# Links Are Valid

All @imports and file references resolve to existing files.

## Pattern

**Good:** @docs/api.md where docs/api.md exists
**Bad:** @docs/old-api.md where file was deleted
