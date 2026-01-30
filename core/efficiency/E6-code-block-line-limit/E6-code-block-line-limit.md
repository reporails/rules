---
id: E6
title: Code Block Line Limit
category: efficiency
type: deterministic
backed_by: []  # Tier: experimental — sources exist but claims not yet extracted
checks:
  - id: E6-code-block-too-long
    name: Code block exceeds 10 lines
    severity: medium
    pattern_confidence: very_high
sources:
  - "https://www.humanlayer.dev/blog/writing-a-good-claude-md"
see_also: [S3, S1]
---

# Code Block Line Limit

Code blocks stay under 10 lines to minimize token usage.

## Pattern

**Good:** 5-line example showing key pattern
**Bad:** 25-line function pasted as example
