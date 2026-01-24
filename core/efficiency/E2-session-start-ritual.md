---
id: E2
title: Session Start Ritual
category: efficiency
type: deterministic
checks:
  - id: E2-no-ritual
    name: No session start ritual documented
    severity: medium
sources:
  - "docs/capability-levels.md"
see_also: [S6, G5]
---

# Session Start Ritual

L6 projects have numbered steps referencing backbone/maps.

## Pattern

**Good:** "1. Read backbone.yml 2. Identify relevant maps 3. Load context"
**Bad:** No guidance on how to start a session
