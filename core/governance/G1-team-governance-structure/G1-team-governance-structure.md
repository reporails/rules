---
id: G1
title: Team Governance Structure
category: governance
type: semantic
backed_by:
  - source: anthropic-teams-claude-code
    claim: governance-roles
checks:
  - id: G1-no-governance
    name: No team governance documented
    severity: medium
    pattern_confidence: medium
question: "Is team governance structure documented?"
criteria:
  - Roles table or responsibility list exists
  - Clear ownership of instruction files
  - Decision-making process documented
sources:
  - "https://claude.com/blog/how-anthropic-teams-use-claude-code"
see_also: [G3, M2]
---

# Team Governance Structure

Roles table or responsibility list documented.

## Pattern

**Good:** "| Role | Responsibility | Owner |" table
**Bad:** No clarity on who owns what
