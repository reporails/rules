---
description: Backbone schema sync constraint for schema file changes
globs:
  - "schemas/**"
---

# Backbone Schema Sync

This rule extends the parent scope for schema directories.

After adding or removing schema files, update the `schemas` section in @.reporails/backbone.yml.

Format in backbone.yml:

```yaml
schemas:
  rule: schemas/rule.schema.yml
```

Schema naming convention follows:
- schemas/rule.schema.yml
- schemas/agent.schema.yml
- schemas/capability.schema.yml

See also @docs/pattern-guide.md
