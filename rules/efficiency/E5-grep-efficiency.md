---
id: E5
title: Grep Efficiency
category: efficiency
type: semantic
detection: Behavioral rule about AI usage patterns
level: L4+
sources: [25]
see_also: [E3]
---

# Grep Efficiency

Prevents output bloat.

## Guidelines

Use appropriate output modes:
- `files_with_matches` for existence checks
- `head_limit` for bounded exploration
- Targeted patterns over broad searches

**Observed waste:** 1,600+ tokens from grep without limits.
