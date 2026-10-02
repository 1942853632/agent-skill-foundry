---
name: claim-audit
description: Audit a technical or research draft for unsupported, overstated or ambiguous claims. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: research
  short-description: Claim Audit
---

# Claim Audit

## Purpose

Audit a technical or research draft for unsupported, overstated or ambiguous claims.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **draft, citations, source files, claim standard**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. extract every externally checkable claim.
2. classify each as fact, interpretation, estimate or recommendation.
3. trace it to evidence or mark it unsupported.
4. compare wording strength with evidence strength.
5. return precise repairs without changing the thesis.

## Output contract

Return: A claim table with status, source, risk and suggested wording.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] Numbers have units, populations and time windows.
- [ ] Causal language has causal support.
- [ ] Recommendations are labeled as recommendations.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

A sentence saying a model 'proves' an effect is softened when the study only reports an association.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
