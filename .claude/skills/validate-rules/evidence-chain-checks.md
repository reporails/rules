# Evidence Chain Validation Checks

Detailed checks for source-claim-rule integrity.

## Check 1: backed_by References Exist

For each rule with `backed_by`:

```
For each entry in backed_by:
  1. source must exist in docs/sources.yml
  2. claim must exist in that source's claims[] array
```

**Error:** `E4001: backed_by references non-existent source "{source}"`
**Error:** `E4002: backed_by references non-existent claim "{claim}" in source "{source}"`

## Check 2: Bidirectional Consistency

**Forward check (rule → source):**
```
Rule S1 has backed_by: [{source: X, claim: Y}]
→ sources.yml X.claims[id=Y].rules must include "S1"
```

**Reverse check (source → rule):**
```
Source X has claim Y with rules: [S1]
→ Rule S1 must have backed_by: [{source: X, claim: Y}]
```

**Error:** `E4003: Rule "{rule}" references claim but claim.rules doesn't include rule`
**Error:** `E4004: Claim "{source}.{claim}" lists rule "{rule}" but rule lacks backed_by`

## Check 3: Confidence Alignment (v2)

| Condition | Required |
|-----------|----------|
| `confidence: confirmed` | `backed_by` with official (weight 1.0) AND research (weight 0.8+) |
| `confidence: high` | `backed_by` with official source (weight 1.0) |
| `confidence: medium` | `backed_by` with research (weight 0.8+) OR 2+ community (weight 0.4+) |
| `confidence: low` | No restriction (methodology-only is valid) |
| No `backed_by` | Must be `confidence: low` |

**Error:** `E4005: Rule "{rule}" has confidence:confirmed but missing official source (weight 1.0)`
**Error:** `E4006: Rule "{rule}" has confidence:confirmed but missing research validation (weight 0.8+)`
**Error:** `E4007: Rule "{rule}" has confidence:high but no backed_by with official weight (1.0)`
**Error:** `E4008: Rule "{rule}" has confidence:medium but no backed_by with research (0.8+) or 2+ community`
**Error:** `E4009: Rule "{rule}" has no backed_by but confidence is not low`

## Check 4: Orphaned Claims

Claims in sources.yml should be referenced by rules:

```
For each source in sources.yml:
  For each claim in source.claims:
    claim.rules should not be empty
```

**Warning:** `W4001: Claim "{source}.{claim}" has no rules referencing it`

## Check 5: Confirmed Confidence Validation

For rules with `confidence: confirmed`:

1. **Must have official backing:**
   - At least one backed_by with source.weight >= 1.0
   - Source type must be 'official'

2. **Must have research validation:**
   - At least one backed_by with source.weight >= 0.8
   - Source type must be 'research'
   - Research must VALIDATE the official claim, not just repeat it

3. **Validation pseudocode:**
   ```
   For each rule where confidence == confirmed:
     official_backing = any(b.weight >= 1.0 AND b.type == official for b in backed_by)
     research_backing = any(b.weight >= 0.8 AND b.type == research for b in backed_by)

     If NOT official_backing:
       ERROR: "confirmed confidence requires official source backing"
     If NOT research_backing:
       ERROR: "confirmed confidence requires research validation"
   ```

**Error format:**
```
ERROR: Invalid confirmed confidence
  Rule: S1
  Issue: Missing research validation
  Has: official backing (claude-code-best-practices)
  Missing: research source with weight >= 0.8
  Action: Add research source that validates the official claim, or downgrade to confidence: high
```

## Auto-fix Support

| Issue | Auto-fixable | Action |
|-------|--------------|--------|
| Missing rule in claim.rules | Yes | Add rule ID to array |
| Missing backed_by in rule | No | Requires manual review |
| Confidence mismatch | Yes | Adjust to match weight |
| Orphaned claim | No | Requires decision |
| Missing research for confirmed | No | Downgrade to high or find research |

## Running Checks

```bash
/validate-rules --source-check  # Includes evidence chain
/validate-rules S1 --source-check  # Single rule
```

## Output Format

```
Evidence Chain: 42 rules | 21 sources | 87 claims
  By confidence: 5 confirmed | 20 high | 10 medium | 7 low
  Resolved: 156/156 backed_by references
  Bidirectional: 2 mismatches
  Confidence: 1 alignment issue
  Orphaned: 3 claims

S1: ✓ confirmed (official + research)
C8: ✗ E4003 - claim.rules missing rule ID
E2: ⚠ W4001 - orphaned claim in backbone
G5: ✓ low (methodology only)
```

## Trust Score Calculation

Confidence levels are weighted to calculate trust score:

```
weights = {
  confirmed: 1.0,   # Full trust (official + research)
  high: 0.8,        # Official recommendation
  medium: 0.5,      # Community consensus
  low: 0.2          # Methodology only
}

weighted_sum = sum(weights[rule.confidence] for rule in rules)
max_possible = len(rules) * 1.0  # If all were confirmed

trust_score = (weighted_sum / max_possible) * 100
```

This rewards having more `confirmed` rules, not just more backed rules.
