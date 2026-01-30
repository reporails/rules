# QA Checklist

Verification criteria for skill workflows.

---

## generate-rule

After running rule creation workflow:

| Check | Verification | Expected |
|-------|--------------|----------|
| Directory exists | `ls -d core/*/SMOKE1-*` | Directory present |
| Files exist | `ls core/*/SMOKE1-*/*.{md,yml}` | Both .md and .yml present |
| Tests exist | `ls core/*/SMOKE1-*/tests/` | fail.md and pass.md present |
| Frontmatter valid | `head -30 core/*/SMOKE1-*/*.md` | id, title, category, type, checks, backed_by, pattern_confidence |
| Check ID format | Inspect .md | `checks[].id` starts with rule ID + hyphen |
| YML matches | Inspect .yml | `rules[].id` matches `checks[].id` from .md |
| OpenGrep validates | `opengrep scan --config core/*/SMOKE1-*/*.yml .` | Exit 0 or 1 |

**Fail indicators:**
- Missing .yml file
- Frontmatter missing required fields
- Check ID doesn't match pattern `{RULE_ID}-{suffix}`
- OpenGrep exit 2 (syntax error) or 7 (no positive pattern)

---

## validate-rules

After running validation workflow:

| Check | Verification | Expected |
|-------|--------------|----------|
| Completes | Workflow finishes | No crash or hang |
| Schema validation | Output | Reports schema errors if any |
| Contract validation | Output | Reports .md/.yml mismatches if any |
| OpenGrep validation | Output | Reports pattern errors if any |
| Summary format | Output | `Rules: N | Schema: N | Contract: N` |

**Fail indicators:**
- Workflow crashes
- Known-good rules reported as errors
- Known-bad rules not caught

---

## audit-evidence-chain

After running evidence audit workflow:

| Check | Verification | Expected |
|-------|--------------|----------|
| Loads sources | Workflow reads | `docs/sources.yml` accessed |
| Bidirectional check | Output | Reports E4003/E4004 if mismatched |
| Confidence check | Output | Reports E4005-E4009 if misaligned |
| Trust score | Output | Numeric score calculated |
| Metrics file | `cat .reporails/trust-metrics.yml` | File exists with score |

**Fail indicators:**
- Can't find sources.yml
- Score calculation errors
- Metrics file not created

---

## update-rule

After running rule update workflow:

| Check | Verification | Expected |
|-------|--------------|----------|
| Locates rule | Workflow finds | Correct .md and .yml |
| ID preserved | `grep "id:" core/*/SMOKE1-*/*.md` | ID unchanged |
| Directory preserved | `ls -d core/*/SMOKE1-*` | Same directory |
| Pattern updated | `cat core/*/SMOKE1-*/*.yml` | New pattern present |
| pattern_confidence reassessed | Inspect .md | pattern_confidence updated if patterns changed |
| OpenGrep validates | `opengrep scan --config core/*/SMOKE1-*/*.yml .` | Exit 0 or 1 |

**Fail indicators:**
- Rule not found
- ID or filename changed
- Pattern not added
- pattern_confidence not reassessed after pattern change
- OpenGrep fails after update

---

## Failure Triage

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| "File not found" on .shared/ | Broken relative path | Check links in SKILL.md |
| Hallucinated patterns | Knowledge not loaded | Verify .shared/knowledge/ links |
| Exit code 2 | Invalid YAML | Check syntax, required fields |
| Exit code 7 | No positive pattern | Add pattern-regex before pattern-not-regex |
| Wrong tier | backed_by doesn't match expected tier | Check sources.yml weights |
| Missing .yml | Workflow step skipped | Check contract step in workflow |
| ID changed on update | Constraint violated | Check rule-update workflow constraints |

---

## Adding Checks for New Skills

When adding a new skill:

1. Add section with skill name as heading
2. List checks as table: Check | Verification | Expected
3. List fail indicators
4. Update qa-smoke-test.md if skill should be in smoke test