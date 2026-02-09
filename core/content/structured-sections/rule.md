---
id: "CORE:C:0015"
slug: structured-sections
title: Structured Sections
category: content
type: deterministic
level: L2
backed_by:
- spec-writing-for-agents
- using-claude-md-files
targets: '{{instruction_files}}'
checks:
- id: "CORE:C:0015:check:0001"
  type: deterministic
  negate: true
  severity: high
question: "Does this instruction file use Markdown headings to organize its content
  into sections?"
criteria:
- File contains at least two Markdown headings (lines starting with   ## or ###)
- No block of consecutive non-heading content exceeds 50 lines without a heading
  break
- Headings use level 2 (##) or level 3 (###) — not level 1 (#) which is reserved
  for the document title
---

# Structured Sections

Instruction files must use Markdown headings (## or ###) to organize content into
distinct named sections.

## Pass / Fail

**Pass:** A CLAUDE.md file organized with `## Commands`, `## Structure`, `## Testing`,
`## Constraints` headings, each followed by relevant content for that topic.
**Fail:** A CLAUDE.md file that is a wall of text — 150 lines of instructions with no headings,
no section breaks, and no structural markers. All content runs together in a single
undifferentiated block.

## Limitations

Cannot assess whether headings are meaningful or well-chosen — only checks for their
presence. A file with headings like "## Section 1", "## Section 2" would pass despite
having non-descriptive section names. Does not check whether content is correctly
placed under its heading. Very short files (under 10 lines) may not need headings.
