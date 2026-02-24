---
description: Backbone path resolution constraint for skill references
globs:
  - ".claude/skills/**"
---

# Backbone Path References

This rule extends the parent scope for skill directories.

Skills resolve paths from @.reporails/backbone.yml. When referencing a new schema or registry file, verify the path exists in `backbone.schemas` or `backbone.registry`.

Example path check in a SKILL.md:

```yaml
# backbone.schemas.rule → schemas/rule.schema.yml
```

Resolution reference:
- @.shared/knowledge/backbone-resolution.md
