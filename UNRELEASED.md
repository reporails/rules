# Unreleased

## Changed

- **BREAKING**: Rule schema v5 — Added `pattern_confidence` field to `checks[]` items. Optional enum (`very_high`, `high`, `medium`, `low`, `very_low`), defaults to `medium`. Indicates OpenGrep pattern precision for LLM pattern generation and CLI telemetry. Non-breaking — existing rules remain valid.
- **pattern_confidence propagated** across all 43 rule frontmatters, 6 documentation/knowledge/workflow files, and 3 skill duplicates. Assessments: 4 very_high, 14 high, 16 medium, 9 low. Fixed stale "Confidence mismatch" reference in validation.md.

## Added

- **levels.yml**: Canonical machine-readable level→rule mappings at repo root, derived from `docs/capability-levels.md` Capability Assessment Matrix. CLIs should prefer this over bundled copies.

## Fixed

- **CLAUDE_S3**: Changed `languages: [yaml]` to `languages: [generic]` with pattern-regex/pattern-not-regex (was targeting .md files with YAML parser). Updated tests to include YAML frontmatter.
- **C3**: Replaced regex backreference `\1` with duplicated alternation (Rust regex engine doesn't support backreferences).
- **CLAUDE_S2**: Replaced `^$` on `.claude/rules/*.md` (can't detect missing dirs) with pattern checking main instruction file for absence of `.claude/rules` references.
- **CLAUDE_M2**: Changed second check `languages: [yaml]` to `languages: [generic]` (targets .md files).
- **G2**: Added missing `anthropic-teams-claude-code` URL to `sources:` array to match `backed_by` reference.
- **G5**: Converted test files from .md to .yml to match YAML pattern target (`.reporails/backbone.yml`).
- **M5**: Converted test files from .md to .yml to match YAML pattern target (`.reporails/backbone.yml`).
- **CLAUDE_G1**: Fixed semantic inversion — pattern now validates managed settings content (checks for org policy keys like `allowedTools`/`permissions`) instead of matching any content. Added limitation note about file-existence detection. Converted tests from .md to .json.
- **E2, E6, S4**: Added explicit experimental tier comments to `backed_by: []` fields.

## Removed

- **Cursor scope**: Removed `cursor:` scope from `docs/sources.yml` (source `cursor-rules` with 2 empty-rules claims)

## Added

- **New community source**: `dometrain-claude-md-guide` — lazy loading, domain terminology, command specificity, duplicate waste, living document claims
- **New community source**: `osmani-ai-coding-workflow` — planning-first, iterative chunks, context packaging, CI force multiplier, commit savepoints claims
- **55 backed_by entries** across 17 rules resolving E4004 violations:
  - S1: +8 entries (codex size limit, instruction capacity, less-is-more, curse-of-instructions, reduction-achieved, kb-limit, optimization-improvement, token-waste-measured)
  - S2: +7 entries (discovery-order, cascading-later-wins, nearest-precedence, modularity, reduction-achieved, service-specific-files, file-placement)
  - S3: +1 entry (code-snippet-beats-prose) — goes from unbacked to community-backed
  - C1: +5 entries (no-required-fields, no-required-format, usage-patterns, practical-examples, optimization-improvement)
  - C3: +1 entry (service-specific-files)
  - C7: +2 entries (less-is-more, curse-of-instructions)
  - C8: +1 entry (context-improves)
  - C9: +2 entries (readme-for-agents, usage-patterns)
  - E1: +1 entry (app-level-code)
  - E8: +3 entries (context-target, frequent-compaction, auto-compaction)
  - M1: +1 entry (file-placement)
  - M2: +2 entries (test-driven-guidance, iterative-tuning)
  - CLAUDE_S2: +2 entries (rules-dir-config, rules-mechanics)
  - CLAUDE_S3: +3 entries (rules-directory, rules-mechanics, loading-behavior)
  - C2: +2 entries (command-specificity, context-packaging)
  - C6: +1 entry (duplicate-instruction-waste)
  - G7: +1 entry (ci-force-multiplier)
- **S3 community backing**: Added to `spec-writing-for-agents:code-snippet-beats-prose` rules array

## Changed

- **S1**: Now references 150-200 instruction limit alongside line counts in rule body

## Added

- **Codex agent support**: New `agents/codex/` with config.yml for OpenAI Codex AGENTS.md files
- **New source**: `codex-agent-loop` from OpenAI official documentation with Codex-specific claims
- **New claims**: Updated `agents-md-spec` with comprehensive claims from Linux Foundation spec
  - `readme-for-agents`, `no-required-fields`, `cross-platform`
- **New claims**: Updated `codex-agents-md` with implementation-specific claims
  - `size-limit-32kb`, `one-file-per-directory`, `discovery-order`

## Changed

- **BREAKING**: Sources schema v3 - Simplified source types and tier derivation
  - Removed `methodology` source type
  - Source types reduced to 3: `official` (1.0), `research` (0.8), `community` (0.4)
  - Rule tiers derived from source weights: `core` (max >= 0.8) vs `experimental` (max < 0.8)
  - Removed `reporails:` section from sources.yml (capability-levels is an organizing principle, not evidence)
  - Rules without external backing are now experimental tier:
    - Generic: S3, S4, E2, E6, G4-G6, M5
    - Agent-specific: CLAUDE_S1, CLAUDE_M2
  - Rules with mixed backing: removed capability-levels entries, kept external:
    - C7 (kept: claude-code-best-practices, instruction-limits-principles)
    - E7 (kept: claude-code-memory)

- **BREAKING**: Rule schema v4 - Removed `confidence` field
  - Tier (core/experimental) is now derived from `backed_by` source weights, not stored
  - Removed `confidence` from all 43 rule frontmatters
  - Removed confidence validation rules from schema
  - Updated all skill/knowledge/workflow files to use tier model
  - Removed `methodology` references from evidence-chain, workflows, and schemas

- Updated `docs/capability-levels.md`:
  - Replaced 4-level confidence (confirmed/high/medium/low) with 2-tier model (core/experimental)
  - Added tier derivation documentation
  - Updated promotion path explanation
  - Removed "Reporails Methodology" references (now "Community patterns")

- **BREAKING**: Renumbered rules to sequential IDs (separate namespaces):
  - Core: S6→S4, S7→S5, G2-G8→G1-G7, M6→M5
  - Claude: CLAUDE_S4→S2, CLAUDE_S5→S3, CLAUDE_M5→M1, CLAUDE_M7→M2
  - Updated schema to clarify: agent rules use OWN namespace (CLAUDE_S1 ≠ override of S1)
  - Added pattern override mechanism via `agents/{agent}/overrides/` folder

- **BREAKING**: Restructured ALL rules into directories with co-located tests:
  ```
  core/{category}/{rule-id}/
  ├── {rule-id}.md
  ├── {rule-id}.yml
  └── tests/
      ├── fail.md   # Should trigger (true positive)
      └── pass.md   # Should not trigger (true negative)
  ```

  Restructured rules (43 total):
  - Structure: S1-S5 (5)
  - Content: C1-C12 (12)
  - Efficiency: E1-E8 (8)
  - Governance: G1-G7 (7)
  - Maintenance: M1-M5 (5)
  - Claude agent: CLAUDE_S1-S3, CLAUDE_G1, CLAUDE_M1-M2 (6)

- Updated all documentation and workflows for new directory structure:
  - `.claude/skills/update-rule/SKILL.md`
  - `.claude/tasks/new-rule.md`
  - `.claude/tasks/smoke-test.md`
  - `.shared/knowledge/qa-checklist.md`
  - `.shared/workflows/qa-smoke-test.md`
  - `.shared/workflows/rule-creation.md`
  - `.shared/workflows/rule-update.md`
  - `docs/rule-template.md`
  - `CLAUDE.md`

## Fixed

- Fix pattern-not-regex rules firing on every heading line instead of checking file-level content. Changed anchor from `^#` to `(?s)\A#[\s\S]+` to match entire file. Affected rules: C4, C12, E2, E3, E4, E5

## Added

- `.semgrepignore` to allow scanning test files (semgrep ignores `tests/` by default)
- Test files (fail.md/pass.md) for all 43 rules to validate OpenGrep patterns
- [META]: `.reporails/trust-metrics.yml` generated by evidence audit
