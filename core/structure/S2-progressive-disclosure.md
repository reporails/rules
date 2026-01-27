---
id: S2
title: Progressive Disclosure
category: structure
type: deterministic
confidence: high
backed_by:
  - source: claude-code-memory
    claim: imports-syntax
  - source: claude-code-memory
    claim: recursive-discovery
  - source: instruction-limits-principles
    claim: progressive-files
checks:
  - id: S2-large-file-no-imports
    name: File over 100 lines without @imports or references
    severity: high
sources:
  - "https://www.anthropic.com/engineering/claude-code-best-practices"
  - "https://code.claude.com/docs/en/memory"
see_also: [S1, E7]
---

# Progressive Disclosure

Large files use @imports or "See X for Y" to avoid token bloat.

## Pattern

**Good:** `@docs/api-reference.md` or "See CONTRIBUTING.md for style guide"
**Bad:** 150-line file with all content inline
