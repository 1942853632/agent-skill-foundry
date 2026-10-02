---
name: study-explainer
description: Explain a difficult concept at the learner's level using checks for understanding rather than a lecture dump. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: daily
  short-description: Study Explainer
---

# Study Explainer

## Purpose

Explain a difficult concept at the learner's level using checks for understanding rather than a lecture dump.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **concept, learner level, known prerequisite, goal, preferred example**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. diagnose the likely missing prerequisite.
2. give a plain-language model before notation.
3. work one example step by step.
4. show one counterexample or common mistake.
5. ask a short retrieval question and provide a self-check.

## Output contract

Return: A layered explanation with example, misconception warning and practice prompt.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] The explanation does not hide a necessary assumption.
- [ ] The example is solved rather than merely named.
- [ ] The self-check tests the target concept.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

A probability explanation starts with sample space, computes one event and contrasts independence with mutual exclusivity.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
