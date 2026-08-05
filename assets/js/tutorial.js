(() => {
  'use strict';
  const T=window.DLHTutorial; if(!T) return;
  const tutorial=T.getTutorial(); const chapter=tutorial.chapters.find(ch=>ch.id===document.body.dataset.chapter); if(!chapter) return;
  const activityRoot=document.getElementById('tutorial-activity');
  const exerciseRoot=document.getElementById('chapter-exercises');
  const esc=T.escapeHtml; const t=T.t;
  const mean=arr=>arr.length?arr.reduce((a,b)=>a+Number(b),0)/arr.length:0;
  const median=arr=>{const x=[...arr].map(Number).sort((a,b)=>a-b);const n=x.length;return n%2?x[(n-1)/2]:(x[n/2-1]+x[n/2])/2;};
  const stdev=arr=>{if(arr.length<2)return 0;const m=mean(arr);return Math.sqrt(arr.reduce((s,x)=>s+(Number(x)-m)**2,0)/(arr.length-1));};
  const corr=(x,y)=>{const mx=mean(x),my=mean(y);const num=x.reduce((s,v,i)=>s+(v-mx)*(y[i]-my),0);const dx=Math.sqrt(x.reduce((s,v)=>s+(v-mx)**2,0));const dy=Math.sqrt(y.reduce((s,v)=>s+(v-my)**2,0));return dx&&dy?num/(dx*dy):0;};
  const table=(rows,headers=null)=>`<div class="table-wrap"><table>${headers?`<thead><tr>${headers.map(h=>`<th>${esc(h)}</th>`).join('')}</tr></thead>`:''}<tbody>${rows.map(r=>`<tr>${r.map(v=>`<td>${esc(v)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;
  function prompt(activity) { return `<p class="activity-prompt">${esc(t(activity.prompt_en,activity.prompt_bn))}</p>`; }
  function reveal(textEn,textBn=textEn) { return `<button class="button small ghost" type="button" data-reveal-guidance>${t('Reveal guidance','Guidance দেখুন')}</button><div class="activity-guidance hidden">${esc(t(textEn,textBn))}</div>`; }
  function resultBox(html='') { return `<div class="activity-result excel-result" aria-live="polite">${html}</div>`; }
  function runButton(label='Run example') { return `<button class="button primary small" type="button" data-run-excel>${t(label,'Example চালান')}</button>`; }
  function formulaBadge(a) { return a.formula?`<div class="formula-block activity-formula"><span>Excel</span><code>${esc(a.formula)}</code><button type="button" class="copy-code" data-copy-code>Copy</button></div>`:''; }

  function renderClassify(a) {
    const types=[...new Set(a.items.map(x=>x.answer))];
    return `${prompt(a)}<div class="classify-grid">${a.items.map(item=>`<div class="classify-row"><span>${esc(item.text)}</span><select data-answer="${esc(item.answer)}"><option value="">${t('Choose…','বেছে নিন…')}</option>${types.map(x=>`<option value="${esc(x)}">${esc(x)}</option>`).join('')}</select><b></b></div>`).join('')}</div><button class="button primary small" data-check-activity type="button">${t('Check classification','Classification check করুন')}</button>${resultBox()}`;
  }
  function renderTable(a) {
    return `${prompt(a)}${table(a.rows,a.columns)}${reveal('Ask: What does one row represent? Which field is the identifier? Which columns are categories and which are quantities?','জিজ্ঞেস করুন: এক row কী represent করে? Identifier কোন field? কোন column category এবং কোনটি quantity?')}`;
  }
  function renderChoice(a) {
    return `${prompt(a)}<div class="activity-choice-grid">${a.options.map(o=>`<button type="button" data-choice="${o.id}" class="activity-choice">${esc(o.label)}</button>`).join('')}</div>${resultBox()}`;
  }
  function renderSampling(a) {
    return `${prompt(a)}<div class="sampling-demo"><p>${t('Population mean','Population mean')}: <strong>${mean(a.population).toFixed(2)}</strong></p><button class="button primary small" type="button" data-random-sample>${t('Draw random sample','Random sample নিন')}</button><button class="button ghost small" type="button" data-convenience-sample>${t('Take first values','First value নিন')}</button><div class="sample-output"></div></div>`;
  }
  function renderProfiler(a) {
    return `${prompt(a)}${table(a.rows,a.columns)}<button class="button primary small" type="button" data-profile>${t('Run quality profile','Quality profile চালান')}</button>${resultBox()}`;
  }
  function renderFrequency(a) {
    return `${prompt(a)}<div class="value-chips">${a.values.map(v=>`<span>${v}</span>`).join('')}</div><button class="button primary small" type="button" data-frequency>${t('Build frequency table','Frequency table তৈরি করুন')}</button>${resultBox()}`;
  }
  function renderChecklist(a) {
    const items=a.items || a.checks || a.steps || a.fields || a.checks_en || [];
    return `${prompt(a)}${formulaBadge(a)}<div class="activity-checklist">${items.map(x=>`<label><input type="checkbox"><span>${esc(Array.isArray(x)?x[0]:x)}</span></label>`).join('')}</div><div class="checklist-progress"><span data-checklist-count>0/${items.length}</span></div>${reveal('Complete every item and write one sentence of evidence for each. Record anything you cannot verify.','প্রতিটি item complete করুন এবং evidence-এর এক sentence লিখুন। যা verify করতে পারেননি তা record করুন।')}`;
  }
  function renderQuestion(a) {
    const items=a.items || [];
    return `${prompt(a)}${formulaBadge(a)}${items.length?`<div class="prompt-list">${items.map(x=>`<span>${esc(x.text||x)}</span>`).join('')}</div>`:''}<textarea class="activity-textarea" rows="6" placeholder="${t('Write your response…','Response লিখুন…')}"></textarea>${reveal((a.hints_en||['Name the input','Apply the rule','Validate the output']).join(' · '),(a.hints_bn||a.hints_en||[]).join(' · '))}`;
  }
  function renderReshape(a) {
    return `${prompt(a)}${table(a.wide,['branch',...a.months])}<button class="button primary small" type="button" data-reshape>${t('Show long form','Long form দেখুন')}</button>${resultBox()}`;
  }

  function renderExcelDemo(a) {
    const op=a.operation;
    if(['workflow','interface','sheet-plan','navigation','find-special','checklist','project-checklist','dashboard','performance'].includes(op)) return renderChecklist(a);
    if(op==='cell-address') return `${prompt(a)}${formulaBadge(a)}${table(a.grid)}<div class="excel-control-row"><select data-excel-select>${a.targets.map(x=>`<option>${esc(x)}</option>`).join('')}</select>${runButton('Locate range')}</div>${resultBox()}`;
    if(op==='type-check') return `${prompt(a)}${formulaBadge(a)}<div class="classify-grid">${a.values.map((v,i)=>`<div class="classify-row"><span>${esc(v)}</span><select data-type-answer="${esc(a.types[i])}"><option value="">Choose type…</option>${a.types.map(x=>`<option value="${esc(x)}">${esc(x)}</option>`).join('')}</select><b></b></div>`).join('')}</div>${runButton('Check types')}${resultBox()}`;
    if(op==='fill-series') return `${prompt(a)}${formulaBadge(a)}<div class="excel-control-grid"><label>Start<input type="number" data-x-start value="${a.start}"></label><label>Step<input type="number" data-x-step value="${a.step}"></label><label>Count<input type="number" min="2" max="20" data-x-count value="${a.count}"></label></div>${runButton('Fill series')}${resultBox()}`;
    if(op==='import-preview') return `${prompt(a)}${formulaBadge(a)}${table(a.rows.slice(1),a.rows[0])}<div class="excel-control-row"><label>ID type <select data-import-id><option>General</option><option>Text</option></select></label><label>Date locale <select data-import-date><option>Automatic</option><option>DMY</option><option>MDY</option></select></label></div>${runButton('Validate import')}${resultBox()}`;
    if(op==='sort-filter') return `${prompt(a)}${formulaBadge(a)}<div data-excel-source>${table(a.rows.slice(1),a.rows[0])}</div><div class="excel-control-row">${a.mode==='sort'?'<select data-sort-field><option value="0">Region</option><option value="2">Revenue</option></select><select data-sort-direction><option value="asc">Ascending</option><option value="desc">Descending</option></select>':'<select data-filter-region><option value="all">All regions</option>'+[...new Set(a.rows.slice(1).map(r=>r[0]))].map(x=>`<option>${esc(x)}</option>`).join('')+'</select><input type="number" data-filter-min value="1000" aria-label="Minimum revenue">'}</div>${runButton(a.mode==='sort'?'Sort rows':'Apply filter')}${resultBox()}`;
    if(op==='table-expand') return `${prompt(a)}${formulaBadge(a)}<div data-table-demo>${table(a.rows.slice(1),a.rows[0])}</div>${runButton('Add a new row')}${resultBox()}`;
    if(op==='validation') return `${prompt(a)}${formulaBadge(a)}<div class="excel-control-row"><select data-validation-value>${a.options.map(x=>`<option>${esc(x)}</option>`).join('')}<option>Finished</option></select></div>${runButton('Test entry')}${resultBox()}`;
    if(op==='reference-copy') return `${prompt(a)}${formulaBadge(a)}<div class="excel-control-grid"><label>First revenue<input type="number" data-ref-revenue value="1000"></label><label>Rate<input type="number" step="0.01" data-ref-rate value="0.05"></label></div>${runButton('Copy formula down')}${resultBox()}`;
    if(['arithmetic','summary','counts','rounding','if','errors','sumifs','countifs','averageifs','margin','descriptive'].includes(op)) return `${prompt(a)}${formulaBadge(a)}<div class="excel-control-row"><label>${t('Change one input','একটি input বদলান')}<input type="number" data-formula-adjust value="0" step="1"></label></div>${runButton('Calculate')}${resultBox()}`;
    if(op==='text-clean') return `${prompt(a)}${formulaBadge(a)}<div class="excel-control-grid">${a.values.map((v,i)=>`<label>Value ${i+1}<input data-text-value value="${esc(v)}"></label>`).join('')}</div>${runButton('Clean text')}${resultBox()}`;
    if(op==='text-extract') return `${prompt(a)}${formulaBadge(a)}<label class="exercise-input">Text<input data-text-value value="${esc(a.value)}"></label>${runButton('Extract parts')}${resultBox()}`;
    if(op==='text-join') return `${prompt(a)}${formulaBadge(a)}<div class="excel-control-grid">${a.values.map((v,i)=>`<label>Part ${i+1}<input data-text-value value="${esc(v)}"></label>`).join('')}</div><label>Delimiter<input data-delimiter value="${esc(a.delimiter)}"></label>${runButton('Join text')}${resultBox()}`;
    if(op==='text-split') return `${prompt(a)}${formulaBadge(a)}<label class="exercise-input">Text<input data-text-value value="${esc(a.value)}"></label><label>Delimiter<input data-delimiter value="${esc(a.delimiter)}"></label>${runButton('Split text')}${resultBox()}`;
    if(op==='date-demo') return `${prompt(a)}${formulaBadge(a)}<div class="excel-control-grid"><label>Start<input type="date" data-date-start value="${a.start}"></label><label>End<input type="date" data-date-end value="${a.end}"></label></div>${runButton('Calculate dates')}${resultBox()}`;
    if(['lookup','lookup-audit'].includes(op)) return `${prompt(a)}${formulaBadge(a)}${op==='lookup'?`<div class="excel-control-row"><select data-lookup>${a.keys.map(x=>`<option>${esc(x)}</option>`).join('')}</select></div>`:`<div class="value-chips">${a.keys.map(x=>`<span>${esc(x)}</span>`).join('')}</div>`}${runButton(op==='lookup'?'Run lookup':'Audit keys')}${resultBox()}`;
    if(op==='dynamic-array') return `${prompt(a)}${formulaBadge(a)}<div class="value-chips">${(a.values||[]).map(x=>`<span>${esc(x)}</span>`).join('')}</div>${runButton('Return dynamic array')}${resultBox()}`;
    if(op==='conditional-format') return `${prompt(a)}${formulaBadge(a)}<div class="value-chips conditional-demo">${a.values.map(x=>`<span data-value="${x}">${x}</span>`).join('')}</div><label>Threshold<input type="number" data-threshold value="${a.threshold}"></label>${runButton('Apply rule')}${resultBox()}`;
    if(op==='correlation') return `${prompt(a)}${formulaBadge(a)}${table(a.x.map((x,i)=>[x,a.y[i]]),['X','Y'])}${runButton('Calculate correlation')}${resultBox()}`;
    if(op==='what-if') return `${prompt(a)}${formulaBadge(a)}<div class="excel-control-grid"><label>Price<input type="number" data-w-price value="${a.price}"></label><label>Variable cost<input type="number" data-w-cost value="${a.variable_cost}"></label><label>Fixed cost<input type="number" data-w-fixed value="${a.fixed_cost}"></label></div>${runButton('Find break-even')}${resultBox()}`;
    if(op==='pivot') return `${prompt(a)}${formulaBadge(a)}${table(a.rows,['Group','Category','Value'])}${runButton('Build Pivot summary')}${resultBox()}`;
    if(op==='chart-choice') return `${prompt(a)}${formulaBadge(a)}<div class="activity-choice-grid">${a.questions.map((q,i)=>`<button type="button" class="activity-choice" data-chart-question="${i}">${esc(q)}</button>`).join('')}</div>${resultBox()}`;
    if(op==='power-query') return `${prompt(a)}${formulaBadge(a)}<ol class="query-pipeline">${a.steps.map((x,i)=>`<li><span>${i+1}</span><strong>${esc(x)}</strong></li>`).join('')}</ol>${runButton('Run transformation preview')}${resultBox()}`;
    if(op==='data-model') return `${prompt(a)}${formulaBadge(a)}<div class="model-diagram">${Object.entries(a.tables).map(([name,cols])=>`<article><strong>${esc(name)}</strong>${cols.map(c=>`<span class="${c===a.key?'key':''}">${esc(c)}</span>`).join('')}</article>`).join('')}<b>↔</b></div>${runButton('Validate relationship')}${resultBox()}`;
    if(op==='dax') return `${prompt(a)}${formulaBadge(a)}${table(a.rows,['Region','Revenue','Cost'])}${runButton('Evaluate measures')}${resultBox()}`;
    if(op==='analysis-toolpak') return `${prompt(a)}${formulaBadge(a)}<div class="value-chips">${a.values.map(x=>`<span>${x}</span>`).join('')}</div>${runButton('Generate statistics')}${resultBox()}`;
    if(op==='audit') return `${prompt(a)}${formulaBadge(a)}<div class="mini-scorecards"><span><small>Source</small><strong>${a.source_total.toLocaleString()}</strong></span><span><small>Report</small><strong>${a.report_total.toLocaleString()}</strong></span></div>${runButton('Run control check')}${resultBox()}`;
    return renderQuestion(a);
  }

  function computeExcel(a, root) {
    const op=a.operation; let html='';
    if(op==='cell-address') { const v=root.querySelector('[data-excel-select]').value; html=`<strong>${esc(v)}</strong> ${t('selected. A cell uses column letter + row number; a range uses start:end.','selected। Cell column letter + row number; range start:end ব্যবহার করে।')}`; }
    else if(op==='type-check') { let right=0; root.querySelectorAll('[data-type-answer]').forEach(s=>{const ok=s.value===s.dataset.typeAnswer;s.parentElement.classList.toggle('correct',ok);if(ok)right++;});html=`<strong>${right}/${a.values.length}</strong> correct`;
    }
    else if(op==='fill-series'){const start=+root.querySelector('[data-x-start]').value,step=+root.querySelector('[data-x-step]').value,count=Math.max(2,Math.min(20,+root.querySelector('[data-x-count]').value));html=`<div class="value-chips">${Array.from({length:count},(_,i)=>`<span>${start+i*step}</span>`).join('')}</div>`;}
    else if(op==='import-preview'){const id=root.querySelector('[data-import-id]').value,date=root.querySelector('[data-import-date]').value;html=(id==='Text'&&date==='DMY')?'<strong>Ready to load.</strong> Leading zeros and DMY dates are protected.':'<strong>Review settings.</strong> Choose Text for the identifier and DMY for these dates.';}
    else if(op==='sort-filter'){let rows=a.rows.slice(1); if(a.mode==='sort'){const f=+root.querySelector('[data-sort-field]').value,d=root.querySelector('[data-sort-direction]').value;rows.sort((x,y)=>{const r=typeof x[f]==='number'?x[f]-y[f]:String(x[f]).localeCompare(String(y[f]));return d==='asc'?r:-r;});}else{const reg=root.querySelector('[data-filter-region]').value,min=+root.querySelector('[data-filter-min]').value;rows=rows.filter(r=>(reg==='all'||r[0]===reg)&&Number(r[2])>=min);} html=table(rows,a.rows[0])+`<p><strong>${rows.length}</strong> visible rows</p>`;}
    else if(op==='table-expand'){const rows=[...a.rows.slice(1),['2026-07-03','North',1400]];html=table(rows,a.rows[0])+'<p>New row is inside the expanding table source.</p>';}
    else if(op==='validation'){const v=root.querySelector('[data-validation-value]').value;html=a.options.includes(v)?`<strong>Accepted:</strong> ${esc(v)}`:`<strong>Rejected:</strong> ${esc(v)} is not in the controlled list.`;}
    else if(op==='reference-copy'){const rev=+root.querySelector('[data-ref-revenue]').value,rate=+root.querySelector('[data-ref-rate]').value;html=table(Array.from({length:a.rows},(_,i)=>[i+2,rev+i*100,(rev+i*100)*rate,`=B${i+2}*$H$2`]),['Row','Revenue','Commission','Copied formula']);}
    else if(op==='arithmetic'){const adj=+root.querySelector('[data-formula-adjust]').value,r=a.values[0]+adj,c=a.values[1];html=`Revenue ${r.toFixed(2)} − Cost ${c.toFixed(2)} = <strong>${(r-c).toFixed(2)}</strong>; Margin ${r?((r-c)/r*100).toFixed(1):'0.0'}%`;}
    else if(op==='summary'){const adj=+root.querySelector('[data-formula-adjust]').value,vals=a.values.map((v,i)=>i===0?v+adj:v);html=`SUM <strong>${vals.reduce((s,v)=>s+v,0).toFixed(2)}</strong> · AVERAGE <strong>${mean(vals).toFixed(2)}</strong> · MIN ${Math.min(...vals)} · MAX ${Math.max(...vals)}`;}
    else if(op==='counts'){const vals=a.values;html=`COUNT <strong>${vals.filter(v=>typeof v==='number').length}</strong> · COUNTA <strong>${vals.filter(v=>v!==''&&v!==null).length}</strong> · COUNTBLANK <strong>${vals.filter(v=>v===''||v===null).length}</strong>`;}
    else if(op==='rounding'){const adj=+root.querySelector('[data-formula-adjust]').value,v=a.value+adj/10;html=`Value ${v.toFixed(4)} · ROUND ${Math.round(v)} · ROUNDUP ${Math.ceil(v)} · ROUNDDOWN ${Math.floor(v)}`;}
    else if(op==='if'){const adj=+root.querySelector('[data-formula-adjust]').value,v=a.value+adj;const label=v>=a.thresholds[1]?'High':v>=a.thresholds[0]?'Medium':'Standard';html=`Value <strong>${v}</strong> → <strong>${label}</strong>`;}
    else if(op==='errors'){const adj=+root.querySelector('[data-formula-adjust]').value,d=a.denominator+adj;html=d===0?'Raw result: <strong>#DIV/0!</strong> · IFERROR result: <strong>0</strong>':`Result: <strong>${(a.numerator/d).toFixed(2)}</strong>`;}
    else if(op==='sumifs'){const rows=a.rows.filter(r=>r[0]===a.criteria);html=`SUMIFS for ${a.criteria}: <strong>${rows.reduce((s,r)=>s+r[2],0).toFixed(2)}</strong>`;}
    else if(op==='countifs'){html=`Matching rows: <strong>${a.rows.filter(r=>r[0]===a.status&&r[1]>=a.min).length}</strong>`;}
    else if(op==='averageifs'){const vals=a.rows.filter(r=>r[0]===a.criteria).map(r=>r[1]);html=`Average for ${a.criteria}: <strong>${mean(vals).toFixed(2)}</strong> from ${vals.length} rows`;
    }
    else if(op==='margin'){html=`Revenue ${a.revenue} · Cost ${a.cost} · Profit ${a.revenue-a.cost} · Margin <strong>${((a.revenue-a.cost)/a.revenue*100).toFixed(1)}%</strong>`;}
    else if(op==='descriptive'){const v=a.values;html=`Count ${v.length} · Mean <strong>${mean(v).toFixed(2)}</strong> · Median <strong>${median(v).toFixed(2)}</strong> · STDEV.S ${stdev(v).toFixed(2)} · Min ${Math.min(...v)} · Max ${Math.max(...v)}`;}
    else if(op==='text-clean'){const vals=[...root.querySelectorAll('[data-text-value]')].map(i=>i.value);html=table(vals.map(v=>[v,v.replace(/\u00a0/g,' ').replace(/\s+/g,' ').trim(),Number(v.replace(/,/g,''))||'—']),['Original','Clean text','Numeric conversion']);}
    else if(op==='text-extract'){const v=root.querySelector('[data-text-value]').value;html=`LEFT: <strong>${esc(v.slice(0,a.left))}</strong> · MID: <strong>${esc(v.slice(a.mid[0]-1,a.mid[0]-1+a.mid[1]))}</strong> · RIGHT: <strong>${esc(v.slice(-a.right))}</strong> · LEN: ${v.length}`;}
    else if(op==='text-join'){const vals=[...root.querySelectorAll('[data-text-value]')].map(i=>i.value).filter(Boolean),d=root.querySelector('[data-delimiter]').value;html=`<strong>${esc(vals.join(d))}</strong>`;}
    else if(op==='text-split'){const v=root.querySelector('[data-text-value]').value,d=root.querySelector('[data-delimiter]').value;html=`<div class="value-chips">${v.split(d).map(x=>`<span>${esc(x)}</span>`).join('')}</div>`;}
    else if(op==='date-demo'){const s=new Date(root.querySelector('[data-date-start]').value+'T00:00:00'),e=new Date(root.querySelector('[data-date-end]').value+'T00:00:00');let days=Math.round((e-s)/86400000);let work=0;for(let d=new Date(s);d<=e;d.setDate(d.getDate()+1)){if(d.getDay()!==0&&d.getDay()!==6&&!((a.holidays||[]).includes(d.toISOString().slice(0,10))))work++;}html=`Calendar difference: <strong>${days} days</strong> · Inclusive working days: <strong>${work}</strong>`;}
    else if(op==='lookup'){const key=root.querySelector('[data-lookup]').value,idx=a.keys.indexOf(key);html=idx>=0?`${esc(key)} → <strong>${esc(a.values[idx])}</strong>`:'<strong>Not found</strong>';}
    else if(op==='lookup-audit'){const counts={};a.keys.forEach(k=>counts[k]=(counts[k]||0)+1);html=table(Object.entries(counts).map(([k,c])=>[k,c,c>1?'Duplicate':'Unique']),['Key','Count','Status']);}
    else if(op==='dynamic-array'){let out=a.values||[];if(a.criteria)out=a.rows.filter(r=>r[0]===a.criteria.region&&r[2]>=a.criteria.min).map(r=>r.join(' | '));else out=[...new Set(out)].sort();html=`<div class="value-chips">${out.map(x=>`<span>${esc(x)}</span>`).join('')}</div><p>${out.length} spilled result(s)</p>`;}
    else if(op==='conditional-format'){const threshold=+root.querySelector('[data-threshold]').value;root.querySelectorAll('[data-value]').forEach(el=>el.classList.toggle('excel-highlight',+el.dataset.value>=threshold));html=`Highlighted values greater than or equal to <strong>${threshold}</strong>.`;}
    else if(op==='correlation'){html=`Pearson CORREL: <strong>${corr(a.x,a.y).toFixed(4)}</strong>. This describes linear association, not causation.`;}
    else if(op==='what-if'){const p=+root.querySelector('[data-w-price]').value,c=+root.querySelector('[data-w-cost]').value,f=+root.querySelector('[data-w-fixed]').value;html=p<=c?'<strong>No finite break-even:</strong> contribution per unit is not positive.':`Break-even units: <strong>${Math.ceil(f/(p-c)).toLocaleString()}</strong>`;}
    else if(op==='pivot'){const groups={};a.rows.forEach(r=>{groups[r[0]]??={};groups[r[0]][r[1]]=(groups[r[0]][r[1]]||0)+r[2];});const cats=[...new Set(a.rows.map(r=>r[1]))];html=table(Object.entries(groups).map(([g,v])=>[g,...cats.map(c=>v[c]||0),Object.values(v).reduce((s,x)=>s+x,0)]),['Group',...cats,'Total']);}
    else if(op==='power-query'){html=`<strong>${a.steps.length} applied steps</strong><p>Preview complete. In Excel, refresh would rerun these steps against the current source.</p>`;}
    else if(op==='data-model'){const left=Object.keys(a.tables)[0],right=Object.keys(a.tables)[1];html=`Validated conceptual relationship: <strong>${esc(left)}[*] → ${esc(right)}[1]</strong> on ${esc(a.key)}. Confirm the key is unique on the one side.`;}
    else if(op==='dax'){const rev=a.rows.reduce((s,r)=>s+r[1],0),cost=a.rows.reduce((s,r)=>s+r[2],0);html=`Total Revenue <strong>${rev}</strong> · Gross Profit <strong>${rev-cost}</strong> · Margin <strong>${((rev-cost)/rev*100).toFixed(1)}%</strong>`;}
    else if(op==='analysis-toolpak'){html=`Count ${a.values.length} · Mean <strong>${mean(a.values).toFixed(2)}</strong> · Median ${median(a.values).toFixed(2)} · STDEV.S ${stdev(a.values).toFixed(2)}`;}
    else if(op==='audit'){const diff=a.source_total-a.report_total;html=diff===0?'<strong class="success-text">OK — totals reconcile.</strong>':`<strong class="danger-text">CHECK — difference ${diff.toLocaleString()}</strong>`;}
    else html='<strong>Activity complete.</strong> Explain the result and record one validation check.';
    root.querySelector('.activity-result').innerHTML=html;
  }

  function bindCommon(root) {
    root.querySelectorAll('[data-copy-code]').forEach(btn=>btn.addEventListener('click',async()=>{const code=btn.parentElement.querySelector('code')?.textContent||'';try{await navigator.clipboard.writeText(code);btn.textContent='Copied';}catch{btn.textContent='Select & copy';}}));
    root.querySelector('[data-reveal-guidance]')?.addEventListener('click',e=>e.currentTarget.nextElementSibling.classList.toggle('hidden'));
    root.querySelectorAll('.activity-checklist input').forEach(input=>input.addEventListener('change',()=>{const all=[...root.querySelectorAll('.activity-checklist input')];const out=root.querySelector('[data-checklist-count]');if(out)out.textContent=`${all.filter(x=>x.checked).length}/${all.length}`;}));
  }

  function renderActivity() {
    const a=chapter.activity; let html='';
    if(a.type==='sql-playground' && window.DLHSQLPractice){ activityRoot.innerHTML='<div class="try-panel"><div id="sql-chapter-playground"></div></div>'; window.DLHSQLPractice.renderActivity(activityRoot.querySelector('#sql-chapter-playground'),a); return; }
    if(a.type==='excel-demo') html=renderExcelDemo(a);
    else if(a.type==='classify' || a.type==='bias-finder' || a.type==='issue-finder') html=renderClassify(a);
    else if(a.type==='table-inspector') html=renderTable(a);
    else if(a.type==='structure-choice') html=renderChoice(a);
    else if(a.type==='sampling-simulator') html=renderSampling(a);
    else if(a.type==='data-profiler') html=renderProfiler(a);
    else if(a.type==='frequency-builder') html=renderFrequency(a);
    else if(a.type==='reshape') html=renderReshape(a);
    else if(['source-evaluator','eda-checklist','documentation-checklist','ethics-review','project-checklist','metric-builder'].includes(a.type)) html=renderChecklist(a);
    else html=renderQuestion(a);
    activityRoot.innerHTML=`<div class="try-panel">${html}</div>`;
    bindCommon(activityRoot);
    activityRoot.querySelector('[data-run-excel]')?.addEventListener('click',()=>computeExcel(a,activityRoot));
    activityRoot.querySelector('[data-check-activity]')?.addEventListener('click',()=>{let right=0,total=0;activityRoot.querySelectorAll('.classify-row').forEach(row=>{const select=row.querySelector('select');const correct=select.value===select.dataset.answer;row.classList.toggle('correct',correct);row.classList.toggle('incorrect',!correct&&select.value);row.querySelector('b').textContent=select.value?(correct?'✓':'×'):'';if(select.value){total++;if(correct)right++;}});activityRoot.querySelector('.activity-result').innerHTML=`<strong>${right}/${total}</strong> ${t('checked correctly','সঠিক')}`;});
    activityRoot.querySelectorAll('[data-choice]').forEach(btn=>btn.addEventListener('click',()=>{const ok=btn.dataset.choice===chapter.activity.answer;activityRoot.querySelectorAll('[data-choice]').forEach(b=>b.classList.remove('correct','incorrect'));btn.classList.add(ok?'correct':'incorrect');activityRoot.querySelector('.activity-result').textContent=ok?t('Correct.','সঠিক।'):t('Try the other option and compare the structure.','অন্য option try করে structure compare করুন।');}));
    activityRoot.querySelectorAll('[data-chart-question]').forEach(btn=>btn.addEventListener('click',()=>{const choices=['Bar or column chart','Line chart','Histogram','Scatter plot'];activityRoot.querySelector('.activity-result').innerHTML=`Recommended: <strong>${choices[+btn.dataset.chartQuestion]}</strong>`;}));
    activityRoot.querySelector('[data-random-sample]')?.addEventListener('click',()=>{const p=[...chapter.activity.population].sort(()=>Math.random()-.5).slice(0,chapter.activity.sample_size);activityRoot.querySelector('.sample-output').innerHTML=`<p>Sample: ${p.join(', ')}</p><p>Sample mean: <strong>${mean(p).toFixed(2)}</strong></p>`;});
    activityRoot.querySelector('[data-convenience-sample]')?.addEventListener('click',()=>{const p=chapter.activity.population.slice(0,chapter.activity.sample_size);activityRoot.querySelector('.sample-output').innerHTML=`<p>First values: ${p.join(', ')}</p><p>Mean: <strong>${mean(p).toFixed(2)}</strong></p><small>${t('Convenience selection can systematically miss later values.','Convenience selection later value miss করতে পারে।')}</small>`;});
    activityRoot.querySelector('[data-profile]')?.addEventListener('click',()=>{const rows=chapter.activity.rows;const blanks=rows.flat().filter(v=>v==='').length;const duplicates=rows.length-new Set(rows.map(r=>JSON.stringify(r))).size;const invalid=rows.filter(r=>String(r[1]).includes('not-a-date')||Number(r[2])<0).length;activityRoot.querySelector('.activity-result').innerHTML=`<div class="mini-scorecards"><span><strong>${blanks}</strong> blanks</span><span><strong>${duplicates}</strong> duplicate rows</span><span><strong>${invalid}</strong> invalid rows</span></div>`;});
    activityRoot.querySelector('[data-frequency]')?.addEventListener('click',()=>{const counts={};chapter.activity.values.forEach(v=>counts[v]=(counts[v]||0)+1);activityRoot.querySelector('.activity-result').innerHTML=`<table><thead><tr><th>Value</th><th>Frequency</th><th>Relative</th></tr></thead><tbody>${Object.entries(counts).map(([v,c])=>`<tr><td>${v}</td><td>${c}</td><td>${(c/chapter.activity.values.length*100).toFixed(1)}%</td></tr>`).join('')}</tbody></table>`;});
    activityRoot.querySelector('[data-reshape]')?.addEventListener('click',()=>{const rows=[];chapter.activity.wide.forEach(r=>chapter.activity.months.forEach((m,i)=>rows.push([r[0],m,r[i+1]])));activityRoot.querySelector('.activity-result').innerHTML=table(rows,['branch','month','sales']);});
  }
  function renderExercises(){exerciseRoot.innerHTML=chapter.exercises.map((x,i)=>T.renderExercise(x,i,'chapter')).join('');T.bindExercises(exerciseRoot,chapter.exercises);}
  function syncComplete(){const yes=T.isComplete(tutorial.id,chapter.id);[document.getElementById('chapter-complete'),document.getElementById('chapter-complete-bottom')].forEach(btn=>{if(btn){btn.textContent=yes?t('Completed ✓','সম্পন্ন ✓'):t('Mark complete','Complete mark করুন');btn.classList.toggle('completed',yes);}});}
  [document.getElementById('chapter-complete'),document.getElementById('chapter-complete-bottom')].forEach(btn=>btn?.addEventListener('click',()=>{T.toggleComplete(tutorial.id,chapter.id);syncComplete();}));
  renderActivity(); renderExercises(); syncComplete();
  window.addEventListener('dlh:language',()=>{renderActivity();renderExercises();syncComplete();});
})();
