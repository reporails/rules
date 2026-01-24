---
id: E6
title: Code Block Line Limit
category: efficiency
type: deterministic
detection: Count lines within triple-backtick blocks
level: L3+
sources: [1]
see_also: [S3]
antipatterns:
  - id: A18
    name: Large embedded code blocks
    severity: high
---

# Code Block Line Limit

Prevents embedding large code samples.

Code blocks in CLAUDE.md should be minimal (< 10 lines). Larger examples belong in referenced files.
