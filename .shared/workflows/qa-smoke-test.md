# QA Smoke Test Workflow

Meta-workflow that validates all skill workflows after structural changes.

```mermaid
flowchart TD
    START([QA Smoke Test]) --> GEN[1. Rule Creation<br/>SMOKE1 core 'Smoke Test']
    GEN --> CHECK1{Checklist passed?}
    CHECK1 -->|No| FAIL1([FAIL: generate-rule])
    CHECK1 -->|Yes| VAL[2. Rule Validation<br/>all rules]
    VAL --> CHECK2{Checklist passed?}
    CHECK2 -->|No| FAIL2([FAIL: validate-rules])
    CHECK2 -->|Yes| AUDIT[3. Evidence Audit<br/>all rules + sources]
    AUDIT --> CHECK3{Checklist passed?}
    CHECK3 -->|No| FAIL3([FAIL: audit-evidence-chain])
    CHECK3 -->|Yes| UPD[4. Rule Update<br/>SMOKE1 add pattern]
    UPD --> CHECK4{Checklist passed?}
    CHECK4 -->|No| FAIL4([FAIL: update-rule])
    CHECK4 -->|Yes| REVAL[5. Re-validate<br/>confirm SMOKE1 still valid]
    REVAL --> CHECK5{Still passes?}
    CHECK5 -->|No| FAIL5([FAIL: regression])
    CHECK5 -->|Yes| CLEANUP[6. Cleanup<br/>rm core/*/SMOKE1-*]
    CLEANUP --> PASS([PASS])
```

## Test Sequence

| Step | Workflow | Input | Verify With |
|------|----------|-------|-------------|
| 1 | rule-creation | `SMOKE1 core "Smoke Test"` | qa-checklist.md#generate-rule |
| 2 | rule-validation | all rules | qa-checklist.md#validate-rules |
| 3 | evidence-audit | all rules + sources | qa-checklist.md#audit-evidence-chain |
| 4 | rule-update | `SMOKE1 "Add test pattern"` | qa-checklist.md#update-rule |
| 5 | rule-validation | all rules | SMOKE1 still passes |
| 6 | cleanup | `rm core/*/SMOKE1-*` | files deleted |

## When to Run

- After changes to `.shared/workflows/`
- After changes to `.shared/knowledge/`
- After changes to `.claude/skills/`
- Before merging PRs that touch skill infrastructure

## Edge Cases

**Step 1 fails (generate):**
- Check `.shared/workflows/rule-creation.md` links
- Check `.shared/knowledge/` files exist
- Check skill imports resolve

**Step 4 fails (update):**
- Check rule-update workflow handles existing files
- Verify SMOKE1 was created correctly in step 1

**Step 5 fails (regression):**
- Update broke something — compare .yml before/after
- Check OpenGrep validation output

## Cleanup on Failure

If any step fails, still run cleanup:

```bash
rm -f core/*/SMOKE1-*
```

Don't leave test artifacts in the repo.