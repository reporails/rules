# Reporails Framework

**Version:** 0.0.1
**Date:** January 2026


## Overview

This framework provides a structured approach to evaluating, creating, and maintaining CLAUDE.md files.

**Contents:**
- [Capability Model](capability-model.md) – L1-L6 level definitions and assessment
- [Structure Rules](rules/structure/) – S1-S7 file organization and size (20 pts)
- [Content Rules](rules/content/) – C1-C12 what to include and how (35 pts)
- [Maintenance Rules](rules/maintenance/) – M1-M7 version control and review (15 pts)
- [Governance Rules](rules/governance/) – G1-G8 org policies and ownership (15 pts)
- [Efficiency Rules](rules/efficiency/) – E1-E8 token optimization (15 pts)

---

## Why This Matters

### The Problem

Without a well-structured CLAUDE.md:

- **Constant context exhaustion:** 200k context window fills in ~15 minutes during normal work
- **Repeated explanations:** Every session starts with "this project uses X pattern, not Y"
- **Wrong suggestions:** Claude confidently proposes patterns that violate your architecture
- **Feature work is slow:** Adding features requires extensive hand-holding and correction

### The Transformation

With L4+ CLAUDE.md architecture:

- **Context lasts:** Sessions only hit limits during major refactoring, not routine feature work
- **Zero explanation needed:** Describe a feature at high level, Claude implements it correctly
- **Bad patterns eliminated:** MUST/MUST NOT rules prevent violations before they happen
- **Feature work is fast:** High-level description leads to accurate implementation

### Measured Benefits

| Area | Before | After (L4+) | Impact |
|------|--------|-------------|--------|
| Context window | Exhausted ~15 min | Full feature sessions | 3-5x longer sessions |
| Corrections | Multiple cycles | Correct first attempt | 50-70% reduction |
| Feature prompts | 30+ min detailed | 2-3 sentences | 10x faster |
| Token waste | 8-10% | < 5% | Significant cost reduction |

---

## Implementation Roadmap

### Phase 1: Foundation (Week 1-2)
**Target: L2**

- Audit existing CLAUDE.md files
- Ensure all projects have reviewed CLAUDE.md
- Add missing core sections
- Remove auto-generated cruft

### Phase 2: Structure (Week 3-4)
**Target: L3**

- Extract details to @imports
- Create /docs/ structure
- Remove embedded code snippets
- Remove code style rules

### Phase 3: Modularization (Week 5-8)
**Target: L4**

- Implement .claude/rules/
- Configure formatting hooks
- Set up hierarchical memory
- Create CLAUDE.local.md template

### Phase 4: Governance (Week 9-16)
**Target: L5**

- Deploy org-level policies
- Build metrics dashboard
- Implement CI/CD checks
- Establish change management

### Phase 5: Adaptive (Optional, Week 17+)
**Target: L6**

Only pursue if criteria met (monorepo, layered architecture, 50k+ lines):

- Design YAML backbone
- Create navigation maps
- Implement contract registry
- Add architecture tests
- Document session ritual

---

## Empirical Results

### Token Efficiency Analysis

**Data source:** 3 production sessions, 367,001 total tokens

| Session | Tokens | Waste | Waste % |
|---------|--------|-------|---------|
| 2026.01.16-ab58 | 129,908 | 9,250 | 7.1% |
| 2026.01.16-4128 | 111,000 | 8,150 | 7.3% |
| 2026.01.17-4323 | 126,093 | 14,000-19,000 | 11-15% |

**Average waste: 8-10% (31,400-36,400 tokens across 3 sessions)**

### Violation Breakdown

| Violation | Frequency | Token Impact | Prevention |
|-----------|-----------|--------------|------------|
| Skipped session ritual | 3/3 sessions | 2,000-3,000/session | Enforce in CLAUDE.md |
| Redundant file reads | All sessions | 4,000-16,500/session | Reference from memory |
| Exploration without limits | 2/3 sessions | 1,800-3,950/session | Purpose-based reading |
| Grep without head_limit | 1/3 sessions | 1,600 | Use files_with_matches |

