(() => {
  'use strict';
  const { DATA, t, escapeHtml } = window.DLH;
  const input = document.getElementById('glossary-search');
  const list = document.getElementById('glossary-grid');
  if (!input || !list) return;
  function render() {
    const q = input.value.trim().toLowerCase();
    const items = DATA.glossary.filter(item => !q || [item.term_en, item.term_bn, item.definition_en, item.definition_bn].join(' ').toLowerCase().includes(q)).sort((a, b) => t(a.term_en, a.term_bn).localeCompare(t(b.term_en, b.term_bn)));
    list.innerHTML = items.length ? items.map(item => `<dl class="glossary-item"><dt>${escapeHtml(t(item.term_en, item.term_bn))}</dt><dd>${escapeHtml(t(item.definition_en, item.definition_bn))}</dd></dl>`).join('') : `<div class="topic-card"><h2>${t('No matching term', 'মিল পাওয়া term নেই')}</h2></div>`;
  }
  input.addEventListener('input', render);
  window.addEventListener('dlh:language', render);
  render();
})();
