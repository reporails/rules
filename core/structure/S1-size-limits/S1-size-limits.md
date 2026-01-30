---
id: S1
title: Size Limits
category: structure
type: deterministic
backed_by:
  - source: claude-code-best-practices
    claim: keep-concise
  - source: instruction-limits-principles
    claim: line-limit
  - source: agents-md-spec
    claim: root-placement
  - source: codex-agents-md
    claim: size-limit-32kb
  - source: instruction-limits-principles
    claim: instruction-capacity
  - source: instruction-limits-principles
    claim: less-is-more
  - source: spec-writing-for-agents
    claim: curse-of-instructions
  - source: monorepo-claude-md-organization
    claim: reduction-achieved
  - source: enterprise-claude-usage
    claim: kb-limit
  - source: claude-md-optimization-study
    claim: optimization-improvement
  - source: claude-code-issue-13579
    claim: token-waste-measured
checks:
  - id: S1-root-too-long
    name: Root instruction file exceeds 200 lines
    severity: critical
    pattern_confidence: very_high
sources:
  - "https://www.anthropic.com/engineering/claude-code-best-practices"
  - "https://www.humanlayer.dev/blog/writing-a-good-claude-md"
see_also: [S2]
---

# Size Limits

Prevents instruction degradation from token bloat. Frontier LLMs follow ~150-200 instructions with reasonable consistency; exceeding this causes uniform quality degradation.

## Pattern

**Good:** Root file under 100 lines with @imports for details
**Bad:** 300-line monolithic instruction file with 200+ instructions