### Key Insight

> "The session ritual was documented but not followed in any session. Instructions exist; compliance requires enforcement mechanisms beyond documentation."

This validates the need for:
1. Explicit ritual in component CLAUDE.md (not just referenced)
2. Token tracking to identify violations
3. Architecture tests for structural compliance

---

## Antipattern Reference

### Critical Antipatterns (-25 pts each)

| ID | Antipattern | Fix |
|----|-------------|-----|
| A1 | Auto-generated without review | Review and trim |
| A2 | Code style enforcement rules | Use hooks for enforcement, CLAUDE.md for guidance |
| A3 | > 200 lines in root | Progressive disclosure |
| A4 | Embedded code snippets | Use file:line references |
| A5 | Philosophy instead of instructions | Concrete bullets |

### High-Impact Antipatterns (-15 pts each)

| ID | Antipattern | Fix |
|----|-------------|-----|
| A6 | Context-specific in root | Move to @imports |
| A7 | Duplicate information | Single source of truth |
| A8 | Conflicting rules | Consolidate |
| A9 | Everything emphasized | Max 3-5 IMPORTANT |
| A10 | Vague instructions | Make specific |

### L6 Antipatterns (-10 pts each)

| ID | Antipattern | Fix |
|----|-------------|-----|
| A11 | Stale navigation maps | CI validation |
| A12 | Skipping session ritual | Enforce in CLAUDE.md |
| A13 | Hard-linking rules | Route through maps |
| A14 | Rule snippets > 40 lines | Split by concern |
| A15 | SHOULD instead of MUST | Binary format |
| A16 | Missing architecture tests | Add boundary tests |

---

## Document Control

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01 | Initial 12-level framework |
| 2.0 | 2026-01 | Collapsed to 6 levels, added empirical data, rule length caps |

---

## Sources & References

### Official Documentation

1. **[Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)**
   Official Anthropic engineering blog. Covers CLAUDE.md structure, what to include, instruction limits, and when to use emphasis.

