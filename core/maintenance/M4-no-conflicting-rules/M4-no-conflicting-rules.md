---
id: M4
title: No Conflicting Rules
category: maintenance
type: semantic
backed_by:
  - source: claude-code-memory
    claim: keep-rules-focused
checks:
  - id: M4-potential-conflict
    name: Potential conflicting MUST/MUST NOT
    severity: high
    pattern_confidence: high
question: "Do any rules contradict each other?"
criteria:
  - No MUST and MUST NOT on same topic
  - Parent and child rules are consistent
  - No implicit contradictions
sources:
  - "https://www.anthropic.com/engineering/claude-code-best-practices"
see_also: [C6, C5]
---

# No Conflicting Rules

No contradictory MUST/MUST NOT on same topic.

## Pattern

**Good:** Consistent rules across all files
**Bad:** Root says "MUST use tabs", child says "MUST use spaces"
