---
id: C4
title: Anti-Pattern Documentation
category: content
type: semantic
detection: Requires AI to assess quality/completeness of antipattern documentation
level: L2+
scoring: 10
sources: [1, 13, 25]
validation: first-party
see_also: [C10]
---

# Anti-Pattern Documentation

Prevents confidently wrong suggestions.

Explicitly document what NOT to do. Claude confidently proposes patterns; telling it what to avoid prevents mistakes.

## Pattern

**Good:** Explicit antipatterns
- "NEVER use `any` type in TypeScript"
- "NEVER modify files in `src/legacy/` directly"
- "NEVER commit directly to `main` branch"
