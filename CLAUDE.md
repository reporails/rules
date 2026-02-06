# Reporails Framework
<!-- Last updated: 2026-02-06 -->

Framework for evaluating and maintaining AI agent instruction files.

## Tech Stack

- Markdown documentation
- YAML schemas and configuration
- OpenGrep patterns for detection
- No application code — framework only

## Session Start

1. Read `.reporails/backbone.yml` for project structure
2. Read `registry/capabilities.yml` and `registry/levels.yml` for architecture

## Structure

```
core/{structure,content,efficiency,maintenance,governance}/  # Core rules (15)
  {slug}/                                                    # Each rule in own directory
    rule.md                                                  # Rule definition
    rule.yml                                                 # OpenGrep patterns
    tests/                                                   # Test cases
      fail.md                                                # Should trigger
      pass.md                                                # Should not trigger
agents/{claude,codex}/{config.yml,rules/}                    # Agent-specific
schemas/                                                     # Schema definitions (7)
registry/                                                    # Capabilities, levels, coordinates, tombstones
docs/                                                        # Documentation
.claude/{skills/,rules/}                                     # Claude config
.shared/{workflows/,knowledge/}                              # Agent-agnostic shared content
```

## Commands

- Check rule lengths: `wc -l core/**/*/rule.md agents/**/rules/*/rule.md`
- List all rules: `find core agents -name "rule.md" | grep -v tests`
- List rule directories: `find core agents -name "rule.yml" -exec dirname {} \;`

## Navigation

Key paths:
- @registry/ — Capabilities, levels, coordinate map, tombstones
- @core/ — Core rules (CORE:S:0001-0004, CORE:C:0001-0005, CORE:E:0001-0002, CORE:M:0001-0004)
- @agents/ — Agent-specific config and rules (CLAUDE:M:0001, CLAUDE:S:0001-0002)
- @schemas/ — Machine-readable contracts (7 schemas)
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
- ALWAYS create tests/fail.md and tests/pass.md for each rule
- ALWAYS update registry/coordinate-map.yml when adding or removing rules

## Shared Resources

Agent-agnostic workflows and knowledge live in `.shared/`:

- `.shared/workflows/` — Process definitions (mermaid flowcharts)
- `.shared/knowledge/` — Domain reference (facts, patterns, validation)

Skills in `.claude/skills/` are entry points that reference shared content.

## Skills

Skills in `.claude/skills/` — each has a SKILL.md linking to shared workflows.
