---
id: C6
title: Single Source of Truth
category: content
type: semantic
backed_by:
  - source: claude-code-memory
    claim: keep-rules-focused
  - source: dometrain-claude-md-guide
    claim: duplicate-instruction-waste
checks:
  - id: C6-duplicate-instruction
    name: Duplicate instruction across files
    severity: high
    pattern_confidence: low
question: "Are instructions duplicated across multiple files?"
criteria:
  - Same rule not stated in multiple locations
  - References point to canonical source
  - No conflicting versions of same instruction
sources:
  - "https://code.claude.com/docs/en/memory"
see_also: [M4, S2]
---

# Single Source of Truth

No duplicate instructions across files.

## Pattern

**Good:** "See @docs/testing.md for test conventions"
**Bad:** Same test rules in root file and docs/testing.md
