---
id: M3
title: Change Management
category: maintenance
type: semantic
checks:
  - id: M3-no-change-process
    name: No change management documented
    severity: medium
question: "Is there a change management process for instructions?"
criteria:
  - Approval matrix or change process documented
  - Breaking changes require notification
  - Versioning strategy exists
sources:
  - "https://claude.com/blog/how-anthropic-teams-use-claude-code"
see_also: [M2, C12]
---

# Change Management

Approval matrix or change process documented.

## Pattern

**Good:** "Major changes require team lead approval"
**Bad:** No guidance on how to propose changes
