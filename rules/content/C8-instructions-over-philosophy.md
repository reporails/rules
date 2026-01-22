---
id: C8
title: Instructions Over Philosophy
category: content
type: semantic
detection: Requires AI to distinguish instruction from explanation
level: L2+
sources: [1]
see_also: [C2]
antipatterns:
  - id: A5
    name: Philosophy instead of instructions
    severity: critical
    points: -25
---

# Instructions Over Philosophy

Ensures actionable guidance.

CLAUDE.md should contain instructions, not explanations of why or background philosophy.

## Pattern

**Good:** Instruction
- "Use adapter logging (see contract.logging)"

**Bad:** Philosophy
- "We believe in clean architecture principles where logging concerns are separated from business logic..."
