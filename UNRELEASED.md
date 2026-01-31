# Unreleased

## Added
- [SCHEMA]: Package schema v0.0.1 — formal contract for rule packages

## Changed
- [STRUCTURE]: Split core rules into focused repository
- [RULES]: Renumbered 18 core rules to fill gaps after removing 26 opinionated rules
- [LEVELS]: Redistributed M3/M4 from L6 to L5; L6 is now detection-only
- [SCHEMA]: Rule schema v0.0.7 — added package layer to resolution stack, reserved_package_prefixes, package ID patterns
- [SCHEMA]: Agent schema v0.0.2 — fixed stale copilot example, fixed stale Claude overrides example
- [SKILLS]: /generate-rule now generates skeletons (contributors fill in patterns)
- [SKILLS]: /validate-rules reduced to schema + contract checks
- [SKILLS]: Removed skills not needed for contributor workflow

## Removed
- [RULES]: 26 opinionated rules (now in reporails/recommended)
- [SKILLS]: /update-rule, /generate-all-rules, /audit-evidence-chain, /extract-claims
- [KNOWLEDGE]: opengrep-patterns.md, evidence-chain.md
- [SCHEMA]: sources.schema.yml
- [WORKFLOWS]: evidence-audit.md, claim-extraction.md
