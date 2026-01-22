---
id: C2
title: Explicit Over Implicit
category: content
type: semantic
detection: Requires AI to judge if instructions are vague vs actionable
level: L2+
sources: [1, 8]
see_also: [C8]
antipatterns:
  - id: A10
    name: Vague instructions
    severity: high
    points: -15
---

# Explicit Over Implicit

+15% instruction adherence.

Instructions must be specific and actionable, not vague.

## Pattern

**Good:** Explicit and actionable
- "Use 2-space indentation (not tabs)"
- "Always explicitly type function return values"

**Bad:** Vague
- "Format code properly"
- "Use good naming conventions"
