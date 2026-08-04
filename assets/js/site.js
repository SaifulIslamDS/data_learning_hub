(() => {
  'use strict';

  const DATA = window.DLH_CONTENT;
  if (!DATA) return;

  const icons = {
    logo: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 18V8m5 10V4m5 14v-7m4 7V6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><path d="M3 20h18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
    search: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7" fill="none" stroke="currentColor" stroke-width="2"/><path d="m16 16 4 4" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
    sun: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 2v2m0 16v2M4.93 4.93l1.42 1.42m11.3 11.3 1.42 1.42M2 12h2m16 0h2M4.93 19.07l1.42-1.42m11.3-11.3 1.42-1.42" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
    moon: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 15.5A8.2 8.2 0 0 1 8.5 4 8.5 8.5 0 1 0 20 15.5Z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>',
    menu: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
    close: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m6 6 12 12M18 6 6 18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
    compass: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="m15.5 8.5-2 5-5 2 2-5 5-2Z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>',
  };

  const moduleMap = Object.fromEntries(DATA.modules.map(item => [item.id, item]));
  const topicMap = Object.fromEntries(DATA.topics.map(item => [item.id, item]));
  const toolMap = Object.fromEntries(DATA.tools.map(item => [item.id, item]));
  const pathMap = Object.fromEntries(DATA.paths.map(item => [item.id, item]));
  const domainMap = Object.fromEntries(DATA.domains.map(item => [item.id, item]));
  const careerPathMap = Object.fromEntries(DATA.career_paths.map(item => [item.id, item]));

  const safeStorage = {
    get(key, fallback = null) {
      try { return localStorage.getItem(key) ?? fallback; } catch { return fallback; }
    },
    set(key, value) {
      try { localStorage.setItem(key, value); } catch { /* private mode can block storage */ }
    },
    remove(key) {
      try { localStorage.removeItem(key); } catch { /* ignore */ }
    },
    json(key, fallback = []) {
      try { return JSON.parse(localStorage.getItem(key) || JSON.stringify(fallback)); } catch { return fallback; }
    },
  };

  function migrateV1Storage() {
    const keys = ['language', 'theme', 'completed', 'bookmarks', 'last-topic'];
    keys.forEach(name => {
      const target = `dlh-${name}`;
      const legacy = `slh-${name}`;
      if (safeStorage.get(target) === null && safeStorage.get(legacy) !== null) {
        safeStorage.set(target, safeStorage.get(legacy));
      }
    });
    if (safeStorage.get('dlh-profile') === null && safeStorage.get('slh-profile') !== null) {
      const profile = safeStorage.json('slh-profile', null);
      if (profile) {
        const goalMap = {
          'statistics-foundations': 'data-analyst',
          'data-scientist': 'data-analyst',
          'data-engineer': 'data-analyst',
          'research-business': 'research-analyst',
        };
        profile.goal = goalMap[profile.goal] || profile.goal || 'data-analyst';
        profile.migratedFrom = 'v1';
        profile.schemaVersion = DATA.storage?.schema_version || 2;
        safeStorage.set('dlh-profile', JSON.stringify(profile));
      }
    }
    safeStorage.set('dlh-storage-version', String(DATA.storage?.schema_version || 2));
  }
  migrateV1Storage();

  const state = {
    language: safeStorage.get('dlh-language', 'en') === 'bn' ? 'bn' : 'en',
    theme: document.documentElement.dataset.theme || 'light',
  };

  function t(en, bn) { return state.language === 'bn' ? bn : en; }
  function escapeHtml(value) {
    return String(value ?? '').replace(/[&<>'"]/g, char => ({ '&':'&amp;', '<':'&lt;', '>':'&gt;', "'":'&#39;', '"':'&quot;' }[char]));
  }

  function getProfile() {
    const profile = safeStorage.json('dlh-profile', null);
    if (!profile) return null;
    if (!pathMap[profile.goal]) profile.goal = 'data-analyst';
    return pathMap[profile.goal] ? profile : null;
  }
  function setProfile(profile) {
    safeStorage.set('dlh-profile', JSON.stringify({ ...profile, schemaVersion: DATA.storage?.schema_version || 2 }));
    window.dispatchEvent(new CustomEvent('dlh:profile', { detail: profile }));
  }
  function clearProfile() {
    safeStorage.remove('dlh-profile');
    window.dispatchEvent(new CustomEvent('dlh:profile', { detail: null }));
  }
  function levelStartIndex(path, level = 'beginner') {
    if (!path?.topics?.length || level === 'beginner') return 0;
    const topics = path.topics.map(id => topicMap[id]).filter(Boolean);
    if (level === 'intermediate') {
      const index = topics.findIndex(topic => topic.difficulty !== 'Beginner');
      return Math.max(0, (index < 0 ? Math.floor(topics.length * 0.2) : index) - 1);
    }
    const index = topics.findIndex(topic => topic.difficulty === 'Advanced');
    return Math.max(0, (index < 0 ? Math.floor(topics.length * 0.55) : index) - 1);
  }
  function getPlanTopics(profile = getProfile()) {
    if (!profile) return [];
    const path = pathMap[profile.goal];
    if (!path) return [];
    const start = Number.isInteger(profile.startIndex) ? profile.startIndex : levelStartIndex(path, profile.level);
    return path.topics.slice(Math.max(0, start)).map(id => topicMap[id]).filter(Boolean);
  }
  function getCompleted() { return new Set(safeStorage.json('dlh-completed', [])); }
  function setCompleted(set) { safeStorage.set('dlh-completed', JSON.stringify([...set])); }
  function getBookmarks() { return new Set(safeStorage.json('dlh-bookmarks', [])); }
  function setBookmarks(set) { safeStorage.set('dlh-bookmarks', JSON.stringify([...set])); }
  function isCompleted(id) { return getCompleted().has(id); }
  function toggleCompleted(id) {
    const completed = getCompleted();
    completed.has(id) ? completed.delete(id) : completed.add(id);
    setCompleted(completed);
    window.dispatchEvent(new CustomEvent('dlh:progress'));
    return completed.has(id);
  }
  function toggleBookmark(id) {
    const bookmarks = getBookmarks();
    bookmarks.has(id) ? bookmarks.delete(id) : bookmarks.add(id);
    setBookmarks(bookmarks);
    window.dispatchEvent(new CustomEvent('dlh:bookmarks'));
    return bookmarks.has(id);
  }
  function getPlanProgress(profile = getProfile()) {
    const topics = getPlanTopics(profile);
    const completed = getCompleted();
    const done = topics.filter(topic => completed.has(topic.id)).length;
    return { done, total: topics.length, percent: topics.length ? Math.round(done / topics.length * 100) : 0 };
  }
  function getNextTopic(profile = getProfile()) {
    const completed = getCompleted();
    return getPlanTopics(profile).find(topic => !completed.has(topic.id)) || null;
  }
  function getNextPlanTopic(currentId, profile = getProfile()) {
    const topics = getPlanTopics(profile);
    const index = topics.findIndex(topic => topic.id === currentId);
    if (index >= 0) return topics.slice(index + 1).find(topic => !isCompleted(topic.id)) || topics[index + 1] || null;
    return getNextTopic(profile);
  }
  function getRecommendedLab(topic) {
    if (!topic) return null;
    if (topic.lab && toolMap[topic.lab]) return toolMap[topic.lab];
    const peers = DATA.topics.filter(item => item.module === topic.module && item.lab && toolMap[item.lab]);
    peers.sort((a, b) => Math.abs(a.order - topic.order) - Math.abs(b.order - topic.order));
    return peers[0] ? toolMap[peers[0].lab] : null;
  }

  function applyLanguage(root = document) {
    document.documentElement.lang = state.language;
    root.querySelectorAll('[data-en][data-bn]').forEach(element => {
      element.textContent = state.language === 'bn' ? element.dataset.bn : element.dataset.en;
    });
    root.querySelectorAll('[data-placeholder-en][data-placeholder-bn]').forEach(element => {
      element.placeholder = state.language === 'bn' ? element.dataset.placeholderBn : element.dataset.placeholderEn;
    });
    document.querySelectorAll('.language-button').forEach(button => {
      const active = button.dataset.lang === state.language;
      button.classList.toggle('active', active);
      button.setAttribute('aria-pressed', String(active));
    });
    window.dispatchEvent(new CustomEvent('dlh:language', { detail: state.language }));
  }
  function setLanguage(language) {
    state.language = language === 'bn' ? 'bn' : 'en';
    safeStorage.set('dlh-language', state.language);
    applyLanguage();
  }
  function setTheme(theme) {
    state.theme = theme === 'dark' ? 'dark' : 'light';
    document.documentElement.dataset.theme = state.theme;
    safeStorage.set('dlh-theme', state.theme);
    updateThemeButtons();
    window.dispatchEvent(new CustomEvent('dlh:theme', { detail: state.theme }));
  }
  function updateThemeButtons() {
    document.querySelectorAll('[data-action="theme"]').forEach(button => {
      const dark = state.theme === 'dark';
      button.innerHTML = dark ? icons.sun : icons.moon;
      button.setAttribute('aria-label', dark ? t('Switch to light theme', 'লাইট থিম চালু করুন') : t('Switch to dark theme', 'ডার্ক থিম চালু করুন'));
      button.title = button.getAttribute('aria-label');
    });
  }

  function navLink(href, en, bn, key) {
    const page = document.body.dataset.page;
    const active = page === key || (page === 'topic' && key === 'learn') || (page === 'tool' && key === 'practice') || (page === 'project' && key === 'projects');
    return `<a href="${href}" class="${active ? 'active' : ''}" data-en="${en}" data-bn="${bn}">${t(en, bn)}</a>`;
  }
  function languageSwitch() {
    return `<div class="language-switch" role="group" aria-label="Language"><button class="language-button ${state.language === 'en' ? 'active' : ''}" data-lang="en" type="button" aria-label="English" aria-pressed="${state.language === 'en'}">EN</button><button class="language-button ${state.language === 'bn' ? 'active' : ''}" data-lang="bn" type="button" aria-label="বাংলা" aria-pressed="${state.language === 'bn'}">BN</button></div>`;
  }
  function renderHeader() {
    const root = document.getElementById('site-header');
    if (!root) return;
    const profile = getProfile();
    const journeyHref = profile ? '/my-learning/' : '/start/';
    const journeyEn = profile ? 'My Learning' : 'Start Here';
    const journeyBn = profile ? 'আমার শেখা' : 'শুরু করুন';
    root.innerHTML = `<header class="site-header" id="site-header-bar"><div class="container navbar"><a class="brand" href="/" aria-label="Data Learning Hub home"><span class="brand-mark">${icons.logo}</span><span class="brand-text">Data Learning Hub<small data-en="Analytics first · careers next" data-bn="প্রথমে Analytics · পরে career">${t('Analytics first · careers next', 'প্রথমে Analytics · পরে career')}</small></span></a><nav class="nav-links" aria-label="Primary navigation">${navLink('/tutorials/', 'Tutorials', 'টিউটোরিয়াল', 'tutorials')}${navLink('/exercises/data-foundations/', 'Exercises', 'Exercise', 'tutorial-exercises')}${navLink('/examples/data-foundations/', 'Examples', 'Example', 'tutorial-examples')}${navLink('/projects/', 'Projects', 'প্রজেক্ট', 'projects')}${navLink('/references/data-foundations/', 'References', 'Reference', 'tutorial-references')}${navLink('/career-paths/', 'Career Paths', 'Career Path', 'career-paths')}</nav><div class="nav-actions"><button class="icon-button" type="button" data-action="search" aria-label="${t('Open search', 'সার্চ খুলুন')}" title="${t('Open search', 'সার্চ খুলুন')}">${icons.search}</button>${languageSwitch()}<button class="icon-button" type="button" data-action="theme"></button><button class="menu-button" id="menu-button" type="button" aria-label="${t('Open navigation', 'নেভিগেশন খুলুন')}" aria-expanded="false">${icons.menu}</button></div></div><div class="container mobile-panel" id="mobile-panel">${navLink('/tutorials/', 'Tutorials', 'টিউটোরিয়াল', 'tutorials')}${navLink('/exercises/data-foundations/', 'Exercises', 'Exercise', 'tutorial-exercises')}${navLink('/examples/data-foundations/', 'Examples', 'Example', 'tutorial-examples')}${navLink('/projects/', 'Projects', 'প্রজেক্ট', 'projects')}${navLink('/references/data-foundations/', 'References', 'Reference', 'tutorial-references')}${navLink('/career-paths/', 'Career Paths', 'Career Path', 'career-paths')}${navLink(journeyHref, journeyEn, journeyBn, profile ? 'my-learning' : 'start')}${navLink('/practice/', 'Statistics Labs', 'Statistics Lab', 'practice')}${navLink('/learn/', 'Legacy Lesson Library', 'Legacy Lesson Library', 'learn')}${navLink('/curriculum/', 'Curriculum', 'Curriculum', 'curriculum')}${navLink('/about/', 'About', 'সম্পর্কে', 'about')}${languageSwitch()}</div></header>`;
    updateThemeButtons();
    root.querySelectorAll('.language-button').forEach(button => button.addEventListener('click', () => setLanguage(button.dataset.lang)));
    root.querySelectorAll('[data-action="theme"]').forEach(button => button.addEventListener('click', () => setTheme(state.theme === 'dark' ? 'light' : 'dark')));
    root.querySelectorAll('[data-action="search"]').forEach(button => button.addEventListener('click', openSearch));
    const menuButton = document.getElementById('menu-button');
    const panel = document.getElementById('mobile-panel');
    menuButton?.addEventListener('click', () => {
      const open = panel.classList.toggle('open');
      menuButton.setAttribute('aria-expanded', String(open));
      menuButton.innerHTML = open ? icons.close : icons.menu;
    });
  }

  function renderFooter() {
    const root = document.getElementById('site-footer');
    if (!root) return;
    root.innerHTML = `<footer class="site-footer"><div class="container footer-grid"><div class="footer-brand"><a class="brand" href="/"><span class="brand-mark">${icons.logo}</span><span class="brand-text">Data Learning Hub<small data-en="Foundations → tools → portfolio" data-bn="Foundation → tool → portfolio">${t('Foundations → tools → portfolio', 'Foundation → tool → portfolio')}</small></span></a><p data-en="Learn Data Analytics through connected concepts, practice, tools, datasets and projects." data-bn="Connected concept, practice, tool, dataset ও project দিয়ে Data Analytics শিখুন।">${t('Learn Data Analytics through connected concepts, practice, tools, datasets and projects.', 'Connected concept, practice, tool, dataset ও project দিয়ে Data Analytics শিখুন।')}</p></div><div class="footer-column"><h3 data-en="Tutorials" data-bn="টিউটোরিয়াল">${t('Tutorials', 'টিউটোরিয়াল')}</h3><a href="/tutorials/data-foundations/">${t('Data Foundations', 'Data Foundations')}</a><a href="/exercises/data-foundations/">${t('Exercises', 'Exercise')}</a><a href="/quiz/data-foundations/">${t('Final quiz', 'Final quiz')}</a></div><div class="footer-column"><h3 data-en="Resources" data-bn="Resource">${t('Resources', 'Resource')}</h3><a href="/examples/data-foundations/">${t('Examples', 'Example')}</a><a href="/references/data-foundations/">${t('References', 'Reference')}</a><a href="/projects/">${t('Projects', 'প্রজেক্ট')}</a><a href="/my-learning/">${t('My Learning', 'আমার শেখা')}</a></div><div class="footer-column"><h3 data-en="Creator" data-bn="Creator">${t('Creator', 'Creator')}</h3><a href="${DATA.site.website}" target="_blank" rel="noopener noreferrer">Website ↗</a><a href="${DATA.site.github}" target="_blank" rel="noopener noreferrer">GitHub ↗</a><a href="${DATA.site.linkedin}" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a></div></div><div class="container footer-bottom"><span>Idea and developed by Saiful Islam.</span><div class="footer-bottom-links"><a href="${DATA.site.inspiration}" target="_blank" rel="noopener noreferrer">${t('Inspired by tafshir027/stats ↗', 'tafshir027/stats দ্বারা অনুপ্রাণিত ↗')}</a><a href="/about/">${t('Privacy & credits', 'Privacy ও credit')}</a></div></div></footer>`;
  }

  function searchItems(query) {
    const q = query.trim().toLowerCase();
    const tutorialItems = (DATA.tutorials || []).flatMap(tutorial => tutorial.chapters.map((chapter, index) => ({ ...chapter, category: 'Tutorial chapter', icon: String(index + 1).padStart(2, '0'), href: `/tutorials/${tutorial.id}/${chapter.id}/` })));
    const items = [
      ...tutorialItems,
      ...DATA.topics.map(item => ({ ...item, category: 'Lesson', icon: 'L', href: `/${item.url}` })),
      ...DATA.tools.map(item => ({ ...item, category: 'Lab', icon: '∑', summary_en: item.description_en, summary_bn: item.description_bn, href: `/${item.url}` })),
      ...DATA.tool_curricula.map(item => ({ ...item, category: 'Curriculum', icon: 'C', summary_en: item.outcome_en, summary_bn: item.outcome_bn, href: `/curriculum/#${item.id}` })),
      ...DATA.projects.filter(item => item.url).map(item => ({ ...item, category: 'Project', icon: 'P', summary_en: item.description_en, summary_bn: item.description_bn, href: item.url })),
    ];
    if (!q) {
      const next = getNextTopic();
      const recommended = next ? [{ ...next, category: 'Lesson', icon: 'L', href: `/${next.url}` }, getRecommendedLab(next)] : [];
      return [...recommended.filter(Boolean).map(item => item.href ? item : ({ ...item, category: 'Lab', icon: '∑', summary_en: item.description_en, summary_bn: item.description_bn, href: `/${item.url}` })), ...items].filter((item, index, all) => all.findIndex(value => value.href === item.href) === index).slice(0, 10);
    }
    return items.filter(item => [item.title_en, item.title_bn, item.summary_en, item.summary_bn, item.category].join(' ').toLowerCase().includes(q)).slice(0, 18);
  }
  function renderSearchResults(query) {
    const root = document.getElementById('global-search-results');
    if (!root) return;
    const found = searchItems(query);
    root.innerHTML = found.length ? found.map(item => `<a class="search-result" href="${item.href}"><span class="search-result-icon">${item.icon}</span><span><strong>${escapeHtml(t(item.title_en, item.title_bn))}</strong><small>${escapeHtml(t(item.summary_en || item.description_en || item.category, item.summary_bn || item.description_bn || item.category))}</small></span><span>→</span></a>`).join('') : `<div class="search-empty">${t('No matching tutorial chapter or resource was found.', 'মিল পাওয়া tutorial chapter বা resource নেই।')}</div>`;
  }
  function openSearch() {
    const overlay = document.querySelector('.search-overlay');
    if (!overlay) return;
    overlay.classList.add('open');
    overlay.setAttribute('aria-hidden', 'false');
    const input = overlay.querySelector('#global-search-input');
    input.value = '';
    renderSearchResults('');
    setTimeout(() => input.focus(), 20);
  }
  function closeSearch() {
    const overlay = document.querySelector('.search-overlay');
    overlay?.classList.remove('open');
    overlay?.setAttribute('aria-hidden', 'true');
  }
  function renderSearch() {
    const root = document.getElementById('search-root');
    if (!root) return;
    root.innerHTML = `<div class="search-overlay" aria-hidden="true"><div class="search-dialog" role="dialog" aria-modal="true" aria-label="Site search"><div class="search-dialog-header">${icons.search}<input id="global-search-input" type="search" placeholder="${t('Search tutorial chapters, examples, exercises and resources…', 'Tutorial chapter, example, exercise ও resource খুঁজুন…')}" data-placeholder-en="Search tutorial chapters, examples, exercises and resources…" data-placeholder-bn="Tutorial chapter, example, exercise ও resource খুঁজুন…"><button class="icon-button" id="close-search" type="button" aria-label="${t('Close search', 'সার্চ বন্ধ করুন')}">${icons.close}</button></div><div class="search-results" id="global-search-results"></div></div></div>`;
    const overlay = root.querySelector('.search-overlay');
    root.querySelector('#close-search')?.addEventListener('click', closeSearch);
    root.querySelector('#global-search-input')?.addEventListener('input', event => renderSearchResults(event.target.value));
    overlay?.addEventListener('click', event => { if (event.target === overlay) closeSearch(); });
    document.addEventListener('keydown', event => {
      if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 'k') { event.preventDefault(); openSearch(); }
      if (event.key === 'Escape') closeSearch();
    });
  }

  function moduleColor(accent) {
    return ({ violet:'#7567ff', cyan:'#12a7b4', blue:'#3978ee', emerald:'#159a72', orange:'#df7f2c', pink:'#d8509a', indigo:'#6557d8', teal:'#168f8b', amber:'#c78a17' })[accent] || '#6557f5';
  }
  function toolCard(tool) {
    return `<a class="tool-card" href="/${tool.url}"><span class="tool-symbol">∑</span><div class="tool-meta"><span class="badge">${escapeHtml(t(moduleMap[tool.module]?.title_en || tool.module, moduleMap[tool.module]?.title_bn || tool.module))}</span></div><h3>${escapeHtml(t(tool.title_en, tool.title_bn))}</h3><p>${escapeHtml(t(tool.description_en, tool.description_bn))}</p><span class="card-footer"><span>${t('Open lab', 'ল্যাব খুলুন')}</span><span class="card-arrow">→</span></span></a>`;
  }
  function pathProgress(path) {
    const completed = getCompleted();
    const done = path.topics.filter(id => completed.has(id)).length;
    return { done, total: path.topics.length, percent: path.topics.length ? Math.round(done / path.topics.length * 100) : 0 };
  }
  function pathCard(path) {
    const progress = pathProgress(path);
    return `<a class="path-card" href="/career-paths/#${path.id}"><span class="eyebrow">${progress.total} ${t('available steps', 'available ধাপ')}</span><h3>${escapeHtml(t(path.title_en, path.title_bn))}</h3><p>${escapeHtml(t(path.description_en, path.description_bn))}</p><div class="progress-track"><span style="width:${progress.percent}%"></span></div><div class="path-summary"><span>${progress.done}/${progress.total} ${t('completed', 'সম্পন্ন')}</span><span>${progress.percent}%</span></div></a>`;
  }
  function modeLabel(mode) {
    return ({ concepts:t('Concept-first', 'কনসেপ্ট-ফার্স্ট'), balanced:t('Balanced', 'ব্যালান্সড'), practice:t('Practice-first', 'প্র্যাকটিস-ফার্স্ট') })[mode] || t('Balanced', 'ব্যালান্সড');
  }

  function statusLabel(status) {
    return ({ 'tutorial-published':t('Complete tutorial', 'Complete tutorial'), available:t('Available now', 'এখন available'), 'curriculum-ready':t('Curriculum ready', 'Curriculum ready'), 'foundation-ready':t('Foundation ready', 'Foundation ready'), roadmap:t('Future roadmap', 'Future roadmap') })[status] || status;
  }
  function renderHome() {
    if (document.body.dataset.page !== 'home') return;
    const profile = getProfile();
    const next = getNextTopic(profile);
    const progress = getPlanProgress(profile);
    const path = profile ? pathMap[profile.goal] : null;
    const primary = document.getElementById('home-primary-cta');
    const secondary = document.getElementById('home-secondary-cta');
    if (primary) {
      primary.href = profile ? '/my-learning/' : '/start/';
      primary.textContent = profile ? t('Continue my learning', 'আমার শেখা চালিয়ে যান') : t('Build my learning plan', 'আমার learning plan তৈরি করুন');
    }
    if (secondary) {
      secondary.href = profile && next ? `/${next.url}` : '/learn/';
      secondary.textContent = profile && next ? t('Open next lesson', 'পরবর্তী lesson খুলুন') : t('Explore learning domains', 'Learning domain দেখুন');
    }
    const stats = document.getElementById('hero-stats');
    if (stats) stats.innerHTML = [
      [`${DATA.topics.length}`, t('comprehensive lessons', 'comprehensive lesson')],
      [`${DATA.tools.length}`, t('browser labs', 'browser lab')],
      [`${DATA.tool_curricula.length}`, t('mapped tool tracks', 'mapped tool track')],
    ].map(([value, label]) => `<span class="stat-chip"><strong>${value}</strong> ${label}</span>`).join('');

    const preview = document.getElementById('home-plan-preview');
    if (preview) {
      if (!profile) {
        preview.innerHTML = `<span class="guide-kicker">${icons.compass} ${t('Your Data Analyst route', 'আপনার Data Analyst route')}</span><h2>${t('Start with what is available—not with the whole roadmap.', 'পুরো roadmap নয়—available অংশ দিয়ে শুরু করুন।')}</h2><ol class="mini-route"><li><span>1</span><div><strong>${t('Data foundations', 'Data foundation')}</strong><small>${t('Questions, variables and data quality', 'Question, variable ও data quality')}</small></div></li><li><span>2</span><div><strong>${t('Statistics for analytics', 'Analytics-এর statistics')}</strong><small>${t('Describe, compare and interpret evidence', 'Evidence describe, compare ও interpret')}</small></div></li><li><span>3</span><div><strong>${t('Tools in controlled releases', 'Controlled release-এ tool')}</strong><small>Excel → SQL → Power BI → Python</small></div></li></ol><a class="text-link" href="/start/">${t('Create my plan →', 'আমার plan তৈরি করুন →')}</a>`;
      } else {
        preview.innerHTML = `<span class="guide-kicker">${icons.compass} ${t('Your active foundation', 'আপনার active foundation')}</span><h2>${escapeHtml(t(path.title_en, path.title_bn))}</h2><p>${escapeHtml(modeLabel(profile.mode))} · ${progress.done}/${progress.total} ${t('available steps complete', 'available ধাপ সম্পন্ন')}</p><div class="progress-track"><span style="width:${progress.percent}%"></span></div>${next ? `<div class="next-mini"><small>${t('Next lesson', 'পরবর্তী lesson')}</small><strong>${escapeHtml(t(next.title_en, next.title_bn))}</strong><a class="button primary" href="/${next.url}">${t('Continue', 'চালিয়ে যান')} →</a></div>` : `<div class="next-mini"><strong>${t('You completed the current foundation.', 'আপনি current foundation সম্পন্ন করেছেন।')}</strong><a class="button primary" href="/curriculum/">${t('View upcoming tracks', 'Upcoming track দেখুন')}</a></div>`}`;
      }
    }

    const method = document.getElementById('home-method-grid');
    if (method) method.innerHTML = [
      ['01', t('Learn', 'শিখুন'), t('Understand the concept, language, assumptions and business purpose.', 'Concept, language, assumption ও business purpose বুঝুন।'), '/learn/'],
      ['02', t('Practice', 'প্র্যাকটিস'), t('Use browser labs and documented synthetic datasets.', 'Browser lab ও documented synthetic dataset ব্যবহার করুন।'), '/practice/'],
      ['03', t('Build', 'তৈরি করুন'), t('Produce a metric table, query, report, notebook or project deliverable.', 'Metric table, query, report, notebook বা project deliverable তৈরি করুন।'), '/projects/'],
      ['04', t('Explain', 'ব্যাখ্যা করুন'), t('State the evidence, decision relevance and limitation.', 'Evidence, decision relevance ও limitation state করুন।'), '/career-paths/'],
    ].map(([number, title, description, url]) => `<a class="method-card" href="${url}"><span>${number}</span><h3>${escapeHtml(title)}</h3><p>${escapeHtml(description)}</p><strong>${t('Explore', 'দেখুন')} →</strong></a>`).join('');

    const nextStep = document.getElementById('home-next-step');
    if (nextStep) {
      if (profile && next) {
        const lab = getRecommendedLab(next);
        nextStep.innerHTML = `<div><span class="eyebrow">${t('Your next focused session', 'আপনার পরবর্তী focused session')}</span><h2>${escapeHtml(t(next.title_en, next.title_bn))}</h2><p>${escapeHtml(t(next.summary_en, next.summary_bn))}</p><div class="session-pills"><span>1 · ${t('Learn', 'শিখুন')}</span>${lab ? `<span>2 · ${t('Practice', 'Practice')}</span>` : ''}<span>${lab ? '3' : '2'} · ${t('Explain', 'ব্যাখ্যা')}</span></div></div><div class="next-step-actions"><a class="button primary" href="/${next.url}">${t('Start lesson', 'Lesson শুরু করুন')}</a><a class="button ghost" href="/my-learning/">${t('View my plan', 'আমার plan দেখুন')}</a></div>`;
      } else {
        nextStep.innerHTML = `<div><span class="eyebrow">${t('Start without overload', 'Overload ছাড়া শুরু করুন')}</span><h2>${t('A short setup turns the active foundation into one clear route.', 'একটি short setup active foundation-কে clear route-এ রূপ দেয়।')}</h2><p>${t('Choose experience, study time and learning style. The complete curriculum stays visible without becoming your immediate task list.', 'Experience, study time ও learning style বেছে নিন। Complete curriculum visible থাকবে, কিন্তু immediate task list হবে না।')}</p></div><a class="button primary" href="/start/">${t('Build my plan', 'আমার plan তৈরি করুন')} →</a>`;
      }
    }

    const roadmap = document.getElementById('domain-roadmap');
    if (roadmap) {
      const ordered = ['data-foundations', 'statistics', 'excel', 'sql', 'power-bi', 'python', 'projects'];
      roadmap.innerHTML = ordered.map((id, index) => {
        const domain = domainMap[id];
        return `<a class="domain-step ${domain.status}" href="${domain.url}"><span class="domain-step-number">${String(index + 1).padStart(2, '0')}</span><span><small>${statusLabel(domain.status)} · ${domain.release}</small><strong>${escapeHtml(t(domain.title_en, domain.title_bn))}</strong><p>${escapeHtml(t(domain.description_en, domain.description_bn))}</p></span><b>→</b></a>`;
      }).join('');
    }

    const featured = document.getElementById('featured-tools');
    if (featured) featured.innerHTML = DATA.tools.slice(0, 3).map(toolCard).join('');
  }

  function setupScroll() {
    const button = document.getElementById('scroll-top');
    const sync = () => {
      document.getElementById('site-header-bar')?.classList.toggle('scrolled', scrollY > 8);
      button?.classList.toggle('visible', scrollY > 500);
    };
    addEventListener('scroll', sync, { passive: true });
    button?.addEventListener('click', () => scrollTo({ top: 0, behavior: 'smooth' }));
    sync();
  }

  window.DLH = {
    DATA, moduleMap, topicMap, toolMap, pathMap, domainMap, careerPathMap, state, t,
    applyLanguage, setLanguage, setTheme, escapeHtml, safeStorage,
    getCompleted, setCompleted, getBookmarks, setBookmarks, isCompleted,
    toggleCompleted, toggleBookmark, toolCard, pathProgress, pathCard, moduleColor,
    getProfile, setProfile, clearProfile, levelStartIndex, getPlanTopics,
    getPlanProgress, getNextTopic, getNextPlanTopic, getRecommendedLab, modeLabel,
    statusLabel,
  };

  renderHeader();
  renderFooter();
  renderSearch();
  renderHome();
  setupScroll();
  window.addEventListener('dlh:profile', () => { renderHeader(); renderHome(); });
  window.addEventListener('dlh:progress', renderHome);
  window.addEventListener('dlh:language', renderHome);
  applyLanguage();
})();
