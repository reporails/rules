---
id: S2
title: Progressive Disclosure
category: structure
type: heuristic
detection: pattern-regex for @path or "See.*for" in files > 100 lines
question: Does this file use progressive disclosure (pointers to external docs)?
criteria: Pass if file has @imports or "See X for Y" patterns; fail if > 100 lines with no external references
level: L3+
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
