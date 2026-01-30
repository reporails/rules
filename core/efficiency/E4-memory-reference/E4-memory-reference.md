---
id: E4
title: Memory Reference
category: efficiency
type: deterministic
backed_by:
  - source: claude-code-issue-13579
    claim: memory-reference
  - source: claude-4-best-practices
    claim: investigate-before-answering
checks:
  - id: E4-no-memory-instruction
    name: No memory reference instruction
    severity: low
    pattern_confidence: low
sources:
  - "https://www.anthropic.com/engineering/claude-code-best-practices"
  - "https://github.com/anthropics/claude-code/issues/13579"
see_also: [E3, E8]
---

# Memory Reference

Instructions mention "reference from memory" for unchanged files.

## Pattern

**Good:** "Reference from memory instead of re-reading unchanged files"
**Bad:** No guidance on avoiding redundant reads
