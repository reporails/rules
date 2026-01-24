---
id: M2
title: Review Process
category: maintenance
type: heuristic
detection: Git history check for PR-based changes to CLAUDE.md files
question: Are changes to instruction files going through code review?
criteria: Pass if CLAUDE.md changes have PR approval history; fail if direct commits without review
level: L3+
sources: [7]
---

# Review Process

Ensures quality and catches errors before deployment.

## Requirements

- Changes to CLAUDE.md should go through code review
- At least one other team member should approve changes
- Review for accuracy, completeness, and conflicts

**Note:** Required at L5+, recommended at L3+.
