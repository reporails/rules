---
description: Coordinate map sync constraint for rule directory changes
globs:
  - "core/**"
  - "agents/*/rules/**"
---

# Coordinate Map Sync

This rule extends the parent scope for core and agent rule directories.

After creating, deleting, or renaming a rule directory, update @registry/coordinate-map.yml to keep the mapping complete.

Format in coordinate-map.yml:

```yaml
slug: "COORDINATE"
# e.g., backbone-index-completeness: "CORE:M:0004"
```

See CORE:M:0004 in the corresponding rule.md for the completeness requirement.

Every rule directory must have these files:
- rule.md
- rule.yml
