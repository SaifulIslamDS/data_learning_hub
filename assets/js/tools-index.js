(() => {
  'use strict';
  const { DATA, moduleMap, t, escapeHtml, toolCard } = window.DLH;
  const search = document.getElementById('tool-search');
  const filter = document.getElementById('tool-module-filter');
  const grid = document.getElementById('tool-grid');
  const count = document.getElementById('tool-count');
  const datasetGrid = document.getElementById('dataset-grid');
  if (!search || !filter || !grid || !count) return;

  function options() {
    const used = [...new Set(DATA.tools.map(item => item.module))];
    filter.innerHTML = `<option value="all">${t('All statistics modules', 'সব statistics module')}</option>` + used.map(id => `<option value="${id}">${escapeHtml(t(moduleMap[id].title_en, moduleMap[id].title_bn))}</option>`).join('');
  }
  function renderLabs() {
    const q = search.value.trim().toLowerCase();
    const moduleId = filter.value;
    const items = DATA.tools.filter(item => (moduleId === 'all' || item.module === moduleId) && (!q || [item.title_en, item.title_bn, item.description_en, item.description_bn].join(' ').toLowerCase().includes(q)));
    count.textContent = `${items.length} ${t(items.length === 1 ? 'lab' : 'labs', 'lab')}`;
    grid.innerHTML = items.length ? items.map(toolCard).join('') : `<div class="topic-card"><h2>${t('No matching lab', 'মিল পাওয়া lab নেই')}</h2></div>`;
  }
  function renderDatasets() {
    if (!datasetGrid) return;
    datasetGrid.innerHTML = DATA.datasets.map(dataset => `<article class="dataset-card"><div class="dataset-card-top"><span class="dataset-icon">CSV</span><span class="status-chip available">${t('Synthetic', 'Synthetic')}</span></div><h3>${escapeHtml(t(dataset.title_en, dataset.title_bn))}</h3><p>${escapeHtml(t(dataset.description_en, dataset.description_bn))}</p><div class="dataset-meta"><span>${dataset.rows} ${t('rows', 'row')}</span><span>${t('Documented fields', 'Documented field')}</span></div><div class="dataset-actions"><a class="button small primary" href="${dataset.file}" download>${t('Download data', 'Data download')}</a><a class="button small ghost" href="${dataset.dictionary}" download>${t('Data dictionary', 'Data dictionary')}</a></div></article>`).join('');
  }

  search.addEventListener('input', renderLabs);
  filter.addEventListener('change', renderLabs);
  window.addEventListener('dlh:language', () => { options(); renderLabs(); renderDatasets(); });
  options();
  renderLabs();
  renderDatasets();
})();
