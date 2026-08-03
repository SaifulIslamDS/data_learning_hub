(() => {
  const { DATA, moduleMap, t, escapeHtml, toolCard } = window.SLH;
  const search = document.getElementById('tool-search');
  const filter = document.getElementById('tool-module-filter');
  const grid = document.getElementById('tools-grid');

  function options(){
    const used = [...new Set(DATA.tools.map(x=>x.module))];
    filter.innerHTML = `<option value="all">${t('All modules','সব মডিউল')}</option>` + used.map(id=>`<option value="${id}">${escapeHtml(t(moduleMap[id].title_en,moduleMap[id].title_bn))}</option>`).join('');
  }
  function render(){
    const q=search.value.trim().toLowerCase(); const m=filter.value;
    const items=DATA.tools.filter(x=>(m==='all'||x.module===m)&&(!q||[x.title_en,x.title_bn,x.description_en,x.description_bn].join(' ').toLowerCase().includes(q)));
    grid.innerHTML=items.map(toolCard).join('');
  }
  search.addEventListener('input',render); filter.addEventListener('change',render);
  window.addEventListener('slh:language',()=>{options();render();});
  options();render();
})();
