---
id: E3
title: Purpose-Based File Reading
category: efficiency
type: semantic
detection: Behavioral rule about AI usage patterns
level: L4+
sources: [5, 25]
---

# Purpose-Based File Reading

60-75% token savings on exploration reads.

## Reading Strategy

| Goal | Strategy | Example |
|------|----------|---------|
| EDIT | Read full file | `Read file_path="app/nodes/x.py"` |
| UNDERSTAND | Read first 30-50 lines | `Read ... offset=0 limit=50` |
| FIND | Grep then targeted read | `Grep pattern="def process"` |
| VERIFY | Grep files_with_matches | `Grep ... output_mode="files_with_matches"` |
