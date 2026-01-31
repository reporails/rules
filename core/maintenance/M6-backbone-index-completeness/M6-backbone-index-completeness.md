---
id: M6
title: Backbone Index Completeness
category: maintenance
type: deterministic
backed_by: []
  # experimental tier — community pattern (no official/research source)
checks:
  - id: M6-index-present
    name: Backbone has rules index section
    severity: medium
    pattern_confidence: low
sources: []
see_also: [M5, S4]
---

# Backbone Index Completeness

Every rule directory on the filesystem is registered in `backbone.yml` `rules.index`.

Complements M5 (which checks the inverse: backbone paths exist on disk). M6 ensures no filesystem entity is orphaned from the index.

## Pattern

**Good:** All rule directories under `core/` and `agents/*/rules/` have corresponding entries in `rules.index`
**Bad:** A rule directory exists but has no entry in `rules.index`, making it invisible to backbone-based path resolution

## Recommended Automation

A pre-commit hook can enforce this automatically:

1. List rule directories matching `core/*/{ID}-{slug}/` and `agents/*/rules/{ID}-{slug}/`
2. Parse `rules.index` from `.reporails/backbone.yml`
3. Warn on mismatches (directories not in index, or index entries without directories)

Example check (conceptual — adapt to your CI toolchain):

```bash
# Extract rule IDs from filesystem
fs_ids=$(find core agents/*/rules -mindepth 2 -maxdepth 2 -type d \
  | sed 's|.*/\([A-Z_]*[0-9]*\)-.*|\1|' | sort -u)

# Extract rule IDs from backbone index
index_ids=$(grep -E '^\s+[A-Z_]+[0-9]+:' .reporails/backbone.yml \
  | sed 's/^\s*\([A-Z_]*[0-9]*\):.*/\1/' | sort -u)

# Compare
diff <(echo "$fs_ids") <(echo "$index_ids")
```

This is documented as a recommendation. The framework does not ship executable hooks.
