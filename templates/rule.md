# Rule Template

Use this template when adding new rules to `rules/[category]/` directories.

---

## Example with Frontmatter

```markdown
---
id: S1
title: Size Limits
category: structure
type: deterministic
detection: Line count, depth counting
level: L2+
scoring: 10
antipatterns:
  - id: A3
    name: Root file > 200 lines
    severity: critical
    points: -25
sources: [1, 10]
see_also: [M7]
---

# Size Limits

Prevents instruction degradation from token bloat.

## Thresholds

| Metric | Target | Warning | Critical |
|--------|--------|---------|----------|
| Root CLAUDE.md lines | < 100 | 100-200 | > 200 |

## Scoring

- Lines < 100: +10 points
- Lines < 200: +5 points
```

---

## Frontmatter Field Reference

| Field        | Required | Type     | Description                                         |
|--------------|----------|----------|-----------------------------------------------------|
| id           | Yes      | string   | Category letter + number (e.g., C9, S3, M2)         |
| title        | Yes      | string   | Short descriptive name                              |
| category     | Yes      | string   | One of: structure, content, maintenance, governance, efficiency |
| type         | Yes      | string   | One of: deterministic, heuristic, semantic          |
| detection    | Yes      | string   | How to detect (method for D/H, reason for Semantic) |
| level        | No       | string   | Minimum maturity level (e.g., L2+, L4+, L6)         |
| scoring      | No       | number   | Points awarded for compliance                       |
| antipatterns | No       | array    | Related antipattern definitions                     |
| sources      | No       | array    | Source reference numbers (see README.md)            |
| see_also     | No       | array    | Related rule IDs                                    |

## Antipattern Object Fields

| Field    | Required | Type   | Description                              |
|----------|----------|--------|------------------------------------------|
| id       | Yes      | string | Antipattern ID (e.g., A3, A7)            |
| name     | Yes      | string | Short description of the antipattern     |
| severity | Yes      | string | One of: critical, high, medium           |
| points   | Yes      | number | Penalty points (negative)                |

## Type Categories

| Type          | Definition                          | Example                                        |
|---------------|-------------------------------------|------------------------------------------------|
| deterministic | 100% certainty via regexp/counting  | Line count, file exists, keyword count         |
| heuristic     | Deterministic with confidence level | Pattern matching that may have false positives |
| semantic      | Requires AI judgment                | Quality assessment, intent detection           |

## Severity Definitions

| Severity | Points  | Meaning                  |
|----------|---------|--------------------------|
| critical | -25 pts | Breaks AI understanding  |
| high     | -15 pts | Significant inefficiency |
| medium   | -10 pts | Minor issue              |

## Body Content Guidelines

After the frontmatter, include:

1. **Title** (H1): Rule name (matches frontmatter title)
2. **Impact statement**: One sentence explaining why this rule matters
3. **Requirements/Thresholds**: Specific criteria (use tables for thresholds)
4. **Pattern examples** (if applicable): Good/bad examples
5. **Scoring details** (if applicable): How points are awarded

Keep body content concise (< 40 lines recommended).

## Checklist Before Adding

- [ ] Rule doesn't duplicate existing rules (check C6)
- [ ] ID follows sequence in category
- [ ] Frontmatter parses as valid YAML
- [ ] Type category is accurate
- [ ] If heuristic, noted confidence level in detection
- [ ] Sources reference numbers from README.md
- [ ] Updated UNRELEASED.md
