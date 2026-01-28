# Unreleased

## Changed

- **BREAKING**: Restructured ALL rules into directories with co-located tests:
  ```
  core/{category}/{rule-id}/
  ├── {rule-id}.md
  ├── {rule-id}.yml
  └── tests/
      ├── fail.md   # Should trigger (true positive)
      └── pass.md   # Should not trigger (true negative)
  ```

  Restructured rules:
  - Structure: S1, S2, S3, S6, S7
  - Content: C1-C12
  - Efficiency: E1-E8
  - Governance: G2-G8
  - Maintenance: M1-M4, M6
  - Claude agent: CLAUDE_S1, CLAUDE_S4, CLAUDE_S5, CLAUDE_G1, CLAUDE_M5, CLAUDE_M7

## Fixed

- Fix pattern-not-regex rules firing on every heading line instead of checking file-level content. Changed anchor from `^#` to `(?s)\A#[\s\S]+` to match entire file. Affected rules: C4, C12, E2, E3, E4, E5

## Added

- `.semgrepignore` to allow scanning test files (semgrep ignores `tests/` by default)
- Test files (fail.md/pass.md) for all 39 rules to validate OpenGrep patterns
