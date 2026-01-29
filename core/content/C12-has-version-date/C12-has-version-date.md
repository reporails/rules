---
id: C12
title: Has Version/Date
category: content
type: deterministic
backed_by:
  - source: claude-code-memory
    claim: review-periodically
checks:
  - id: C12-no-version
    name: No version or date marker
    severity: low
sources:
  - "https://www.anthropic.com/engineering/claude-code-best-practices"
see_also: [M1, C1]
---

# Has Version/Date

Root instruction file has version pattern or date in header.

## Pattern

**Good:** "<!-- Last updated: 2024-01-15 -->" or "v1.2.0"
**Bad:** No version tracking in file
