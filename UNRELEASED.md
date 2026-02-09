# Unreleased

### Added
- [SKILLS]: `/implement-rule` skill — implement checks, patterns, and fixtures for rule skeletons
- [RUNTIME]: Contributor test harness — Docker-based runner for validating rules against fixtures
- [RUNTIME]: 15 mechanical check functions (file_exists, directory_exists, line_count, byte_size, file_count, git_tracked, frontmatter_field, aggregate_byte_size, import_depth, directory_file_types, frontmatter_valid_glob, content_absent, and more)
- [RUNTIME]: OpenGrep integration for deterministic pattern testing
- [RUNTIME]: `--package` flag for testing additional rule packages (e.g., `--package /recommended`)
- [RUNTIME]: Docker compose mounts recommended/ at `/recommended:ro` for package testing
- [CORE]: All 47 core rules fully implemented — checks, patterns, and fixtures wired (47/47 passing)
- [REGISTRY]: Capabilities, levels, coordinate map, tombstones
- [REGISTRY]: 9 tombstone entries for coordinates moved to recommended package
- [SCHEMAS]: Capability schema v0.1.0

### Fixed
- [CORE:S:0004]: Replaced Stripe-format fake API key in test fixture with generic value to avoid GitHub Push Protection rejection
- [CORE:S:0003]: Use `.git_marker` as trackable alternative to `.git` in test fixtures — git cannot track paths named `.git`, causing CI failures
- [SCHEMAS]: Agent schema — restored `prefix`, `name` as optional fields; `overrides` as optional object; `main_instruction_file`/`instruction_files` accept string or list
- [AGENTS]: Claude and Codex configs — added required `version: "0.1.0"` field
- [AGENTS]: Codex config — removed stale v0.2 overrides (E4-, E2-, E5- identifiers)
- [CORE:S:0010]: Changed `type: deterministic` → `type: mechanical` (all checks are mechanical)
- [CORE:S:0009]: Updated prose to match check behavior (file existence, not git tracking)
- [OPENGREP]: Fixed 6 negated-rule messages from absence-language to presence-language (CORE:C:0002, C:0003, C:0004, C:0005, C:0015, CORE:S:0011)

### Removed
- [CORE:C]: Removed 7 rules reclassified as recommended (0008, 0013, 0014, 0018, 0020, 0021, 0024)
- [CLAUDE:S]: Removed 2 rules reclassified as recommended (0006, 0007)

### Migration
- [CORE]: Migrated 15 rules from short-ID format (`S1-size-limits/`) to coordinate-based (`size-limits/rule.md`)
- [CORE]: Archived old rule directories to `archive/v0.2.1/core/`
- [CORE]: Archived root `levels.yml` to `archive/v0.2.1/levels.yml` (superseded by `registry/levels.yml`)
- [CORE]: M1 (version-control) reclassified from `deterministic` to `mechanical`
- [CORE]: C2 (single-source-of-truth) now `supersedes: CORE:C:0001`
- [CORE]: Level assignments — L1: M1, C3 | L2: S1, S3, S4, C1, C5, E1 | L3: S2, C2, C4, E2, M2 | L5: M3, M4
- [CORE]: Fixed M4 frontmatter bug (had `id: M2`, now `id: CORE:M:0004`)
- [CORE]: All `backed_by` converted to source ID format (references `docs/sources.yml`)
- [CORE]: All `checks[].id` now follow `{rule_id}:check:{slot}` coordinate pattern

### Fixed
- [BACKBONE]: Added missing `sources` schema to backbone registry
- [META]: CLAUDE.md — replaced hardcoded structure tree with backbone reference
- [META]: CLAUDE.md — added constraint: resolve paths from backbone before exploratory commands

### Changed
- [SKILLS]: `/implement-rule` rewritten — violation class identification, structural pattern design, anti-negate strategy, realistic fixture criteria
- [WORKFLOWS]: `rule-implementation.md` rewritten — violation class step, fixture quality gate, reanalysis loop
- [FIXTURES]: Migrated test fixtures from stub files (tests/pass.md, tests/fail.md) to directories (tests/pass/, tests/fail/)
- [BACKBONE]: Updated test_pass/test_fail patterns for directory-based fixtures
- [SCHEMAS]: Rule schema rewrite — coordinate IDs, gate checks, governance category
- [SCHEMAS]: Agent schema — prefix/name/overrides restored as optional after config audit
- [SCHEMAS]: Levels schema rewrite — cross-reference validation only
- [SCHEMAS]: Package schema — AILS→RRAILS prefix, coordinate format
- [SCHEMAS]: Project and user schemas — semver schema_version
- [BACKBONE]: v3 — slug-based patterns, registry section, removed index/artifacts
- [META]: CLAUDE.md and rules updated for coordinate format
- [SKILLS]: All 5 skills updated for coordinate and registry paths
- [SKILLS]: `/generate-rule` updated — fixture step now creates `tests/pass/` and `tests/fail/` directories with `.gitkeep`
