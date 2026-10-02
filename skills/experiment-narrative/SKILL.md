---
name: experiment-narrative
description: Write a transparent result narrative from experiment logs, tables and plots. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: research
  short-description: Experiment Narrative
---

# Experiment Narrative

## Purpose

Write a transparent result narrative from experiment logs, tables and plots.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **hypothesis, setup, metrics, results, artifacts, limitations**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. state the hypothesis and comparison first.
2. describe only setup details needed to interpret results.
3. report effect size and uncertainty before interpretation.
4. connect each conclusion to an artifact.
5. include failed runs and boundary conditions.

## Output contract

Return: A result section that separates observation, interpretation and limitation.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] Baseline and evaluation split are clear.
- [ ] Metrics are defined before results.
- [ ] The conclusion does not exceed the experiment.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

A ranking experiment narrative reports offline gains, confidence intervals and the missing online validation.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
