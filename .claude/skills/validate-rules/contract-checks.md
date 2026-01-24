# Contract Validation Checks

## .md ↔ .yml Pairing

Every rule .md file must have a matching .yml file with OpenGrep patterns.

## Checks

- [ ] .yml file exists for every .md rule
- [ ] Every `checks[].id` in .md has matching `rules[].id` in .yml
- [ ] Every `rules[].id` in .yml has matching `checks[].id` in .md
- [ ] OpenGrep severity matches rule severity mapping
- [ ] Paths use template variables, not hardcoded paths

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

Use these instead of hardcoded paths:

| Variable | Description |
|----------|-------------|
| `{{instruction_files}}` | Main instruction files (e.g., `**/CLAUDE.md`) |
| `{{rules_dir}}` | Rules directory (e.g., `.claude/rules`) |
| `{{skills_dir}}` | Skills directory (e.g., `.claude/skills`) |
| `{{local_file}}` | Local preferences file |

Variables are defined in `agents/{agent}/config.yml`.
