---
name: workflow-decomposer
description: Break a complex request into agent-sized steps with clear handoffs and dependencies. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: agent
  short-description: Workflow Decomposer
---

# Workflow Decomposer

## Purpose

Break a complex request into agent-sized steps with clear handoffs and dependencies.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **goal, constraints, artifacts, tools, people**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. separate research, transformation, decision and mutation work.
2. order steps by information dependency.
3. define artifact and owner at each handoff.
4. mark parallel work and join conditions.
5. add checkpoints for ambiguity and risk.

## Output contract

Return: A workflow graph or numbered plan with inputs, outputs, dependencies and checkpoints.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] Each step has one dominant purpose.
- [ ] Handoffs name the artifact, not just a status.
- [ ] High-impact mutations have a review gate.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

A release workflow separates changelog drafting, test verification, approval and deployment instead of one giant agent prompt.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
