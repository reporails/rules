---
id: "CORE:C:0012"
slug: has-domain-terminology
title: Has Domain Terminology
category: content
type: deterministic
level: L2
backed_by:
- claude-md-optimization-study
- dometrain-claude-md-guide
targets: '{{instruction_files}}'
checks:
- id: "CORE:C:0012:check:0001"
  type: deterministic
  negate: true
  severity: high
question: "Do the instruction files define project-specific terminology or acronyms?"
criteria:
- At least one instruction file defines domain-specific terms, acronyms, or 
  business concepts
- Definitions include enough context to use the term correctly (not just 
  expanding an acronym)
- At least two terms are defined
---

# Has Domain Terminology

The instruction files must define domain-specific terminology, acronyms, or business
concepts used in the project.

## Pass / Fail

**Pass:** The instruction file contains:
```
## Terminology
- PDP: Product Detail Page -- the main page displaying a single product
- SKU: Stock Keeping Unit -- unique identifier for a purchasable product variant
- Fulfillment: the process of picking, packing, and shipping an order from warehouse
  to customer delivery
- Cart abandonment: when a user adds items to cart but does not complete checkout
```
Each term is defined with enough context for the agent to use it correctly.
**Fail:** The instruction file uses acronyms and domain terms throughout:
```
The PDP component fetches SKU data from the fulfillment API. Handle cart
abandonment events in the analytics pipeline.
```
But never defines PDP, SKU, fulfillment, or cart abandonment. The agent must guess
what these terms mean.

## Limitations

Cannot verify that defined terms are used consistently throughout the codebase. Cannot
detect domain terms that are used in the codebase but missing from the glossary. Cannot
assess whether definitions are accurate for the project's business domain. Projects with
no domain-specific terminology (pure infrastructure, for example) may legitimately lack
this section.
