---
id: S2
title: Progressive Disclosure
category: structure
type: heuristic
detection: Detect @imports or "See ..." patterns; may miss custom pointer formats
level: L3+
scoring: 5
sources: [2, 10]
---

# Progressive Disclosure

Reduces root file size by 50-70% and context consumption per session.

Root file contains pointers; details live in referenced documents and load on demand.

## Pattern

**Good:** Pointer to detailed docs
- `See @docs/database-patterns.md for schema conventions`

**Bad:** Full content in root file
- 50+ lines of schema rules embedded in root

## Efficiency Impact

- Context loads only when relevant to current task
- Sessions stay within token limits longer
- Enables targeted reading vs full file consumption
