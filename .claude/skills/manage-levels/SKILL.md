---
name: manage-levels
description: Sync, diff, and list level-rule mappings from capability matrix
---

# /manage-levels

Manage `levels.yml` from the authoritative `docs/capability-levels.md` Capability Assessment Matrix.

## Usage

```
/manage-levels <command> [options]
```

**Commands:**

| Command | Description |
|---------|-------------|
| `sync` | Parse matrix from capability-levels.md, regenerate levels.yml |
| `diff` | Show discrepancies between matrix and current levels.yml without writing |
| `list [level]` | List rules per level (all levels, or a specific one like `L2`) |

## Examples

```
/manage-levels sync              # Regenerate levels.yml from matrix
/manage-levels diff              # Show discrepancies only
/manage-levels list              # List all levels and their rules
/manage-levels list L2           # List rules at L2 only
```

## Workflow

Follow: [@.shared/workflows/level-sync.md](../../../.shared/workflows/level-sync.md)

## Quick Reference

| Source of truth | `backbone.artifacts.capability_levels` |
|---|---|
| Derived artifact | `backbone.artifacts.levels` |
| Assignment logic | First `+` in a row = rule's introduction level |
| Level metadata | Name and description from Level Descriptions section |
