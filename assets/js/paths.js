(() => {
  const { DATA, topicMap, t, escapeHtml, pathProgress, getCompleted } = window.SLH;
  const root=document.getElementById('paths-grid');
  function render(){
    const completed=getCompleted();
    root.innerHTML=DATA.paths.map(path=>{
      const p=pathProgress(path);
      const steps=path.topics.map((id,i)=>{ const topic=topicMap[id]; if(!topic)return''; return `<a class="path-step ${completed.has(id)?'done':''}" href="/${topic.url}"><span class="path-step-number">${completed.has(id)?'✓':i+1}</span><span><strong>${escapeHtml(t(topic.title_en,topic.title_bn))}</strong><small class="muted">${topic.minutes} ${t('min','মিনিট')} · ${escapeHtml(t(topic.difficulty,({Beginner:'বিগিনার',Intermediate:'ইন্টারমিডিয়েট',Advanced:'অ্যাডভান্সড'})[topic.difficulty]))}</small></span></a>`; }).join('');
      return `<section class="path-detail" id="${path.id}"><div class="path-detail-header"><div><span class="eyebrow">${p.total} ${t('steps','ধাপ')}</span><h2>${escapeHtml(t(path.title_en,path.title_bn))}</h2><p class="muted">${escapeHtml(t(path.description_en,path.description_bn))}</p></div><div><strong>${p.percent}%</strong> ${t('complete','সম্পন্ন')}</div></div><div class="progress-track"><span style="width:${p.percent}%"></span></div><div class="path-lessons">${steps}</div></section>`;
    }).join('');
    if(location.hash){ setTimeout(()=>document.querySelector(location.hash)?.scrollIntoView({behavior:'smooth'}),50); }
  }
  window.addEventListener('slh:language',render); window.addEventListener('slh:progress',render); render();
})();
