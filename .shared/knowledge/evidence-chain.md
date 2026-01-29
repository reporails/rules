# Evidence Chain Reference

How rules link to source claims for auditable traceability.

## Core Concepts

```
Source (docs/sources.yml)
  └── Claims (id, text, rules[])
        └── Rules (backed_by: source + claim)
```

## backed_by Structure

```yaml
# In rule frontmatter
backed_by:
  - source: source-id-from-sources-yml
    claim: claim-id-within-that-source
```

Multiple claims can back a single rule:

```yaml
backed_by:
  - source: claude-code-best-practices
    claim: keep-concise
  - source: instruction-limits-principles
    claim: line-limit
```

## Confidence Levels

| Level | Requirements | Example |
|-------|--------------|---------|
| confirmed | Official (1.0) + Research validates (0.8+) | Anthropic says + Arize measured |
| high | Official source (1.0) | Anthropic recommends |
| medium | Research (0.8+) OR 2+ community (0.4+) | Pattern from multiple blogs |
| experimental | Community-only or no backing | Community pattern |

**Decision tree:**

```
Has official backing (weight 1.0)?
├── Yes → Has research validation (0.8+)?
│         ├── Yes → confirmed
│         └── No → high
└── No → Has research backing (0.8+)?
         ├── Yes → medium
         └── No → Has 2+ community (0.4+)?
                  ├── Yes → medium
                  └── No → low
```

## Source Weights & Admission

| Type | Weight | Requirements |
|------|--------|--------------|
| Official | 1.0 | Vendor domain, official docs/announcement |
| Research | 0.8-0.9 | Measured data, reproducible results |
| Community | 0.4-0.5 | Blog posts, guides, tutorials |
| Community | 0.4-0.5 | Verifiable author, specific claims |

**Admission threshold:** weight >= 0.4

**Auto-reject if:**
- Anonymous or unverifiable author
- No specific claims (vague advice only)
- Single anecdote without supporting data
- Weight would be < 0.4

## Reporting Format

### Evidence Coverage (Primary Display)

Show the breakdown by backing type — this tells the real story:

```
Evidence Coverage
├── Official backing:     81% (35/43 rules)
├── Research validated:    0% (0/43 rules)
└── Experimental (no backing): ~23% of rules
```

**What each line means:**

| Metric | Meaning | Interpretation |
|--------|---------|----------------|
| Core tier | Rules backed by official (1.0) or research (0.8+) sources | "Vendor-confirmed or empirically validated" |
| Experimental tier | Rules with community-only (0.4) backing or no backing | "Community patterns, not yet validated" |

### Trust Score (Derived Metric)

The weighted score provides a single number for CI gates and trends:

```
Trust Score: 68.8%
(weighted: confirmed=1.0, high=0.8, medium=0.5, low=0.2)
```

**Calculation:**

```python
weights = {confirmed: 1.0, high: 0.8, medium: 0.5, low: 0.2}
weighted_sum = sum(max(source.weight for source in rule.backed_by) or 0 for rule in rules)
trust_score = (weighted_sum / len(rules)) * 100
```

### Full Report Format

```
Trust Score: 68.8%

Evidence Coverage
├── Official backing:     81% (35/43 rules)
├── Research validated:    0% (0/43 rules)
└── Experimental (no backing): ~23% of rules

Distribution
┌────────────┬───────┬──────────┬──────┐
│ Confidence │ Count │ × Weight │  =   │
├────────────┼───────┼──────────┼──────┤
│ confirmed  │ 0     │ × 1.0    │ 0.0  │
│ high       │ 35    │ × 0.8    │ 28.0 │
│ medium     │ 0     │ × 0.5    │ 0.0  │
│ low        │ 8     │ × 0.2    │ 1.6  │
├────────────┼───────┼──────────┼──────┤
│ Total      │ 43    │          │ 29.6 │
└────────────┴───────┴──────────┴──────┘
```

### Improving the Score

| Goal | Action | Impact |
|------|--------|--------|
| Low → High | Find official source backing the pattern | +0.6 per rule |
| Low → Medium | Find research or 2+ community sources | +0.3 per rule |
| High → Confirmed | Find research that validates the official claim | +0.2 per rule |

**Priority:** Focus on upgrading `low` rules first — biggest impact per effort.

## Validation Checks

### Check 1: backed_by References Exist

```
For each entry in backed_by:
  1. source must exist in docs/sources.yml
  2. claim must exist in that source's claims[] array
```

- `E4001`: backed_by references non-existent source
- `E4002`: backed_by references non-existent claim

### Check 2: Bidirectional Consistency

```
Forward:  Rule.backed_by → Source.claim.rules must include rule
Reverse:  Source.claim.rules → Rule.backed_by must reference claim
```

- `E4003`: Rule references claim but claim.rules doesn't include rule
- `E4004`: Claim lists rule but rule lacks backed_by

### Check 3: Confidence Alignment

| Condition | Required |
|-----------|----------|
| Core tier | max(backing_source_weights) >= 0.8 |
| Experimental tier | max(backing_source_weights) < 0.8 or no backing |

- `E4005-E4009`: Confidence/backing mismatches

### Check 4: Orphaned Claims

Claims in sources.yml should be referenced by rules.

- `W4001`: Claim has no rules referencing it

### Check 5: Source Admission

```
1. weight must be >= 0.4
2. type must match weight range
3. claims[] must not be empty
```

- `E4010`: Source weight below admission threshold
- `E4011`: Source type doesn't match weight
- `W4002`: Source has no claims

## Auto-fixable Issues

| Issue | Auto-fixable |
|-------|--------------|
| Missing rule in claim.rules | Yes |
| Missing backed_by in rule | No |
| Confidence mismatch | Yes |
| Orphaned claim | No |