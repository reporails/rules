# Validation Checks

## Schema Compliance

- [ ] `agent` — lowercase, matches directory name
- [ ] `prefix` — UPPERCASE, in reserved_agent_prefixes
- [ ] `name` — human-readable, ≤64 chars
- [ ] `vars.main_instruction_file` — required (universal)
- [ ] `vars.instruction_files` — required (universal)

## Variable Completeness

### Universal (required for ALL agents)

| Variable | Description | Example |
|----------|-------------|---------|
| `main_instruction_file` | Primary instruction file | `**/CLAUDE.md` |
| `instruction_files` | All instruction files | `**/CLAUDE.md`, `.claude/rules/**/*.md` |

### Agent-Specific (if feature supported)

| Variable | Required if... | Example |
|----------|----------------|---------|
| `supplementary_files` | Agent has rules directory | `.claude/rules/**/*.md` |
| `rules_dir` | Agent has rules directory | `.claude/rules` |
| `skills_dir` | Agent has skills directory | `.claude/skills` |

## Excludes Completeness

For each core rule, verify agent supports the underlying feature:

| Rule | Feature Required | Exclude if missing |
|------|------------------|-------------------|
| S4 | Hierarchical memory | ✓ |
| S5 | Path-scoped rules | ✓ |
| S4 | YAML backbone | ✓ |
| E2 | Session ritual concept | ✓ |
| E3 | File reading strategy | ✓ |
| E4 | Memory reference | ✓ |
| E5 | Grep configuration | ✓ |
| M7 | Rules directory | ✓ |

## Overrides Review

Empty `overrides` is suspicious. For each applicable rule:

1. Is default severity appropriate for this agent?
2. Are there agent-specific behaviors that change severity?
3. Should any checks be disabled (not excluded)?

### Override vs Exclude

- **Exclude**: Rule doesn't apply (agent lacks feature)
- **Override**: Rule applies but needs adjustment (different severity or disabled)

Example:
```yaml
# Agent supports the feature but with different expectations
overrides:
  S1-root-too-long:
    severity: medium  # This agent allows longer files
  E5-no-grep-guidance:
    disabled: true    # Agent handles this differently
```

## Validation Command

```bash
# Validate config structure
yq eval '.' agents/{agent}/config.yml

# Check required fields
yq eval '.vars.main_instruction_file' agents/{agent}/config.yml
yq eval '.vars.instruction_files' agents/{agent}/config.yml
```
