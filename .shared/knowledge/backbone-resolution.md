# Backbone Path Resolution

How to resolve paths from `.reporails/backbone.yml` instead of hardcoding them.

## Step 0: Load Backbone

Read `.reporails/backbone.yml` before resolving any paths. All paths are relative to repo root.

## Resolution Table

| Need | Backbone Key | Example Value |
|------|-------------|---------------|
| Core rules base | `rules.core` | `core/` |
| Agent rules base | `rules.agent_rules.{agent}` | `agents/claude/rules/` |
| Category dir | `rules.categories.{category}` | `core/structure/` |
| Rule dir pattern | `rules.patterns.rule_dir` | `{category}/{slug}/` |
| Rule definition | `rules.patterns.definition` | `rule.md` |
| Rule OpenGrep | `rules.patterns.opengrep` | `rule.yml` |
| Test pass dir | `rules.patterns.test_pass` | `tests/pass/` |
| Test fail dir | `rules.patterns.test_fail` | `tests/fail/` |
| Schema files | `schemas.{name}` | `schemas/rule.schema.yml` |
| Registry files | `registry.{name}` | `registry/coordinate-map.yml` |
| Source registry | `docs.sources` | `docs/sources.yml` |
| Agent config | `agents.{agent}.config` | `agents/claude/config.yml` |
| Agent skills | `agents.{agent}.skills` | `.claude/skills/` |
| Shared knowledge | `shared.knowledge` | `.shared/knowledge/` |
| Shared workflows | `shared.workflows` | `.shared/workflows/` |

## Coordinate-to-Path Algorithm

To resolve a coordinate (e.g., `CORE:S:0001`) to its filesystem path:

1. Look up slug in `registry/coordinate-map.yml` (e.g., `instruction-file-exists: "CORE:S:0001"`)
2. Determine category from the coordinate map's YAML structure (the slug lives under `core.structure`, so category = `structure`)
3. For agent coordinates (`CLAUDE:*`, `CODEX:*`), use `rules.agent_rules.{agent}` as base
4. Combine: `{category_dir}/{slug}/rule.md` (and `rule.yml`)

**Example:** `CORE:S:0001`
- Coordinate map: `core.structure.instruction-file-exists: "CORE:S:0001"`
- Category dir: `rules.categories.structure` → `core/structure/`
- Path: `core/structure/instruction-file-exists/rule.md`

**Agent example:** `CLAUDE:S:0001`
- Coordinate map: `agents.claude.claude-md-file-placement: "CLAUDE:S:0001"`
- Agent rules base: `rules.agent_rules.claude` → `agents/claude/rules/`
- Path: `agents/claude/rules/claude-md-file-placement/rule.md`

## When to Update backbone.yml

Update the backbone when:
- **New schema added** — add entry to `schemas`
- **New registry file added** — add entry to `registry`
- **New agent configured** — add entry to `agents`
- **New doc artifact added** — add entry to `docs`

Rule directories are NOT tracked in the backbone — they're tracked in `registry/coordinate-map.yml`.
