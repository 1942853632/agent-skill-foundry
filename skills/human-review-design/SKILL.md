---
name: human-review-design
description: Place human approval where an Agent's uncertainty or side effect warrants it. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: agent
  short-description: Human Review Design
---

# Human Review Design

## Purpose

Place human approval where an Agent's uncertainty or side effect warrants it.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **workflow, risk classes, reversibility, reviewer role**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. classify actions by impact and reversibility.
2. set automatic, review-required and prohibited bands.
3. define reviewer evidence and decision choices.
4. record approval, rejection and override reasons.
5. measure queue burden and false escalations.

## Output contract

Return: A review policy with gates, reviewer UI fields and escalation metrics.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] Review is required before irreversible effects.
- [ ] The reviewer sees enough evidence to decide.
- [ ] Low-risk work is not routed to a human by default.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

An Agent may draft a refund automatically but requires approval before issuing money or changing account ownership.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