2. **[Claude Code Memory Documentation](https://code.claude.com/docs/en/memory)**
   Official documentation on CLAUDE.md, file hierarchy, @imports, .claude/rules/, and CLAUDE.local.md.

3. **[Claude Code Hooks Guide](https://code.claude.com/docs/en/hooks-guide)**
   Official hooks documentation. Covers pre-commit, post-tool, and custom hook configuration.

4. **[Claude Code Settings](https://code.claude.com/docs/en/settings)**
   Official settings documentation. Includes .claude/rules/ configuration and path scoping.

5. **[Context Windows Documentation](https://platform.claude.com/docs/en/build-with-claude/context-windows)**
   Official context management docs. Explains token limits and context optimization.

6. **[Using CLAUDE.md Files](https://claude.com/blog/using-claude-md-files)**
   Official Claude blog on CLAUDE.md usage patterns and best practices.

7. **[How Anthropic Teams Use Claude Code](https://claude.com/blog/how-anthropic-teams-use-claude-code)**
   Internal Anthropic practices. Documents how teams use CLAUDE.md for onboarding, continuous improvement loops, and the # shortcut for live documentation.

8. **[Claude 4 Best Practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices)**
   Official prompting guidance. Explains instruction-following behavior, when to use emphasis, and providing context for rules.

### Empirical & Research Sources

9. **[Claude Code Issue #13579](https://github.com/anthropics/claude-code/issues/13579)**
    Community-documented 7 token-wasting patterns with 700K+ tokens of measured waste. Covers compaction issues (language switch, context loss after summarization) and multi-agent coordination problems.

10. **[Organizing CLAUDE.md in a Monorepo](https://dev.to/anvodev/how-i-organized-my-claudemd-in-a-monorepo-with-too-many-contexts-37k7)**
    Real-world case study: reduced main CLAUDE.md from 47k words to ~9k words (~80% reduction) using hierarchical structure and service-specific files.

11. **[Writing a Good CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md)**
    Quantifies instruction limits (150-200 max for frontier LLMs). Recommends <300 lines, progressive disclosure, and "less is more" philosophy.

12. **[CLAUDE.md Optimization Study](https://arize.com/blog/claude-md-best-practices-learned-from-optimizing-claude-code-with-prompt-learning/)**
    Empirical study showing +5.19% general improvement and +10.87% repo-specific improvement from prompt optimization alone. No model changes required.

13. **[How I Use Every Claude Code Feature](https://blog.sshh.io/p/how-i-use-every-claude-code-feature)**
    Enterprise perspective: 13KB strict limit, 30% engineer usage threshold. Key insight: "start with problems, not manuals" and pair NEVER statements with positive alternatives.

### Community Guides

14. **[Claude MD Guide](https://www.builder.io/blog/claude-md-guide)**
    Comprehensive community guide covering file placement, .claude/rules/, path-scoped rules, and practical examples.

15. **[Claude Rules Directory Mechanics](https://claudefa.st/blog/guide/mechanics/rules-directory)**
    Detailed .claude/rules/ mechanics including path scoping, YAML frontmatter, and loading behavior.

16. **[How to Write a Good Spec for AI Agents](https://addyosmani.com/blog/good-spec/)**
    PRD-style structure for agent instructions. Introduces three-tier boundaries (Always/Ask First/Never) and modular prompt design.

### Cross-Tool Standards

17. **[AGENTS.md Specification](https://agents.md/)**
    Open standard for agent instructions. Compatible with Codex, Cursor, Copilot, Jules, Factory, Aider. Includes cascading rules and discovery precedence.

18. **[OpenAI Codex AGENTS.md Guide](https://developers.openai.com/codex/guides/agents-md)**
    Official Codex documentation for AGENTS.md. Documents 32KB size limit, override hierarchy, and cross-tool compatibility patterns.

19. **[Cursor Rules for AI](https://cursor.com/docs/context/rules)**
    Cursor's rules documentation. Covers `.cursor/rules/` structure, glob patterns, and team rules.

20. **[GitHub Copilot Custom Instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot)**
    GitHub Copilot custom instructions via `.github/copilot-instructions.md`. Documents path-specific instructions and agent personas.

21. **[JetBrains AI Agent Guidelines](https://blog.jetbrains.com/idea/2025/05/coding-guidelines-for-your-ai-agents/)**
    JetBrains Junie agent configuration via `.junie/guidelines.md`. IDE-specific perspective on coding agent instructions.

22. **[Keep a Changelog](https://keepachangelog.com/en/1.1.0/)**
    Changelog format specification. Used for UNRELEASED.md structure.

### Capability Model Foundations

23. **[CMMI Maturity Levels](https://cmmiinstitute.com/learning/appraisals/levels)**
    Capability Maturity Model Integration. Inspired the L1-L6 progression structure.

24. **[Cloud Native Maturity Model](https://maturitymodel.cncf.io/)**
    CNCF capability model. Similar tiered approach for infrastructure capability.

### Original Research

25. **Reporails Empirical Data** *(first-party data, unverified)*
    Original measurements from 310+ hours of development across 50+ sessions. Documented 8-10% token waste from context file antipatterns. This is self-reported project data and has not been independently validated.

26. **[Advanced Context Engineering for Coding Agents](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents)**
    HumanLayer's methodology for scaling AI coding to large codebases. Introduces "Frequent Intentional Compaction" framework with 40-60% context utilization target. Successfully applied to 300k LOC projects with 35k LOC feature additions.

---

*Review quarterly. Update based on Claude capability changes and measured outcomes.*
