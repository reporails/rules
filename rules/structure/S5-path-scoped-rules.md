---
id: S5
title: Path-Scoped Rules
category: structure
type: deterministic
detection: YAML frontmatter parse for "paths:" key in .claude/rules/*.md
level: L4+
sources: [2, 4, 15]
---

# Path-Scoped Rules

Rules load only for matching files.

## Example

`.claude/rules/api-routes.md`:

```yaml
---
paths: ["src/api/**/*.ts"]
---
```

Rules in this file apply only when editing files matching `src/api/**/*.ts`.
