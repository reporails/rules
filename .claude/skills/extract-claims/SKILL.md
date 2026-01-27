---
name: extract-claims
description: Extract claims from a source URL for sources.yml
---

# /extract-claims

Extract specific claims from a source document for the evidence chain.

## Usage

```
/extract-claims <url> [--source-id <id>]
```

- `<url>`: Source URL to fetch and analyze
- `--source-id <id>`: Optional source ID (defaults to derived from URL)

## Process

### Step 0: Source Admission Check

Before extracting claims, validate source meets admission criteria.

**1. Determine source type** (official, research, community):

| Type | Indicators |
|------|------------|
| Official | Vendor domain (anthropic.com, github.com/docs), official announcement |
| Research | Has measured data, methodology described, author credentials |
| Community | Developer blog, tutorial, practical guide |

**2. Check minimum criteria:**

| Type | Weight | Requirements |
|------|--------|--------------|
| Official | 1.0 | Published on vendor domain, official docs or announcement |
| Research | 0.8-0.9 | Measured data, methodology, specific/reproducible findings |
| Community | 0.4 | Verifiable author, recognized platform, specific claims |

**3. Auto-reject if:**
- Anonymous or unverifiable author
- No specific claims (vague advice only)
- Single anecdote without supporting data
- Contradicts official sources without evidence
- Self-promotional without substance
- Weight would be < 0.4

**4. Output admission decision:**

```yaml
# Admitted source
admission:
  status: admitted
  type: research
  weight: 0.8
  rationale: "Measured data from optimization study, methodology documented"

# Rejected source
admission:
  status: rejected
  reason: "No specific claims - article is general advice without measurable recommendations"
  suggestion: "Find a source that makes specific, testable claims"
```

**If rejected:** Stop here. Do not proceed to claim extraction.

### Step 1: Fetch and Extract

1. **Fetch source content** from URL
2. **Identify enforceable claims:**
   - Specific recommendations ("Keep under 300 lines")
   - Thresholds ("No more than 5 emphases")
   - Patterns ("Use @imports for...")
   - Anti-patterns ("Don't include style rules")

3. **For each claim, determine:**
   - `id`: short identifier (lowercase, hyphens)
   - `text`: the claim (quote or paraphrase, max 200 chars)
   - `quote`: true if direct quote
   - `section`: where in document
   - `rules`: which existing rules this backs (or empty)

4. **Output YAML** for sources.yml

## Output Format

```yaml
claims:
  - id: claim-id
    text: "The specific claim"
    quote: true
    section: "Section Name"
    rules: [S1, C2]

  - id: another-claim
    text: "Another recommendation"
    quote: false
    section: "Another Section"
    rules: []  # No matching rule yet
```

## Guidelines

### What Makes a Good Claim

| Good | Bad |
|------|-----|
| "Keep CLAUDE.md under 300 lines" | "Has advice about file size" |
| "Use @imports for documentation" | "Talks about imports" |
| "5 IMPORTANT markers maximum" | "Mentions emphasis" |

### Extraction by Source Type

| Source type | Approach |
|-------------|----------|
| Official docs | Direct quotes preferred |
| Research | Data points, measurements |
| Community | Patterns, practical advice |
| Methodology | Internal reasoning |

### Rules for Claims

- One claim per distinct recommendation
- Keep text under 200 characters
- Don't combine unrelated advice
- If claim doesn't match existing rule, set `rules: []`
- Prefer direct quotes for official sources

## Mapping to Rules

Reference these rule categories when mapping:

| Category | Rules | Topics |
|----------|-------|--------|
| Structure | S1-S7 | Size, imports, hierarchy, markdown |
| Content | C1-C12 | Sections, patterns, emphasis, antipatterns |
| Efficiency | E1-E8 | Tools, reading, grep, context |
| Governance | G2-G8 | Teams, security, ownership, CI |
| Maintenance | M1-M6 | Version, review, change, conflicts |

## Example

**Input:** `https://www.anthropic.com/engineering/claude-code-best-practices`

**Output:**
```yaml
claims:
  - id: size-limit
    text: "Keep your CLAUDE.md file under 300 lines"
    quote: true
    section: "Keep it concise"
    rules: [S1]

  - id: progressive-disclosure
    text: "Use @-imports to reference external documentation"
    quote: false
    section: "Progressive disclosure"
    rules: [S2]

  - id: no-style-rules
    text: "Don't include code style rules - use linters instead"
    quote: false
    section: "What not to include"
    rules: [E1]

  - id: emphasis-sparingly
    text: "Use emphasis (IMPORTANT, CRITICAL) sparingly"
    quote: false
    section: "Emphasis"
    rules: [C7]
```

## Admission Check Example

**Source:** `https://example.com/blog/my-claude-tips`

**Check:**
- Author: John Doe (verifiable LinkedIn) ✓
- Platform: Company engineering blog ✓
- Claims: "I use @imports" (anecdotal, single data point) ⚠
- Data: None ✗
- Specificity: Low ✗

**Decision:**
```yaml
admission:
  status: rejected
  reason: "Anecdotal experience without measured data or specific thresholds"
  suggestion: "Would need multiple corroborating sources or measured impact data"
```

**Contrasting admitted source:**

**Source:** `https://arize.com/blog/claude-md-optimization-study`

**Check:**
- Author: Arize AI team (verifiable company) ✓
- Platform: Company research blog ✓
- Claims: "+5.19% improvement from optimization" (measured) ✓
- Data: A/B test results ✓
- Specificity: High ✓

**Decision:**
```yaml
admission:
  status: admitted
  type: research
  weight: 0.8
  rationale: "Measured improvement data with specific percentages, reproducible methodology"
```
