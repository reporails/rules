---
id: E8
title: Context Window Awareness
category: efficiency
type: deterministic
backed_by:
  - source: claude-context-windows
    claim: context-awareness
  - source: claude-context-windows
    claim: avoid-token-warnings
  - source: claude-code-issue-13579
    claim: token-waste-measured
  - source: advanced-context-engineering
    claim: context-target
  - source: advanced-context-engineering
    claim: frequent-compaction
  - source: codex-agent-loop
    claim: auto-compaction
  - source: dometrain-claude-md-guide
    claim: lazy-loading-context
  - source: dometrain-claude-md-guide
    claim: duplicate-instruction-waste
  - source: osmani-ai-coding-workflow
    claim: iterative-chunks
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
