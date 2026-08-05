from __future__ import annotations
import csv, json, zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'assets/datasets/power_bi_retail_model'
EXPECTED={'DimDate.csv':730,'DimProduct.csv':12,'DimCustomer.csv':60,'DimRegion.csv':4,'FactSales.csv':360,'FactTargets.csv':96}
errors=[]
rows={}
for name,count in EXPECTED.items():
    path=DATA/name
    if not path.exists():
        errors.append(f'missing {name}'); continue
    with path.open(encoding='utf-8-sig',newline='') as f:
        rows[name]=list(csv.DictReader(f))
    if len(rows[name])!=count: errors.append(f'{name}: expected {count}, got {len(rows[name])}')

if rows:
    product={r['ProductKey'] for r in rows['DimProduct.csv']}
    customer={r['CustomerKey'] for r in rows['DimCustomer.csv']}
    region={r['RegionKey'] for r in rows['DimRegion.csv']}
    dates={r['Date'] for r in rows['DimDate.csv']}
    sales=rows['FactSales.csv']
    if len({r['SalesLineKey'] for r in sales})!=len(sales): errors.append('FactSales SalesLineKey is not unique')
    for i,r in enumerate(sales,2):
        if r['ProductKey'] not in product: errors.append(f'FactSales row {i}: orphan ProductKey')
        if r['CustomerKey'] not in customer: errors.append(f'FactSales row {i}: orphan CustomerKey')
        if r['RegionKey'] not in region: errors.append(f'FactSales row {i}: orphan RegionKey')
        if r['OrderDate'] not in dates: errors.append(f'FactSales row {i}: OrderDate missing from DimDate')
        revenue=float(r['Revenue']); cost=float(r['Cost']); profit=float(r['GrossProfit'])
        if abs((revenue-cost)-profit)>0.011: errors.append(f'FactSales row {i}: GrossProfit reconciliation failed')
    for i,r in enumerate(rows['FactTargets.csv'],2):
        if r['RegionKey'] not in region: errors.append(f'FactTargets row {i}: orphan RegionKey')
        if r['MonthStart'] not in dates: errors.append(f'FactTargets row {i}: MonthStart missing from DimDate')

zip_path=ROOT/'assets/downloads/power-bi-retail-practice-data.zip'
if not zip_path.exists(): errors.append('missing practice ZIP')
else:
    with zipfile.ZipFile(zip_path) as z:
        if set(z.namelist())!=set(EXPECTED): errors.append('practice ZIP contents differ from model CSV set')

course=json.loads((ROOT/'content/tutorials/power_bi_data_analytics.json').read_text(encoding='utf-8'))
if course.get('version')!='2.4.0' or len(course.get('chapters',[]))!=77: errors.append('Power BI course version/chapter count mismatch')
if len(course.get('modules',[]))!=9: errors.append('Power BI module count mismatch')
if any(ch.get('activity',{}).get('type')!='powerbi-demo' for ch in course.get('chapters',[])): errors.append('one or more Power BI chapters lack powerbi-demo activity')
if any(not all(r.get('url','').startswith('https://learn.microsoft.com/') for r in ch.get('references',[])) for ch in course.get('chapters',[])): errors.append('one or more Power BI chapter references are not official Microsoft Learn URLs')

for relative in ['assets/downloads/power-bi-dax-measures.txt','assets/downloads/power-bi-power-query-m-examples.txt','assets/downloads/power-bi-project-qa-checklist.csv','assets/datasets/power_bi_data_dictionary.csv']:
    p=ROOT/relative
    if not p.exists() or p.stat().st_size<100: errors.append(f'missing or empty {relative}')

if errors:
    print('Power BI practice audit failed:')
    for e in errors[:40]: print('-',e)
    raise SystemExit(1)
print('Validated Power BI tutorial: 77 chapters across 9 modules.')
print('Validated retail star-schema practice data: DimDate=730, DimProduct=12, DimCustomer=60, DimRegion=4, FactSales=360, FactTargets=96.')
print('Validated keys, date coverage, gross-profit reconciliation, official chapter references, ZIP contents and downloadable practice assets.')
