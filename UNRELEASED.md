# Unreleased

## Added

- [META]: Pre-commit hook enforces UNRELEASED.md is staged for core/, agents/, schemas/, registry/, docs/ changes

## Changed

- [SCHEMAS]: Added `context_quality` category (letter `X`) to coordinate patterns and category enums
- [SCHEMAS]: Normalized agent override severity enum syntax and added `critical` value
- [SCHEMAS]: Added pattern validation to agent config `excludes` items
- [SCHEMAS]: Added `internal` source type to sources schema
- [SCHEMAS]: Agent config examples updated to use arrays for `main_instruction_file`

- [RULES]: Expanded core rule catalog — 32 content, 36 structure, 7 context_quality, 5 efficiency, 9 governance, 1 maintenance rules with definitions, patterns, and pass/fail fixtures

## Removed

- [RULES]: Deprecated core rules: avoid-generic-placeholder-content, boundary-constraints, include-project-context, project-architecture-documentation, verification-build-commands, cross-agent-compatibility, valid-glob-patterns-in-frontmatter, valid-internal-references, monorepo-nested-instruction-files, root-instruction-file-presence, structured-markdown-format
- [RULES]: Deprecated agent rules: CLAUDE import-syntax-for-modular-content, path-scoped-rules, rules-directory-for-modular-instructions; CODEX combined-instruction-size-limit; COPILOT copilot-instructions-placement, copilot-path-specific-instructions

## Fixed

- [AGENTS]: Claude config exclude coordinate corrected from `CORE:G:0001` to `CORE:C:0026`
- [SCHEMAS]: Stale check ID validation rule text corrected to `{NAMESPACE}.{CATEGORY}.{SLOT}.{descriptive-name}`
- [META]: Replaced all "OpenGrep" references with "regex" / "pattern matching"; runtime migrated to reporails-cli regex engine
- [DOCS]: Renamed `docs/opengrep-guide.md` → `docs/pattern-guide.md`
- [META]: Renamed backbone key `rules.patterns.opengrep` → `rules.patterns.patterns_yml`
- [SCHEMAS]: Schema version bumped to `0.1.1` (removed "OpenGrep" from pattern field description)
- [SCHEMAS]: Check ID format canonicalized to `NAMESPACE.CATEGORY.SLOT.descriptive-name`
- [DOCS]: CONTRIBUTING.md — added developer setup with git hooks, fleshed out submission flow
- [DOCS]: Fixed phantom coordinates in copilot-instructions.md, pattern guide, qa-smoke-test.md
- [META]: Purged pre-0.4.0 phantom coordinates from config files and skill docs
