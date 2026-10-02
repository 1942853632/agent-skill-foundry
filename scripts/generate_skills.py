from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / 'skill_catalog.json'
SKILLS = ROOT / 'skills'

def make_skill(item: dict) -> str:
    steps = '\n'.join(f'{i}. {step}.' for i, step in enumerate(item['steps'], 1))
    checks = '\n'.join(f'- [ ] {check}' for check in item['checks'])
    return f'''---
name: {item['name']}
description: {item['purpose']} Use when the user needs this specific workflow. Do not use it as a generic substitute for unrelated work.
metadata:
  category: {item['category']}
  short-description: {item['title']}
---

# {item['title']}

## Purpose

{item['purpose']}

This skill is deliberately narrow. It produces a reviewable artifact rather than pretending to complete work that requires missing evidence.

## Required input

Start by collecting: **{item['inputs']}**.

If a required input is missing, ask for it or mark the resulting assumption explicitly. Never fill a factual gap with a plausible detail.

## Workflow

{steps}

## Output contract

Return: {item['output']}

Keep three layers separate:

- **Source facts:** what was supplied or observed.
- **Reasoning:** how the facts were organized or interpreted.
- **Decisions:** what the user should approve, change or verify.

## Quality gate

Before delivering, check:

{checks}

If a check fails, report the gap instead of silently lowering the standard.

## Example shape

{item['example']}

## Boundaries

- Do not invent names, measurements, citations, permissions or outcomes.
- Keep private or sensitive material limited to what the task requires.
- Prefer a small, testable artifact over a broad list of generic advice.
'''

def main() -> None:
    catalog = json.loads(CATALOG.read_text(encoding='utf-8'))
    seen = set()
    for item in catalog:
        name = item['name']
        if name in seen:
            raise SystemExit(f'duplicate skill name: {name}')
        seen.add(name)
        path = SKILLS / name
        path.mkdir(parents=True, exist_ok=True)
        (path / 'SKILL.md').write_text(make_skill(item), encoding='utf-8')
    lines = ['# Skill Catalog', '', '| Category | Skill | Purpose |', '| --- | --- | --- |']
    for item in catalog:
        lines.append(f"| {item['category']} | [`{item['name']}`](skills/{item['name']}/SKILL.md) | {item['purpose']} |")
    (ROOT / 'CATALOG.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'generated {len(catalog)} skills')

if __name__ == '__main__':
    main()
