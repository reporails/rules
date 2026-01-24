---
id: G4
title: Ownership Assignment
category: governance
type: heuristic
detection: pattern-regex for owner/maintainer keywords in file headers or CODEOWNERS
question: Do instruction files have designated owners?
criteria: Pass if ownership is documented; fail if no owner assignment visible
level: L5+
sources: [7]
validation: theoretical
---

# Ownership Assignment

Ensures maintenance responsibility.

Every CLAUDE.md file should have a designated owner who:
- Reviews proposed changes
- Keeps content current
- Resolves conflicts with other files
