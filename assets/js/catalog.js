(() => {
  const { DATA, moduleMap, state, t, escapeHtml, moduleColor } = window.SLH;
  const grid = document.getElementById('catalog-grid');
  const search = document.getElementById('catalog-search');
  const moduleFilter = document.getElementById('module-filter');
  const difficultyFilter = document.getElementById('difficulty-filter');
  const kindFilter = document.getElementById('kind-filter');
  const count = document.getElementById('catalog-count');

  function options() {
    moduleFilter.innerHTML = `<option value="all">${t('All modules','সব মডিউল')}</option>` + DATA.modules.map(m => `<option value="${m.id}">${escapeHtml(t(m.title_en,m.title_bn))}</option>`).join('');
    const requested = new URLSearchParams(location.search).get('module');
    if (requested && moduleMap[requested]) moduleFilter.value = requested;
    difficultyFilter.options[0].text = t('All levels','সব লেভেল');
    kindFilter.options[0].text = t('All formats','সব ফরম্যাট');
    [...difficultyFilter.options].slice(1).forEach(option => option.text = ({Beginner:t('Beginner','বিগিনার'),Intermediate:t('Intermediate','ইন্টারমিডিয়েট'),Advanced:t('Advanced','অ্যাডভান্সড')})[option.value]);
    [...kindFilter.options].slice(1).forEach(option => option.text = ({lesson:t('Lesson','লেসন'),lab:t('Lab-linked','ল্যাব-লিঙ্কড'),practice:t('Practice','প্র্যাকটিস')})[option.value]);
  }

  function card(topic) {
    const module = moduleMap[topic.module];
    return `<a class="lesson-card" style="--accent:${moduleColor(module.accent)}" href="/${topic.url}"><div class="lesson-meta"><span class="badge level-${topic.difficulty}">${escapeHtml(t(topic.difficulty, ({Beginner:'বিগিনার',Intermediate:'ইন্টারমিডিয়েট',Advanced:'অ্যাডভান্সড'})[topic.difficulty]))}</span><span class="badge">${escapeHtml(t(module.title_en,module.title_bn))}</span></div><h3>${escapeHtml(t(topic.title_en,topic.title_bn))}</h3><p>${escapeHtml(t(topic.summary_en,topic.summary_bn))}</p><span class="card-footer"><span>${topic.minutes} ${t('min','মিনিট')} · ${topic.kind === 'lab' ? t('Lab-linked','ল্যাব-লিঙ্কড') : topic.kind === 'practice' ? t('Practice','প্র্যাকটিস') : t('Lesson','লেসন')}</span><span class="card-arrow">→</span></span></a>`;
  }

  function render() {
    const q = search.value.trim().toLowerCase();
    const module = moduleFilter.value;
    const difficulty = difficultyFilter.value;
    const kind = kindFilter.value;
    const filtered = DATA.topics.filter(topic => {
      const haystack = [topic.title_en,topic.title_bn,topic.summary_en,topic.summary_bn,topic.formula_en,topic.module].join(' ').toLowerCase();
      return (!q || haystack.includes(q)) && (module === 'all' || topic.module === module) && (difficulty === 'all' || topic.difficulty === difficulty) && (kind === 'all' || topic.kind === kind);
    });
    count.textContent = `${filtered.length} ${t(filtered.length === 1 ? 'lesson' : 'lessons','লেসন')}`;
    grid.innerHTML = filtered.length ? filtered.map(card).join('') : `<div class="topic-card"><h2>${t('No matching lessons','মিল পাওয়া কোনো লেসন নেই')}</h2><p>${t('Try a broader keyword or clear one of the filters.','আরও সাধারণ keyword ব্যবহার করুন অথবা filter clear করুন।')}</p></div>`;
  }

  [search,moduleFilter,difficultyFilter,kindFilter].forEach(el => el.addEventListener(el === search ? 'input' : 'change',render));
  document.getElementById('clear-filters').addEventListener('click',()=>{ search.value=''; moduleFilter.value='all'; difficultyFilter.value='all'; kindFilter.value='all'; render(); });
  window.addEventListener('slh:language',()=>{ options(); render(); });
  options(); render();
})();
