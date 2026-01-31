---
id: M1
title: Version Control
category: maintenance
type: deterministic
backed_by:
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
  - "https://agents.md/"
see_also: [M2, C12]
---

# Version Control

Instruction files are git-tracked for change history.

## Pattern

**Good:** CLAUDE.md committed and tracked in git
**Bad:** Instruction file in .gitignore

## Limitations

Pattern detects explicit exclusion via `.gitignore` only. Cannot detect files that were never `git add`-ed — that requires runtime `git status` checks (tooling concern, not static analysis).
