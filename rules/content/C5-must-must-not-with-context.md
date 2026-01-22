---
id: C5
title: MUST/MUST NOT with Context
category: content
type: heuristic
detection: Grep for SHOULD vs MUST; context presence validation
level: L6
sources: [8, 9, 16]
see_also: [C2]
antipatterns:
  - id: A15
    name: SHOULD instead of MUST
    severity: medium
    points: -10
---

# MUST/MUST NOT with Context

Binary compliance with improved adherence through context.

Rules should be binary (must/must not) AND include context for why.

## Pattern

**Good:** Binary with context
- "MUST use type hints — enables IDE autocomplete and catches errors at compile time"
- "MUST NOT put domain reasoning into node modules — keeps nodes testable and reusable"

**Bad:** Binary without context
- "MUST use type hints"
- "MUST NOT put domain reasoning into node modules"

**Bad:** Advisory
- "Should consider using type hints"
- "Consider keeping nodes simple"
