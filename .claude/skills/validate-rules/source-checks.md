# Source Validation Checks

## Process

For each rule with sources:

1. **Fetch each source URL**
2. **Extract key claims** from source content
3. **Compare** rule's checks against source claims
4. **Report drift:**
   - "Rule X enforces Y, but source doesn't mention Y"
   - "Source says Z, but rule doesn't enforce Z"
   - "Source updated, rule may be stale"

## Validation Logic

For each rule with sources:
1. Fetch source URL content
2. Extract enforceable claims from source
3. Check: does each rule check have source support?
4. Check: does source have claims the rule doesn't enforce?
5. Report findings for manual review

## What to Extract from Sources

| Source type | Look for |
|-------------|----------|
| Official docs | Explicit recommendations, limits, patterns |
| Research | Measured data, percentages, thresholds |
| Community | Practical patterns, real-world examples |

## Claim Matching

A source claim supports a check if:
- Source mentions specific threshold → Check enforces that threshold
- Source recommends pattern → Check detects pattern absence/presence
- Source warns against antipattern → Check detects antipattern

## Drift Detection

Flag for review if:
- Source page returns 404 (broken link)
- Source content changed significantly (hash mismatch)
- Source mentions different thresholds than rule
- Source no longer mentions the pattern rule enforces

## Weight-Based Validation

For each rule:

1. **Load sources** from rule's `sources:` field
2. **Look up weights** from `docs/sources.yml`
3. **Validate confidence level:**

| Rule confidence | Required source weight |
|-----------------|------------------------|
| high | At least one source with weight >= 0.8 |
| medium | At least one source with weight >= 0.6 OR 2+ sources with weight >= 0.4 |
| low | Any source |

4. **Flag mismatches:**
   - confidence: high but no weight >= 0.8 source → ERROR
   - confidence: high but source doesn't explicitly state pattern → WARNING
   - confidence: low but has weight >= 0.8 source → SUGGESTION (upgrade confidence?)

## Reporails Methodology Rules

Rules sourcing from Reporails docs (L5-L6 patterns):
- S6, M6, G5, G6, E2

These are **self-sourced**. Validation checks:
- [ ] Rule cites Reporails source
- [ ] Empirical data is documented
- [ ] Methodology is explained

Skip external source validation — you ARE the source.

## Rules Without Sources

If `sources: []` is empty:
- Flag for review
- Either: find supporting source
- Or: mark as Reporails methodology
- Or: remove rule (unsupported opinion)
