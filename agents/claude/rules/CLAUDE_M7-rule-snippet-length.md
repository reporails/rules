---
id: CLAUDE_M7
title: Rule Snippet Length
category: maintenance
type: semantic
checks:
  - id: CLAUDE_M7-body-too-long
    name: Rule file body exceeds 40 lines (excluding frontmatter)
    severity: medium
  - id: CLAUDE_M7-scope-too-broad
    name: Rule file paths scope matches many files
    severity: medium
question: "Is this rule file justified in its length and scope?"
criteria:
  - File is focused on single concern
  - Length is necessary for completeness (cannot trim without losing value)
  - Broad scope is intentional (content applies to all matched files)
  - Cannot be reasonably split without fragmenting the topic
sources:
  - "docs/methodology-thresholds.md"
see_also: [S1, S2]
---

# Rule Snippet Length

Rule files that are long or broadly scoped consume tokens on every matched file operation.

## Pattern

**Good:** Focused 30-line rule scoped to specific paths
**Bad:** 180-line reference doc scoped to all rule files
