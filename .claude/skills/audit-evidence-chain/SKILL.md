---
name: audit-evidence-chain
description: Audit trust architecture and generate metrics for source-claim-rule integrity
---

# /audit-evidence-chain

Audit the evidence chain and generate trust metrics.

## Usage

```
/audit-evidence-chain [options]
```

**Options:**
- `--output <path>`: Output metrics file (default: `.reporails/trust-metrics.yml`)
- `--report`: Generate human-readable report (`.reporails/audit-report.md`)
- `--fail-below <n>`: Exit non-zero if trust score < n (for CI)
- `--verbose`: Show detailed validation for each rule

**Examples:**
```
/audit-evidence-chain                      # Run audit, output metrics
/audit-evidence-chain --report             # Include human-readable report
/audit-evidence-chain --fail-below 70      # CI gate at 70% trust score
/audit-evidence-chain --verbose            # Show all rule details
```

## Purpose

This skill answers: **"How trustworthy is my rule set?"**

Unlike `/validate-rules` which checks correctness, this skill measures:
- Evidence coverage (how many rules have backing)
- Confidence distribution (confirmed vs low)
- Bidirectional integrity (source ↔ rule links)
- Trust score (weighted metric)

## Workflow

### Step 1: Load Data

```
1. Read all rules from core/ and agents/*/rules/
2. Read docs/sources.yml
3. Build lookup maps for fast validation
```

### Step 2: Run Evidence Chain Checks

See [evidence-chain-checks.md](evidence-chain-checks.md) for detailed validation logic.

**Checks performed:**
1. `backed_by` references exist (source + claim)
2. Bidirectional consistency (rule ↔ claim links)
3. Confidence alignment (matches source weights)
4. Orphaned claims (claims with no rules)
5. Confirmed validation (official + research required)

### Step 3: Calculate Trust Score

```python
weights = {
    'confirmed': 1.0,   # Official + research validated
    'high': 0.8,        # Official recommendation
    'medium': 0.5,      # Community consensus
    'low': 0.2          # Methodology only
}

weighted_sum = sum(weights[rule.confidence] for rule in rules)
max_possible = len(rules) * 1.0

trust_score = (weighted_sum / max_possible) * 100
```

### Step 4: Generate Outputs

**trust-metrics.yml:**
```yaml
generated: 2025-01-28T12:00:00Z
schema_version: 1

summary:
  total_rules: 42
  trust_score: 71
  
rules:
  by_confidence:
    confirmed: 5
    high: 18
    medium: 7
    low: 12
  
  by_backing:
    official: 24      # Rules with official source
    research: 12      # Rules with research source
    community: 8      # Rules with community source
    methodology: 12   # Rules with methodology only
    unbacked: 0       # Rules with no backed_by

claims:
  total: 87
  enforced: 74        # Claims linked to rules
  orphaned: 13        # Claims with empty rules[]

validation:
  errors: 0
  warnings: 2
  
  issues:
    - type: warning
      code: W4001
      message: "Claim 'keepachangelog.unreleased-section' has no rules"
```

**audit-report.md** (with `--report`):
```markdown
# Trust Audit Report

Generated: 2025-01-28 12:00:00

## Summary

| Metric | Value |
|--------|-------|
| Trust Score | 71% |
| Total Rules | 42 |
| Confirmed | 5 (12%) |
| High | 18 (43%) |
| Medium | 7 (17%) |
| Low | 12 (29%) |

## Confidence Distribution

[chart or breakdown]

## Issues

### Warnings (2)

- W4001: Claim 'keepachangelog.unreleased-section' has no rules
- W4001: Claim 'jetbrains-junie-guidelines.guidelines-structure' has no rules

## Upgrade Opportunities

Rules that could be upgraded with additional backing:

| Rule | Current | Missing for Upgrade |
|------|---------|---------------------|
| S1 | high | Research validation → confirmed |
| C7 | medium | Official source → high |
```

### Step 5: CI Integration

With `--fail-below`:
```bash
/audit-evidence-chain --fail-below 70

# Exit 0 if trust_score >= 70
# Exit 1 if trust_score < 70 (fails CI)
```

## Output Files

| File | Purpose |
|------|---------|
| `.reporails/trust-metrics.yml` | Machine-readable metrics for CI/automation |
| `.reporails/audit-report.md` | Human-readable report for review |

## When to Run

- After rule changes (create, update, delete)
- After source changes (new claims, weight updates)
- In CI pipeline (PR checks)
- Before releases (quality gate)

## Reference Files

- [evidence-chain-checks.md](evidence-chain-checks.md) — Detailed validation checks
- [trust-metrics-schema.md](trust-metrics-schema.md) — Metrics file schema
