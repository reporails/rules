---
id: C9
title: Has Project Description
category: content
type: deterministic
backed_by:
  - source: anthropic-teams-claude-code
    claim: team-onboarding
  - source: agents-md-spec
    claim: recommended-sections
  - source: agents-md-spec
    claim: readme-for-agents
  - source: using-claude-md-files
    claim: usage-patterns
  - source: dometrain-claude-md-guide
    claim: domain-terminology
checks:
  - id: C9-no-description
    name: First line after title is empty
    severity: medium
    pattern_confidence: high
sources:
  - "https://claude.com/blog/using-claude-md-files"
see_also: [C1, S5]
---

# Has Project Description

First line after title is non-empty project description.

## Pattern

**Good:** "# MyApp\n\nA REST API for user management."
**Bad:** "# MyApp\n\n## Tech Stack" (no description)
