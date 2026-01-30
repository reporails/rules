---
id: C7
title: Emphasis Discipline
category: content
type: deterministic
backed_by:
  - source: claude-code-best-practices
    claim: emphasis-words
  - source: instruction-limits-principles
    claim: instruction-capacity
  - source: instruction-limits-principles
    claim: less-is-more
  - source: spec-writing-for-agents
    claim: curse-of-instructions
checks:
  - id: C7-too-many-emphasis
    name: More than 5 IMPORTANT/CRITICAL per file
    severity: medium
    pattern_confidence: high
sources:
  - "https://www.anthropic.com/engineering/claude-code-best-practices"
  - "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices"
see_also: [C4, C5]
---

# Emphasis Discipline

Limit IMPORTANT/CRITICAL to 5 per file to maintain impact.

## Pattern

**Good:** 2-3 truly critical items emphasized
**Bad:** 10 items marked IMPORTANT (dilutes priority)
