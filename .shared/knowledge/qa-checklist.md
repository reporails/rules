# QA Checklist

Verification criteria for skill workflows.

---

## generate-rule

After running rule creation workflow:

| Check | Verification | Expected |
|-------|--------------|----------|
| Directory exists | `ls core/{category}/{slug}/` | Directory present |
| Files exist | `ls core/{category}/{slug}/rule.{md,yml}` | Both rule.md and rule.yml present |
| Tests exist | `ls core/{category}/{slug}/tests/` | pass/ and fail/ directories present |
| Frontmatter valid | `head -30 core/{category}/{slug}/rule.md` | id, slug, title, category, type, level, checks, backed_by |
| Check ID format | Inspect rule.md | `checks[].id` follows `NAMESPACE.CATEGORY.SLOT.check.NNNN` |
| YML matches | Inspect rule.yml | `rules[].id` matches `checks[].id` from rule.md |
| OpenGrep validates | `opengrep scan --config core/{category}/{slug}/rule.yml .` | Exit 0 or 1 |

**Fail indicators:**
- Missing rule.yml file
- Frontmatter missing required fields
- Check ID doesn't match coordinate pattern (e.g., `CORE.S.0001.check.0001`)
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

## update-rule

After running rule update workflow:

| Check | Verification | Expected |
|-------|--------------|----------|
| Locates rule | Workflow finds | Correct rule.md and rule.yml |
| ID preserved | `grep "id:" core/{category}/{slug}/rule.md` | Coordinate unchanged |
| Directory preserved | `ls -d core/{category}/{slug}/` | Same directory |
| Pattern updated | `cat core/{category}/{slug}/rule.yml` | New pattern present |
| OpenGrep validates | `opengrep scan --config core/{category}/{slug}/rule.yml .` | Exit 0 or 1 |

**Fail indicators:**
- Rule not found
- Coordinate or slug changed
- Pattern not added
- OpenGrep fails after update

---

## Failure Triage

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| "File not found" on .shared/ | Broken relative path | Check links in SKILL.md |
| Hallucinated patterns | Knowledge not loaded | Verify .shared/knowledge/ links |
| Exit code 2 | Invalid YAML | Check syntax, required fields |
| Exit code 7 | No positive pattern | Add pattern-regex before pattern-not-regex |
| Wrong tier | backed_by doesn't match expected tier | Check docs/sources.yml weights |
| Missing rule.yml | Workflow step skipped | Check contract step in workflow |
| Coordinate changed on update | Constraint violated | Check rule-update workflow constraints |

---

## Adding Checks for New Skills

When adding a new skill:

1. Add section with skill name as heading
2. List checks as table: Check | Verification | Expected
3. List fail indicators
4. Update qa-smoke-test.md if skill should be in smoke test
