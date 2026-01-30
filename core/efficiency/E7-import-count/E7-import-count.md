---
id: E7
title: Import Count
category: efficiency
type: deterministic
backed_by:
  - source: claude-code-memory
    claim: import-max-depth
checks:
  - id: E7-too-many-imports
    name: More than 10 @imports in root file
    severity: medium
    pattern_confidence: high
sources:
  - "https://code.claude.com/docs/en/memory"
  - "https://dev.to/anvodev/how-i-organized-my-claudemd-in-a-monorepo-with-too-many-contexts-37k7"
see_also: [S2, S1]
---

# Import Count

@imports scale with file size; root file under 10 imports.

## Pattern

**Good:** 3-5 imports to key documentation
**Bad:** 15 imports loading everything at once
