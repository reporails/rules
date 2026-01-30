---
id: E3
title: Purpose-Based File Reading
category: efficiency
type: deterministic
backed_by:
  - source: claude-code-issue-13579
    claim: purpose-based-reading
  - source: claude-4-best-practices
    claim: investigate-before-answering
checks:
  - id: E3-no-reading-strategy
    name: No file reading strategy documented
    severity: low
    pattern_confidence: medium
sources:
  - "https://github.com/anthropics/claude-code/issues/13579"
see_also: [E4, E8]
---

# Purpose-Based File Reading

Instructions document reading strategies (full vs partial).

## Pattern

**Good:** "Read full for EDIT, partial for UNDERSTAND"
**Bad:** No guidance on context-efficient reading
