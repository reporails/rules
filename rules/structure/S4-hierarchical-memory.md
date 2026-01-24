---
id: S4
title: Hierarchical Memory
category: structure
type: deterministic
detection: Directory existence (.claude/rules/) and file glob (**/CLAUDE.md)
level: L4+
sources: [2, 4, 14, 15]
---

# Hierarchical Memory

Context loads only when relevant.

## Structure

- `~/.claude/CLAUDE.md` — User preferences (all projects)
- `project/CLAUDE.md` — Project root (shared team)
- `project/.claude/rules/` — Modular rules (testing.md, security.md)
- `project/src/api/CLAUDE.md` — Subdirectory context

## Symlink Support

The `.claude/rules/` directory supports symlinks for sharing rules across projects:

```bash
# Symlink shared rules directory
ln -s ~/shared-claude-rules .claude/rules/shared

# Symlink individual rule files
ln -s ~/company-standards/security.md .claude/rules/security.md
```

Symlinks are resolved and contents loaded normally. Circular symlinks are detected and handled gracefully.

## Benefits

- User preferences persist across projects
- Team rules shared at project level
- Domain-specific rules load only for matching paths
- Symlinks enable org-wide rule sharing
