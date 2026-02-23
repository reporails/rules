---
name: bootstrap
description: Load project context — backbone, registry, and constraints — before any work
---

# /bootstrap

Initialize session context by building a working mental model of the project — topology, navigation, operations, and constraints.

## Usage

```
/bootstrap
```

## Workflow

Follow: [@.shared/workflows/bootstrap.md](../../../.shared/workflows/bootstrap.md)

### 1. Load backbone (project topology)

Read `.reporails/backbone.yml`. This is the single source of truth for all paths in the project. After this step you MUST NOT use exploratory commands (find, ls, glob) to discover paths the backbone already provides.

Extract and hold:
- **Agents**: which agents exist, their config paths, their instruction file names
- **Rule categories**: the category → directory mapping (e.g., `structure` → `core/structure/`)
- **Schemas**: the schema name → path mapping (8 schemas)
- **Registry**: capabilities, levels, coordinate map, tombstones paths

### 2. Load registry (architecture)

Read from backbone-resolved paths:

| Backbone Key | Purpose |
|---|---|
| `registry.capabilities` | Capability taxonomy — what features each level requires |
| `registry.levels` | Level definitions — L0 through L6 progression |

Build understanding: levels are the horizontal axis (which rules apply), score is the vertical axis (pass-rate against applicable rules). Level is INPUT to rule selection, not output of scoring.

### 3. Load coordinate map (rule index)

Read `registry/coordinate-map.yml` (from `backbone.registry.coordinate_map`).

Establish the resolution chain:
```
Coordinate (e.g., CORE:S:0001)
  → coordinate-map → slug (e.g., root-instruction-file-exists)
  → backbone.rules.categories.{cat} → base path (e.g., core/structure/)
  → base path + slug + "/" → rule directory
```

Count rules per category for the report. Flag any coordinate-map entries whose directories don't exist.

### 4. Load task-scoped constraints

Read all files in `.claude/rules/`:

| File | Constraint |
|---|---|
| `core-rules.md` | Coordinate map sync after rule changes |
| `schemas.md` | Backbone schema sync after schema changes |
| `skills.md` | Backbone path resolution for skills |

These are active constraints — they apply to every operation in this session.

### 5. Check project state

Read `VERSION` and `UNRELEASED.md`:
- Current version number and branch name
- What changes are staged for next release, grouped by area
- Whether unreleased changes overlap with any area the agent might touch

### 6. Report understanding

Produce a synthesized context report:

```
Bootstrap complete.

Project: Reporails Framework v{version} (branch: {branch})
Rules: {total} ({n} structure, {n} content, {n} context_quality, {n} efficiency, {n} governance, {n} maintenance, {n} agent)
Levels: L0-L6, {n} capabilities
Agents: {list from backbone.agents}

Navigation:
  Coordinate → path: coordinate-map → slug → backbone.rules.categories.{cat}/{slug}/
  Schemas: backbone.schemas.{name}
  Agent config: backbone.agents.{agent}.config

Operations:
  Create rule     → /generate-rule (skeleton + coordinate assignment)
  Implement rule  → /implement-rule (checks, patterns, fixtures)
  Test rules      → /test-rules (docker compose local harness, runs fixtures)
  Validate rules  → /validate-rules (schema + contract validation)

Constraints active:
  - {constraint summary from each .claude/rules/ file}

Unreleased: {count} changes ({areas touched})
```

## Examples

```
> /bootstrap

Bootstrap complete.

Project: Reporails Framework v0.4.1 (branch: 0.5.0)
Rules: 101 (36 structure, 32 content, 7 context_quality, 5 efficiency, 9 governance, 1 maintenance, 16 agent)
Levels: L0-L6, 12 capabilities
Agents: claude, codex, copilot, generic

Navigation:
  Coordinate → path: coordinate-map → slug → backbone.rules.categories.{cat}/{slug}/
  Schemas: backbone.schemas.{name}
  Agent config: backbone.agents.{agent}.config

Operations:
  Create rule     → /generate-rule
  Implement rule  → /implement-rule
  Test rules      → /test-rules (docker local harness)
  Validate rules  → /validate-rules (schema contracts)

Constraints active:
  - Coordinate map sync required after rule changes
  - Backbone schema sync required after schema changes
  - Skills must resolve paths from backbone

Unreleased: 16 changes (schemas, agents, meta, docs)
```

## Reference

- Backbone: `.reporails/backbone.yml` — project topology, all path resolution
- Path resolution: `.shared/knowledge/backbone-resolution.md` — coordinate-to-path algorithm
- Capabilities: `registry/capabilities.yml` — capability taxonomy per level
- Levels: `registry/levels.yml` — L0-L6 progression definitions
- Coordinate map: `registry/coordinate-map.yml` — slug-to-coordinate index

## Quick Reference

| Question | Answer |
|---|---|
| How do I find a rule by coordinate? | coordinate-map → slug → `backbone.rules.categories.{cat}/{slug}/` |
| How do I test rules? | `/test-rules` — docker compose local harness, runs pass/fail fixtures |
| How do I validate rules against schema? | `/validate-rules` — schema + contract checks |
| What schemas exist? | `backbone.schemas` — 8 schemas (rule, capability, levels, agent, package, project, sources, user) |
| What constraints apply? | `.claude/rules/` — core-rules.md, schemas.md, skills.md |
