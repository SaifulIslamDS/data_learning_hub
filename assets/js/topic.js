(() => {
  'use strict';
  const {
    DATA, topicMap, moduleMap, toolMap, pathMap, t, escapeHtml, isCompleted,
    toggleCompleted, getBookmarks, toggleBookmark, getProfile, getPlanTopics,
    getNextPlanTopic, getRecommendedLab, safeStorage,
  } = window.SLH;
  const id = document.body.dataset.topic;
  const topic = topicMap[id];
  if (!topic) return;
  const module = moduleMap[topic.module];
  const root = document.getElementById('topic-content');
  safeStorage.set('slh-last-topic', id);

  function adjacentPeers() {
    const peers = DATA.topics.filter(item => item.module === topic.module);
    const index = peers.findIndex(item => item.id === id);
    return {
      previous: index > 0 ? peers[index - 1] : null,
      next: index >= 0 && index < peers.length - 1 ? peers[index + 1] : null,
    };
  }

  function planContext() {
    const profile = getProfile();
    if (!profile) return null;
    const topics = getPlanTopics(profile);
    const index = topics.findIndex(item => item.id === id);
    if (index < 0) return { profile, path: pathMap[profile.goal], index: -1, total: topics.length };
    return { profile, path: pathMap[profile.goal], index, total: topics.length };
  }

  function updateActions() {
    const completed = isCompleted(id);
    const bookmarked = getBookmarks().has(id);
    const complete = document.getElementById('complete-topic');
    const bookmark = document.getElementById('bookmark-topic');
    if (complete) {
      complete.textContent = completed ? t('Completed ✓','সম্পন্ন ✓') : t('Mark complete','সম্পন্ন করুন');
      complete.classList.toggle('success', completed);
    }
    if (bookmark) {
      bookmark.textContent = bookmarked ? '★' : '☆';
      bookmark.setAttribute('aria-label', bookmarked ? t('Remove bookmark','বুকমার্ক সরান') : t('Bookmark lesson','লেসন বুকমার্ক করুন'));
    }
  }

  function stateObjectives() {
    return [
      t(`Explain what ${topic.title_en} means and why it is used.`,`${topic.title_bn} কী এবং কেন ব্যবহার করা হয় তা ব্যাখ্যা করুন।`),
      t('Recognize the data requirements and assumptions that affect validity.','validity-কে প্রভাবিত করা data requirement ও assumption শনাক্ত করুন।'),
      t('Apply the idea to a small practical example using a stated convention.','উল্লেখিত convention অনুযায়ী ছোট practical example-এ ধারণাটি প্রয়োগ করুন।'),
      t('Interpret the output without overstating certainty or causality.','certainty বা causality অতিরঞ্জিত না করে output ব্যাখ্যা করুন।'),
    ];
  }

  function render() {
    document.querySelector('.topic-hero .eyebrow').textContent = t(module.title_en,module.title_bn);
    document.querySelector('.topic-hero h1').textContent = t(topic.title_en,topic.title_bn);
    document.querySelector('.topic-hero p').textContent = t(topic.summary_en,topic.summary_bn);

    const objectives = stateObjectives();
    const peers = adjacentPeers();
    const context = planContext();
    const directLab = topic.lab ? toolMap[topic.lab] : null;
    const recommendedLab = directLab || getRecommendedLab(topic);
    const nextPlan = getNextPlanTopic(id);
    const nextTopic = nextPlan || peers.next;
    const pathPosition = context && context.index >= 0
      ? `<span>${t('Step','ধাপ')} ${context.index + 1} / ${context.total} · ${escapeHtml(t(context.path.title_en,context.path.title_bn))}</span>`
      : `<a href="/start/">${t('Add this to a guided plan','এটি guided plan-এ যোগ করুন')} →</a>`;

    root.innerHTML = `<section class="lesson-guide-card"><div><span class="eyebrow">${t('Guided lesson','গাইডেড লেসন')}</span><h2>${t('Use this page in three passes','এই পেজ তিন ধাপে ব্যবহার করুন')}</h2><p>${t('Do not try to memorize everything. Understand the idea, test it, then explain the result.','সবকিছু মুখস্থ করার চেষ্টা করবেন না। ধারণা বুঝুন, পরীক্ষা করুন, তারপর ফলাফল ব্যাখ্যা করুন।')}</p></div><div class="lesson-guide-steps"><span><b>1</b>${t('Understand','বুঝুন')}</span><span><b>2</b>${recommendedLab ? t('Experiment','এক্সপেরিমেন্ট') : t('Work an example','উদাহরণ করুন')}</span><span><b>3</b>${t('Interpret','ব্যাখ্যা করুন')}</span></div><div class="lesson-path-position">${pathPosition}</div></section>
      <div class="topic-layout"><article class="topic-main"><section class="topic-card lesson-section"><span class="section-number">01</span><h2>${t('What you should learn','আপনার যা শেখা উচিত')}</h2><ul class="objective-list">${objectives.map(item => `<li>${escapeHtml(item)}</li>`).join('')}</ul></section><section class="topic-card lesson-section"><span class="section-number">02</span><h2>${t('Understand the core idea','মূল ধারণা বুঝুন')}</h2><p>${escapeHtml(t(topic.summary_en,topic.summary_bn))}</p><div class="formula-block">${escapeHtml(t(topic.formula_en,topic.formula_bn))}</div></section><section class="topic-card lesson-section"><span class="section-number">03</span><h2>${t('See it in a practical workflow','প্র্যাকটিক্যাল workflow-এ দেখুন')}</h2><p>${escapeHtml(t(topic.example_en,topic.example_bn))}</p><ol class="check-list"><li>${t('Define the analytical question and target quantity before calculating.','হিসাবের আগে analytical question ও target quantity নির্ধারণ করুন।')}</li><li>${t('Check data type, sampling process and method assumptions.','data type, sampling process ও method assumption যাচাই করুন।')}</li><li>${t('Calculate or organize the required quantities using the stated convention.','উল্লেখিত convention অনুযায়ী প্রয়োজনীয় quantity হিসাব বা সংগঠিত করুন।')}</li><li>${t('Interpret magnitude, uncertainty and limitations in context.','context অনুযায়ী magnitude, uncertainty ও limitation ব্যাখ্যা করুন।')}</li></ol></section>${recommendedLab ? `<section class="topic-card lab-callout lesson-section"><span class="section-number">04</span><span class="eyebrow">${directLab ? t('Interactive practice','ইন্টারঅ্যাকটিভ প্র্যাকটিস') : t('Related practice','সম্পর্কিত প্র্যাকটিস')}</span><h2>${escapeHtml(t(recommendedLab.title_en,recommendedLab.title_bn))}</h2><p>${escapeHtml(t(recommendedLab.description_en,recommendedLab.description_bn))}</p><div class="lab-action-row"><a class="button primary" href="/${recommendedLab.url}">${t('Open the lab','ল্যাব খুলুন')} →</a><span>${t('Load the example, then change one input at a time.','example load করে একবারে একটি input বদলান।')}</span></div></section>` : ''}<section class="topic-card lesson-section"><span class="section-number">${recommendedLab ? '05' : '04'}</span><h2>${t('Interpretation standard','ব্যাখ্যার স্ট্যান্ডার্ড')}</h2><p>${t('A numerical result is not a decision by itself. Explain the population, units, direction, magnitude, uncertainty, assumptions and practical consequence. For observational data, do not claim causation from association alone.','একটি numerical result নিজে কোনো decision নয়। population, unit, direction, magnitude, uncertainty, assumption ও practical consequence ব্যাখ্যা করুন। observational data থেকে শুধু association দেখে causation দাবি করবেন না।')}</p><div class="reflection-box"><strong>${t('Before you continue, say or write:','এগিয়ে যাওয়ার আগে বলুন বা লিখুন:')}</strong><p>${t(`“${topic.title_en} is useful when … The result means … One limitation is …”`,`“${topic.title_bn} কাজে লাগে যখন … ফলাফলের অর্থ … একটি limitation হলো …”`)}</p></div></section><details class="topic-card disclosure-card"><summary>${t('Common mistakes and caution','সাধারণ ভুল ও সতর্কতা')} <span>＋</span></summary><div><p>${escapeHtml(t(topic.mistakes_en,topic.mistakes_bn))}</p><p class="small">${t('Definitions use standard statistical conventions. A method can still be inappropriate when its data requirements or assumptions are not met.','সংজ্ঞায় standard statistical convention ব্যবহার করা হয়েছে। data requirement বা assumption পূরণ না হলে method অনুপযুক্ত হতে পারে।')}</p></div></details><section class="lesson-complete-card"><div><span class="eyebrow">${t('Finish this step','এই ধাপ শেষ করুন')}</span><h2>${isCompleted(id) ? t('This lesson is complete.','এই lesson সম্পন্ন।') : t('Can you explain it without copying?','না দেখে কি ব্যাখ্যা করতে পারেন?')}</h2><p>${t('Mark complete only after you can describe the idea, use a small example and state one limitation.','ধারণা ব্যাখ্যা, ছোট example ব্যবহার ও একটি limitation বলার পরই complete করুন।')}</p></div><div class="lesson-complete-actions"><button class="button ${isCompleted(id) ? 'success' : 'primary'}" id="complete-topic-bottom" type="button">${isCompleted(id) ? t('Completed ✓','সম্পন্ন ✓') : t('Mark complete','সম্পন্ন করুন')}</button>${nextTopic ? `<a class="button ghost" href="/${nextTopic.url}">${t('Next:','পরবর্তী:')} ${escapeHtml(t(nextTopic.title_en,nextTopic.title_bn))} →</a>` : `<a class="button ghost" href="/my-learning/">${t('Return to My Learning','My Learning-এ ফিরুন')}</a>`}</div></section></article><aside class="topic-sidebar"><section class="topic-card focus-card"><span class="eyebrow">${t('Focus','ফোকাস')}</span><h2>${topic.minutes} ${t('minutes','মিনিট')}</h2><p>${t('Complete one lesson. Do not open multiple topics at once.','একটি lesson সম্পন্ন করুন। একসঙ্গে অনেক topic খুলবেন না।')}</p><a class="text-link" href="/my-learning/">${t('Back to My Learning →','My Learning-এ ফিরুন →')}</a></section><section class="topic-card"><h2>${t('Lesson details','লেসনের তথ্য')}</h2><div class="meta-list"><div class="meta-row"><span>${t('Module','মডিউল')}</span><strong>${escapeHtml(t(module.title_en,module.title_bn))}</strong></div><div class="meta-row"><span>${t('Level','লেভেল')}</span><strong>${escapeHtml(t(topic.difficulty,({Beginner:'বিগিনার',Intermediate:'ইন্টারমিডিয়েট',Advanced:'অ্যাডভান্সড'})[topic.difficulty]))}</strong></div><div class="meta-row"><span>${t('Format','ফরম্যাট')}</span><strong>${topic.kind === 'lab' ? t('Lesson + lab','লেসন + ল্যাব') : topic.kind === 'practice' ? t('Practice lesson','প্র্যাকটিস লেসন') : t('Concept lesson','কনসেপ্ট লেসন')}</strong></div></div></section><section class="topic-card"><h2>${t('Nearby lessons','কাছাকাছি লেসন')}</h2><div class="related-list">${peers.previous ? `<a href="/${peers.previous.url}">← ${escapeHtml(t(peers.previous.title_en,peers.previous.title_bn))}</a>` : ''}${peers.next ? `<a href="/${peers.next.url}">${escapeHtml(t(peers.next.title_en,peers.next.title_bn))} →</a>` : ''}</div></section></aside></div>`;

    document.getElementById('complete-topic-bottom')?.addEventListener('click', () => {
      toggleCompleted(id);
      render();
      updateActions();
    });
    updateActions();
  }

  document.getElementById('complete-topic')?.addEventListener('click', () => { toggleCompleted(id); render(); updateActions(); });
  document.getElementById('bookmark-topic')?.addEventListener('click', () => { toggleBookmark(id); updateActions(); });
  window.addEventListener('slh:language', render);
  window.addEventListener('slh:profile', render);
  render();
})();
