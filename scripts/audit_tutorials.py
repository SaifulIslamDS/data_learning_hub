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
expected={'data-foundations':21,'excel-data-analytics':56,'sql-data-analytics':66,'power-bi-data-analytics':77}
if len(tutorials)!=len(expected): errors.append(f'Expected {len(expected)} published tutorials, found {len(tutorials)}')
summary=[]
for tutorial in tutorials:
    tid=tutorial.get('id')
    if tutorial.get('status')!='published': errors.append(f'{tid}: not published')
    chapters=tutorial.get('chapters',[])
    if tid not in expected: errors.append(f'{tid}: unexpected published tutorial')
    elif len(chapters)!=expected[tid]: errors.append(f'{tid}: expected {expected[tid]} chapters, found {len(chapters)}')
    ids=set(); objective_count=section_count=term_count=exercise_count=0
    module_ids={m.get('id') for m in tutorial.get('modules',[])}
    for i,ch in enumerate(chapters,1):
        cid=ch.get('id')
        if not cid or cid in ids: errors.append(f'{tid} chapter {i}: missing or duplicate id {cid}')
        ids.add(cid)
        if module_ids and ch.get('module') not in module_ids: errors.append(f'{cid}: invalid or missing module')
        for field in ['title_en','title_bn','summary_en','summary_bn','objectives','sections','terms','worked_example','activity','exercises','recap','references']:
            if not ch.get(field): errors.append(f'{cid}: missing {field}')
        objectives=ch.get('objectives',[]); sections=ch.get('sections',[]); terms=ch.get('terms',[]); exercises=ch.get('exercises',[])
        objective_count+=len(objectives); section_count+=len(sections); term_count+=len(terms); exercise_count+=len(exercises)
        if len(objectives)<4: errors.append(f'{cid}: fewer than 4 objectives')
        if len(sections)<3: errors.append(f'{cid}: fewer than 3 teaching sections')
        if len(terms)<4: errors.append(f'{cid}: fewer than 4 terms')
        if len(exercises)<3: errors.append(f'{cid}: fewer than 3 exercises')
        types={e.get('type') for e in exercises}
        if not {'mcq','fill','short'}.issubset(types): errors.append(f'{cid}: exercise types incomplete {types}')
        worked=ch.get('worked_example',{})
        if len(worked.get('steps_en',[]))<4 or len(worked.get('steps_en',[]))!=len(worked.get('steps_bn',[])): errors.append(f'{cid}: worked example steps incomplete')
        if len(ch.get('references',[]))<2: errors.append(f'{cid}: fewer than 2 references')
        if ch.get('summary_en') == ch.get('summary_bn'):
            errors.append(f'{cid}: Bangla summary duplicates English')
        for s in sections:
            if len(s.get('body_en',''))<120 or len(s.get('body_bn',''))<80: errors.append(f'{cid}: teaching section too short')
            if s.get('body_en') == s.get('body_bn'): errors.append(f'{cid}: Bangla teaching section duplicates English')
        page=ROOT/'tutorials'/tid/cid/'index.html'
        if not page.exists(): errors.append(f'{cid}: generated page missing')
    for route in [ROOT/'tutorials'/tid/'index.html',ROOT/'exercises'/tid/'index.html',ROOT/'quiz'/tid/'index.html',ROOT/'examples'/tid/'index.html',ROOT/'references'/tid/'index.html']:
        if not route.exists(): errors.append(f'missing route {route.relative_to(ROOT)}')
    for item in tutorial.get('downloads',[]):
        target=ROOT/item['url'].lstrip('/')
        if not target.exists(): errors.append(f'{tid}: missing download {item["url"]}')
    summary.append((tid,len(chapters),objective_count,section_count,term_count,exercise_count))
for route in [ROOT/'tutorials'/'index.html',ROOT/'exercises'/'index.html',ROOT/'quiz'/'index.html',ROOT/'examples'/'index.html',ROOT/'references'/'index.html']:
    if not route.exists(): errors.append(f'missing multi-course route {route.relative_to(ROOT)}')
if errors:
    print('Tutorial audit failed:')
    for e in errors: print('-',e)
    raise SystemExit(1)
print(f'Validated {len(tutorials)} published tutorials with {sum(x[1] for x in summary)} complete chapters.')
for tid,chapters,objectives,sections,terms,exercises in summary:
    print(f'- {tid}: {chapters} chapters, {objectives} objectives, {sections} teaching sections, {terms} key terms, {exercises} exercises.')
print('Tutorial, exercise, quiz, example, reference, module and downloadable-file routes are present.')
