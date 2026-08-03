(() => {
  const { DATA, t, escapeHtml } = window.SLH;
  const input=document.getElementById('glossary-search'); const list=document.getElementById('glossary-list');
  function render(){
    const q=input.value.trim().toLowerCase();
    const items=DATA.glossary.filter(x=>!q||[x.term_en,x.term_bn,x.definition_en,x.definition_bn].join(' ').toLowerCase().includes(q)).sort((a,b)=>t(a.term_en,a.term_bn).localeCompare(t(b.term_en,b.term_bn)));
    list.innerHTML=items.map(x=>`<dl class="glossary-item"><dt>${escapeHtml(t(x.term_en,x.term_bn))}</dt><dd>${escapeHtml(t(x.definition_en,x.definition_bn))}</dd></dl>`).join('') || `<div class="topic-card"><h2>${t('No matching term','মিল পাওয়া term নেই')}</h2></div>`;
  }
  input.addEventListener('input',render); window.addEventListener('slh:language',render); render();
})();
