---
id: M2
title: Review Process
category: maintenance
type: semantic
backed_by:
  - source: claude-code-best-practices
    claim: iterative-refinement
  - source: claude-code-memory
    claim: review-periodically
  - source: anthropic-teams-claude-code
    claim: review-process
  - source: agents-md-spec
    claim: living-document
  - source: anthropic-teams-claude-code
    claim: test-driven-guidance
  - source: claude-md-optimization-study
    claim: iterative-tuning
  - source: dometrain-claude-md-guide
    claim: living-document-updates
checks:
  - id: M2-no-review-process
    name: No PR review process documented
    severity: medium
question: "Is there a review process for instruction file changes?"
criteria:
  - PR approval documented or CODEOWNERS exists
  - Changes require review before merge
  - Review responsibility is clear
sources:
  - "https://claude.com/blog/how-anthropic-teams-use-claude-code"
see_also: [M3, G3]
---

# Review Process

PR approval process documented or CODEOWNERS exists.

## Pattern

**Good:** CODEOWNERS with @team for CLAUDE.md
**Bad:** Anyone can modify instructions without review
