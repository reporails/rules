---
id: C2
title: Explicit Over Implicit
category: content
type: deterministic
backed_by:
  - source: claude-code-memory
    claim: be-specific
  - source: claude-4-best-practices
    claim: be-explicit
  - source: agents-md-spec
    claim: chat-overrides
  - source: dometrain-claude-md-guide
    claim: command-specificity
  - source: osmani-ai-coding-workflow
    claim: context-packaging
checks:
  - id: C2-vague-instruction
    name: Vague instruction without specifics
    severity: medium
sources:
  - "https://www.anthropic.com/engineering/claude-code-best-practices"
  - "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices"
see_also: [C8, C5]
---

# Explicit Over Implicit

Avoid "properly", "correctly", "appropriate" without specifics.

## Pattern

**Good:** "Use 2-space indentation"
**Bad:** "Format code properly"
