from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
raw=(ROOT/'assets/js/content.js').read_text(encoding='utf-8')
prefix='window.DLH_CONTENT = '
if not raw.startswith(prefix): raise SystemExit('Invalid content payload')
data=json.loads(raw[len(prefix):].rstrip().rstrip(';'))
errors=[]
tutorials=data.get('tutorials',[])
if len(tutorials)!=1: errors.append(f'Expected one published tutorial, found {len(tutorials)}')
for tutorial in tutorials:
    if tutorial.get('status')!='published': errors.append(f"{tutorial.get('id')}: not published")
    chapters=tutorial.get('chapters',[])
    if len(chapters)!=21: errors.append(f"{tutorial.get('id')}: expected 21 chapters, found {len(chapters)}")
    ids=set()
    for i,ch in enumerate(chapters,1):
        cid=ch.get('id')
        if not cid or cid in ids: errors.append(f'chapter {i}: missing or duplicate id {cid}')
        ids.add(cid)
        for field in ['title_en','title_bn','summary_en','summary_bn','objectives','sections','terms','worked_example','activity','exercises','recap','references']:
            if not ch.get(field): errors.append(f'{cid}: missing {field}')
        if len(ch.get('objectives',[]))<4: errors.append(f'{cid}: fewer than 4 objectives')
        if len(ch.get('sections',[]))<3: errors.append(f'{cid}: fewer than 3 teaching sections')
        if len(ch.get('terms',[]))<4: errors.append(f'{cid}: fewer than 4 terms')
        if len(ch.get('exercises',[]))<3: errors.append(f'{cid}: fewer than 3 exercises')
        types={e.get('type') for e in ch.get('exercises',[])}
        if not {'mcq','fill','short'}.issubset(types): errors.append(f'{cid}: exercise types incomplete {types}')
        worked=ch.get('worked_example',{})
        if len(worked.get('steps_en',[]))<4 or len(worked.get('steps_en',[]))!=len(worked.get('steps_bn',[])): errors.append(f'{cid}: worked example steps incomplete')
        if len(ch.get('references',[]))<2: errors.append(f'{cid}: fewer than 2 references')
        for s in ch.get('sections',[]):
            if len(s.get('body_en',''))<120 or len(s.get('body_bn',''))<80: errors.append(f'{cid}: teaching section too short')
        page=ROOT/'tutorials'/tutorial['id']/cid/'index.html'
        if not page.exists(): errors.append(f'{cid}: generated page missing')
    for route in [ROOT/'tutorials'/tutorial['id']/'index.html',ROOT/'exercises'/tutorial['id']/'index.html',ROOT/'quiz'/tutorial['id']/'index.html',ROOT/'examples'/tutorial['id']/'index.html',ROOT/'references'/tutorial['id']/'index.html']:
        if not route.exists(): errors.append(f'missing route {route.relative_to(ROOT)}')
if errors:
    print('Tutorial audit failed:')
    for e in errors: print('-',e)
    raise SystemExit(1)
print('Validated 1 published tutorial with 21 complete bilingual chapters.')
print('Validated 84 learning objectives, 63+ teaching sections, 84+ key terms, 21 worked examples, 21 activities and 63 exercises.')
print('Tutorial landing, exercise library, final quiz, example library and reference routes are present.')
