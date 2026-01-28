---
id: C3
title: Context-Specific Content
category: content
type: semantic
confidence: high
backed_by:
  - source: claude-code-memory
    claim: keep-rules-focused
  - source: instruction-limits-principles
    claim: progressive-files
  - source: spec-writing-for-agents
    claim: modularity
checks:
  - id: C3-domain-in-root
    name: Domain-specific content in root instruction file
    severity: medium
question: "Is domain-specific content appropriately placed?"
criteria:
  - Root file contains general project context only
  - Domain details are in @imports or path-scoped rules
  - No API endpoints or implementation details in root
sources:
  - "https://www.anthropic.com/engineering/claude-code-best-practices"
  - "https://code.claude.com/docs/en/memory"
see_also: [S2, CLAUDE_S3]
---

# Context-Specific Content

Root file is general; domain content lives in @imports or rules.

## Pattern

**Good:** Root has stack overview; API details in @docs/api.md
**Bad:** Root file with 50 lines of endpoint documentation
