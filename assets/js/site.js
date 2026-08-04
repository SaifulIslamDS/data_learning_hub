(() => {
  'use strict';

  const DATA = window.SLH_CONTENT;
  if (!DATA) return;

  const icons = {
    logo: '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" d="M4 18V9m5 9V5m5 13v-7m5 7V3"/></svg>',
    search: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7" fill="none" stroke="currentColor" stroke-width="2"/><path d="m16 16 4 4" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
    sun: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 2v2m0 16v2M4.93 4.93l1.42 1.42m11.3 11.3 1.42 1.42M2 12h2m16 0h2M4.93 19.07l1.42-1.42m11.3-11.3 1.42-1.42" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
    moon: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 15.5A8.2 8.2 0 0 1 8.5 4 8.5 8.5 0 1 0 20 15.5Z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>',
    menu: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
    close: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m6 6 12 12M18 6 6 18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
    compass: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="m15.5 8.5-2 5-5 2 2-5 5-2Z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>',
  };

  const moduleMap = Object.fromEntries(DATA.modules.map(m => [m.id, m]));
  const topicMap = Object.fromEntries(DATA.topics.map(t => [t.id, t]));
  const toolMap = Object.fromEntries(DATA.tools.map(t => [t.id, t]));
  const pathMap = Object.fromEntries(DATA.paths.map(p => [p.id, p]));

  const safeStorage = {
    get(key, fallback = null) {
      try { return localStorage.getItem(key) ?? fallback; } catch { return fallback; }
    },
    set(key, value) {
      try { localStorage.setItem(key, value); } catch { /* storage can be unavailable */ }
    },
    remove(key) {
      try { localStorage.removeItem(key); } catch { /* storage can be unavailable */ }
    },
    json(key, fallback = []) {
      try { return JSON.parse(localStorage.getItem(key) || JSON.stringify(fallback)); } catch { return fallback; }
    },
  };

  const state = {
    language: safeStorage.get('slh-language', 'en'),
    theme: document.documentElement.dataset.theme || 'light',
  };

  function t(en, bn) { return state.language === 'bn' ? bn : en; }
  function escapeHtml(value) {
    return String(value ?? '').replace(/[&<>'"]/g, char => ({ '&':'&amp;', '<':'&lt;', '>':'&gt;', "'":'&#39;', '"':'&quot;' }[char]));
  }

  function getProfile() {
    const profile = safeStorage.json('slh-profile', null);
    return profile && pathMap[profile.goal] ? profile : null;
  }
  function setProfile(profile) {
    safeStorage.set('slh-profile', JSON.stringify(profile));
    window.dispatchEvent(new CustomEvent('slh:profile', { detail: profile }));
  }
  function clearProfile() {
    safeStorage.remove('slh-profile');
    window.dispatchEvent(new CustomEvent('slh:profile', { detail: null }));
  }
  function levelStartIndex(path, level = 'beginner') {
    if (!path?.topics?.length || level === 'beginner') return 0;
    const topics = path.topics.map(id => topicMap[id]).filter(Boolean);
    if (level === 'intermediate') {
      const index = topics.findIndex(topic => topic.difficulty !== 'Beginner');
      return Math.max(0, (index < 0 ? Math.floor(topics.length * .2) : index) - 1);
    }
    const index = topics.findIndex(topic => topic.difficulty === 'Advanced');
    return Math.max(0, (index < 0 ? Math.floor(topics.length * .5) : index) - 1);
  }
  function getPlanTopics(profile = getProfile()) {
    if (!profile) return [];
    const path = pathMap[profile.goal];
    const start = Number.isInteger(profile.startIndex) ? profile.startIndex : levelStartIndex(path, profile.level);
    return path.topics.slice(Math.max(0, start)).map(id => topicMap[id]).filter(Boolean);
  }
  function getPlanProgress(profile = getProfile()) {
    const topics = getPlanTopics(profile);
    const completed = getCompleted();
    const done = topics.filter(topic => completed.has(topic.id)).length;
    return { done, total: topics.length, percent: topics.length ? Math.round(done / topics.length * 100) : 0 };
  }
  function getNextTopic(profile = getProfile()) {
    const topics = getPlanTopics(profile);
    const completed = getCompleted();
    return topics.find(topic => !completed.has(topic.id)) || null;
  }
  function getNextPlanTopic(currentId, profile = getProfile()) {
    const topics = getPlanTopics(profile);
    const currentIndex = topics.findIndex(topic => topic.id === currentId);
    if (currentIndex >= 0) return topics.slice(currentIndex + 1).find(topic => !isCompleted(topic.id)) || topics[currentIndex + 1] || null;
    return getNextTopic(profile);
  }
  function getRecommendedLab(topic) {
    if (!topic) return null;
    if (topic.lab && toolMap[topic.lab]) return toolMap[topic.lab];
    const peers = DATA.topics.filter(item => item.module === topic.module && item.lab && toolMap[item.lab]);
    if (!peers.length) return null;
    peers.sort((a, b) => Math.abs(a.order - topic.order) - Math.abs(b.order - topic.order));
    return toolMap[peers[0].lab];
  }

  function applyLanguage(root = document) {
    document.documentElement.lang = state.language;
    root.querySelectorAll('[data-en][data-bn]').forEach(el => {
      el.textContent = state.language === 'bn' ? el.dataset.bn : el.dataset.en;
    });
    root.querySelectorAll('[data-placeholder-en][data-placeholder-bn]').forEach(el => {
      el.placeholder = state.language === 'bn' ? el.dataset.placeholderBn : el.dataset.placeholderEn;
    });
    document.querySelectorAll('.language-button').forEach(button => {
      const active = button.dataset.lang === state.language;
      button.classList.toggle('active', active);
      button.setAttribute('aria-pressed', String(active));
    });
    window.dispatchEvent(new CustomEvent('slh:language', { detail: state.language }));
  }

  function setLanguage(language) {
    state.language = language === 'bn' ? 'bn' : 'en';
    safeStorage.set('slh-language', state.language);
    applyLanguage();
  }

  function setTheme(theme) {
    state.theme = theme === 'dark' ? 'dark' : 'light';
    document.documentElement.dataset.theme = state.theme;
    safeStorage.set('slh-theme', state.theme);
    updateThemeButtons();
    window.dispatchEvent(new CustomEvent('slh:theme', { detail: state.theme }));
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
    const active = page === key || (page === 'topic' && key === 'catalog') || (page === 'tool' && key === 'tools');
    return `<a href="${href}" class="${active ? 'active' : ''}" data-en="${en}" data-bn="${bn}">${t(en,bn)}</a>`;
  }

  function languageSwitch() {
    return `<div class="language-switch" role="group" aria-label="Language"><button class="language-button ${state.language === 'en' ? 'active' : ''}" data-lang="en" type="button" aria-label="English" aria-pressed="${state.language === 'en'}">EN</button><button class="language-button ${state.language === 'bn' ? 'active' : ''}" data-lang="bn" type="button" aria-label="বাংলা" aria-pressed="${state.language === 'bn'}">BN</button></div>`;
  }

  function renderHeader() {
    const headerRoot = document.getElementById('site-header');
    if (!headerRoot) return;
    const profile = getProfile();
    const journeyHref = profile ? '/my-learning/' : '/start/';
    const journeyEn = profile ? 'My Learning' : 'Start Here';
    const journeyBn = profile ? 'আমার শেখা' : 'শুরু করুন';
    headerRoot.innerHTML = `<header class="site-header" id="site-header-bar"><div class="container navbar"><a class="brand" href="/" aria-label="Statistics Learning Hub home"><span class="brand-mark">${icons.logo}</span><span class="brand-text">Statistics Learning Hub<small data-en="One clear step at a time" data-bn="একবারে একটি পরিষ্কার ধাপ">${t('One clear step at a time','একবারে একটি পরিষ্কার ধাপ')}</small></span></a><nav class="nav-links" aria-label="Primary navigation">${navLink(journeyHref,journeyEn,journeyBn,profile ? 'my-learning' : 'start')}${navLink('/catalog/','Learn','শিখুন','catalog')}${navLink('/tools/','Practice','প্র্যাকটিস','tools')}${navLink('/paths/','Apply','প্রয়োগ','paths')}</nav><div class="nav-actions"><button class="icon-button" type="button" data-action="search" aria-label="${t('Open search','সার্চ খুলুন')}" title="${t('Open search','সার্চ খুলুন')}">${icons.search}</button>${languageSwitch()}<button class="icon-button" type="button" data-action="theme"></button><button class="menu-button" id="menu-button" type="button" aria-label="${t('Open navigation','নেভিগেশন খুলুন')}" aria-expanded="false">${icons.menu}</button></div></div><div class="container mobile-panel" id="mobile-panel">${navLink(journeyHref,journeyEn,journeyBn,profile ? 'my-learning' : 'start')}${navLink('/catalog/','Learn','শিখুন','catalog')}${navLink('/tools/','Practice','প্র্যাকটিস','tools')}${navLink('/paths/','Apply','প্রয়োগ','paths')}${navLink('/glossary/','Glossary','গ্লসারি','glossary')}${navLink('/about/','About','সম্পর্কে','about')}${languageSwitch()}</div></header>`;
    updateThemeButtons();

    headerRoot.querySelectorAll('.language-button').forEach(button => button.addEventListener('click', () => setLanguage(button.dataset.lang)));
    headerRoot.querySelectorAll('[data-action="theme"]').forEach(button => button.addEventListener('click', () => setTheme(state.theme === 'dark' ? 'light' : 'dark')));
    headerRoot.querySelectorAll('[data-action="search"]').forEach(button => button.addEventListener('click', openSearch));

    const menuButton = document.getElementById('menu-button');
    const mobilePanel = document.getElementById('mobile-panel');
    menuButton?.addEventListener('click', () => {
      const open = mobilePanel.classList.toggle('open');
      menuButton.setAttribute('aria-expanded', String(open));
      menuButton.innerHTML = open ? icons.close : icons.menu;
    });
  }

  function renderFooter() {
    const footerRoot = document.getElementById('site-footer');
    if (!footerRoot) return;
    footerRoot.innerHTML = `<footer class="site-footer"><div class="container footer-grid"><div class="footer-brand"><a class="brand" href="/"><span class="brand-mark">${icons.logo}</span><span class="brand-text">Statistics Learning Hub<small data-en="Guided · bilingual · interactive" data-bn="গাইডেড · দ্বিভাষিক · ইন্টারঅ্যাকটিভ">${t('Guided · bilingual · interactive','গাইডেড · দ্বিভাষিক · ইন্টারঅ্যাকটিভ')}</small></span></a><p data-en="Understand one concept, test it in a browser lab, then apply it to an analytical decision." data-bn="একটি ধারণা বুঝুন, ব্রাউজার ল্যাবে পরীক্ষা করুন, তারপর analytical decision-এ প্রয়োগ করুন।">${t('Understand one concept, test it in a browser lab, then apply it to an analytical decision.','একটি ধারণা বুঝুন, ব্রাউজার ল্যাবে পরীক্ষা করুন, তারপর analytical decision-এ প্রয়োগ করুন।')}</p></div><div class="footer-column"><h3 data-en="Your journey" data-bn="আপনার যাত্রা">${t('Your journey','আপনার যাত্রা')}</h3><a href="/start/" data-en="Build or change plan" data-bn="প্ল্যান তৈরি বা পরিবর্তন করুন">${t('Build or change plan','প্ল্যান তৈরি বা পরিবর্তন করুন')}</a><a href="/my-learning/" data-en="My Learning" data-bn="আমার শেখা">${t('My Learning','আমার শেখা')}</a><a href="/paths/" data-en="Career paths" data-bn="ক্যারিয়ার পাথ">${t('Career paths','ক্যারিয়ার পাথ')}</a></div><div class="footer-column"><h3 data-en="Explore" data-bn="এক্সপ্লোর">${t('Explore','এক্সপ্লোর')}</h3><a href="/catalog/" data-en="Lesson catalog" data-bn="লেসন ক্যাটালগ">${t('Lesson catalog','লেসন ক্যাটালগ')}</a><a href="/tools/" data-en="Interactive labs" data-bn="ইন্টারঅ্যাকটিভ ল্যাব">${t('Interactive labs','ইন্টারঅ্যাকটিভ ল্যাব')}</a><a href="/glossary/" data-en="Glossary" data-bn="গ্লসারি">${t('Glossary','গ্লসারি')}</a></div><div class="footer-column"><h3 data-en="Creator" data-bn="ক্রিয়েটর">${t('Creator','ক্রিয়েটর')}</h3><a href="https://saifulshuvo.com" target="_blank" rel="noopener noreferrer">Website ↗</a><a href="https://github.com/SaifulIslamDS/" target="_blank" rel="noopener noreferrer">GitHub ↗</a><a href="https://www.linkedin.com/in/saifulislampro/" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a></div></div><div class="container footer-bottom"><span data-en="Idea and developed by Saiful Islam." data-bn="Idea and developed by Saiful Islam.">${t('Idea and developed by Saiful Islam.','Idea and developed by Saiful Islam.')}</span><div class="footer-bottom-links"><a href="https://github.com/tafshir027/stats" target="_blank" rel="noopener noreferrer" data-en="Inspired by tafshir027/stats ↗" data-bn="tafshir027/stats দ্বারা অনুপ্রাণিত ↗">${t('Inspired by tafshir027/stats ↗','tafshir027/stats দ্বারা অনুপ্রাণিত ↗')}</a><a href="/about/" data-en="Privacy & credits" data-bn="প্রাইভেসি ও ক্রেডিট">${t('Privacy & credits','প্রাইভেসি ও ক্রেডিট')}</a></div></div></footer>`;
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
    if (!overlay) return;
    overlay.classList.remove('open');
    overlay.setAttribute('aria-hidden', 'true');
  }

  function searchItems(query) {
    const q = query.trim().toLowerCase();
    const items = [
      ...DATA.topics.map(item => ({ ...item, category: 'Lesson', icon: 'L' })),
      ...DATA.tools.map(item => ({ ...item, category: 'Lab', summary_en: item.description_en, summary_bn: item.description_bn, icon: '∑' })),
    ];
    if (!q) {
      const next = getNextTopic();
      const recommended = next ? [next, getRecommendedLab(next)].filter(Boolean) : [];
      return [...recommended, ...items].filter((item, index, all) => all.findIndex(x => x.url === item.url) === index).slice(0, 10);
    }
    return items.filter(item => [item.title_en, item.title_bn, item.summary_en, item.summary_bn, item.module].join(' ').toLowerCase().includes(q)).slice(0, 18);
  }

  function renderSearchResults(query) {
    const results = document.getElementById('global-search-results');
    if (!results) return;
    const found = searchItems(query);
    if (!found.length) {
      results.innerHTML = `<div class="search-empty" data-en="No matching lesson or lab was found." data-bn="মিল পাওয়া কোনো lesson বা lab নেই।">${t('No matching lesson or lab was found.','মিল পাওয়া কোনো lesson বা lab নেই।')}</div>`;
      return;
    }
    results.innerHTML = found.map(item => {
      const title = t(item.title_en, item.title_bn);
      const summary = t(item.summary_en || item.description_en, item.summary_bn || item.description_bn);
      return `<a class="search-result" href="/${item.url}"><span class="search-result-icon">${item.icon || 'L'}</span><span><strong>${escapeHtml(title)}</strong><small>${escapeHtml(summary)}</small></span><span>→</span></a>`;
    }).join('');
  }

  function renderSearch() {
    const root = document.getElementById('search-root');
    if (!root) return;
    root.innerHTML = `<div class="search-overlay" aria-hidden="true"><div class="search-dialog" role="dialog" aria-modal="true" aria-label="Site search"><div class="search-dialog-header">${icons.search}<input id="global-search-input" type="search" placeholder="${t('Search lessons and labs…','Lesson ও lab খুঁজুন…')}" data-placeholder-en="Search lessons and labs…" data-placeholder-bn="Lesson ও lab খুঁজুন…" aria-label="${t('Search lessons and labs','Lesson ও lab খুঁজুন')}"><button class="icon-button" id="close-search" type="button" aria-label="${t('Close search','সার্চ বন্ধ করুন')}">${icons.close}</button></div><div class="search-results" id="global-search-results"></div></div></div>`;
    const overlay = root.querySelector('.search-overlay');
    root.querySelector('#close-search')?.addEventListener('click', closeSearch);
    root.querySelector('#global-search-input')?.addEventListener('input', event => renderSearchResults(event.target.value));
    overlay?.addEventListener('click', event => { if (event.target === overlay) closeSearch(); });
    document.addEventListener('keydown', event => {
      if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 'k') { event.preventDefault(); openSearch(); }
      if (event.key === 'Escape') closeSearch();
    });
  }

  function getCompleted() { return new Set(safeStorage.json('slh-completed', [])); }
  function setCompleted(set) { safeStorage.set('slh-completed', JSON.stringify([...set])); }
  function getBookmarks() { return new Set(safeStorage.json('slh-bookmarks', [])); }
  function setBookmarks(set) { safeStorage.set('slh-bookmarks', JSON.stringify([...set])); }
  function isCompleted(id) { return getCompleted().has(id); }
  function toggleCompleted(id) {
    const completed = getCompleted();
    completed.has(id) ? completed.delete(id) : completed.add(id);
    setCompleted(completed);
    window.dispatchEvent(new CustomEvent('slh:progress'));
    return completed.has(id);
  }
  function toggleBookmark(id) {
    const bookmarks = getBookmarks();
    bookmarks.has(id) ? bookmarks.delete(id) : bookmarks.add(id);
    setBookmarks(bookmarks);
    window.dispatchEvent(new CustomEvent('slh:bookmarks'));
    return bookmarks.has(id);
  }

  function moduleColor(accent) {
    return ({ violet:'#7567ff', cyan:'#12a7b4', blue:'#3978ee', emerald:'#159a72', orange:'#df7f2c', pink:'#d8509a', indigo:'#6557d8', teal:'#168f8b', amber:'#c78a17' })[accent] || '#6557f5';
  }

  function toolCard(tool) {
    return `<a class="tool-card" href="/${tool.url}"><span class="tool-symbol">∑</span><div class="tool-meta"><span class="badge">${escapeHtml(t(moduleMap[tool.module]?.title_en || tool.module, moduleMap[tool.module]?.title_bn || tool.module))}</span></div><h3>${escapeHtml(t(tool.title_en, tool.title_bn))}</h3><p>${escapeHtml(t(tool.description_en, tool.description_bn))}</p><span class="card-footer"><span>${t('Open lab','ল্যাব খুলুন')}</span><span class="card-arrow">→</span></span></a>`;
  }

  function pathProgress(path) {
    const completed = getCompleted();
    const done = path.topics.filter(id => completed.has(id)).length;
    return { done, total: path.topics.length, percent: path.topics.length ? Math.round(done / path.topics.length * 100) : 0 };
  }

  function pathCard(path) {
    const progress = pathProgress(path);
    return `<a class="path-card" href="/paths/#${path.id}"><span class="eyebrow">${progress.total} ${t('steps','ধাপ')}</span><h3>${escapeHtml(t(path.title_en, path.title_bn))}</h3><p>${escapeHtml(t(path.description_en, path.description_bn))}</p><div class="progress-track" aria-label="${progress.percent}% completed"><span style="width:${progress.percent}%"></span></div><div class="path-summary"><span>${progress.done}/${progress.total} ${t('completed','সম্পন্ন')}</span><span>${progress.percent}%</span></div></a>`;
  }

  function modeLabel(mode) {
    return ({
      concepts: t('Concept-first','কনসেপ্ট-ফার্স্ট'),
      balanced: t('Balanced','ব্যালান্সড'),
      practice: t('Practice-first','প্র্যাকটিস-ফার্স্ট'),
    })[mode] || t('Balanced','ব্যালান্সড');
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
      primary.textContent = profile ? t('Continue my learning','আমার শেখা চালিয়ে যান') : t('Build my learning plan','আমার লার্নিং প্ল্যান তৈরি করুন');
    }
    if (secondary) {
      secondary.href = profile ? (next ? `/${next.url}` : '/paths/') : '/catalog/';
      secondary.textContent = profile ? (next ? t('Open next lesson','পরবর্তী লেসন খুলুন') : t('Explore another path','অন্য পাথ দেখুন')) : t('Explore without a plan','প্ল্যান ছাড়াই এক্সপ্লোর করুন');
    }

    const stats = document.getElementById('hero-stats');
    if (stats) stats.innerHTML = [
      [`${DATA.topics.length}`, t('lessons','লেসন')],
      [`${DATA.tools.length}`, t('labs','ল্যাব')],
      ['1', t('recommended next step','প্রস্তাবিত পরবর্তী ধাপ')],
    ].map(([value,label]) => `<span class="stat-chip"><strong>${value}</strong> ${label}</span>`).join('');

    const preview = document.getElementById('home-plan-preview');
    if (preview) {
      if (!profile) {
        preview.innerHTML = `<span class="guide-kicker">${icons.compass} ${t('Your guided route','আপনার গাইডেড রুট')}</span><h2>${t('No need to choose from 108 lessons.','১০৮টি লেসন থেকে বেছে নিতে হবে না।')}</h2><ol class="mini-route"><li><span>1</span><div><strong>${t('Tell us your goal','আপনার লক্ষ্য বলুন')}</strong><small>${t('Career, level and learning preference','ক্যারিয়ার, লেভেল ও শেখার পছন্দ')}</small></div></li><li><span>2</span><div><strong>${t('Receive a focused sequence','একটি ফোকাসড সিকোয়েন্স নিন')}</strong><small>${t('Only the next useful steps','শুধু প্রয়োজনীয় পরবর্তী ধাপ')}</small></div></li><li><span>3</span><div><strong>${t('Learn, practice and apply','শিখুন, প্র্যাকটিস করুন ও প্রয়োগ করুন')}</strong><small>${t('One session at a time','একবারে একটি সেশন')}</small></div></li></ol><a class="text-link" href="/start/">${t('Create my plan →','আমার প্ল্যান তৈরি করুন →')}</a>`;
      } else {
        preview.innerHTML = `<span class="guide-kicker">${icons.compass} ${t('Your active plan','আপনার সক্রিয় প্ল্যান')}</span><h2>${escapeHtml(t(path.title_en,path.title_bn))}</h2><p>${escapeHtml(modeLabel(profile.mode))} · ${progress.done}/${progress.total} ${t('steps complete','ধাপ সম্পন্ন')}</p><div class="progress-track"><span style="width:${progress.percent}%"></span></div>${next ? `<div class="next-mini"><small>${t('Next lesson','পরবর্তী লেসন')}</small><strong>${escapeHtml(t(next.title_en,next.title_bn))}</strong><a class="button primary" href="/${next.url}">${t('Continue','চালিয়ে যান')} →</a></div>` : `<div class="next-mini"><strong>${t('You completed this plan.','আপনি এই পাথ সম্পন্ন করেছেন।')}</strong><a class="button primary" href="/paths/">${t('Choose another path','অন্য পাথ বেছে নিন')}</a></div>`}`;
      }
    }

    const method = document.getElementById('home-method-grid');
    if (method) method.innerHTML = [
      ['01', t('Learn','শিখুন'), t('Understand the idea, assumptions and language before calculating.','হিসাবের আগে ধারণা, assumption ও ভাষা বুঝুন।'), '/catalog/'],
      ['02', t('Practice','প্র্যাকটিস'), t('Change inputs in a browser lab and observe what changes.','ব্রাউজার ল্যাবে input বদলে ফলাফলের পরিবর্তন দেখুন।'), '/tools/'],
      ['03', t('Apply','প্রয়োগ'), t('Explain the result in context and connect it to real analytical work.','ফলাফল context-এ ব্যাখ্যা করে বাস্তব analytical work-এর সঙ্গে যুক্ত করুন।'), '/paths/'],
    ].map(([n,title,description,url]) => `<a class="method-card" href="${url}"><span>${n}</span><h3>${escapeHtml(title)}</h3><p>${escapeHtml(description)}</p><strong>${t('Explore','দেখুন')} →</strong></a>`).join('');

    const nextStep = document.getElementById('home-next-step');
    if (nextStep) {
      if (profile && next) {
        const lab = getRecommendedLab(next);
        nextStep.innerHTML = `<div><span class="eyebrow">${t('Your next focused session','আপনার পরবর্তী ফোকাসড সেশন')}</span><h2>${escapeHtml(t(next.title_en,next.title_bn))}</h2><p>${escapeHtml(t(next.summary_en,next.summary_bn))}</p><div class="session-pills"><span>1 · ${t('Understand','বুঝুন')}</span>${lab ? `<span>2 · ${t('Try the lab','ল্যাব করুন')}</span>` : ''}<span>${lab ? '3' : '2'} · ${t('Explain in your words','নিজের ভাষায় ব্যাখ্যা করুন')}</span></div></div><div class="next-step-actions"><a class="button primary" href="/${next.url}">${t('Start this lesson','এই লেসন শুরু করুন')}</a><a class="button ghost" href="/my-learning/">${t('View my plan','আমার প্ল্যান দেখুন')}</a></div>`;
      } else {
        nextStep.innerHTML = `<div><span class="eyebrow">${t('Start without overwhelm','চাপ ছাড়াই শুরু করুন')}</span><h2>${t('A short setup turns the full library into one clear route.','একটি ছোট setup পুরো library-কে একটি পরিষ্কার route-এ রূপ দেয়।')}</h2><p>${t('Choose your goal, current level and preferred learning style. The plan stays only in your browser.','আপনার লক্ষ্য, বর্তমান লেভেল ও শেখার ধরন বেছে নিন। প্ল্যান শুধু আপনার ব্রাউজারেই থাকবে।')}</p></div><a class="button primary" href="/start/">${t('Build my plan','আমার প্ল্যান তৈরি করুন')} →</a>`;
      }
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

  window.SLH = {
    DATA, moduleMap, topicMap, toolMap, pathMap, state, t, applyLanguage, setLanguage, setTheme,
    escapeHtml, safeStorage, getCompleted, setCompleted, getBookmarks, setBookmarks,
    isCompleted, toggleCompleted, toggleBookmark, toolCard, pathProgress, pathCard, moduleColor,
    getProfile, setProfile, clearProfile, levelStartIndex, getPlanTopics, getPlanProgress,
    getNextTopic, getNextPlanTopic, getRecommendedLab, modeLabel,
  };

  renderHeader();
  renderFooter();
  renderSearch();
  renderHome();
  setupScroll();
  window.addEventListener('slh:profile', () => { renderHeader(); renderHome(); });
  window.addEventListener('slh:progress', renderHome);
  window.addEventListener('slh:language', renderHome);
  applyLanguage();
})();
