# Unreleased

## Added

- [META]: Pre-commit hook enforces UNRELEASED.md is staged for core/, agents/, schemas/, registry/, docs/ changes

## Changed

- [SCHEMAS]: Added `context_quality` category (letter `X`) to coordinate patterns and category enums
- [META]: Replaced all "OpenGrep" references with "regex" / "pattern matching"; runtime migrated to reporails-cli regex engine
- [DOCS]: Renamed `docs/opengrep-guide.md` → `docs/pattern-guide.md`
- [META]: Renamed backbone key `rules.patterns.opengrep` → `rules.patterns.patterns_yml`
- [SCHEMAS]: Schema version bumped to `0.1.1` (removed "OpenGrep" from pattern field description)
- [SCHEMAS]: Check ID format canonicalized to `NAMESPACE.CATEGORY.SLOT.descriptive-name`
- [DOCS]: CONTRIBUTING.md — added developer setup with git hooks, fleshed out submission flow
- [DOCS]: Fixed phantom coordinates in copilot-instructions.md, pattern guide, qa-smoke-test.md
- [META]: Purged pre-0.4.0 phantom coordinates from config files and skill docs
