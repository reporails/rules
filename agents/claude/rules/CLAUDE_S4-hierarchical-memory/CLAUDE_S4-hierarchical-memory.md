---
id: CLAUDE_S4
title: Hierarchical Memory
category: structure
type: deterministic
confidence: high
backed_by:
  - source: claude-code-memory
    claim: memory-hierarchy
  - source: claude-code-memory
    claim: rules-directory
  - source: agents-md-spec
    claim: nested-monorepo
checks:
  - id: CLAUDE_S4-rules-dir-missing
    name: .claude/rules/ directory does not exist
    severity: high
sources:
  - "https://code.claude.com/docs/en/memory"
  - "https://code.claude.com/docs/en/settings"
see_also: [CLAUDE_S5, S2]
---

# Hierarchical Memory

L4+ projects require `.claude/rules/` directory for modular rules.

## Pattern

**Good:** `.claude/rules/` with path-scoped rule files
**Bad:** All rules in root CLAUDE.md
