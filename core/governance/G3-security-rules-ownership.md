---
id: G3
title: Security Rules Ownership
category: governance
type: semantic
confidence: high
backed_by:
  - source: anthropic-teams-claude-code
    claim: governance-roles
checks:
  - id: G3-security-unowned
    name: Security rules lack qualified owners
    severity: high
question: "Are security rules properly owned by qualified personnel?"
criteria:
  - Security rules have designated owners
  - Owners have relevant expertise
  - Review process exists for security changes
sources:
  - "https://www.anthropic.com/engineering/claude-code-best-practices"
  - "docs/methodology-thresholds.md"
see_also: [G2, G4]
---

# Security Rules Ownership

Security rules have qualified owners.

## Pattern

**Good:** "@security-team owns all NEVER statements about credentials"
**Bad:** Security rules with no clear ownership
