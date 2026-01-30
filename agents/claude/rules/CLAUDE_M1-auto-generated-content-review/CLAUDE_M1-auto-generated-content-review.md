---
id: CLAUDE_M1
title: Auto-Generated Content Review
category: maintenance
type: deterministic
backed_by:
  - source: using-claude-md-files
    claim: customized-content
checks:
  - id: CLAUDE_M1-init-boilerplate
    name: Unmodified /init boilerplate detected
    severity: high
    pattern_confidence: medium
sources:
  - "https://www.anthropic.com/engineering/claude-code-best-practices"
  - "https://claude.com/blog/using-claude-md-files"
see_also: [C1, C9]
---

# Auto-Generated Content Review

No unmodified /init boilerplate signatures.

## Pattern

**Good:** Customized CLAUDE.md with project-specific content
**Bad:** Default /init output with generic placeholders
