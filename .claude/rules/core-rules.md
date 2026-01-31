---
globs:
  - "core/**"
  - "agents/*/rules/**"
---

# Backbone Index Sync

After creating, deleting, or renaming a rule directory, update `rules.index` in `.reporails/backbone.yml` to keep the index complete.

Format: `{ID}: {slug}` (e.g., `M6: backbone-index-completeness`).

See rule M6 for the completeness requirement.
