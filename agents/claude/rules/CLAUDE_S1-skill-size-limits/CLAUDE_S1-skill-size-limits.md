---
id: CLAUDE_S1
title: Skill Size Limits
category: structure
type: deterministic
backed_by: []
checks:
  - id: CLAUDE_S1-skill-too-long
    name: SKILL.md file exceeds 100 lines
    severity: medium
    pattern_confidence: very_high
sources: []
see_also: [S1, CLAUDE_M2]
---

# Skill Size Limits

Keeps .claude/skills/*/SKILL.md files under 100 lines. Extract details to supporting files.

## Pattern

**Good:** Focused 60-line SKILL.md with references to supporting files
**Bad:** 250-line SKILL.md with embedded documentation
