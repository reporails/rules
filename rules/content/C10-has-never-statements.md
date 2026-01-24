---
id: C10
title: Has NEVER Statements
category: content
type: deterministic
detection: pattern-regex for NEVER (≥1), then NEVER.*[—–-]|NEVER.*instead for alternatives
level: L2+
sources: [1, 9, 13]
see_also: [C4]
---

# Has NEVER Statements

Validates antipattern documentation exists with escape hatches.

Two-step check: (1) at least one NEVER exists, (2) each NEVER has a positive alternative.

## Pattern

**Good:** NEVER with positive alternative
- "NEVER use `any` type — use `unknown` or specific types instead"
- "NEVER commit secrets to git — use environment variables"

**Acceptable:** NEVER alone (when alternative is obvious)
- "NEVER modify files in `src/legacy/`"

**Bad:** NEVER without escape hatch
- Negative-only rules can cause agents to get stuck [13]
