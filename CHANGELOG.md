# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v0.1.1] - 2026-01-28

Release automatizations with task hydration templates and streamlined workflows.

### Added
- **Structure**: `.shared/` directory for agent-agnostic workflows and knowledge
- **Structure**: `.claude/tasks/` directory with 7 task templates for release automation
- **Schema**: Trust architecture with weighted sources, confidence levels, and admission criteria
- **Schema**: `confirmed` confidence level requiring both official docs and research validation
- **Skills**: `/extract-claims` skill for source evidence extraction
- **Reporting**: Trust Score with Evidence Coverage breakdown (Official/Research/Methodology)
- **Rules**: Complete rule set - S1-S7, C1-C12, E1-E8, G1-G8, M1-M7
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

