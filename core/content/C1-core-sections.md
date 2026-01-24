---
id: C1
title: Core Sections
category: content
type: semantic
checks:
  - id: C1-missing-sections
    name: Large file missing core sections
    severity: high
question: "Does this file have adequate coverage of project context?"
criteria:
  - Files 100+ lines have Project/Stack/Commands/Constraints sections
  - Section names may vary but concepts must be present
  - Smaller files may omit sections if context is clear
sources:
  - "https://www.anthropic.com/engineering/claude-code-best-practices"
  - "https://claude.com/blog/using-claude-md-files"
see_also: [C9, S1]
---

# Core Sections

Large instruction files include Project, Stack, Commands, Constraints.

## Pattern

**Good:** ## Stack, ## Commands, ## Constraints sections present
**Bad:** 150-line file with no organizational structure
