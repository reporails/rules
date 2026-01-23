# Reporails Framework
<!-- Last updated: 2026-01-22 -->

Documentation repository for the AI context file capability model.

## Tech Stack

- Markdown documentation
- YAML configuration (backbone.yml)
- No code — documentation only

## Commands

- Check rule lengths: `wc -l rules/**/*.md`
- Validate links: `Grep pattern="\]\(.*\.md\)" path="." glob="*.md" output_mode="content" head_limit=20`

## Navigation

See `.reporails/backbone.yml` for file map.

Key paths:
- @capability-model.md — Level definitions and assessment
- @rules/structure/ — S1-S7 structure rules
- @rules/content/ — C1-C12 content rules
- @rules/maintenance/ — M1-M7 maintenance rules
- @rules/governance/ — G1-G8 governance rules
- @rules/efficiency/ — E1-E8 efficiency rules
- @README.md — Public overview and sources

## Efficiency

- Read files based on purpose: full for EDIT, partial for UNDERSTAND
- Reference from memory instead of re-reading unchanged files
- Use `files_with_matches` and `head_limit` for grep
- Trust context window awareness — no need for token-saving reminders

## Constraints

- NEVER duplicate level definitions — reference @capability-model.md instead
- NEVER add implementation details — describe patterns abstractly
- NEVER read CHANGELOG.md — use UNRELEASED.md instead
- ALWAYS update UNRELEASED.md when modifying rules
- ALWAYS run /add-changelog-entry after changes
