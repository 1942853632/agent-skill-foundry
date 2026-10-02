---
name: experiment-design
description: Turn a product or model question into a statistically defensible experiment plan. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: data
  short-description: Experiment Design
---

# Experiment Design

## Purpose

Turn a product or model question into a statistically defensible experiment plan.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **hypothesis, unit, treatment, outcome, constraints, expected effect**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. define estimand and randomization unit.
2. choose primary outcome and guardrails.
3. set inclusion, exclusion and exposure rules.
4. plan power, duration and stopping policy.
5. specify analysis, failure modes and interpretation.

## Output contract

Return: An experiment protocol with pre-registration fields and an analysis checklist.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] Treatment cannot leak into control.
- [ ] Primary outcome is chosen before results.
- [ ] Operational constraints are explicit.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

A recommendation experiment specifies user-level assignment, purchase conversion, exposure minimum and a guardrail for latency.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
