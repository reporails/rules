---
id: S3
title: No Embedded Code Snippets
category: structure
type: deterministic
backed_by:
  - source: spec-writing-for-agents
    claim: code-snippet-beats-prose
checks:
  - id: S3-code-block-too-long
    name: Code block exceeds 10 lines
    severity: medium
    pattern_confidence: very_high
sources:
  - "https://www.humanlayer.dev/blog/writing-a-good-claude-md"
see_also: [E6, S1]
---

# No Embedded Code Snippets

Code blocks should be brief examples, not function definitions.

## Pattern

**Good:** 3-line config example
**Bad:** 20-line function pasted inline
