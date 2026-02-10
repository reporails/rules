---
id: "CORE:S:0004"
slug: no-sensitive-information
title: No Sensitive Information in Instruction Files
category: structure
type: deterministic
level: L2
backed_by:
- dometrain-claude-md-guide
- spec-writing-for-agents
- using-claude-md-files
targets: '{{instruction_files}}'
checks:
- id: "CORE:S:0004:check:0001"
  type: deterministic
  severity: high
question: "Do any instruction files contain secrets, API keys, credentials, or connection
  strings?"
criteria:
- No instruction file contains strings matching common API key patterns (AWS, 
  GitHub, Stripe, OpenAI, etc.)
- No instruction file contains database connection strings with embedded 
  credentials
- No instruction file contains base64-encoded tokens longer than 40 characters
- No instruction file contains private key material (BEGIN RSA PRIVATE KEY, 
  etc.)
- No instruction file contains password assignments (password=, passwd=, 
  secret=)
---

# No Sensitive Information in Instruction Files

No instruction file may contain secrets, API keys, credentials, or connection strings.

## Pass / Fail

**Pass:** A CLAUDE.md file references environment variables by name ("Use $DATABASE_URL
for connections") or refers to a secrets manager ("API keys are stored in
AWS Secrets Manager") without including the actual values. The file contains
no patterns matching API key formats, no base64-encoded tokens, and no
connection strings with embedded passwords.
**Fail:** A CLAUDE.md file contains the line "Use this API key for testing:
sk-proj-abc123def456ghi789". Or it includes a database connection string
like "postgresql://admin:p4ssw0rd@db.example.com:5432/production". Or it
embeds an AWS access key "AKIAIOSFODNN7EXAMPLE".

## Limitations

Pattern matching produces false positives on example/placeholder values,
documentation about secret formats, and strings that coincidentally match
secret patterns (e.g., long base64 strings in code examples). Cannot detect
secrets in custom or proprietary formats that do not match known patterns.
Cannot distinguish between a real secret and a deliberately redacted example.
