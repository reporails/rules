---
id: M1
title: Version Control
category: maintenance
type: deterministic
backed_by:
  - source: claude-code-best-practices
    claim: root-placement
  - source: claude-code-best-practices
    claim: version-control
  - source: agents-md-spec
    claim: living-document
  - source: claude-md-guide
    claim: file-placement
  - source: dometrain-claude-md-guide
    claim: living-document-updates
  - source: osmani-ai-coding-workflow
    claim: commit-savepoints
checks:
  - id: M1-not-tracked
    name: Instruction file not in git
    severity: high
    pattern_confidence: high
sources:
  - "https://www.anthropic.com/engineering/claude-code-best-practices"
see_also: [M2, C12]
---

# Version Control

Instruction files are git-tracked for change history.

## Pattern

**Good:** CLAUDE.md committed and tracked in git
**Bad:** Instruction file in .gitignore
