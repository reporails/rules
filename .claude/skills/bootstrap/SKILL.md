---
name: bootstrap
description: Load project context — backbone, registry, and constraints — before any work
---

# /bootstrap

Initialize session context by reading the foundational files that all other skills and tasks depend on.

## Usage

```
/bootstrap [--verbose]
```

- `--verbose`: Print summaries of each loaded file instead of just confirmation

## When to Use

- At the start of every session before doing any work
- After switching branches (context may have shifted)
- When you're unsure whether foundational context is loaded

## Workflow

### 1. Load backbone (project topology)

Read `.reporails/backbone.yml`. This is the single source of truth for:
- Agent configurations and instruction file locations
- Rule directory patterns and category paths
- Schema file paths
- Registry file paths
- Shared knowledge and workflow locations

**After this step you MUST NOT use exploratory commands (find, ls, glob) to discover paths the backbone already provides.**

### 2. Load registry (architecture)

Read these two files from paths resolved via backbone:

| Backbone Key | File | Purpose |
|---|---|---|
| `registry.capabilities` | `registry/capabilities.yml` | Capability taxonomy — what each level requires |
| `registry.levels` | `registry/levels.yml` | Level definitions — L0 through L6 progression |

These define the scoring and evaluation model that all rules target.

### 3. Load coordinate map (rule index)

Read `registry/coordinate-map.yml` (from `backbone.registry.coordinate_map`).

This maps every rule slug to its coordinate (e.g., `instruction-file-exists: "CORE:S:0001"`). Required for:
- Resolving coordinates to filesystem paths
- Detecting gaps or duplicates when creating rules
- Understanding what rules exist in each category

### 4. Load task-scoped constraints

Read all files in `.claude/rules/`:

| File | Scope |
|---|---|
| `core-rules.md` | Coordinate map sync after rule changes |
| `schemas.md` | Backbone schema sync after schema changes |
| `skills.md` | Backbone path resolution for skills |

These are context-specific constraints that apply during the session.

### 5. Check project state

Read `VERSION` and `UNRELEASED.md` to understand:
- Current version number
- What changes are already staged for the next release
- Which areas have been recently modified

### 6. Confirm readiness

Report what was loaded:

```
Bootstrap complete.
- Backbone: v{version}, {n} schemas, {n} registry files
- Capabilities: {n} capabilities across {n} levels
- Coordinate map: {n} rules indexed
- Constraints: {n} rule files loaded
- Version: {version}, {n} unreleased changes
```

## Reference

- Backbone: [.reporails/backbone.yml](../../../.reporails/backbone.yml)
- Path resolution: [@.shared/knowledge/backbone-resolution.md](../../../.shared/knowledge/backbone-resolution.md)
- Capabilities: [registry/capabilities.yml](../../../registry/capabilities.yml)
- Levels: [registry/levels.yml](../../../registry/levels.yml)
- Coordinate map: [registry/coordinate-map.yml](../../../registry/coordinate-map.yml)
