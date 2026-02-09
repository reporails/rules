# Reporails Framework
<!-- Last updated: 2026-02-06 -->

Framework for evaluating and maintaining AI agent instruction files.

## Tech Stack

- Markdown documentation
- YAML schemas and configuration
- OpenGrep patterns for detection
- No application code — framework only

## Bootstrap

1. Read `.reporails/backbone.yml` for project structure
2. Read `registry/capabilities.yml` and `registry/levels.yml` for architecture

## Structure

```
core/{structure,content,efficiency,maintenance,governance}/  # Core rules
  {slug}/                                                    # Each rule in own directory
    rule.md                                                  # Rule definition
    rule.yml                                                 # OpenGrep patterns
    tests/                                                   # Test fixtures
      pass/                                                  # Simulated project that passes
      fail/                                                  # Simulated project that fails
agents/{claude,codex}/{config.yml,rules/}                    # Agent-specific
schemas/                                                     # Schema definitions (8)
registry/                                                    # Capabilities, levels, coordinates, tombstones
runtime/                                                     # Contributor test harness (Docker)
docs/                                                        # Documentation
.claude/{skills/,rules/}                                     # Claude config
.shared/{workflows/,knowledge/}                              # Agent-agnostic shared content
```

## Commands

- Check rule lengths: `wc -l core/**/*/rule.md agents/**/rules/*/rule.md`
- List all rules: `find core agents -name "rule.md" | grep -v tests`
- List rule directories: `find core agents -name "rule.yml" -exec dirname {} \;`

### Test Harness

```bash
# Build test image
docker compose -f runtime/docker-compose.yml build

# Run all rules
docker compose -f runtime/docker-compose.yml run test

# Run one rule
docker compose -f runtime/docker-compose.yml run test --rule CORE:S:0001

# Run one category
docker compose -f runtime/docker-compose.yml run test core/structure/

# Use codex agent vars
docker compose -f runtime/docker-compose.yml run test --agent codex

# Include recommended package
docker compose -f runtime/docker-compose.yml run test --package /recommended

# Verbose (show OpenGrep output)
docker compose -f runtime/docker-compose.yml run test --verbose
```

## Navigation

Key paths:
- @registry/ — Capabilities, levels, coordinate map, tombstones
- @core/ — Core rules (12 structure, 18 content)
- @agents/ — Agent-specific config and rules (10 Claude, 7 Codex)
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

## Shared Resources

Agent-agnostic workflows and knowledge live in `.shared/`:

- `.shared/workflows/` — Process definitions (mermaid flowcharts)
- `.shared/knowledge/` — Domain reference (facts, patterns, validation)

Skills in `.claude/skills/` are entry points that reference shared content.

## Skills

Skills in `.claude/skills/` — each has a SKILL.md linking to shared workflows.

| Skill | Purpose |
|-------|---------|
| `/generate-rule` | Create rule skeleton with coordinate, directory, and placeholder files |
| `/implement-rule` | Implement checks, patterns, and fixtures for an existing rule skeleton |
| `/validate-rules` | Validate rules against schema and contracts |
| `/manage-levels` | Sync level definitions with capability model |
| `/manage-agent-config` | Create, update, and validate agent configurations |
| `/add-changelog-entry` | Add changelog entry to UNRELEASED.md |
