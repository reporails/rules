# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.0] - 2026-02-10

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

### Fixed
- [CORE:S:0004]: Replaced Stripe-format fake API key in test fixture with generic value to avoid GitHub Push Protection rejection
- [CORE:S:0003]: Use `.git_marker` as trackable alternative to `.git` in test fixtures — git cannot track paths named `.git`, causing CI failures
- [SCHEMAS]: Agent schema — restored `prefix`, `name` as optional fields; `overrides` as optional object; `main_instruction_file`/`instruction_files` accept string or list
- [AGENTS]: Claude and Codex configs — added required `version: "0.1.0"` field
- [AGENTS]: Codex config — removed stale v0.2 overrides (E4-, E2-, E5- identifiers)
- [CORE:S:0010]: Changed `type: deterministic` → `type: mechanical` (all checks are mechanical)
- [CORE:S:0009]: Updated prose to match check behavior (file existence, not git tracking)
- [OPENGREP]: Fixed 6 negated-rule messages from absence-language to presence-language (CORE:C:0002, C:0003, C:0004, C:0005, C:0015, CORE:S:0011)
- [BACKBONE]: Added missing `sources` schema to backbone registry
- [META]: CLAUDE.md — replaced hardcoded structure tree with backbone reference
- [META]: CLAUDE.md — added constraint: resolve paths from backbone before exploratory commands

### Removed
- [CORE:C]: Removed 7 rules reclassified as recommended (0008, 0013, 0014, 0018, 0020, 0021, 0024)
- [CLAUDE:S]: Removed 2 rules reclassified as recommended (0006, 0007)

### Migration
- [CORE]: Migrated 15 rules from short-ID format (`S1-size-limits/`) to coordinate-based (`size-limits/rule.md`)
- [CORE]: Removed old short-ID rule directories (superseded by coordinate-based layout)
- [CORE]: Removed root `levels.yml` (superseded by `registry/levels.yml`)
- [CORE]: M1 (version-control) reclassified from `deterministic` to `mechanical`
- [CORE]: C2 (single-source-of-truth) now `supersedes: CORE:C:0001`
- [CORE]: Level assignments — L1: M1, C3 | L2: S1, S3, S4, C1, C5, E1 | L3: S2, C2, C4, E2, M2 | L5: M3, M4
- [CORE]: Fixed M4 frontmatter bug (had `id: M2`, now `id: CORE:M:0004`)
- [CORE]: All `backed_by` converted to source ID format (references `docs/sources.yml`)
- [CORE]: All `checks[].id` now follow `{rule_id}:check:{slot}` coordinate pattern

## [0.2.2] - 2026-02-04

### Changed
- **Package Schema**: 0.2.2
- Collapsed rules listing in CLAUDE.md.

### Fixed
- Rule ID mapping inconsistency in CLAUDE_S2

## [0.2.1] - 2026-02-01

Focus split — 18 core rules in dedicated repo, opinionated rules moved to reporails/recommended.

### Added
- **Package Schema**: v0.0.1 — formal contract for rule packages

### Changed
- **Structure**: Split core rules into focused repository
- **Rules**: Renumbered 18 core rules to fill gaps after removing 26 opinionated rules
- **Levels**: Redistributed M3/M4 from L6 to L5; L6 is now detection-only
- **Schemas**: Rule schema v0.0.7 — added package layer, reserved_package_prefixes, package ID patterns
- **Schemas**: Agent schema v0.0.2 — fixed stale copilot and Claude overrides examples
- **Skills**: /generate-rule now generates skeletons; /validate-rules reduced to schema + contract checks; removed unused skills
- **Docs**: README and CONTRIBUTING rewritten — validation framing, quickstart aligned with CLI, streamlined contributor path

### Removed
- **Rules**: 26 opinionated rules (now in reporails/recommended)
- **Skills**: /update-rule, /generate-all-rules, /audit-evidence-chain, /extract-claims
- **Knowledge**: opengrep-patterns.md, evidence-chain.md
- **Schema**: sources.schema.yml
- **Workflows**: evidence-audit.md, claim-extraction.md

### Metrics
- Rules: 18 (15 core + 3 Claude-specific)
- Schemas: 6 (rule, agent, project, package, user, levels)

## [0.2.0] - 2026-01-31

Trust Architecture — tier-derived rule classification, schema breaking changes, directory restructuring with co-located tests, and multi-agent support.

