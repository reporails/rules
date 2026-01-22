---
id: E8
title: Context Window Awareness
category: efficiency
type: semantic
detection: Behavioral rule about AI usage patterns
level: L4+
sources: [5, 8]
---

# Context Window Awareness

Design for Claude 4.5's native token budget tracking.

Claude 4.5 models track remaining context throughout conversations. At session start, Claude receives its total budget; after each tool call, it receives remaining capacity updates.

## Implications for CLAUDE.md

- Sessions only hit limits during major refactoring, not routine work
- Don't waste tokens explaining context exhaustion handling
- Consider multi-window workflows for complex tasks
- Claude understands its own capacity—no need for "watch your tokens" instructions

## Pattern

**Good:** Trust the model's awareness
- Design CLAUDE.md for normal operation
- Let Claude manage its own token budget

**Bad:** Redundant guidance
- "Be careful not to exceed context limits"
- "Summarize long outputs to save tokens"
