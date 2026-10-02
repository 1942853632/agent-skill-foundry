---
name: migration-plan
description: Plan a data or API migration with compatibility, rollback and observability. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: engineering
  short-description: Migration Plan
---

# Migration Plan

## Purpose

Plan a data or API migration with compatibility, rollback and observability.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **current state, target state, consumers, volume, downtime limit**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. inventory readers, writers and invariants.
2. choose expand, backfill and contract phases.
3. define dual-read or dual-write behavior when needed.
4. set validation, cutover and rollback checkpoints.
5. plan cleanup and ownership after migration.

## Output contract

Return: A migration runbook with phases, commands, metrics, rollback and completion criteria.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] Old and new versions coexist safely during rollout.
- [ ] Backfill is resumable and verifiable.
- [ ] Rollback does not destroy the source of truth.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

A nullable column migration adds the field, backfills in batches, validates parity and removes the old path later.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
