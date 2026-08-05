from __future__ import annotations
import json, sqlite3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
tutorial=json.loads((ROOT/'content/tutorials/sql_data_analytics.json').read_text(encoding='utf-8'))
seed=(ROOT/'assets/downloads/sql-analytics-practice-database.sql').read_text(encoding='utf-8')

def statements(sql):
    return [part.strip() for part in sql.split(';') if part.strip()]

required={'customers','products','employees','orders','order_items','web_events'}
base=sqlite3.connect(':memory:'); base.executescript(seed)
tables={r[0] for r in base.execute("SELECT name FROM sqlite_master WHERE type='table'")}
missing=required-tables
if missing: raise SystemExit(f'Missing SQL practice tables: {sorted(missing)}')
counts={t:base.execute(f'SELECT COUNT(*) FROM {t}').fetchone()[0] for t in required}
base.close()
fail=[]; result_queries=0
for ch in tutorial['chapters']:
    conn=sqlite3.connect(':memory:')
    try:
        conn.executescript(seed)
        had_result=False
        for stmt in statements(ch['activity']['sql']):
            cur=conn.execute(stmt)
            if cur.description:
                cur.fetchall(); had_result=True
        if had_result: result_queries+=1
        else: fail.append((ch['id'],'No result-producing statement'))
    except Exception as exc: fail.append((ch['id'],str(exc)))
    finally: conn.close()
if fail:
    print('SQL audit failures:')
    for item in fail: print('-',*item)
    raise SystemExit(1)
print(f"Validated SQL practice database tables: {', '.join(sorted(required))}")
print('Row counts:', ', '.join(f'{k}={counts[k]}' for k in sorted(counts)))
print(f"Executed {result_queries}/{len(tutorial['chapters'])} chapter starter queries successfully with SQLite.")
