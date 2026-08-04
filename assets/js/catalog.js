(() => {
  'use strict';
  const {
    DATA, moduleMap, domainMap, t, escapeHtml, moduleColor, getProfile,
    getPlanTopics, getNextTopic, isCompleted, statusLabel,
  } = window.DLH;
  const grid = document.getElementById('catalog-grid');
  const search = document.getElementById('catalog-search');
  const domainFilter = document.getElementById('domain-filter');
  const moduleFilter = document.getElementById('module-filter');
  const difficultyFilter = document.getElementById('difficulty-filter');
  const kindFilter = document.getElementById('kind-filter');
  const count = document.getElementById('catalog-count');
  const guide = document.getElementById('guided-catalog');
  const planButton = document.getElementById('recommended-only');
  const domainOverview = document.getElementById('learning-domain-overview');
  if (!grid || !search || !domainFilter || !moduleFilter || !difficultyFilter || !kindFilter || !count) return;

  let recommendedOnly = Boolean(getProfile()) && new URLSearchParams(location.search).get('all') !== '1';

  function domainCards() {
    if (!domainOverview) return;
    const ordered = ['data-foundations', 'statistics', 'excel', 'sql', 'power-bi', 'python'];
    domainOverview.innerHTML = ordered.map(id => {
      const domain = domainMap[id];
      const clickable = domain.status === 'available';
      return `<${clickable ? 'button' : 'a'} class="learning-domain-card ${domain.status}" ${clickable ? `type="button" data-domain="${domain.id}"` : `href="${domain.url}"`}><span class="status-chip ${domain.status}">${statusLabel(domain.status)}</span><small>${domain.release}</small><h2>${escapeHtml(t(domain.title_en, domain.title_bn))}</h2><p>${escapeHtml(t(domain.description_en, domain.description_bn))}</p><strong>${clickable ? t('Filter available lessons', 'Available lesson filter করুন') : t('View curriculum scope', 'Curriculum scope দেখুন')} →</strong></${clickable ? 'button' : 'a'}>`;
    }).join('');
    domainOverview.querySelectorAll('[data-domain]').forEach(button => button.addEventListener('click', () => {
      recommendedOnly = false;
      domainFilter.value = button.dataset.domain;
      planButton?.classList.remove('active');
      render();
      document.querySelector('.filter-panel')?.scrollIntoView({ behavior:'smooth', block:'start' });
    }));
  }

  function options() {
    const availableDomains = DATA.domains.filter(domain => domain.status === 'available');
    domainFilter.innerHTML = `<option value="all">${t('All available domains', 'সব available domain')}</option>` + availableDomains.map(domain => `<option value="${domain.id}">${escapeHtml(t(domain.title_en, domain.title_bn))}</option>`).join('');
    moduleFilter.innerHTML = `<option value="all">${t('All modules', 'সব module')}</option>` + DATA.modules.map(module => `<option value="${module.id}">${escapeHtml(t(module.title_en, module.title_bn))}</option>`).join('');
    const params = new URLSearchParams(location.search);
    if (params.get('domain') && domainMap[params.get('domain')]?.status === 'available') domainFilter.value = params.get('domain');
    if (params.get('module') && moduleMap[params.get('module')]) moduleFilter.value = params.get('module');
    difficultyFilter.options[0].text = t('All levels', 'সব level');
    kindFilter.options[0].text = t('All formats', 'সব format');
    [...difficultyFilter.options].slice(1).forEach(option => option.text = ({ Beginner:t('Beginner', 'বিগিনার'), Intermediate:t('Intermediate', 'ইন্টারমিডিয়েট'), Advanced:t('Advanced', 'অ্যাডভান্সড') })[option.value]);
    [...kindFilter.options].slice(1).forEach(option => option.text = ({ lesson:t('Lesson', 'Lesson'), lab:t('Lab-linked', 'Lab-linked'), practice:t('Practice', 'Practice') })[option.value]);
  }

  function card(topic) {
    const module = moduleMap[topic.module];
    const status = isCompleted(topic.id) ? `<span class="badge completed-badge">✓ ${t('Completed', 'সম্পন্ন')}</span>` : '';
    return `<a class="lesson-card" style="--accent:${moduleColor(module.accent)}" href="/${topic.url}"><div class="lesson-meta"><span class="badge level-${topic.difficulty}">${escapeHtml(t(topic.difficulty, ({ Beginner:'বিগিনার', Intermediate:'ইন্টারমিডিয়েট', Advanced:'অ্যাডভান্সড' })[topic.difficulty]))}</span><span class="badge">${escapeHtml(t(domainMap[topic.domain]?.title_en || topic.domain, domainMap[topic.domain]?.title_bn || topic.domain))}</span>${status}</div><h3>${escapeHtml(t(topic.title_en, topic.title_bn))}</h3><p>${escapeHtml(t(topic.summary_en, topic.summary_bn))}</p><span class="card-footer"><span>${topic.minutes} ${t('min', 'মিনিট')} · ${topic.kind === 'lab' ? t('Lab-linked', 'Lab-linked') : topic.kind === 'practice' ? t('Practice', 'Practice') : t('Lesson', 'Lesson')}</span><span class="card-arrow">→</span></span></a>`;
  }

  function renderGuide() {
    const profile = getProfile();
    if (!guide) return;
    if (!profile) {
      guide.innerHTML = `<div><span class="eyebrow">${t('Need a starting point?', 'শুরু কোথা থেকে করবেন?')}</span><h2>${t('Turn the active foundation into one guided route.', 'Active foundation-কে guided route-এ রূপ দিন।')}</h2><p>${t('Choose experience, study time and learning preference, then see only the next useful lessons.', 'Experience, study time ও learning preference বেছে নিয়ে শুধু next useful lesson দেখুন।')}</p></div><a class="button primary" href="/start/">${t('Build my plan', 'আমার plan তৈরি করুন')} →</a>`;
      planButton?.classList.add('hidden');
      return;
    }
    const next = getNextTopic(profile);
    guide.innerHTML = `<div><span class="eyebrow">${t('Guided view', 'Guided view')}</span><h2>${next ? `${t('Your next lesson:', 'আপনার next lesson:')} ${escapeHtml(t(next.title_en, next.title_bn))}` : t('The current foundation is complete.', 'Current foundation complete।')}</h2><p>${t('Recommended view hides unrelated available lessons without hiding the curriculum roadmap.', 'Recommended view unrelated available lesson hide করে, curriculum roadmap নয়।')}</p></div>${next ? `<a class="button primary" href="/${next.url}">${t('Open next lesson', 'Next lesson খুলুন')} →</a>` : `<a class="button primary" href="/projects/retail-sales-foundations/">${t('Open foundation project', 'Foundation project খুলুন')}</a>`}`;
    planButton?.classList.remove('hidden');
    planButton.textContent = recommendedOnly ? t('Show all available lessons', 'সব available lesson দেখুন') : t('Show only my route', 'শুধু আমার route দেখুন');
    planButton.classList.toggle('active', recommendedOnly);
  }

  function filteredTopics() {
    const q = search.value.trim().toLowerCase();
    const recommendedIds = new Set(getPlanTopics().map(topic => topic.id));
    return DATA.topics.filter(topic => {
      if (recommendedOnly && !recommendedIds.has(topic.id)) return false;
      if (domainFilter.value !== 'all' && topic.domain !== domainFilter.value) return false;
      if (moduleFilter.value !== 'all' && topic.module !== moduleFilter.value) return false;
      if (difficultyFilter.value !== 'all' && topic.difficulty !== difficultyFilter.value) return false;
      if (kindFilter.value !== 'all' && topic.kind !== kindFilter.value) return false;
      if (q && ![topic.title_en, topic.title_bn, topic.summary_en, topic.summary_bn, topic.formula_en, moduleMap[topic.module]?.title_en].join(' ').toLowerCase().includes(q)) return false;
      return true;
    });
  }

  function render() {
    renderGuide();
    const items = filteredTopics();
    count.textContent = `${items.length} ${t(items.length === 1 ? 'available lesson' : 'available lessons', 'available lesson')}`;
    grid.innerHTML = items.length ? items.map(card).join('') : `<div class="topic-card empty-result"><h2>${t('No matching available lesson', 'মিল পাওয়া available lesson নেই')}</h2><p>${t('Clear filters or view the curriculum for future tool modules.', 'Filter clear করুন অথবা future tool module-এর curriculum দেখুন।')}</p><a class="button ghost" href="/curriculum/">${t('View curriculum', 'Curriculum দেখুন')}</a></div>`;
  }

  search.addEventListener('input', render);
  domainFilter.addEventListener('change', () => { if (domainFilter.value !== 'all') moduleFilter.value = 'all'; render(); });
  moduleFilter.addEventListener('change', render);
  difficultyFilter.addEventListener('change', render);
  kindFilter.addEventListener('change', render);
  planButton?.addEventListener('click', () => { recommendedOnly = !recommendedOnly; render(); });
  document.getElementById('clear-filters')?.addEventListener('click', () => { search.value = ''; domainFilter.value = 'all'; moduleFilter.value = 'all'; difficultyFilter.value = 'all'; kindFilter.value = 'all'; recommendedOnly = false; render(); });
  window.addEventListener('dlh:language', () => { domainCards(); options(); render(); });
  window.addEventListener('dlh:progress', render);

  domainCards();
  options();
  render();
})();
