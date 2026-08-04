(() => {
  'use strict';
  const {
    pathMap, topicMap, t, escapeHtml, getProfile, getPlanTopics, getPlanProgress,
    getNextTopic, getRecommendedLab, getCompleted, getBookmarks, setCompleted,
    modeLabel,
  } = window.SLH;
  const root = document.getElementById('learning-dashboard');
  if (!root) return;

  const applyPrompts = {
    'statistics-foundations': [
      'Explain the concept using a small example from daily life or work.',
      'দৈনন্দিন জীবন বা কাজের ছোট উদাহরণ দিয়ে ধারণাটি ব্যাখ্যা করুন।',
    ],
    'data-analyst': [
      'Write a two-sentence business interpretation: what changed, and what should be checked next?',
      'দুই বাক্যে business interpretation লিখুন: কী বদলেছে এবং এরপর কী যাচাই করা উচিত?',
    ],
    'data-scientist': [
      'State one modeling assumption, one validation check, and one limitation.',
      'একটি modeling assumption, একটি validation check ও একটি limitation লিখুন।',
    ],
    'data-engineer': [
      'Translate the concept into one data-quality rule or pipeline validation check.',
      'ধারণাটিকে একটি data-quality rule বা pipeline validation check-এ রূপ দিন।',
    ],
    'research-business': [
      'Write what the evidence supports, what it does not support, and what decision remains.',
      'evidence কী সমর্থন করে, কী করে না এবং কোন decision বাকি থাকে তা লিখুন।',
    ],
  };

  function sessionSteps(profile, next, lab) {
    const concept = {
      title: t('Understand','বুঝুন'),
      text: t(`Read “${next ? next.title_en : 'the next lesson'}” and identify the core idea, assumptions and units.`, `“${next ? next.title_bn : 'পরবর্তী লেসন'}” পড়ে মূল ধারণা, assumption ও unit শনাক্ত করুন।`),
      time: profile.mode === 'practice' ? 5 : profile.mode === 'concepts' ? 15 : 10,
    };
    const practice = {
      title: lab ? t('Experiment','এক্সপেরিমেন্ট') : t('Work an example','উদাহরণ করুন'),
      text: lab ? t(`Open ${lab.title_en}, load the example, then change one input at a time.`, `${lab.title_bn} খুলে example load করুন, তারপর একবারে একটি input বদলান।`) : t('Create a small example and calculate or organize the required quantities.','একটি ছোট example তৈরি করে প্রয়োজনীয় quantity হিসাব বা সংগঠিত করুন।'),
      time: profile.mode === 'practice' ? 15 : profile.mode === 'concepts' ? 5 : 10,
    };
    const apply = {
      title: t('Interpret','ব্যাখ্যা করুন'),
      text: t(...(applyPrompts[profile.goal] || applyPrompts['statistics-foundations'])),
      time: 5,
    };
    return profile.mode === 'concepts' ? [concept, apply, practice] : profile.mode === 'practice' ? [practice, concept, apply] : [concept, practice, apply];
  }

  function roadmap(topics, completed, next) {
    const currentIndex = next ? topics.findIndex(topic => topic.id === next.id) : topics.length;
    const start = Math.max(0, currentIndex - 1);
    return topics.slice(start, start + 6).map((topic, index) => {
      const done = completed.has(topic.id);
      const current = next?.id === topic.id;
      return `<a class="roadmap-row ${done ? 'done' : ''} ${current ? 'current' : ''}" href="/${topic.url}"><span class="roadmap-status">${done ? '✓' : current ? '→' : start + index + 1}</span><span><strong>${escapeHtml(t(topic.title_en,topic.title_bn))}</strong><small>${topic.minutes} ${t('min','মিনিট')} · ${escapeHtml(t(topic.difficulty, ({Beginner:'বিগিনার',Intermediate:'ইন্টারমিডিয়েট',Advanced:'অ্যাডভান্সড'})[topic.difficulty]))}</small></span>${current ? `<span class="badge">${t('Next','পরবর্তী')}</span>` : ''}</a>`;
    }).join('');
  }

  function render() {
    const profile = getProfile();
    if (!profile) {
      root.innerHTML = `<section class="empty-plan"><span class="empty-plan-icon">◎</span><h1>${t('Build one clear learning route','একটি পরিষ্কার learning route তৈরি করুন')}</h1><p>${t('Choose your goal, current level and preferred learning style. The full library stays available, but your dashboard will show only the next useful steps.','আপনার লক্ষ্য, বর্তমান লেভেল ও শেখার ধরন বেছে নিন। পুরো library খোলা থাকবে, তবে dashboard শুধু প্রয়োজনীয় পরবর্তী ধাপ দেখাবে।')}</p><a class="button primary" href="/start/">${t('Build my plan','আমার প্ল্যান তৈরি করুন')} →</a></section>`;
      return;
    }

    const path = pathMap[profile.goal];
    const topics = getPlanTopics(profile);
    const progress = getPlanProgress(profile);
    const completed = getCompleted();
    const next = getNextTopic(profile);
    const lab = getRecommendedLab(next);
    const steps = sessionSteps(profile, next, lab);
    const bookmarked = [...getBookmarks()].map(id => topicMap[id]).filter(Boolean).slice(0, 4);
    const isNew = new URLSearchParams(location.search).get('new') === '1';

    root.innerHTML = `${isNew ? `<div class="success-banner"><span>✓</span><div><strong>${t('Your guided plan is ready.','আপনার guided plan প্রস্তুত।')}</strong><p>${t('Start with one focused session. You can change this plan at any time.','একটি focused session দিয়ে শুরু করুন। যেকোনো সময় plan পরিবর্তন করতে পারবেন।')}</p></div></div>` : ''}
      <section class="dashboard-hero"><div><span class="eyebrow">${t('My Learning','আমার শেখা')}</span><h1>${escapeHtml(t(path.title_en,path.title_bn))}</h1><p>${escapeHtml(t(path.description_en,path.description_bn))}</p><div class="profile-chips"><span>${escapeHtml(modeLabel(profile.mode))}</span><span>${escapeHtml(t(({beginner:'Beginner start',intermediate:'Experienced start',advanced:'Advanced start'})[profile.level],({beginner:'বিগিনার শুরু',intermediate:'অভিজ্ঞ শুরু',advanced:'অ্যাডভান্সড শুরু'})[profile.level]))}</span><a href="/start/">${t('Change plan','প্ল্যান পরিবর্তন')} ↗</a></div></div><div class="dashboard-progress-ring" style="--progress:${progress.percent * 3.6}deg"><div><strong>${progress.percent}%</strong><small>${progress.done}/${progress.total} ${t('steps','ধাপ')}</small></div></div></section>
      ${next ? `<section class="next-session-card"><div class="next-session-copy"><span class="eyebrow">${t('Your next focused session','আপনার পরবর্তী focused session')}</span><h2>${escapeHtml(t(next.title_en,next.title_bn))}</h2><p>${escapeHtml(t(next.summary_en,next.summary_bn))}</p><div class="next-meta"><span>${next.minutes} ${t('minute lesson','মিনিটের লেসন')}</span>${lab ? `<span>${t('Related lab','সম্পর্কিত ল্যাব')}: ${escapeHtml(t(lab.title_en,lab.title_bn))}</span>` : ''}</div><div class="hero-actions"><a class="button primary" href="/${next.url}">${t('Start lesson','লেসন শুরু করুন')} →</a>${lab && profile.mode === 'practice' ? `<a class="button ghost" href="/${lab.url}">${t('Start with the lab','ল্যাব দিয়ে শুরু করুন')}</a>` : ''}</div></div><div class="session-plan"><h3>${t('Use this simple session','এই simple session অনুসরণ করুন')}</h3>${steps.map((item,index) => `<div class="session-step"><span>${index + 1}</span><div><strong>${escapeHtml(item.title)}</strong><p>${escapeHtml(item.text)}</p></div><small>${item.time} ${t('min','মিনিট')}</small></div>`).join('')}</div></section>` : `<section class="completion-card"><span>✓</span><div><h2>${t('You completed this guided path.','আপনি এই guided path সম্পন্ন করেছেন।')}</h2><p>${t('Review bookmarks, explore another path, or continue with the full catalog.','bookmark review করুন, অন্য path বেছে নিন অথবা full catalog থেকে এগিয়ে যান।')}</p></div><a class="button primary" href="/paths/">${t('Explore another path','অন্য path দেখুন')}</a></section>`}
      <section class="dashboard-grid"><article class="dashboard-panel"><div class="panel-heading"><div><span class="eyebrow">${t('Now, next, later','এখন, এরপর, পরে')}</span><h2>${t('Your visible roadmap','আপনার visible roadmap')}</h2></div><a class="text-link" href="/paths/#${profile.goal}">${t('Full path →','পুরো path →')}</a></div><div class="roadmap-list">${roadmap(topics, completed, next)}</div></article><aside class="dashboard-side"><section class="dashboard-panel"><span class="eyebrow">${t('Use the hub well','হাবটি ভালোভাবে ব্যবহার করুন')}</span><h2>${t('Do not rush the catalog','Catalog দ্রুত শেষ করার চেষ্টা করবেন না')}</h2><ul class="compact-checks"><li>${t('Complete one concept at a time.','একবারে একটি concept সম্পন্ন করুন।')}</li><li>${t('Change one lab input at a time.','একবারে একটি lab input বদলান।')}</li><li>${t('Write a plain-language interpretation.','সহজ ভাষায় interpretation লিখুন।')}</li><li>${t('Reproduce important work in Excel, SQL, Python, R or Power BI.','গুরুত্বপূর্ণ কাজ Excel, SQL, Python, R বা Power BI-তে পুনরায় করুন।')}</li></ul></section><section class="dashboard-panel"><div class="panel-heading"><div><span class="eyebrow">${t('Bookmarks','বুকমার্ক')}</span><h2>${t('Saved for review','রিভিউয়ের জন্য সংরক্ষিত')}</h2></div></div>${bookmarked.length ? `<div class="bookmark-list">${bookmarked.map(topic => `<a href="/${topic.url}"><strong>${escapeHtml(t(topic.title_en,topic.title_bn))}</strong><small>${escapeHtml(t(topic.summary_en,topic.summary_bn))}</small></a>`).join('')}</div>` : `<p class="muted">${t('Bookmark difficult lessons and they will appear here.','কঠিন lesson bookmark করলে এখানে দেখাবে।')}</p>`}</section><section class="dashboard-panel danger-zone"><h2>${t('Progress controls','Progress control')}</h2><button class="button ghost" type="button" id="reset-progress">${t('Reset completed lessons','সম্পন্ন lesson reset করুন')}</button></section></aside></section>`;

    document.getElementById('reset-progress')?.addEventListener('click', () => {
      if (confirm(t('Reset all completed lessons? Your plan and bookmarks will remain.','সব completed lesson reset করবেন? Plan ও bookmark থাকবে।'))) {
        setCompleted(new Set());
        window.dispatchEvent(new CustomEvent('slh:progress'));
        render();
      }
    });
  }

  window.addEventListener('slh:language', render);
  window.addEventListener('slh:progress', render);
  window.addEventListener('slh:bookmarks', render);
  window.addEventListener('slh:profile', render);
  render();
})();
