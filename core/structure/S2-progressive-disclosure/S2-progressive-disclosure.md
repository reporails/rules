---
id: S2
title: Progressive Disclosure
category: structure
type: deterministic
backed_by:
  - source: claude-code-memory
    claim: imports-syntax
  - source: claude-code-memory
    claim: recursive-discovery
  - source: instruction-limits-principles
    claim: progressive-files
  - source: agents-md-spec
    claim: nested-monorepo
  - source: codex-agents-md
    claim: discovery-order
  - source: codex-agent-loop
    claim: cascading-later-wins
  - source: agents-md-spec
    claim: nearest-precedence
  - source: spec-writing-for-agents
    claim: modularity
  - source: monorepo-claude-md-organization
    claim: reduction-achieved
  - source: monorepo-claude-md-organization
    claim: service-specific-files
  - source: claude-md-guide
    claim: file-placement
  - source: dometrain-claude-md-guide
    claim: lazy-loading-context
checks:
  - id: S2-large-file-no-imports
    name: File over 100 lines without @imports or references
    severity: high
    pattern_confidence: high
sources:
  - "https://code.claude.com/docs/en/memory"
see_also: [S1, E7]
---

# Progressive Disclosure

Large files use @imports or "See X for Y" to avoid token bloat.

## Pattern

**Good:** `@docs/api-reference.md` or "See CONTRIBUTING.md for style guide"
**Bad:** 150-line file with all content inline
