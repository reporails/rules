---
id: E6
title: Code Block Line Limit
category: efficiency
type: deterministic
confidence: high
backed_by:
  - source: capability-levels
    claim: methodology-threshold-code-blocks
checks:
  - id: E6-code-block-too-long
    name: Code block exceeds 10 lines
    severity: medium
sources:
  - "https://www.anthropic.com/engineering/claude-code-best-practices"
  - "https://www.humanlayer.dev/blog/writing-a-good-claude-md"
  - "docs/methodology-thresholds.md"
see_also: [S3, S1]
---

# Code Block Line Limit

Code blocks stay under 10 lines to minimize token usage.

## Pattern

**Good:** 5-line example showing key pattern
**Bad:** 25-line function pasted as example
