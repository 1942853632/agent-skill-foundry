---
name: prompt-test-design
description: Build a regression set that tests an Agent instruction against normal, ambiguous and adversarial inputs. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: agent
  short-description: Prompt Test Design
---

# Prompt Test Design

## Purpose

Build a regression set that tests an Agent instruction against normal, ambiguous and adversarial inputs.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **skill or prompt, target behavior, known failures, policy boundaries**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. derive cases from intended behavior and exclusions.
2. include minimal pairs that change one fact.
3. add missing-input and conflicting-instruction cases.
4. define expected behavior and evidence.
5. tag tests by severity and automate stable checks.

## Output contract

Return: A prompt test matrix with fixtures, expected outcomes and evaluation notes.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] Tests cover refusal and clarification behavior.
- [ ] Expected outcomes are behavior-based, not exact wording.
- [ ] A failed test points to a specific instruction gap.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

A summarization skill is tested with an empty source, contradictory dates, injected instructions and a normal report.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
