---
id: S5
title: Path-Scoped Rules
category: structure
type: heuristic
detection: YAML frontmatter with "paths:" key; cannot verify paths are meaningful
level: L4+
scoring: 5
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
