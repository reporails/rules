# Reporails Framework
<!-- Last updated: 2026-01-28 -->

Framework for evaluating and maintaining AI agent instruction files.

## Tech Stack

- Markdown documentation
- YAML schemas and configuration
- OpenGrep patterns for detection
- No application code — framework only

## Session Start

1. Read `.reporails/backbone.yml` for project structure
2. Read `docs/capability-levels.md` for architecture decisions

## Structure

```
levels.yml                                                   # Canonical level→rule mappings
core/{structure,content,efficiency,governance,maintenance}/  # Generic rules
  {rule-id}/                                                 # Each rule in own directory
    {rule-id}.md                                             # Rule definition
    {rule-id}.yml                                            # OpenGrep patterns
    tests/                                                   # Test cases
      fail.md                                                # Should trigger
      pass.md                                                # Should not trigger
agents/claude/{config.yml,rules/}                            # Agent-specific (same structure)
schemas/{rule,agent,sources}.schema.yml                      # Schemas
docs/                                                        # Documentation
.claude/{skills/,rules/}                                     # Claude config
.shared/{workflows/,knowledge/}                              # Agent-agnostic shared content
```

## Commands

- Check rule lengths: `wc -l core/**/*/*.md agents/**/rules/*/*.md`
- List all rules: `find core agents -type d -name "[A-Z]*" | grep -v tests`
- List rule files: `find core agents -path "*/tests" -prune -o -name "*.md" -print | grep -v README`

## Navigation

Key paths:
- @docs/capability-levels.md — Level definitions
- @core/ — Generic rules (S1-S5, C1-C12, E1-E8, G1-G7, M1-M5)
- @agents/claude/ — Claude-specific config and rules
- @schemas/ — Machine-readable contracts
- @docs/ — Contributor guides and source registry

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
- ALWAYS create both .md and .yml for each rule
- ALWAYS create tests/fail.md and tests/pass.md for each rule

## Shared Resources

Agent-agnostic workflows and knowledge live in `.shared/`:

- `.shared/workflows/` — Process definitions (mermaid flowcharts)
- `.shared/knowledge/` — Domain reference (facts, patterns, validation)

Skills in `.claude/skills/` are entry points that reference shared content.

## Skills

Skills are in `.claude/skills/`. Each has a SKILL.md that links to shared workflows.

### /generate-rule <id> <scope> <title>
Generate a new rule with proper schema and OpenGrep patterns.

### /validate-rules [id] [--source-check]
Validate rules against schema, contracts, and sources.

### /add-changelog-entry
Add entry to UNRELEASED.md after making changes.

### /generate-all-rules [--scope core|claude]
Batch generate or regenerate all rules from specification.

### /update-rule <id> <instruction>
Update an existing rule's OpenGrep patterns based on instruction.

### /extract-claims <url>
Extract claims from a source URL for sources.yml evidence chain.

### /manage-levels <sync|diff|list> [level]
Sync levels.yml from capability matrix, diff discrepancies, or list rules per level.