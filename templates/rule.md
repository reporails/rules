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
antipatterns:
  - id: A3
    name: Root file > 200 lines
    severity: critical
sources: [1, 10]
see_also: [M7]
---

# Size Limits

Prevents instruction degradation from token bloat.

## Thresholds

| Metric | Target | Warning | Critical |
|--------|--------|---------|----------|
| Root CLAUDE.md lines | < 100 | 100-200 | > 200 |

## Pattern

**Good:** Root file under 100 lines with @imports
**Bad:** 300-line monolithic CLAUDE.md
```

---

## Frontmatter Field Reference

| Field        | Required | Type     | Description                                         |
|--------------|----------|----------|-----------------------------------------------------|
| id           | Yes      | string   | Category letter + number (e.g., C9, S3, M2)         |
| title        | Yes      | string   | Short descriptive name                              |
| category     | Yes      | string   | One of: structure, content, maintenance, governance, efficiency |
| type         | Yes      | string   | One of: deterministic, heuristic, semantic, behavioral |
| detection    | Yes      | string   | How to detect (method for D/H, reason for Semantic) |
| level        | No       | string   | Minimum capability level (e.g., L2+, L4+, L6)       |
| question     | Heuristic| string   | LLM confirmation question (required for heuristic)  |
| criteria     | Heuristic| string   | Pass/fail criteria for LLM judgment                 |
| antipatterns | No       | array    | Related antipattern definitions                     |
| sources      | No       | array    | Source reference numbers (see README.md)            |
| see_also     | No       | array    | Related rule IDs                                    |

## Antipattern Object Fields

| Field    | Required | Type   | Description                              |
|----------|----------|--------|------------------------------------------|
| id       | Yes      | string | Antipattern ID (e.g., A3, A7)            |
| name     | Yes      | string | Short description of the antipattern     |
| severity | Yes      | string | One of: critical, high, medium, low      |
| weight   | No       | number | Override default weight (default: severity weight) |

## Type Categories

| Type          | Definition                          | Example                                        |
|---------------|-------------------------------------|------------------------------------------------|
| deterministic | 100% certainty via regexp/counting  | Line count, file exists, keyword count         |
| heuristic     | OpenGrep gate + LLM confirmation    | Pattern match → LLM validates                  |
| semantic      | LLM judgment only (no pattern gate) | Quality assessment, intent detection           |
| behavioral    | Runtime behavior, not file content  | Memory reference, purpose-based reading        |

## Heuristic Validation Flow

Heuristic rules use a two-stage filter to minimize LLM cost:

```
OpenGrep pattern match (gate)
    │
    ├── No match → Pass (95% of files, zero LLM cost)
    │
    └── Match → JudgmentRequest
                    │
                    └── LLM evaluates question + criteria
                            │
                            ├── Confirmed → Violation
                            └── Dismissed → Pass
```

**Required frontmatter for heuristic rules:**
- `question`: What to ask the LLM when pattern matches
- `criteria`: How to determine pass/fail

## Severity Definitions

| Severity | Weight | Impact                              |
|----------|--------|-------------------------------------|
| critical | 5.5    | Clarification loop + partial redo   |
| high     | 4.0    | Clarification loop                  |
| medium   | 2.5    | Brief clarification                 |
| low      | 1.0    | Minor friction                      |

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
- [ ] If heuristic, includes question + criteria fields
- [ ] Sources reference numbers from README.md
- [ ] Updated UNRELEASED.md
