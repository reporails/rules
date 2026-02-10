---
globs:
  - "core/**"
  - "agents/*/rules/**"
---

# Coordinate Map Sync

After creating, deleting, or renaming a rule directory, update `registry/coordinate-map.yml` to keep the mapping complete.

Format: `slug: "COORDINATE"` (e.g., `backbone-index-completeness: "CORE:M:0004"`).

See rule CORE:M:0004 for the completeness requirement.
