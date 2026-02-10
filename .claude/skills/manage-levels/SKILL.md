---
name: manage-levels
description: Sync, diff, and list level-capability mappings from registry
---

# /manage-levels

Manage level definitions in `registry/levels.yml` against the capability taxonomy in `registry/capabilities.yml`.

## Usage

```
/manage-levels <command> [options]
```

**Commands:**

| Command | Description |
|---------|-------------|
| `sync` | Regenerate levels.yml from capabilities.yml |
| `diff` | Show discrepancies between capabilities and levels without writing |
| `list [level]` | List capabilities per level (all levels, or a specific one like `L2`) |

## Examples

```
/manage-levels sync              # Regenerate levels.yml from capabilities
/manage-levels diff              # Show discrepancies only
/manage-levels list              # List all levels and their capabilities
/manage-levels list L2           # List capabilities at L2 only
```

## Workflow

Follow: [@.shared/workflows/level-sync.md](../../../.shared/workflows/level-sync.md)

## Quick Reference

| Source of truth | `registry/capabilities.yml` |
|---|---|
| Derived file | `registry/levels.yml` |
| Assignment logic | Each capability declares its level |
| Level metadata | Names and descriptions in levels.yml |
| Schema | `schemas/levels.schema.yml` |