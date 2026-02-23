# Reporails Framework
<!-- Last updated: 2026-02-06 -->

Framework for evaluating and maintaining AI agent instruction files.

## Tech Stack

- Markdown documentation
- YAML schemas and configuration
- Regex patterns for detection
- No application code — framework only

## Initialization

Run `/bootstrap` to load project context, or manually read these files before searching or modifying anything:

1. Read `.reporails/backbone.yml` for project structure and path resolution
2. Read `registry/capabilities.yml` and `registry/levels.yml` for architecture
3. Read `.claude/rules/` for context-specific constraints on the current task

## Structure

Defined in `.reporails/backbone.yml` — the single source of truth for project topology, paths, schemas, and registry locations.

**BEFORE** running `find`, `grep`, `ls`, or glob to locate project files, you **MUST** read `.reporails/backbone.yml` first. All schema paths, registry paths, rule directories, agent configs, and doc locations are mapped there. You **MUST NOT** use exploratory commands to discover paths that the backbone already provides.

## Commands

- Check rule lengths: `wc -l core/**/*/rule.md agents/**/rules/*/rule.md`
- List all rules: `find core agents -name "rule.md" | grep -v tests`
- List rule directories: `find core agents -name "rule.yml" -exec dirname {} \;`

### Test Harness

```bash
# Build test image
docker compose -f runtime/docker-compose.yml build

# Run all rules
docker compose -f runtime/docker-compose.yml run --rm test

# Run one rule
docker compose -f runtime/docker-compose.yml run --rm test --rule CORE:S:0001

# Run one category
docker compose -f runtime/docker-compose.yml run --rm test core/structure/

# Use codex agent vars
docker compose -f runtime/docker-compose.yml run --rm test --agent codex

# Include recommended package
docker compose -f runtime/docker-compose.yml run --rm test --package /recommended

# Verbose
docker compose -f runtime/docker-compose.yml run --rm test --verbose
```

## Navigation

Key paths:
- @registry/ — Capabilities, levels, coordinate map, tombstones
- @core/ — Core rules (3 structure, 5 content, 1 governance, 2 maintenance)
- @agents/ — Agent-specific config and rules (3 Claude, 1 Codex, 2 Copilot)
- @schemas/ — Machine-readable contracts (8 schemas)
- @docs/ — Contributor guides and source registry

Additional rules available in [reporails/recommended](https://github.com/reporails/recommended).

## Efficiency

- Read files based on purpose: full for EDIT, partial for UNDERSTAND
- Reference from memory instead of re-reading unchanged files
- Use `files_with_matches` mode for searches, `head_limit` to cap results
- For rule work, start with `.claude/rules/` instructions

## Constraints

- NEVER duplicate schema definitions — reference `schemas/` instead
- NEVER hardcode agent paths in core rules — use `{{instruction_files}}`
- NEVER read CHANGELOG.md — use UNRELEASED.md instead
- ALWAYS update UNRELEASED.md when modifying rules
- ALWAYS create both rule.md and rule.yml for each rule
- ALWAYS create tests/pass/ and tests/fail/ fixture directories for each rule
- ALWAYS update registry/coordinate-map.yml when adding or removing rules
- NEVER execute destructive or irreversible operations without explicit user confirmation
- ALWAYS resolve paths from `.reporails/backbone.yml` before using exploratory commands

## Shared Resources

Agent-agnostic workflows and knowledge live in `.shared/`:

- `.shared/workflows/` — Process definitions (mermaid flowcharts)
- `.shared/knowledge/` — Domain reference (facts, patterns, validation)

Skills in `.claude/skills/` are entry points that reference shared content.

## Skills

Skills in `.claude/skills/` — each has a SKILL.md linking to shared workflows.

| Skill | Purpose |
|-------|---------|
| `/bootstrap` | Load project context — backbone, registry, and constraints — before any work |
| `/generate-rule` | Create rule skeleton with coordinate, directory, and placeholder files |
| `/implement-rule` | Implement checks, patterns, and fixtures for an existing rule skeleton |
| `/validate-rules` | Validate rules against schema and contracts |
| `/manage-levels` | Sync level definitions with capability model |
| `/manage-agent-config` | Create, update, and validate agent configurations |
| `/add-changelog-entry` | Add changelog entry to UNRELEASED.md |
