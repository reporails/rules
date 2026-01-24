---
id: E8
title: Context Window Awareness
category: efficiency
type: deterministic
checks:
  - id: E8-redundant-token-warning
    name: Redundant token management instruction
    severity: low
sources:
  - "https://platform.claude.com/docs/en/build-with-claude/context-windows"
  - "https://www.anthropic.com/engineering/claude-code-best-practices"
see_also: [E3, E4]
---

# Context Window Awareness

Avoid redundant "watch your tokens" instructions (model handles this).

## Pattern

**Good:** Specific strategies like "use files_with_matches"
**Bad:** "Be mindful of token limits" (unhelpful, model-native)