### Added
- **Trust Architecture**: Two-tier model (core/experimental) derived from source weights replaces stored confidence. 55 new `backed_by` entries across 17 rules; 2 new community sources (`dometrain-claude-md-guide`, `osmani-ai-coding-workflow`)
- **Rule Structure**: Co-located test files (fail/pass) for all rules; `.semgrepignore` to enable test scanning; `pattern_confidence` field across all 43 rule frontmatters (4 very_high, 14 high, 16 medium, 9 low)
- **Levels**: `levels.yml` canonical level→rule mappings; `levels.schema.yml`; `/manage-levels` skill for sync/diff/list
- **M6 Rule**: Backbone index completeness — ensures filesystem rule directories are registered in `backbone.yml`
- **Codex Agent**: `agents/codex/` with config.yml for OpenAI Codex AGENTS.md files; `codex-agent-loop` source
- **Backbone**: `.claude/rules/` path-scoped reminders; `.shared/knowledge/backbone-resolution.md` central resolution reference

### Changed
- **BREAKING — Rule Schema v5**: Added `pattern_confidence` to `checks[]` items; removed `confidence` field (v4); tiers now derived from `backed_by` source weights
- **BREAKING — Sources Schema v3**: Source types reduced to 3 (`official` 1.0, `research` 0.8, `community` 0.4); tier derivation replaces stored confidence; removed `reporails:` section and `methodology` type
- **BREAKING — Project Schema v3**: `tiers` object replaces `confidence`/`profile` fields
- **BREAKING — Rule IDs**: Sequential renumbering (S6→S4, S7→S5, G2-G8→G1-G7, M6→M5; Claude: CLAUDE_S4→S2, CLAUDE_S5→S3, CLAUDE_M5→M1, CLAUDE_M7→M2). Agent rules use own namespace
- **BREAKING — Directory Structure**: All rules restructured into `{rule-id}/` directories with co-located `{rule-id}.yml` and `tests/`
- **Schema Versions**: Converted from integers to semver strings (`"0.0.X"`) across all 6 schema files
- **Release Tags**: Dropped `v` prefix — tags are now bare semver (e.g., `0.2.0`); workflow trigger updated to `[0-9]*`
- **M1 moved to L1**: Version control is now a Basic requirement; sharpens L2 as content/structure quality
- **Schema field rename**: `schema_version` → `version` in all schema files
- **Skills**: Backbone path resolution replaces hardcoded path tables in 8 skills/workflows
- **Docs**: Capability levels updated for tier model, M6 added to L6

### Fixed
- **Pattern Anchoring**: `pattern-not-regex` rules (C4, C12, E2, E3, E4, E5) now use `(?s)\A#[\s\S]+` instead of `^#` to match file-level content
- **Rule Fixes**: CLAUDE_S3 language target; C3 backreference removal; CLAUDE_S2 detection strategy; CLAUDE_M2 language target; G2 missing source URL; CLAUDE_G1 semantic inversion; G4/S4 YAML language alignment; backbone test file extension templates
- **Tier Comments**: E2, E6, S4 — explicit experimental tier comments on `backed_by: []`

### Removed
- **Cursor scope**: Removed from `docs/sources.yml`

### Metrics
- Rules: 44 (37 core + 6 Claude-specific + 1 Codex)
- Schemas: 6 (rule, agent, project, sources, user, levels) — all semver versioned
- Sources: 23 weighted sources with extracted claims
- Agents: 2 (Claude, Codex)

## [0.1.1] - 2026-01-28

Release automatizations with task hydration templates and streamlined workflows.

### Added
- **Structure**: `.shared/` directory for agent-agnostic workflows and knowledge
- **Structure**: `.claude/tasks/` directory with 7 task templates for release automation
- **Schema**: Trust architecture with weighted sources, confidence levels, and admission criteria
- **Schema**: `confirmed` confidence level requiring both official docs and research validation
- **Skills**: `/extract-claims` skill for source evidence extraction
- **Reporting**: Trust Score with Evidence Coverage breakdown (Official/Research/Methodology)
- **Rules**: Complete rule set - S1-S5, C1-C12, E1-E8, G1-G7, M1-M5
- **Docs**: Capability levels L1-L6 with assessment matrix and progression guide

### Changed
- **Skills**: Refactored to thin entry points (~35-50 lines) linking to shared workflows
- **Skills**: Deleted 11 redundant files (~1,100 lines removed)
- **Structure**: Moved from `.claude/rules/` to `.shared/knowledge/` for agent-agnostic content
- **Rules**: All 43 rules now have confidence field and backed_by source references
- **Rules**: Simplified type system to deterministic/semantic (32 deterministic, 10 semantic)
- **Sources**: Refactored to evidence chain format with 21 weighted sources

### Fixed
- **QA**: 42/43 rules pass validation (M1 deferred - architectural issue)

### Metrics
- Rules: 43 total (42 passing)
- Sources: 21 weighted sources with extracted claims

## [0.0.1] - [2026-01-22](https://github.com/reporails/framework/releases/tag/0.0.1)

