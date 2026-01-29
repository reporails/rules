---
id: G2
title: Security Rules Ownership
category: governance
type: semantic
backed_by:
  - source: anthropic-teams-claude-code
    claim: governance-roles
checks:
  - id: G2-security-unowned
    name: Security rules lack qualified owners
    severity: high
question: "Are security rules properly owned by qualified personnel?"
criteria:
  - Security rules have designated owners
  - Owners have relevant expertise
  - Review process exists for security changes
sources:
  - "https://www.anthropic.com/engineering/claude-code-best-practices"
  - "https://claude.com/blog/how-anthropic-teams-use-claude-code"
see_also: [G1, G3]
---

# Security Rules Ownership

Security rules have qualified owners.

## Pattern

**Good:** "@security-team owns all NEVER statements about credentials"
**Bad:** Security rules with no clear ownership
