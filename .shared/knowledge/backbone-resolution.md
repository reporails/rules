# Backbone Path Resolution

How to resolve paths from `.reporails/backbone.yml` instead of hardcoding them.

## Step 0: Load Backbone

Read `.reporails/backbone.yml` before resolving any paths. All paths are relative to repo root.

## Resolution Table

| Need | Backbone Key | Example Value |
|------|-------------|---------------|
| Rule base dir (core) | `rules.core` | `core/` |
| Rule base dir (agent) | `rules.agent_rules.{agent}` | `agents/claude/rules/` |
| Rule category dir | `rules.categories.{category}` | `core/structure/` |
| Rule dir pattern | `rules.patterns.rule_dir` | `{category}/{id}-{slug}/` |
| Rule definition | `rules.patterns.definition` | `{id}-{slug}.md` |
| Rule OpenGrep | `rules.patterns.opengrep` | `{id}-{slug}.yml` |
| Test pass | `rules.patterns.test_pass` | `tests/pass.{ext}` |
| Test fail | `rules.patterns.test_fail` | `tests/fail.{ext}` |
| Schema files | `schemas.{name}` | `schemas/rule.schema.yml` |
| Sources file | `artifacts.sources` | `docs/sources.yml` |
| Levels file | `artifacts.levels` | `levels.yml` |
| Capability levels | `artifacts.capability_levels` | `docs/capability-levels.md` |
| Changelog | `artifacts.changelog` | `UNRELEASED.md` |
| Agent config | `agents.{agent}.config` | `agents/claude/config.yml` |
| Agent skills | `agents.{agent}.skills` | `.claude/skills/` |
| Shared knowledge | `shared.knowledge` | `.shared/knowledge/` |
| Shared workflows | `shared.workflows` | `.shared/workflows/` |

## Test File Extension

The `{ext}` variable in test patterns is determined by the rule's target file type:

| Rule's `languages` / target | `{ext}` |
|-----------------------------|---------|
| markdown / `{{instruction_files}}` | `md` (default) |
| yaml / `.reporails/backbone.yml` | `yml` |
| json / settings files | `json` |

The test file must be parseable by the OpenGrep language mode the rule uses.

## ID-to-Path Algorithm

To resolve a rule ID (e.g., `S1`) to its filesystem path:

1. Look up slug in `rules.index` (e.g., `S1: size-limits`)
2. Determine category from ID prefix: `S`=structure, `C`=content, `E`=efficiency, `G`=governance, `M`=maintenance
3. For agent-prefixed IDs (e.g., `CLAUDE_S1`), use `rules.agent_rules.{agent}` as base
4. Combine: `{base}/{id}-{slug}/{id}-{slug}.md` (and `.yml`)

**Example:** `S1` resolves to `core/structure/S1-size-limits/S1-size-limits.md`

## When to Update backbone.yml

Update the backbone index when:
- **New rule created** — add entry to `rules.index`
- **New schema added** — add entry to `schemas`
- **New agent configured** — add entry to `agents`
- **New artifact added** — add entry to `artifacts`
- **Rule renamed/deleted** — update or remove from `rules.index`
