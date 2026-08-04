(() => {
  'use strict';
  const {
    DATA, topicMap, pathMap, t, escapeHtml, getCompleted, getProfile, setProfile,
    pathProgress, levelStartIndex,
  } = window.SLH;
  const selector = document.getElementById('path-selector');
  const detailRoot = document.getElementById('path-detail-root');
  if (!selector || !detailRoot) return;

  const hashId = location.hash.replace('#','');
  let selectedId = pathMap[hashId] ? hashId : (getProfile()?.goal || DATA.paths[0].id);

  const phaseLabels = [
    ['Phase 1 · Foundations', 'পর্যায় ১ · ভিত্তি'],
    ['Phase 2 · Core skills', 'পর্যায় ২ · মূল দক্ষতা'],
    ['Phase 3 · Applied practice', 'পর্যায় ৩ · প্রয়োগভিত্তিক প্র্যাকটিস'],
    ['Phase 4 · Decision-ready work', 'পর্যায় ৪ · সিদ্ধান্তযোগ্য কাজ'],
  ];

  function splitPhases(items) {
    const size = Math.ceil(items.length / 4);
    return Array.from({ length: 4 }, (_, index) => items.slice(index * size, Math.min(items.length, (index + 1) * size))).filter(group => group.length);
  }

  function renderSelector() {
    const activeProfile = getProfile();
    selector.innerHTML = DATA.paths.map(path => {
      const progress = pathProgress(path);
      const active = path.id === selectedId;
      const chosen = activeProfile?.goal === path.id;
      return `<button class="path-choice ${active ? 'selected' : ''}" type="button" data-path="${path.id}"><span class="path-choice-top"><strong>${escapeHtml(t(path.title_en,path.title_bn))}</strong>${chosen ? `<span class="badge">${t('My plan','আমার প্ল্যান')}</span>` : ''}</span><small>${path.topics.length} ${t('steps','ধাপ')} · ${progress.percent}% ${t('complete','সম্পন্ন')}</small></button>`;
    }).join('');
    selector.querySelectorAll('[data-path]').forEach(button => button.addEventListener('click', () => {
      selectedId = button.dataset.path;
      history.replaceState(null, '', `#${selectedId}`);
      render();
    }));
  }

  function renderDetail() {
    const path = pathMap[selectedId];
    const activeProfile = getProfile();
    const completed = getCompleted();
    const progress = pathProgress(path);
    const topics = path.topics.map(id => topicMap[id]).filter(Boolean);
    const phases = splitPhases(topics);
    const next = topics.find(topic => !completed.has(topic.id));
    const isActive = activeProfile?.goal === path.id;

    detailRoot.innerHTML = `<section class="selected-path-hero"><div><span class="eyebrow">${t('Guided career route','গাইডেড career route')}</span><h2>${escapeHtml(t(path.title_en,path.title_bn))}</h2><p>${escapeHtml(t(path.description_en,path.description_bn))}</p><div class="path-facts"><span>${topics.length} ${t('focused lessons','focused lesson')}</span><span>${phases.length} ${t('manageable phases','সহজ phase')}</span><span>${progress.percent}% ${t('complete','সম্পন্ন')}</span></div></div><div class="selected-path-actions">${isActive ? `<a class="button primary" href="/my-learning/">${t('Continue my plan','আমার প্ল্যান চালিয়ে যান')} →</a><a class="button ghost" href="/start/">${t('Adjust plan','প্ল্যান পরিবর্তন')}</a>` : `<button class="button primary" id="use-path" type="button">${t('Use this path','এই path ব্যবহার করুন')}</button>`}</div></section><div class="phase-stack">${phases.map((phase,index) => {
      const phaseDone = phase.filter(topic => completed.has(topic.id)).length;
      const hasNext = next && phase.some(topic => topic.id === next.id);
      return `<details class="path-phase" ${hasNext || (!next && index === phases.length - 1) || (next && index === 0 && progress.done === 0) ? 'open' : ''}><summary><span><small>${t(...phaseLabels[index])}</small><strong>${phaseDone}/${phase.length} ${t('completed','সম্পন্ন')}</strong></span><span>＋</span></summary><div class="phase-lessons">${phase.map((topic,topicIndex) => `<a class="phase-lesson ${completed.has(topic.id) ? 'done' : ''} ${next?.id === topic.id ? 'current' : ''}" href="/${topic.url}"><span>${completed.has(topic.id) ? '✓' : topicIndex + 1}</span><div><strong>${escapeHtml(t(topic.title_en,topic.title_bn))}</strong><small>${topic.minutes} ${t('min','মিনিট')} · ${escapeHtml(t(topic.difficulty,({Beginner:'বিগিনার',Intermediate:'ইন্টারমিডিয়েট',Advanced:'অ্যাডভান্সড'})[topic.difficulty]))}</small></div>${next?.id === topic.id ? `<em>${t('Next','পরবর্তী')}</em>` : ''}</a>`).join('')}</div></details>`;
    }).join('')}</div>`;

    document.getElementById('use-path')?.addEventListener('click', () => {
      const current = getProfile();
      const level = current?.level || 'beginner';
      setProfile({
        goal: path.id,
        level,
        mode: current?.mode || 'balanced',
        startIndex: levelStartIndex(path, level),
        createdAt: current?.createdAt || new Date().toISOString(),
        updatedAt: new Date().toISOString(),
      });
      location.href = '/my-learning/?new=1';
    });
  }

  function render() {
    renderSelector();
    renderDetail();
  }

  window.addEventListener('slh:language', render);
  window.addEventListener('slh:progress', render);
  window.addEventListener('slh:profile', render);
  render();
})();
