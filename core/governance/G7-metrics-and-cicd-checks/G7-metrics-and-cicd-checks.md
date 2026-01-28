---
id: G7
title: Metrics and CI/CD Checks
category: governance
type: deterministic
confidence: high
backed_by:
  - source: anthropic-teams-claude-code
    claim: automated-pr-comments
checks:
  - id: G7-no-ci-checks
    name: No CI workflow with instruction file checks
    severity: medium
sources:
  - "https://claude.com/blog/how-anthropic-teams-use-claude-code"
see_also: [G6, M2]
---

# Metrics and CI/CD Checks

.github/workflows/*.yml with instruction file checks.

## Pattern

**Good:** CI workflow that validates CLAUDE.md on PR
**Bad:** No automated validation of instruction files
