---
id: C1
title: Core Sections
category: content
type: semantic
backed_by:
  - source: claude-code-memory
    claim: use-structure
  - source: spec-writing-for-agents
    claim: commands-early
  - source: agents-md-spec
    claim: root-placement
  - source: agents-md-spec
    claim: executable-commands
  - source: agents-md-spec
    claim: recommended-sections
  - source: agents-md-spec
    claim: no-required-fields
  - source: using-claude-md-files
    claim: usage-patterns
  - source: claude-md-guide
    claim: practical-examples
  - source: claude-md-optimization-study
    claim: optimization-improvement
  - source: dometrain-claude-md-guide
    claim: domain-terminology
  - source: dometrain-claude-md-guide
    claim: command-specificity
  - source: osmani-ai-coding-workflow
    claim: planning-before-coding
checks:
  - id: C1-missing-sections
    name: Large file missing core sections
    severity: high
    pattern_confidence: high
question: "Does this file have adequate coverage of project context?"
criteria:
  - Files 100+ lines have Project/Stack/Commands/Constraints sections
  - Section names may vary but concepts must be present
  - Smaller files may omit sections if context is clear
sources:
  - "https://claude.com/blog/using-claude-md-files"
see_also: [C9, S1]
---

# Core Sections

Large instruction files include Project, Stack, Commands, Constraints.

## Pattern

**Good:** ## Stack, ## Commands, ## Constraints sections present
**Bad:** 150-line file with no organizational structure
