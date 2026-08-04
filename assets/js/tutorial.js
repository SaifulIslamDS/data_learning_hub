(() => {
  'use strict';
  const T=window.DLHTutorial; if(!T) return;
  const tutorial=T.getTutorial(); const chapter=tutorial.chapters.find(ch=>ch.id===document.body.dataset.chapter); if(!chapter) return;
  const activityRoot=document.getElementById('tutorial-activity');
  const exerciseRoot=document.getElementById('chapter-exercises');
  const esc=T.escapeHtml;
  const t=T.t;
  const mean=arr=>arr.reduce((a,b)=>a+Number(b),0)/arr.length;
  function prompt(activity) { return `<p class="activity-prompt">${esc(t(activity.prompt_en,activity.prompt_bn))}</p>`; }
  function reveal(textEn,textBn=textEn) { return `<button class="button small ghost" type="button" data-reveal-guidance>${t('Reveal guidance','Guidance দেখুন')}</button><div class="activity-guidance hidden">${esc(t(textEn,textBn))}</div>`; }
  function renderClassify(a) {
    const types=[...new Set(a.items.map(x=>x.answer))];
    return `${prompt(a)}<div class="classify-grid">${a.items.map((item,i)=>`<div class="classify-row"><span>${esc(item.text)}</span><select data-answer="${esc(item.answer)}"><option value="">${t('Choose…','বেছে নিন…')}</option>${types.map(x=>`<option value="${esc(x)}">${esc(x)}</option>`).join('')}</select><b></b></div>`).join('')}</div><button class="button primary small" data-check-activity type="button">${t('Check classification','Classification check করুন')}</button><div class="activity-result" aria-live="polite"></div>`;
  }
  function renderTable(a) {
    const rows=a.rows.map(row=>`<tr>${row.map(v=>`<td>${esc(v)}</td>`).join('')}</tr>`).join('');
    return `${prompt(a)}<div class="table-wrap"><table><thead><tr>${a.columns.map(c=>`<th>${esc(c)}</th>`).join('')}</tr></thead><tbody>${rows}</tbody></table></div>${reveal('Ask: What does one row represent? Which field is the identifier? Which columns are categories and which are quantities?','জিজ্ঞেস করুন: এক row কী represent করে? Identifier কোন field? কোন column category এবং কোনটি quantity?')}`;
  }
  function renderChoice(a) {
    return `${prompt(a)}<div class="activity-choice-grid">${a.options.map(o=>`<button type="button" data-choice="${o.id}" class="activity-choice">${esc(o.label)}</button>`).join('')}</div><div class="activity-result" aria-live="polite"></div>`;
  }
  function renderSampling(a) {
    return `${prompt(a)}<div class="sampling-demo"><p>${t('Population mean','Population mean')}: <strong>${mean(a.population).toFixed(2)}</strong></p><button class="button primary small" type="button" data-random-sample>${t('Draw random sample','Random sample নিন')}</button><button class="button ghost small" type="button" data-convenience-sample>${t('Take first values','First value নিন')}</button><div class="sample-output"></div></div>`;
  }
  function renderProfiler(a) {
    const rows=a.rows.map(row=>`<tr>${row.map(v=>`<td>${esc(v===''?'(blank)':v)}</td>`).join('')}</tr>`).join('');
    return `${prompt(a)}<div class="table-wrap"><table><thead><tr>${a.columns.map(c=>`<th>${esc(c)}</th>`).join('')}</tr></thead><tbody>${rows}</tbody></table></div><button class="button primary small" type="button" data-profile>${t('Run quality profile','Quality profile চালান')}</button><div class="activity-result"></div>`;
  }
  function renderFrequency(a) {
    return `${prompt(a)}<div class="value-chips">${a.values.map(v=>`<span>${v}</span>`).join('')}</div><button class="button primary small" type="button" data-frequency>${t('Build frequency table','Frequency table তৈরি করুন')}</button><div class="activity-result"></div>`;
  }
  function renderChecklist(a) {
    const items=a.items || a.checks || a.steps || a.fields || a.checks_en || [];
    return `${prompt(a)}<div class="activity-checklist">${items.map((x,i)=>`<label><input type="checkbox"><span>${esc(Array.isArray(x)?x[0]:x)}</span></label>`).join('')}</div>${reveal('Complete every item, write one sentence of evidence for each, and record anything you cannot verify.','প্রতিটি item complete করুন, evidence-এর এক sentence লিখুন এবং যা verify করতে পারেননি তা record করুন।')}`;
  }
  function renderQuestion(a) {
    const items=a.items || [];
    return `${prompt(a)}${items.length?`<div class="prompt-list">${items.map(x=>`<span>${esc(x.text||x)}</span>`).join('')}</div>`:''}<textarea class="activity-textarea" rows="6" placeholder="${t('Write your response…','Response লিখুন…')}"></textarea>${reveal((a.hints_en||['Name the population or entity','Name a measure','Add a time period and comparison']).join(' · '),(a.hints_bn||a.hints_en||[]).join(' · '))}`;
  }
  function renderReshape(a) {
    return `${prompt(a)}<div class="table-wrap"><table><thead><tr><th>branch</th>${a.months.map(m=>`<th>${m}</th>`).join('')}</tr></thead><tbody>${a.wide.map(r=>`<tr>${r.map(v=>`<td>${v}</td>`).join('')}</tr>`).join('')}</tbody></table></div><button class="button primary small" type="button" data-reshape>${t('Show long form','Long form দেখুন')}</button><div class="activity-result"></div>`;
  }
  function renderActivity() {
    const a=chapter.activity; let html='';
    if(a.type==='classify' || a.type==='bias-finder' || a.type==='issue-finder') html=renderClassify(a);
    else if(a.type==='table-inspector') html=renderTable(a);
    else if(a.type==='structure-choice') html=renderChoice(a);
    else if(a.type==='sampling-simulator') html=renderSampling(a);
    else if(a.type==='data-profiler') html=renderProfiler(a);
    else if(a.type==='frequency-builder') html=renderFrequency(a);
    else if(a.type==='reshape') html=renderReshape(a);
    else if(['source-evaluator','eda-checklist','documentation-checklist','ethics-review','project-checklist','metric-builder'].includes(a.type)) html=renderChecklist(a);
    else html=renderQuestion(a);
    activityRoot.innerHTML=`<div class="try-panel">${html}</div>`;
    activityRoot.querySelector('[data-reveal-guidance]')?.addEventListener('click',e=>e.currentTarget.nextElementSibling.classList.toggle('hidden'));
    activityRoot.querySelector('[data-check-activity]')?.addEventListener('click',()=>{let right=0,total=0;activityRoot.querySelectorAll('.classify-row').forEach(row=>{const select=row.querySelector('select');const correct=select.value===select.dataset.answer;row.classList.toggle('correct',correct);row.classList.toggle('incorrect',!correct&&select.value);row.querySelector('b').textContent=select.value?(correct?'✓':'×'):'';if(select.value){total++;if(correct)right++;}});activityRoot.querySelector('.activity-result').innerHTML=`<strong>${right}/${total}</strong> ${t('checked correctly','সঠিক')}`;});
    activityRoot.querySelectorAll('[data-choice]').forEach(btn=>btn.addEventListener('click',()=>{const ok=btn.dataset.choice===chapter.activity.answer;activityRoot.querySelectorAll('[data-choice]').forEach(b=>b.classList.remove('correct','incorrect'));btn.classList.add(ok?'correct':'incorrect');activityRoot.querySelector('.activity-result').textContent=ok?t('Correct. This structure keeps month as a variable.','সঠিক। এই structure month-কে variable রাখে।'):t('Try the other structure and think about filtering by month.','অন্য structure try করুন এবং month filter নিয়ে ভাবুন।');}));
    activityRoot.querySelector('[data-random-sample]')?.addEventListener('click',()=>{const p=[...chapter.activity.population].sort(()=>Math.random()-.5).slice(0,chapter.activity.sample_size);activityRoot.querySelector('.sample-output').innerHTML=`<p>Sample: ${p.join(', ')}</p><p>Sample mean: <strong>${mean(p).toFixed(2)}</strong></p>`;});
    activityRoot.querySelector('[data-convenience-sample]')?.addEventListener('click',()=>{const p=chapter.activity.population.slice(0,chapter.activity.sample_size);activityRoot.querySelector('.sample-output').innerHTML=`<p>First values: ${p.join(', ')}</p><p>Mean: <strong>${mean(p).toFixed(2)}</strong></p><small>${t('Convenience selection can systematically miss later values.','Convenience selection later value miss করতে পারে।')}</small>`;});
    activityRoot.querySelector('[data-profile]')?.addEventListener('click',()=>{const rows=chapter.activity.rows;const blanks=rows.flat().filter(v=>v==='').length;const duplicates=rows.length-new Set(rows.map(r=>JSON.stringify(r))).size;const invalid=rows.filter(r=>String(r[1]).includes('not-a-date')||Number(r[2])<0).length;activityRoot.querySelector('.activity-result').innerHTML=`<div class="mini-scorecards"><span><strong>${blanks}</strong> blanks</span><span><strong>${duplicates}</strong> duplicate rows</span><span><strong>${invalid}</strong> invalid rows</span></div>`;});
    activityRoot.querySelector('[data-frequency]')?.addEventListener('click',()=>{const counts={};chapter.activity.values.forEach(v=>counts[v]=(counts[v]||0)+1);activityRoot.querySelector('.activity-result').innerHTML=`<table><thead><tr><th>Value</th><th>Frequency</th><th>Relative</th></tr></thead><tbody>${Object.entries(counts).map(([v,c])=>`<tr><td>${v}</td><td>${c}</td><td>${(c/chapter.activity.values.length*100).toFixed(1)}%</td></tr>`).join('')}</tbody></table>`;});
    activityRoot.querySelector('[data-reshape]')?.addEventListener('click',()=>{const rows=[];chapter.activity.wide.forEach(r=>chapter.activity.months.forEach((m,i)=>rows.push([r[0],m,r[i+1]])));activityRoot.querySelector('.activity-result').innerHTML=`<table><thead><tr><th>branch</th><th>month</th><th>sales</th></tr></thead><tbody>${rows.map(r=>`<tr>${r.map(v=>`<td>${v}</td>`).join('')}</tr>`).join('')}</tbody></table>`;});
  }
  function renderExercises(){exerciseRoot.innerHTML=chapter.exercises.map((x,i)=>T.renderExercise(x,i,'chapter')).join('');T.bindExercises(exerciseRoot,chapter.exercises);}
  function syncComplete(){const yes=T.isComplete(tutorial.id,chapter.id);[document.getElementById('chapter-complete'),document.getElementById('chapter-complete-bottom')].forEach(btn=>{if(btn){btn.textContent=yes?t('Completed ✓','সম্পন্ন ✓'):t('Mark complete','Complete mark করুন');btn.classList.toggle('completed',yes);}});}
  [document.getElementById('chapter-complete'),document.getElementById('chapter-complete-bottom')].forEach(btn=>btn?.addEventListener('click',()=>{T.toggleComplete(tutorial.id,chapter.id);syncComplete();}));
  renderActivity(); renderExercises(); syncComplete();
  window.addEventListener('dlh:language',()=>{renderActivity();renderExercises();syncComplete();});
})();
