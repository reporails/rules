---
id: S5
title: Clear Markdown Structure
category: structure
type: deterministic
backed_by:
  - source: claude-code-memory
    claim: use-structure
  - source: agents-md-spec
    claim: standard-markdown
checks:
  - id: S5-heading-hierarchy-skip
    name: Heading level skipped (e.g., # to ###)
    severity: medium
    pattern_confidence: medium
sources:
  - "https://code.claude.com/docs/en/memory"
see_also: [C1, S2]
---

# Clear Markdown Structure

Headings follow hierarchy: # then ## then ###, no skipping.

## Pattern

**Good:** # Title, ## Section, ### Subsection
**Bad:** # Title, ### Subsection (skipped ##)
