from __future__ import annotations
import csv, json, zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
projects=json.loads((ROOT/'content/projects/portfolio_projects.json').read_text(encoding='utf-8'))
errors=[]
if len(projects)!=6: errors.append(f'Expected 6 projects, found {len(projects)}')
ids=set(); total_rows=0
for project in projects:
    pid=project.get('id')
    if not pid or pid in ids: errors.append(f'Missing or duplicate project id: {pid}')
    ids.add(pid)
    for field in ['title_en','title_bn','summary_en','summary_bn','level','estimated_hours','tools','files','questions','deliverables','workflow','quality_gates','portfolio_sections','downloads','url']:
        if not project.get(field): errors.append(f'{pid}: missing {field}')
    if project.get('status')!='available': errors.append(f'{pid}: status is not available')
    if len(project.get('workflow',[]))!=8: errors.append(f'{pid}: expected 8 workflow phases')
    if len(project.get('questions',[]))<3: errors.append(f'{pid}: fewer than 3 analytical questions')
    if len(project.get('deliverables',[]))<5: errors.append(f'{pid}: fewer than 5 deliverables')
    if len(project.get('quality_gates',[]))<5: errors.append(f'{pid}: fewer than 5 quality gates')
    page=ROOT/project['url'].lstrip('/')/'index.html'
    if not page.exists(): errors.append(f'{pid}: generated page missing')
    for filename in project.get('files',[]):
        path=ROOT/'assets/datasets/portfolio'/filename
        if not path.exists(): errors.append(f'{pid}: missing dataset asset {filename}')
        elif path.suffix=='.csv' and not filename.endswith('_dictionary.csv'):
            with path.open(encoding='utf-8-sig',newline='') as f: rows=sum(1 for _ in csv.reader(f))-1
            if rows<=0: errors.append(f'{pid}: dataset {filename} is empty')
            total_rows += max(rows,0)
    for item in project.get('downloads',[]):
        zpath=ROOT/item['url'].lstrip('/')
        if not zpath.exists(): errors.append(f'{pid}: missing project package {item["url"]}')
        elif zpath.suffix=='.zip':
            with zipfile.ZipFile(zpath) as z:
                names=set(z.namelist())
                for filename in project.get('files',[]):
                    if not any(Path(name).name==filename for name in names): errors.append(f'{pid}: package missing {filename}')
                for required in ['project-brief.md','starter-sql.sql','starter-python.py','excel-build-guide.md','power-bi-build-guide.md','portfolio-readme-template.md']:
                    if not any(Path(name).name==required for name in names): errors.append(f'{pid}: package missing {required}')
for required in ['data-analytics-portfolio-toolkit.zip','project-charter-template.md','analysis-plan-template.md','portfolio-readme-template.md','presentation-outline-template.md','project-qa-checklist.csv','metric-dictionary-template.csv','data-quality-audit-template.csv','insight-log-template.csv']:
    if not (ROOT/'assets/downloads/portfolio'/required).exists(): errors.append(f'Missing portfolio toolkit asset: {required}')
if errors:
    print('Portfolio project audit failed:')
    for error in errors: print('-',error)
    raise SystemExit(1)
print(f'Validated {len(projects)} complete portfolio projects, {sum(len(p["workflow"]) for p in projects)} workflow phases, and {total_rows} synthetic project data rows.')
print('All project pages, data files, dictionaries, downloadable packages, templates, deliverables, and quality gates are present.')
