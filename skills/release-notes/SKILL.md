---
name: release-notes
description: Write release notes that tell users what changed, who is affected and what to do. Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: engineering
  short-description: Release Notes
---

# Release Notes

## Purpose

Write release notes that tell users what changed, who is affected and what to do.

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **merged changes, issue links, known limitations, upgrade steps**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

1. group changes by user outcome.
2. separate new behavior, fixes and breaking changes.
3. write migration or configuration steps.
4. call out known limitations and rollback path.
5. verify every claim against merged artifacts.

## Output contract

Return: Audience-focused release notes with upgrade guidance and issue references.

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

- [ ] Breaking changes are prominent.
- [ ] Examples use the released interface.
- [ ] Internal implementation details are omitted unless operationally relevant.

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

A version note explains a changed authentication default, migration command and affected configuration key.

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
