# Common Mistakes

| Mistake | Fix |
|---------|-----|
| Using source IDs | Use full URLs |
| Missing .yml file | Always create both files |
| Wrong check ID format | Must be `{rule_id}-{suffix}` |
| Semantic without question | Add question + criteria |
| Deterministic with question | Remove question + criteria |
| Hardcoded paths in .yml | Use `{{instruction_files}}` |
| Title > 64 characters | Shorten or abbreviate |
| Body > 40 lines | Extract to supporting docs |
| Missing severity mapping | critical→ERROR, others→WARNING |
| Citing L5-L6 patterns as Anthropic docs | Use docs/capability-levels.md |
