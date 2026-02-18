# Unreleased

## Added

- **Pre-commit hook** (`.githooks/pre-commit`): Enforces `UNRELEASED.md` is staged when committing changes to `core/`, `agents/`, `schemas/`, `registry/`, or `docs/`

## Changed

- **Terminology migration**: Replaced all "OpenGrep" references with "regex" / "pattern matching" across docs, workflows, knowledge, skills, tasks, and schemas. Runtime migrated to `reporails-cli` built-in regex engine; rule.yml format unchanged.
- **Renamed** `docs/opengrep-guide.md` → `docs/pattern-guide.md`
- **Renamed** backbone key `rules.patterns.opengrep` → `rules.patterns.patterns_yml`
- **Schema version** bumped to `0.1.1` (removed "OpenGrep" from pattern field description)
- **Check ID format canonicalized**: Schema pattern, examples, knowledge files, skill docs, and pattern guide all updated to match actual rule format (`NAMESPACE.CATEGORY.SLOT.descriptive-name` with dots, not colons or numbered slots)
- **CONTRIBUTING.md**: Added developer setup with git hooks, fleshed out submission flow with changelog requirement, fixed semantic rule example (`CORE:G:0001`, not `CORE:C:0001`)
- **Stale references fixed**: Corrected phantom coordinates in `copilot-instructions.md` (CORE:C:0006, CORE:C:0017 → real coordinates), updated pattern guide semantic example to use actual rule CORE:G:0001, fixed `/update-rule` skill reference in `qa-smoke-test.md`
- **Phantom coordinates purged**: Replaced all pre-0.4.0 coordinates with current equivalents or removed dead references — `.reporails/config.yml` (removed 4 phantom disabled rules), `agents/claude/config.yml` (CORE:S:0010 → CORE:G:0001), `docs/methodology-thresholds.md` (marked planned rules), skill docs (`manage-agent-config`, `generate-rule`, `implement-rule`)
