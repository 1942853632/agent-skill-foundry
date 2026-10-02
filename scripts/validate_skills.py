from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / 'skill_catalog.json'
SKILLS = ROOT / 'skills'

def main() -> int:
    catalog = json.loads(CATALOG.read_text(encoding='utf-8'))
    names = [item['name'] for item in catalog]
    errors: list[str] = []
    if len(names) != len(set(names)):
        errors.append('catalog contains duplicate names')
    for item in catalog:
        name = item['name']
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
            errors.append(f'invalid skill name: {name}')
        file = SKILLS / name / 'SKILL.md'
        if not file.exists():
            errors.append(f'missing: {file}')
            continue
        text = file.read_text(encoding='utf-8')
        for required in ('---', '## Purpose', '## Required input', '## Workflow', '## Output contract', '## Quality gate', '## Boundaries'):
            if required not in text:
                errors.append(f'{name}: missing {required}')
        if len(text) < 900:
            errors.append(f'{name}: skill body is too short')
    actual = {p.name for p in SKILLS.iterdir() if p.is_dir()}
    errors.extend(f'catalog skill missing directory: {n}' for n in sorted(set(names) - actual))
    errors.extend(f'unlisted skill directory: {n}' for n in sorted(actual - set(names)))
    if errors:
        print('\n'.join(errors))
        return 1
    print(f'validated {len(names)} skills')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
