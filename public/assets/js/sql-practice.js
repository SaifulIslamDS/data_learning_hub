(() => {
  'use strict';
  const CDN = 'https://cdn.jsdelivr.net/npm/sql.js@1.14.1/dist/';
  const SEED = '/assets/downloads/sql-analytics-practice-database.sql';
  let SQLPromise = null;
  const esc = value => String(value ?? '').replace(/[&<>'"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]));
  const loadScript = src => new Promise((resolve,reject)=>{
    if (window.initSqlJs) return resolve();
    const existing=document.querySelector(`script[src="${src}"]`); if(existing){existing.addEventListener('load',resolve,{once:true});existing.addEventListener('error',reject,{once:true});return;}
    const s=document.createElement('script');s.src=src;s.async=true;s.onload=resolve;s.onerror=()=>reject(new Error('Could not load the browser SQL engine. Check the internet connection or content-security policy.'));document.head.appendChild(s);
  });
  const engine = () => SQLPromise ||= loadScript(`${CDN}sql-wasm.js`).then(()=>window.initSqlJs({locateFile:file=>`${CDN}${file}`}));
  const loadSeed = async url => { const res=await fetch(url||SEED); if(!res.ok) throw new Error(`Could not load practice database (${res.status}).`); return res.text(); };
  const resultTable = result => {
    const head=result.columns.map(c=>`<th>${esc(c)}</th>`).join('');
    const rows=result.values.slice(0,250).map(r=>`<tr>${r.map(v=>`<td>${esc(v===null?'NULL':v)}</td>`).join('')}</tr>`).join('');
    const note=result.values.length>250?`<p class="small">Showing first 250 of ${result.values.length} rows.</p>`:'';
    return `<div class="sql-result-block"><div class="table-wrap"><table><thead><tr>${head}</tr></thead><tbody>${rows}</tbody></table></div>${note}</div>`;
  };
  async function createDb(seedUrl){ const SQL=await engine(); const db=new SQL.Database(); db.run(await loadSeed(seedUrl)); return db; }
  function shell(prompt, note, sql){
    return `<div class="sql-practice-shell"><p class="activity-prompt">${esc(prompt)}</p><p class="sql-dialect-note">${esc(note)}</p><label class="sql-editor-label">SQL editor<textarea class="sql-editor" spellcheck="false">${esc(sql)}</textarea></label><div class="sql-action-row"><button class="button primary small" type="button" data-sql-run>Run query</button><button class="button ghost small" type="button" data-sql-reset>Reset query</button><button class="button ghost small" type="button" data-sql-db-reset>Reset database</button></div><div class="sql-status" aria-live="polite">Ready. The database will load when you run the first query.</div><div class="sql-results"></div></div>`;
  }
  function mount(root, config){
    const initial=config.sql||'SELECT * FROM orders LIMIT 10;';
    root.innerHTML=shell(config.prompt||'Edit and run the query.',config.note||'Runs locally in your browser with SQLite-compatible sql.js.',initial);
    let db=null;
    const editor=root.querySelector('.sql-editor'), status=root.querySelector('.sql-status'), results=root.querySelector('.sql-results');
    const ensure=async()=>db||(db=await createDb(config.seed||root.dataset.seed||SEED));
    root.querySelector('[data-sql-run]').addEventListener('click',async()=>{
      status.textContent='Loading database and running query…'; results.innerHTML=''; const started=performance.now();
      try{const active=await ensure(); const out=active.exec(editor.value); results.innerHTML=out.length?out.map(resultTable).join(''):'<div class="sql-empty-result">Query completed successfully. No result table was returned.</div>'; status.textContent=`Completed in ${Math.max(1,Math.round(performance.now()-started))} ms.`;}
      catch(error){status.textContent='Query error'; results.innerHTML=`<pre class="sql-error">${esc(error.message||error)}</pre>`;}
    });
    root.querySelector('[data-sql-reset]').addEventListener('click',()=>{editor.value=initial;results.innerHTML='';status.textContent='Query reset.';});
    root.querySelector('[data-sql-db-reset]').addEventListener('click',()=>{try{db?.close();}catch{}db=null;results.innerHTML='';status.textContent='Database reset. It will be recreated on the next run.';});
  }
  window.DLHSQLPractice={
    renderActivity(root,activity){mount(root,{prompt:(document.documentElement.lang==='bn'?activity.prompt_bn:activity.prompt_en)||activity.prompt_en,note:(document.documentElement.lang==='bn'?activity.dialect_note_bn:activity.dialect_note_en)||activity.dialect_note_en,sql:activity.sql});},
    mountStandalone(){const root=document.getElementById('sql-playground-root');if(root)mount(root,{seed:root.dataset.seed,prompt:'Write a query against the retail analytics practice database.',note:'Runs locally with SQLite-compatible sql.js. PostgreSQL is the primary teaching dialect.',sql:'SELECT region, COUNT(*) AS orders\nFROM orders\nWHERE status <> \'Cancelled\'\nGROUP BY region\nORDER BY orders DESC;'});}
  };
  document.addEventListener('DOMContentLoaded',()=>window.DLHSQLPractice.mountStandalone());
})();
