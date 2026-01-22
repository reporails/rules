---
id: C9
title: Has Project Description
category: content
type: deterministic
detection: First line after # heading is non-empty
level: L2+
scoring: 5
sources: [1, 6]
---

# Has Project Description

Ensures Claude understands project context immediately.

The root CLAUDE.md must have a project description as the first content after the title.

## Pattern

**Good:** Clear context
- "This is a Next.js e-commerce platform with Stripe integration."

**Bad:** Missing description
- Title followed immediately by section headers
