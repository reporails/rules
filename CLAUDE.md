# Reporails Framework
<!-- Last updated: 2026-01-24 -->

Framework for evaluating and maintaining AI agent instruction files.

## Tech Stack

- Markdown documentation
- YAML schemas and configuration
- OpenGrep patterns for detection
- No application code — framework only

## Structure

```
core/{structure,content,efficiency,governance,maintenance}/  # Generic rules
agents/claude/{config.yml,rules/}                            # Agent-specific
schemas/{rule,agent,sources}.schema.yml                      # Schemas
docs/                                                        # Documentation
.claude/{skills/,rules/}                                     # Claude config
```

## Commands

- Check rule lengths: `wc -l core/**/*.md agents/**/rules/*.md`
- List all rules: `find core agents -name "*.md" | grep -v README`

## Navigation

Key paths:
- @docs/capability-levels.md — Level definitions
- @core/ — Generic rules (S1-S7, C1-C12, E1-E8, G1-G8, M1-M7)
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

## Skills

Skills are in `.claude/skills/`. Each has a SKILL.md with workflow and supporting files.

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