(() => {
  'use strict';
  const {
    DATA, pathMap, topicMap, t, escapeHtml, getProfile, getPlanTopics, getPlanProgress,
    getNextTopic, getRecommendedLab, getCompleted, getBookmarks, setCompleted, modeLabel,
    statusLabel,
  } = window.DLH;
  const root = document.getElementById('learning-dashboard');
  if (!root) return;

  function sessionSteps(profile, next, lab) {
    const total = Number(profile.time || 40);
    const concept = Math.max(8, Math.round(total * (profile.mode === 'practice' ? 0.25 : profile.mode === 'concepts' ? 0.5 : 0.38)));
    const practice = Math.max(5, Math.round(total * (profile.mode === 'practice' ? 0.5 : profile.mode === 'concepts' ? 0.22 : 0.34)));
    const explain = Math.max(5, total - concept - practice);
    const items = [
      { title:t('Learn', 'শিখুন'), time:concept, text:t(`Read “${next?.title_en || 'the lesson'}” and identify the core idea, data requirements and limitations.`, `“${next?.title_bn || 'lesson'}” পড়ে core idea, data requirement ও limitation শনাক্ত করুন।`) },
      { title:lab ? t('Practice', 'Practice') : t('Work an example', 'Example করুন'), time:practice, text:lab ? t(`Run ${lab.title_en}, then change one input and observe the effect.`, `${lab.title_bn} run করে একটি input বদলে effect দেখুন।`) : t('Create a small example, organize the data and follow the lesson workflow.', 'একটি ছোট example তৈরি করে data organize করুন এবং lesson workflow অনুসরণ করুন।') },
      { title:t('Explain', 'ব্যাখ্যা করুন'), time:explain, text:t('Write what the evidence shows, why it matters and one limitation.', 'Evidence কী দেখায়, কেন গুরুত্বপূর্ণ এবং একটি limitation লিখুন।') },
    ];
    return profile.mode === 'practice' ? [items[1], items[0], items[2]] : items;
  }

  function visibleRoadmap(topics, completed, next) {
    const currentIndex = next ? topics.findIndex(topic => topic.id === next.id) : topics.length;
    const start = Math.max(0, currentIndex - 1);
    return topics.slice(start, start + 5).map((topic, index) => {
      const done = completed.has(topic.id);
      const current = next?.id === topic.id;
      return `<a class="roadmap-row ${done ? 'done' : ''} ${current ? 'current' : ''}" href="/${topic.url}"><span class="roadmap-status">${done ? '✓' : current ? '→' : start + index + 1}</span><span><strong>${escapeHtml(t(topic.title_en, topic.title_bn))}</strong><small>${topic.minutes} ${t('min', 'মিনিট')} · ${escapeHtml(t(topic.difficulty, ({ Beginner:'বিগিনার', Intermediate:'ইন্টারমিডিয়েট', Advanced:'অ্যাডভান্সড' })[topic.difficulty]))}</small></span>${current ? `<span class="badge">${t('Next', 'পরবর্তী')}</span>` : ''}</a>`;
    }).join('');
  }

  function phaseRoadmap() {
    const career = DATA.career_paths.find(item => item.id === 'data-analyst');
    return career.phases.map((phase, index) => `<div class="journey-phase ${phase.status}"><span>${String(index + 1).padStart(2, '0')}</span><div><small>${statusLabel(phase.status)} · ${phase.release}</small><strong>${escapeHtml(t(phase.title_en, phase.title_bn))}</strong></div></div>`).join('');
  }

  function render() {
    const profile = getProfile();
    if (!profile) {
      root.innerHTML = `<section class="empty-dashboard"><span class="eyebrow">${t('My Learning', 'আমার শেখা')}</span><h1>${t('Create a focused Data Analyst plan first.', 'প্রথমে focused Data Analyst plan তৈরি করুন।')}</h1><p>${t('The setup uses your experience, study time and preferred learning style to choose one next lesson.', 'Setup আপনার experience, study time ও learning style দিয়ে একটি next lesson বেছে নেয়।')}</p><a class="button primary" href="/start/">${t('Build my plan', 'আমার plan তৈরি করুন')} →</a></section>`;
      return;
    }

    const path = pathMap[profile.goal] || pathMap['data-analyst'];
    const topics = getPlanTopics(profile);
    const progress = getPlanProgress(profile);
    const next = getNextTopic(profile);
    const lab = getRecommendedLab(next);
    const completed = getCompleted();
    const bookmarks = getBookmarks();
    const bookmarked = [...bookmarks].map(id => topicMap[id]).filter(Boolean).slice(0, 5);
    const steps = sessionSteps(profile, next, lab);
    const knownTools = profile.knowledge?.length ? profile.knowledge.map(value => ({ excel:'Excel', sql:'SQL', 'power-bi':'Power BI', python:'Python' })[value]).filter(Boolean).join(', ') : t('No prior tool experience selected', 'কোনো prior tool experience select করা হয়নি');

    root.innerHTML = `<section class="dashboard-header"><div><span class="eyebrow">${t('My Learning', 'আমার শেখা')}</span><h1>${escapeHtml(t(path.title_en, path.title_bn))}</h1><p>${t('This dashboard shows only the active foundation. Future tool phases stay visible as a roadmap, not as unfinished tasks.', 'Dashboard শুধু active foundation দেখায়। Future tool phase roadmap হিসেবে visible থাকে, unfinished task হিসেবে নয়।')}</p></div><div class="dashboard-profile"><span>${modeLabel(profile.mode)}</span><span>${profile.time || 40} ${t('min/session', 'মিনিট/session')}</span><a href="/start/">${t('Change plan', 'Plan বদলান')}</a></div></section>
    <section class="dashboard-progress-card"><div><span class="eyebrow">${t('Current foundation progress', 'Current foundation progress')}</span><h2>${progress.done}/${progress.total} ${t('available lessons complete', 'available lesson complete')}</h2></div><div class="progress-track large"><span style="width:${progress.percent}%"></span></div><strong>${progress.percent}%</strong></section>
    ${next ? `<section class="next-session-card"><div class="next-session-copy"><span class="eyebrow">${t('Your next focused session', 'আপনার next focused session')}</span><h2>${escapeHtml(t(next.title_en, next.title_bn))}</h2><p>${escapeHtml(t(next.summary_en, next.summary_bn))}</p><div class="next-meta"><span>${next.minutes} ${t('minute lesson', 'মিনিটের lesson')}</span>${lab ? `<span>${t('Related lab', 'Related lab')}: ${escapeHtml(t(lab.title_en, lab.title_bn))}</span>` : ''}</div><div class="hero-actions"><a class="button primary" href="/${next.url}">${t('Start lesson', 'Lesson শুরু করুন')} →</a>${lab && profile.mode === 'practice' ? `<a class="button ghost" href="/${lab.url}">${t('Start with the lab', 'Lab দিয়ে শুরু করুন')}</a>` : ''}</div></div><div class="session-plan"><h3>${t('Your session plan', 'আপনার session plan')}</h3>${steps.map((item, index) => `<div class="session-step"><span>${index + 1}</span><div><strong>${escapeHtml(item.title)}</strong><p>${escapeHtml(item.text)}</p></div><small>${item.time} ${t('min', 'মিনিট')}</small></div>`).join('')}</div></section>` : `<section class="completion-card"><span>✓</span><div><h2>${t('You completed the currently available foundation.', 'আপনি currently available foundation complete করেছেন।')}</h2><p>${t('Review bookmarks, complete the foundation project or inspect the next tool-track curriculum.', 'Bookmark review, foundation project complete অথবা next tool-track curriculum দেখুন।')}</p></div><a class="button primary" href="/projects/retail-sales-foundations/">${t('Open foundation project', 'Foundation project খুলুন')}</a></section>`}
    <section class="dashboard-grid"><article class="dashboard-panel"><div class="panel-heading"><div><span class="eyebrow">${t('Now, next, later', 'এখন, এরপর, পরে')}</span><h2>${t('Only the next few lessons', 'শুধু পরবর্তী কয়েকটি lesson')}</h2></div><a class="text-link" href="/learn/">${t('Open full available library →', 'Full available library →')}</a></div><div class="roadmap-list">${visibleRoadmap(topics, completed, next)}</div></article><aside class="dashboard-side"><section class="dashboard-panel"><span class="eyebrow">${t('Your preferences', 'আপনার preference')}</span><h2>${t('Learning setup', 'Learning setup')}</h2><dl class="profile-facts"><div><dt>${t('Level', 'Level')}</dt><dd>${escapeHtml(profile.level)}</dd></div><div><dt>${t('Study time', 'Study time')}</dt><dd>${profile.time || 40} ${t('minutes', 'মিনিট')}</dd></div><div><dt>${t('Known tools', 'Known tool')}</dt><dd>${escapeHtml(knownTools)}</dd></div></dl></section><section class="dashboard-panel"><span class="eyebrow">${t('Bookmarks', 'Bookmark')}</span><h2>${t('Saved for review', 'Review-এর জন্য save')}</h2>${bookmarked.length ? `<div class="bookmark-list">${bookmarked.map(topic => `<a href="/${topic.url}"><strong>${escapeHtml(t(topic.title_en, topic.title_bn))}</strong><small>${escapeHtml(t(topic.summary_en, topic.summary_bn))}</small></a>`).join('')}</div>` : `<p class="muted">${t('Bookmark difficult lessons and they will appear here.', 'কঠিন lesson bookmark করলে এখানে দেখাবে।')}</p>`}</section><section class="dashboard-panel danger-zone"><h2>${t('Progress controls', 'Progress control')}</h2><button class="button ghost" type="button" id="reset-progress">${t('Reset completed lessons', 'Completed lesson reset করুন')}</button></section></aside></section>
    <section class="dashboard-panel journey-map-panel"><div class="panel-heading"><div><span class="eyebrow">${t('Complete Data Analyst journey', 'Complete Data Analyst journey')}</span><h2>${t('Your current work is only phases 1 and 2', 'Current কাজ শুধু phase 1 ও 2')}</h2><p>${t('Curriculum-ready phases are visible so you know where the platform is going, but they are not added to your immediate task list.', 'Curriculum-ready phase visible যাতে roadmap বোঝেন, কিন্তু immediate task list-এ যোগ হয় না।')}</p></div><a class="text-link" href="/curriculum/">${t('View curriculum →', 'Curriculum দেখুন →')}</a></div><div class="journey-phase-grid">${phaseRoadmap()}</div></section>`;

    document.getElementById('reset-progress')?.addEventListener('click', () => {
      if (!confirm(t('Reset all completed lessons on this browser?', 'এই browser-এর সব completed lesson reset করবেন?'))) return;
      setCompleted(new Set());
      window.dispatchEvent(new CustomEvent('dlh:progress'));
      render();
    });
  }

  window.addEventListener('dlh:language', render);
  window.addEventListener('dlh:progress', render);
  window.addEventListener('dlh:bookmarks', render);
  render();
})();
