---
id: "CLAUDE:S:0011"
slug: sensitive-files-denied
title: Sensitive Files Denied in Permissions
category: structure
type: deterministic
level: L2
backed_by:
- claude-code-settings
- using-claude-md-files
targets: '{{instruction_files}}'
checks:
- id: "CLAUDE:S:0011:check:0001"
  type: deterministic
  negate: true
  severity: high
question: "Are all sensitive files in the project covered by permissions.deny in Claude
  Code settings?"
criteria:
- All .env files (including .env.local, .env.production) are matched by a deny 
  pattern
- Private key files (*.pem, *.key) are matched by a deny pattern if present
- Credential files (credentials.json, secrets.yml) are matched by a deny pattern
  if present
- The permissions.deny configuration exists in .claude/settings.json or 
  .claude/settings.local.json
---

# Sensitive Files Denied in Permissions

If sensitive files exist in the project (.env, credentials), they must be listed in permissions.deny in the Claude Code settings.

## Pass / Fail

**Pass:** The project contains .env and config/secrets.yml. The file .claude/settings.json includes
permissions.deny entries matching .env and config/secrets.yml. Claude Code cannot access
these files.
**Fail:** The project contains .env.production with database credentials. Neither .claude/settings.json
nor .claude/settings.local.json includes a permissions.deny entry covering .env* files.
Claude Code can freely read and reference the credentials.

## Limitations

This check scans for common sensitive file patterns (.env*, *.pem, *credentials*, *secret*)
and verifies deny coverage. Custom sensitive files with non-standard names (e.g., my-keys.txt)
are not detected. The check also cannot verify that deny patterns are syntactically correct
in the settings file, only that plausible deny entries exist for discovered sensitive files.
