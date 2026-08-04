(() => {
  'use strict';
  const {
    DATA, moduleMap, topicMap, t, escapeHtml, moduleColor, getProfile,
    getPlanTopics, getNextTopic, isCompleted,
  } = window.SLH;
  const grid = document.getElementById('catalog-grid');
  const search = document.getElementById('catalog-search');
  const moduleFilter = document.getElementById('module-filter');
  const difficultyFilter = document.getElementById('difficulty-filter');
  const kindFilter = document.getElementById('kind-filter');
  const count = document.getElementById('catalog-count');
  const guide = document.getElementById('guided-catalog');
  const planButton = document.getElementById('recommended-only');
  if (!grid || !search || !moduleFilter || !difficultyFilter || !kindFilter || !count) return;

  let recommendedOnly = Boolean(getProfile()) && new URLSearchParams(location.search).get('all') !== '1';

  function options() {
    moduleFilter.innerHTML = `<option value="all">${t('All modules','সব মডিউল')}</option>` + DATA.modules.map(module => `<option value="${module.id}">${escapeHtml(t(module.title_en,module.title_bn))}</option>`).join('');
    const requested = new URLSearchParams(location.search).get('module');
    if (requested && moduleMap[requested]) moduleFilter.value = requested;
    difficultyFilter.options[0].text = t('All levels','সব লেভেল');
    kindFilter.options[0].text = t('All formats','সব ফরম্যাট');
    [...difficultyFilter.options].slice(1).forEach(option => option.text = ({Beginner:t('Beginner','বিগিনার'),Intermediate:t('Intermediate','ইন্টারমিডিয়েট'),Advanced:t('Advanced','অ্যাডভান্সড')})[option.value]);
    [...kindFilter.options].slice(1).forEach(option => option.text = ({lesson:t('Lesson','লেসন'),lab:t('Lab-linked','ল্যাব-লিঙ্কড'),practice:t('Practice','প্র্যাকটিস')})[option.value]);
  }

  function card(topic) {
    const module = moduleMap[topic.module];
    const status = isCompleted(topic.id) ? `<span class="badge completed-badge">✓ ${t('Completed','সম্পন্ন')}</span>` : '';
    return `<a class="lesson-card" style="--accent:${moduleColor(module.accent)}" href="/${topic.url}"><div class="lesson-meta"><span class="badge level-${topic.difficulty}">${escapeHtml(t(topic.difficulty, ({Beginner:'বিগিনার',Intermediate:'ইন্টারমিডিয়েট',Advanced:'অ্যাডভান্সড'})[topic.difficulty]))}</span><span class="badge">${escapeHtml(t(module.title_en,module.title_bn))}</span>${status}</div><h3>${escapeHtml(t(topic.title_en,topic.title_bn))}</h3><p>${escapeHtml(t(topic.summary_en,topic.summary_bn))}</p><span class="card-footer"><span>${topic.minutes} ${t('min','মিনিট')} · ${topic.kind === 'lab' ? t('Lab-linked','ল্যাব-লিঙ্কড') : topic.kind === 'practice' ? t('Practice','প্র্যাকটিস') : t('Lesson','লেসন')}</span><span class="card-arrow">→</span></span></a>`;
  }

  function renderGuide() {
    const profile = getProfile();
    if (!guide) return;
    if (!profile) {
      guide.innerHTML = `<div><span class="eyebrow">${t('Need a starting point?','শুরু কোথা থেকে করবেন?')}</span><h2>${t('Turn the full catalog into one guided route.','পুরো catalog-কে একটি guided route-এ রূপ দিন।')}</h2><p>${t('Choose your goal and level, then see only the next useful lessons.','লক্ষ্য ও level বেছে নিয়ে শুধু প্রয়োজনীয় পরবর্তী lesson দেখুন।')}</p></div><a class="button primary" href="/start/">${t('Build my plan','আমার প্ল্যান তৈরি করুন')} →</a>`;
      planButton?.classList.add('hidden');
      return;
    }
    const next = getNextTopic(profile);
    guide.innerHTML = `<div><span class="eyebrow">${t('Guided catalog','গাইডেড catalog')}</span><h2>${next ? `${t('Your next lesson:','আপনার পরবর্তী lesson:')} ${escapeHtml(t(next.title_en,next.title_bn))}` : t('Your selected path is complete.','আপনার selected path সম্পন্ন।')}</h2><p>${t('Recommended view hides unrelated lessons without removing access to the full library.','Recommended view unrelated lesson লুকায়, তবে full library-র access থাকে।')}</p></div>${next ? `<a class="button primary" href="/${next.url}">${t('Open next lesson','পরবর্তী lesson খুলুন')} →</a>` : `<a class="button primary" href="/paths/">${t('Choose another path','অন্য path বেছে নিন')}</a>`}`;
    if (planButton) {
      planButton.classList.remove('hidden');
      planButton.textContent = recommendedOnly ? t('Show all 108 lessons','সব ১০৮টি lesson দেখুন') : t('Show only my path','শুধু আমার path দেখুন');
    }
  }

  function render() {
    const q = search.value.trim().toLowerCase();
    const module = moduleFilter.value;
    const difficulty = difficultyFilter.value;
    const kind = kindFilter.value;
    const planIds = new Set(getPlanTopics().map(topic => topic.id));
    const filtered = DATA.topics.filter(topic => {
      const haystack = [topic.title_en,topic.title_bn,topic.summary_en,topic.summary_bn,topic.formula_en,topic.module].join(' ').toLowerCase();
      return (!recommendedOnly || planIds.has(topic.id)) && (!q || haystack.includes(q)) && (module === 'all' || topic.module === module) && (difficulty === 'all' || topic.difficulty === difficulty) && (kind === 'all' || topic.kind === kind);
    });
    count.textContent = `${filtered.length} ${t(filtered.length === 1 ? 'lesson' : 'lessons','লেসন')}${recommendedOnly ? ` · ${t('your path','আপনার path')}` : ''}`;
    grid.innerHTML = filtered.length ? filtered.map(card).join('') : `<div class="topic-card"><h2>${t('No matching lessons','মিল পাওয়া কোনো লেসন নেই')}</h2><p>${t('Try a broader keyword or clear one of the filters.','আরও সাধারণ keyword ব্যবহার করুন অথবা filter clear করুন।')}</p></div>`;
    renderGuide();
  }

  [search,moduleFilter,difficultyFilter,kindFilter].forEach(element => element.addEventListener(element === search ? 'input' : 'change', render));
  document.getElementById('clear-filters')?.addEventListener('click', () => {
    search.value=''; moduleFilter.value='all'; difficultyFilter.value='all'; kindFilter.value='all'; render();
  });
  planButton?.addEventListener('click', () => { recommendedOnly = !recommendedOnly; render(); });
  window.addEventListener('slh:language', () => { options(); render(); });
  window.addEventListener('slh:profile', render);
  window.addEventListener('slh:progress', render);
  options();
  render();
})();
