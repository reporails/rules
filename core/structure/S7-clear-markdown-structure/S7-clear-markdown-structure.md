---
id: S7
title: Clear Markdown Structure
category: structure
type: deterministic
confidence: high
backed_by:
  - source: claude-code-memory
    claim: use-structure
  - source: agents-md-spec
    claim: standard-markdown
checks:
  - id: S7-heading-hierarchy-skip
    name: Heading level skipped (e.g., # to ###)
    severity: medium
sources:
  - "https://www.anthropic.com/engineering/claude-code-best-practices"
see_also: [C1, S2]
---

# Clear Markdown Structure

Headings follow hierarchy: # then ## then ###, no skipping.

## Pattern

**Good:** # Title, ## Section, ### Subsection
**Bad:** # Title, ### Subsection (skipped ##)
