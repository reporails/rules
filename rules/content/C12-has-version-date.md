---
id: C12
title: Has Version/Date
category: content
type: deterministic
detection: Regex for version pattern or date in frontmatter/header
level: L2+
sources: [1]
---

# Has Version/Date

Enables staleness detection and compatibility tracking.

CLAUDE.md should indicate when it was last updated or its version.

## Pattern

**Good:** Clear versioning
- `<!-- Last updated: 2025-01-21 -->`
- `version: 1.2.0` in YAML frontmatter

**Bad:** No version info
- No indication of when content was written
