---
id: C9
title: Has Project Description
category: content
type: deterministic
confidence: high
backed_by:
  - source: claude-code-best-practices
    claim: include-core-files
  - source: anthropic-teams-claude-code
    claim: team-onboarding
  - source: agents-md-spec
    claim: recommended-sections
checks:
  - id: C9-no-description
    name: First line after title is empty
    severity: medium
sources:
  - "https://www.anthropic.com/engineering/claude-code-best-practices"
  - "https://claude.com/blog/using-claude-md-files"
see_also: [C1, S7]
---

# Has Project Description

First line after title is non-empty project description.

## Pattern

**Good:** "# MyApp\n\nA REST API for user management."
**Bad:** "# MyApp\n\n## Tech Stack" (no description)
