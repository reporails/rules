---
id: C8
title: Instructions Over Philosophy
category: content
type: semantic
backed_by:
  - source: claude-4-best-practices
    claim: instructions-not-philosophy
  - source: spec-writing-for-agents
    claim: code-snippet-beats-prose
  - source: claude-4-best-practices
    claim: context-improves
  - source: osmani-ai-coding-workflow
    claim: context-packaging
checks:
  - id: C8-philosophy-detected
    name: Explanatory prose instead of imperatives
    severity: low
    pattern_confidence: low
question: "Is this content actionable instruction or explanatory prose?"
criteria:
  - Content uses imperative verbs (use, run, add, create)
  - Avoids lengthy explanations of why
  - Focuses on what to do, not theory
sources:
  - "https://www.anthropic.com/engineering/claude-code-best-practices"
  - "https://addyosmani.com/blog/good-spec/"
see_also: [C2, C5]
---

# Instructions Over Philosophy

Imperative guidance, not explanatory prose.

## Pattern

**Good:** "Run pytest before committing"
**Bad:** "Testing is important because it helps catch bugs early..."
