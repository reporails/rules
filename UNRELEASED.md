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
- [DOCS]: Moved capability-levels.md to docs/
- [RULES]: L6 rules (S6, E2, M6, G5, G6, G7) now source from docs/capability-levels.md
- [SOURCES]: Added reporails section with capability-levels as methodology source
- [RULES]: Regenerated all 42 rules using new schema (rule.schema.yml)
- [RULES]: All rules now have matching .md and .yml files with OpenGrep patterns
- [RULES]: Core rules (37) in core/{category}/, Claude-specific (5) in agents/claude/rules/
- [RULES]: Simplified type system to deterministic/semantic (removed heuristic/behavioral)
- [META]: Updated .claude/rules/rules.md with behavioral type and severity weights
- [TEMPLATES]: Rule template aligned with 0-10 weighted scoring spec
- [RULES]: All 42 rules aligned with capability-levels.yml spec
- [RULES]: Removed legacy scoring/points fields from frontmatter
- [RULES]: Updated type values per backbone.yml rule_index
- [RULES]: Added behavioral type to E3, E4, E5, E8
- [RULES]: Upgraded 9 rules from heuristic to deterministic (OpenGrep detection)
- [META]: Updated backbone.yml rule_index (23 deterministic, 17 heuristic, 1 semantic, 1 behavioral)
- [RULES]: S1 adds 100-line threshold exemption for C1 section requirements
- [RULES]: Converted 5 semantic rules to heuristic with pattern gates (E2, C2, S3, M1, C8)
- [RULES]: Reframed E3, E4, E5 from behavioral to deterministic (check instruction exists, not agent behavior)
- [RULES]: All 17 heuristic rules now have question + criteria for LLM confirmation
- [TEMPLATES]: Rule template documents heuristic two-stage validation flow
- [DOCS]: capability-levels.md updated with detection types (17 heuristic, 1 semantic)