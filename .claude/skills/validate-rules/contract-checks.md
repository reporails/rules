# Contract Validation Checks

## .md ↔ .yml Pairing

Every rule .md file must have a matching .yml file with OpenGrep patterns.

## Checks

- [ ] .yml file exists for every .md rule
- [ ] Every `checks[].id` in .md has matching `rules[].id` in .yml
- [ ] Every `rules[].id` in .yml has matching `checks[].id` in .md
- [ ] OpenGrep severity matches rule severity mapping
- [ ] Has positive pattern (`pattern-regex` or `pattern`)
- [ ] `pattern-not-regex` is inside `patterns:` block, NOT at top level
- [ ] Core rules use only `{{instruction_files}}`
- [ ] Paths use template variables, not hardcoded paths

## Required .yml Schema

```yaml
rules:
  - id: RULE-check-name
    message: "Human-readable description"
    severity: ERROR | WARNING | INFO
    languages: [generic]
    patterns:                     # ← REQUIRED for multiple patterns
      - pattern-regex: "..."      # ← positive pattern FIRST
      - pattern-not-regex: "..."  # ← exclusions INSIDE patterns:
    paths:
      include:
        - "{{instruction_files}}"
```

**Invalid:** `pattern-not-regex` at rule top level (outside `patterns:`)

## OpenGrep Validation Command

```bash
~/.reporails/bin/opengrep scan --config path/to/rule.yml .
```

| Exit | Meaning | Action |
|------|---------|--------|
| 0 | Valid, no matches | OK |
| 1 | Valid, matches found | OK |
| 2 | Syntax/schema error | Fix structure |
| 7 | No positive pattern | Add `pattern-regex` |

## Validation Logic

For each `.md` rule file:
1. Check `.yml` file exists (same name, different extension)
2. Extract `checks[].id` from .md frontmatter
3. Extract `rules[].id` from .yml
4. Verify 1:1 mapping between check IDs and rule IDs

## Severity Mapping

| .md severity | .yml severity |
|--------------|---------------|
| critical | ERROR |
| high | WARNING |
| medium | WARNING |
| low | WARNING |

## Template Variables

| Variable | Core rules | Agent rules |
|----------|------------|-------------|
| `{{instruction_files}}` | ✓ | ✓ |
| `{{rules_dir}}` | ✗ | ✓ |
| `{{skills_dir}}` | ✗ | ✓ |
| `{{local_file}}` | ✗ | ✓ |

Variables defined in `agents/{agent}/config.yml`.

## Template Resolution for Validation

Use `--agent <name>` to specify which agent config to use (default: `claude`).

**Resolution process:**
1. Read `agents/{agent}/config.yml`
2. Extract `vars:` section
3. Replace `{{var}}` in .yml paths with actual values
4. Run OpenGrep on resolved file

**Example (claude agent):**
```yaml
# config.yml vars:
vars:
  instruction_files:
    - "**/CLAUDE.md"
    - ".claude/rules/**/*.md"

# Rule template → Resolved
paths:
  include:
    - "{{instruction_files}}"    # template (stored)
    - "**/CLAUDE.md"             # resolved (validation only)
    - ".claude/rules/**/*.md"
```
