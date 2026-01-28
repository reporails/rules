---
id: CLAUDE_S1
title: Skill Size Limits
category: structure
type: deterministic
confidence: low
backed_by:
  - source: capability-levels
    claim: methodology-skill-size
checks:
  - id: CLAUDE_S1-skill-too-long
    name: SKILL.md file exceeds 100 lines
    severity: medium
sources:
  - "docs/methodology-thresholds.md"
see_also: [S1, CLAUDE_M2]
---

# Skill Size Limits

Keeps .claude/skills/*/SKILL.md files under 100 lines. Extract details to supporting files.

## Pattern

**Good:** Focused 60-line SKILL.md with references to supporting files
**Bad:** 250-line SKILL.md with embedded documentation
