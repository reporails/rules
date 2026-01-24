# Unreleased

### Added
- [META]: Repository structure with CLAUDE.md, backbone.yml
- [META]: .claude/rules/ for path-scoped rule editing
- [META]: Add-changelog-entry command
- [DOCS]: README with framework overview and 26 sources
- [DOCS]: Maturity model with L1-L6 definitions and assessment
- [DOCS]: Deep Validation Checklist for pattern-based checks
- [RULES]: Structure rules S1-S7 (size, disclosure, hierarchy)
- [RULES]: Content rules C1-C12 (sections, patterns, constraints)
- [RULES]: Maintenance rules M1-M7 (versioning, review, staleness)
- [RULES]: Governance rules G1-G8 (org policies, contracts, CI)
- [RULES]: Efficiency rules E1-E8 (tools, reading, grep, context)
- [TEMPLATES]: Rule template with frontmatter reference
- [DOCS]: OpenGrep research for rule detection capabilities

### Changed
- [META]: Updated .claude/rules/rules.md with behavioral type and severity weights
- [TEMPLATES]: Rule template aligned with 0-10 weighted scoring spec
- [RULES]: All 42 rules aligned with capability-levels.yml spec
- [RULES]: Removed legacy scoring/points fields from frontmatter
- [RULES]: Updated type values per backbone.yml rule_index
- [RULES]: Added behavioral type to E3, E4, E5, E8
- [RULES]: Upgraded 9 rules from heuristic to deterministic (OpenGrep detection)
- [META]: Updated backbone.yml rule_index (20 deterministic, 12 heuristic, 6 semantic, 4 behavioral)
- [RULES]: S1 adds 100-line threshold exemption for C1 section requirements
- [RULES]: All 12 heuristic rules now have question + criteria for LLM confirmation
- [TEMPLATES]: Rule template documents heuristic two-stage validation flow
- [DOCS]: capability-levels.md adds Rule Detection Types and OpenGrep sections