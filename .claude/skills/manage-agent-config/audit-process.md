# Audit Process

Systematic review of agent configuration completeness.

## Step 1: Feature Detection

Research the agent's capabilities:

| Feature | Question | Where to check |
|---------|----------|----------------|
| Main instruction file | What file does the agent read? | Agent docs |
| Rules directory | Can rules be split into files? | Agent docs |
| Skills directory | Does agent support skills? | Agent docs |
| Session rituals | Does agent have session concept? | Agent behavior |
| Memory features | Can agent reference previous context? | Agent docs |
| Backbone/maps | Does agent support structured navigation? | Agent docs |

Document findings:
```
Agent: {agent}
Documentation: {url}

Feature Support:
  Main instruction file: ✓ ({pattern})
  Rules directory: ✓/✗
  Skills directory: ✓/✗
  Session rituals: ✓/✗
  Memory features: ✓/✗
  Backbone/maps: ✓/✗
```

## Step 2: Rule Applicability

For each core rule:

1. Read rule `.md` file — understand what it checks
2. Determine if agent supports the underlying feature
3. Decision matrix:

| Agent supports feature? | Action |
|------------------------|--------|
| Yes | Rule applies, no exclude |
| No | Add to `excludes` |
| Partial | Consider override with adjusted severity |

## Step 3: Build Excludes List

Based on Step 2, compile excludes:

```yaml
excludes:
  - S4   # Reason: No hierarchical memory
  - S5   # Reason: No path-scoped rules
  - E2   # Reason: No session concept
```

## Step 4: Severity Review

For each **applicable** rule (not excluded):

| Question | If yes... |
|----------|-----------|
| Is default severity too strict for this agent? | Override to lower severity |
| Is default severity too lenient for this agent? | Override to higher severity |
| Does agent handle this differently? | Consider `disabled: true` |
| Is this critical for agent's use case? | Ensure severity is `high`/`critical` |

## Step 5: Generate Report

```
═══════════════════════════════════════════════════
AGENT AUDIT: {agent}
═══════════════════════════════════════════════════

SCHEMA: ✓ Valid

VARIABLES:
  ✓ main_instruction_file: {value}
  ✓ instruction_files: {value}
  ✗ supplementary_files: MISSING (agent supports rules dir)

EXCLUDES:
  Current: [S4, S5]
  Expected: [S4, S5, E2]
  Missing: [E2]
  Extra: (none)

OVERRIDES:
  Current: (none)
  Recommendations:
    - S1-root-too-long: Consider medium (agent allows longer files)
    - E5-no-grep-guidance: Consider disabled (agent handles differently)

ACTION ITEMS:
  1. Add E2 to excludes
  2. Add supplementary_files variable
  3. Review override recommendations
```

## Step 6: Apply (if --apply)

1. Update config with missing excludes
2. Add recommended overrides (with confirmation)
3. Validate updated config
4. Show diff
