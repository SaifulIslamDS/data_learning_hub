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
    bookmark: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18l-6-4-6 4Z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>',
  };

  const moduleMap = Object.fromEntries(DATA.modules.map(m => [m.id, m]));
  const topicMap = Object.fromEntries(DATA.topics.map(t => [t.id, t]));
  const toolMap = Object.fromEntries(DATA.tools.map(t => [t.id, t]));

  const safeStorage = {
    get(key, fallback = null) {
      try { return localStorage.getItem(key) ?? fallback; } catch { return fallback; }
    },
    set(key, value) {
      try { localStorage.setItem(key, value); } catch { /* storage can be unavailable */ }
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
    headerRoot.innerHTML = `<header class="site-header" id="site-header-bar"><div class="container navbar"><a class="brand" href="/" aria-label="Statistics Learning Hub home"><span class="brand-mark">${icons.logo}</span><span class="brand-text">Statistics Learning Hub<small data-en="Learn with evidence" data-bn="প্রমাণের সঙ্গে শিখুন">${t('Learn with evidence','প্রমাণের সঙ্গে শিখুন')}</small></span></a><nav class="nav-links" aria-label="Primary navigation">${navLink('/catalog/','Lessons','লেসন','catalog')}${navLink('/tools/','Labs','ল্যাব','tools')}${navLink('/paths/','Paths','পাথ','paths')}${navLink('/glossary/','Glossary','গ্লসারি','glossary')}${navLink('/about/','About','সম্পর্কে','about')}</nav><div class="nav-actions"><button class="icon-button" type="button" data-action="search" aria-label="${t('Open search','সার্চ খুলুন')}" title="${t('Open search','সার্চ খুলুন')}">${icons.search}</button>${languageSwitch()}<button class="icon-button" type="button" data-action="theme"></button><button class="menu-button" id="menu-button" type="button" aria-label="${t('Open navigation','নেভিগেশন খুলুন')}" aria-expanded="false">${icons.menu}</button></div></div><div class="container mobile-panel" id="mobile-panel">${navLink('/catalog/','Lessons','লেসন','catalog')}${navLink('/tools/','Labs','ল্যাব','tools')}${navLink('/paths/','Paths','পাথ','paths')}${navLink('/glossary/','Glossary','গ্লসারি','glossary')}${navLink('/about/','About','সম্পর্কে','about')}${languageSwitch()}</div></header>`;
    updateThemeButtons();

    headerRoot.querySelectorAll('.language-button').forEach(button => button.addEventListener('click', () => setLanguage(button.dataset.lang)));
    headerRoot.querySelectorAll('[data-action="theme"]').forEach(button => button.addEventListener('click', () => setTheme(state.theme === 'dark' ? 'light' : 'dark')));
    headerRoot.querySelectorAll('[data-action="search"]').forEach(button => button.addEventListener('click', openSearch));

    const menuButton = document.getElementById('menu-button');
    const mobilePanel = document.getElementById('mobile-panel');
    menuButton.addEventListener('click', () => {
      const open = mobilePanel.classList.toggle('open');
      menuButton.setAttribute('aria-expanded', String(open));
      menuButton.innerHTML = open ? icons.close : icons.menu;
    });
  }

  function renderFooter() {
    const footerRoot = document.getElementById('site-footer');
    footerRoot.innerHTML = `<footer class="site-footer"><div class="container footer-grid"><div class="footer-brand"><a class="brand" href="/"><span class="brand-mark">${icons.logo}</span><span class="brand-text">Statistics Learning Hub<small data-en="Static · bilingual · interactive" data-bn="স্ট্যাটিক · দ্বিভাষিক · ইন্টারঅ্যাকটিভ">${t('Static · bilingual · interactive','স্ট্যাটিক · দ্বিভাষিক · ইন্টারঅ্যাকটিভ')}</small></span></a><p data-en="A structured learning hub for statistics, analytics, data science and data engineering—without accounts, backend services or data collection." data-bn="পরিসংখ্যান, অ্যানালিটিক্স, ডেটা সায়েন্স ও ডেটা ইঞ্জিনিয়ারিংয়ের structured learning hub—account, backend service বা data collection ছাড়া।">${t('A structured learning hub for statistics, analytics, data science and data engineering—without accounts, backend services or data collection.','পরিসংখ্যান, অ্যানালিটিক্স, ডেটা সায়েন্স ও ডেটা ইঞ্জিনিয়ারিংয়ের structured learning hub—account, backend service বা data collection ছাড়া।')}</p></div><div class="footer-column"><h3 data-en="Learn" data-bn="শিখুন">${t('Learn','শিখুন')}</h3><a href="/catalog/" data-en="Lesson catalog" data-bn="লেসন ক্যাটালগ">${t('Lesson catalog','লেসন ক্যাটালগ')}</a><a href="/paths/" data-en="Career paths" data-bn="ক্যারিয়ার পাথ">${t('Career paths','ক্যারিয়ার পাথ')}</a><a href="/glossary/" data-en="Glossary" data-bn="গ্লসারি">${t('Glossary','গ্লসারি')}</a></div><div class="footer-column"><h3 data-en="Practice" data-bn="প্র্যাকটিস">${t('Practice','প্র্যাকটিস')}</h3><a href="/tools/" data-en="Interactive labs" data-bn="ইন্টারঅ্যাকটিভ ল্যাব">${t('Interactive labs','ইন্টারঅ্যাকটিভ ল্যাব')}</a><a href="/tools/summary-statistics/">Summary statistics</a><a href="/tools/linear-regression/">Linear regression</a></div><div class="footer-column"><h3 data-en="Creator" data-bn="ক্রিয়েটর">${t('Creator','ক্রিয়েটর')}</h3><a href="https://saifulshuvo.com" target="_blank" rel="noopener noreferrer">Website ↗</a><a href="https://github.com/SaifulIslamDS/" target="_blank" rel="noopener noreferrer">GitHub ↗</a><a href="https://www.linkedin.com/in/saifulislampro/" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a></div></div><div class="container footer-bottom"><span data-en="Idea and developed by Saiful Islam." data-bn="Idea and developed by Saiful Islam.">${t('Idea and developed by Saiful Islam.','Idea and developed by Saiful Islam.')}</span><div class="footer-bottom-links"><a href="https://github.com/tafshir027/stats" target="_blank" rel="noopener noreferrer" data-en="Inspired by tafshir027/stats ↗" data-bn="tafshir027/stats দ্বারা অনুপ্রাণিত ↗">${t('Inspired by tafshir027/stats ↗','tafshir027/stats দ্বারা অনুপ্রাণিত ↗')}</a><a href="/about/" data-en="Privacy & credits" data-bn="প্রাইভেসি ও ক্রেডিট">${t('Privacy & credits','প্রাইভেসি ও ক্রেডিট')}</a></div></div></footer>`;
  }

  function openSearch() {
    const overlay = document.querySelector('.search-overlay');
    overlay.classList.add('open');
    overlay.setAttribute('aria-hidden', 'false');
    const input = overlay.querySelector('#global-search-input');
    input.value = '';
    renderSearchResults('');
    setTimeout(() => input.focus(), 20);
  }

  function closeSearch() {
    const overlay = document.querySelector('.search-overlay');
    overlay.classList.remove('open');
    overlay.setAttribute('aria-hidden', 'true');
  }

  function searchItems(query) {
    const q = query.trim().toLowerCase();
    const items = [
      ...DATA.topics.map(item => ({ ...item, category: 'Lesson', icon: 'L' })),
      ...DATA.tools.map(item => ({ ...item, category: 'Lab', summary_en: item.description_en, summary_bn: item.description_bn, icon: '∑' })),
    ];
    if (!q) return items.slice(0, 10);
    return items.filter(item => [item.title_en, item.title_bn, item.summary_en, item.summary_bn, item.module].join(' ').toLowerCase().includes(q)).slice(0, 18);
  }

  function renderSearchResults(query) {
    const results = document.getElementById('global-search-results');
    const found = searchItems(query);
    if (!found.length) {
      results.innerHTML = `<div class="search-empty" data-en="No matching lesson or lab was found." data-bn="মিল পাওয়া কোনো lesson বা lab নেই।">${t('No matching lesson or lab was found.','মিল পাওয়া কোনো lesson বা lab নেই।')}</div>`;
      return;
    }
    results.innerHTML = found.map(item => {
      const title = t(item.title_en, item.title_bn);
      const summary = t(item.summary_en || item.description_en, item.summary_bn || item.description_bn);
      return `<a class="search-result" href="/${item.url}"><span class="search-result-icon">${item.icon}</span><span><strong>${escapeHtml(title)}</strong><small>${escapeHtml(summary)}</small></span><span>→</span></a>`;
    }).join('');
  }

  function renderSearch() {
    const root = document.getElementById('search-root');
    root.innerHTML = `<div class="search-overlay" aria-hidden="true"><div class="search-dialog" role="dialog" aria-modal="true" aria-label="Site search"><div class="search-dialog-header">${icons.search}<input id="global-search-input" type="search" placeholder="${t('Search lessons and labs…','Lesson ও lab খুঁজুন…')}" aria-label="${t('Search lessons and labs','Lesson ও lab খুঁজুন')}"><button class="icon-button" id="close-search" type="button" aria-label="${t('Close search','সার্চ বন্ধ করুন')}">${icons.close}</button></div><div class="search-results" id="global-search-results"></div></div></div>`;
    const overlay = root.querySelector('.search-overlay');
    root.querySelector('#close-search').addEventListener('click', closeSearch);
    root.querySelector('#global-search-input').addEventListener('input', e => renderSearchResults(e.target.value));
    overlay.addEventListener('click', event => { if (event.target === overlay) closeSearch(); });
    document.addEventListener('keydown', event => {
      if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 'k') { event.preventDefault(); openSearch(); }
      if (event.key === 'Escape') closeSearch();
    });
  }

  function escapeHtml(value) {
    return String(value ?? '').replace(/[&<>'"]/g, char => ({ '&':'&amp;', '<':'&lt;', '>':'&gt;', "'":'&#39;', '"':'&quot;' }[char]));
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
    return bookmarks.has(id);
  }

  function moduleColor(accent) {
    return ({ violet:'#7567ff', cyan:'#12a7b4', blue:'#3978ee', emerald:'#159a72', orange:'#df7f2c', pink:'#d8509a', indigo:'#6557d8', teal:'#168f8b', amber:'#c78a17' })[accent] || '#6557f5';
  }

  function renderHome() {
    if (document.body.dataset.page !== 'home') return;
    const stats = document.getElementById('hero-stats');
    stats.innerHTML = [
      [`${DATA.topics.length}`, t('complete lessons','পূর্ণাঙ্গ লেসন')],
      [`${DATA.tools.length}`, t('interactive labs','ইন্টারঅ্যাকটিভ ল্যাব')],
      [`${DATA.modules.length}`, t('learning modules','লার্নিং মডিউল')],
      ['0', t('dead links','ডেড লিংক')],
    ].map(([value,label]) => `<span class="stat-chip"><strong>${value}</strong> ${label}</span>`).join('');

    document.getElementById('module-grid').innerHTML = DATA.modules.map((module, index) => {
      const color = moduleColor(module.accent);
      const title = t(module.title_en, module.title_bn);
      const description = t(module.description_en, module.description_bn);
      return `<a class="module-card" style="--accent:${color}" href="/catalog/?module=${module.id}"><span class="module-icon">${String(index + 1).padStart(2,'0')}</span><h3>${escapeHtml(title)}</h3><p>${escapeHtml(description)}</p><span class="card-footer"><span>${module.topics.length} ${t('lessons','লেসন')}</span><span class="card-arrow">→</span></span></a>`;
    }).join('');

    document.getElementById('featured-tools').innerHTML = DATA.tools.slice(0, 8).map(tool => toolCard(tool)).join('');
    document.getElementById('featured-paths').innerHTML = DATA.paths.map(path => pathCard(path)).join('');
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

  function setupScroll() {
    const header = document.getElementById('site-header-bar');
    const button = document.getElementById('scroll-top');
    const sync = () => {
      header?.classList.toggle('scrolled', scrollY > 8);
      button?.classList.toggle('visible', scrollY > 500);
    };
    addEventListener('scroll', sync, { passive: true });
    button?.addEventListener('click', () => scrollTo({ top: 0, behavior: 'smooth' }));
    sync();
  }

  window.SLH = {
    DATA, moduleMap, topicMap, toolMap, state, t, applyLanguage, setLanguage, setTheme,
    escapeHtml, safeStorage, getCompleted, setCompleted, getBookmarks, setBookmarks,
    isCompleted, toggleCompleted, toggleBookmark, toolCard, pathProgress, pathCard, moduleColor,
  };

  renderHeader();
  renderFooter();
  renderSearch();
  renderHome();
  setupScroll();
  applyLanguage();
})();
