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
  const lesson = topic.lesson;
  const root = document.getElementById('topic-content');
  safeStorage.set('slh-last-topic', id);

  const h = value => escapeHtml(value);
  const tx = pair => h(t(pair.en, pair.bn));
  const list = (items, className = '') => `<ul class="${className}">${items.map(item => `<li>${item}</li>`).join('')}</ul>`;

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
    return {
      profile,
      path: pathMap[profile.goal],
      index,
      total: topics.length,
    };
  }

  function objectives() {
    const type = lesson.lesson_type;
    const typeSpecific = {
      concept: t('Distinguish the important terms and classify a small example correctly.', 'গুরুত্বপূর্ণ term আলাদা করুন এবং ছোট example সঠিকভাবে classify করুন।'),
      formula: t('Calculate the quantity using a stated convention and explain its unit.', 'stated convention অনুযায়ী quantity calculate করে unit explain করুন।'),
      method: t('Recognize when the method fits the question, design and assumptions.', 'method কখন question, design ও assumption-এর সঙ্গে মেলে তা বুঝুন।'),
      workflow: t('Follow a repeatable workflow with clear inputs, checks and outputs.', 'clear input, check ও output-সহ repeatable workflow follow করুন।'),
    }[type];
    return [
      t(`Explain ${topic.title_en} in plain language.`, `${topic.title_bn} সহজ ভাষায় ব্যাখ্যা করুন।`),
      typeSpecific,
      t('Work through a practical scenario and identify the analytical decision.', 'practical scenario follow করে analytical decision শনাক্ত করুন।'),
      t('Apply the idea in a suitable tool or documented process.', 'উপযুক্ত tool বা documented process-এ ধারণাটি apply করুন।'),
      t('Interpret the result responsibly and state one limitation.', 'result responsibly interpret করে একটি limitation state করুন।'),
    ];
  }

  function renderConcepts() {
    return lesson.concepts.map(item => `
      <article class="concept-card">
        <h3>${h(t(item.term_en, item.term_bn))}</h3>
        <p>${h(t(item.definition_en, item.definition_bn))}</p>
      </article>`).join('');
  }

  function renderWorkflow() {
    return lesson.workflow.map((step, index) => `
      <li><span>${String(index + 1).padStart(2, '0')}</span><p>${h(t(step.en, step.bn))}</p></li>`).join('');
  }

  function renderImplementations() {
    return lesson.implementations.map((guide, index) => `
      <details class="implementation-card" ${index === 0 ? 'open' : ''}>
        <summary><span>${h(t(guide.tool_en, guide.tool_bn))}</span><span aria-hidden="true">＋</span></summary>
        <ol>${(t(guide.steps_en, guide.steps_bn) || []).map(step => `<li>${h(step)}</li>`).join('')}</ol>
      </details>`).join('');
  }

  function renderQuiz() {
    return `
      <div class="quiz-card" id="lesson-quiz">
        <p class="quiz-question">${h(t(lesson.quiz.question_en, lesson.quiz.question_bn))}</p>
        <div class="quiz-options">
          ${lesson.quiz.options.map((option, index) => `
            <label class="quiz-option">
              <input type="radio" name="lesson-quiz-option" value="${index}">
              <span>${h(t(option.en, option.bn))}</span>
            </label>`).join('')}
        </div>
        <div class="quiz-actions">
          <button class="button secondary" id="check-quiz" type="button">${t('Check answer', 'উত্তর যাচাই করুন')}</button>
          <span class="quiz-feedback" id="quiz-feedback" aria-live="polite"></span>
        </div>
        <div class="quiz-explanation" id="quiz-explanation" hidden>${h(t(lesson.quiz.explanation_en, lesson.quiz.explanation_bn))}</div>
      </div>`;
  }

  function updateActions() {
    const completed = isCompleted(id);
    const bookmarked = getBookmarks().has(id);
    document.querySelectorAll('[data-complete-topic]').forEach(button => {
      button.textContent = completed ? t('Completed ✓', 'সম্পন্ন ✓') : t('Mark complete', 'সম্পন্ন করুন');
      button.classList.toggle('success', completed);
      button.classList.toggle('primary', !completed);
    });
    const bookmark = document.getElementById('bookmark-topic');
    if (bookmark) {
      bookmark.textContent = bookmarked ? '★' : '☆';
      bookmark.setAttribute('aria-label', bookmarked ? t('Remove bookmark', 'বুকমার্ক সরান') : t('Bookmark lesson', 'লেসন বুকমার্ক করুন'));
    }
  }

  function bindQuiz() {
    document.getElementById('check-quiz')?.addEventListener('click', () => {
      const selected = document.querySelector('input[name="lesson-quiz-option"]:checked');
      const feedback = document.getElementById('quiz-feedback');
      const explanation = document.getElementById('quiz-explanation');
      if (!selected) {
        feedback.textContent = t('Choose one answer first.', 'আগে একটি উত্তর বাছাই করুন।');
        feedback.className = 'quiz-feedback warning';
        return;
      }
      const correct = Number(selected.value) === lesson.quiz.answer;
      feedback.textContent = correct ? t('Correct.', 'সঠিক।') : t('Review the explanation.', 'ব্যাখ্যাটি দেখুন।');
      feedback.className = `quiz-feedback ${correct ? 'correct' : 'incorrect'}`;
      explanation.hidden = false;
      document.querySelectorAll('.quiz-option').forEach((label, index) => {
        label.classList.toggle('correct', index === lesson.quiz.answer);
        label.classList.toggle('incorrect', index === Number(selected.value) && !correct);
      });
    });
  }

  function bindComplete() {
    document.querySelectorAll('[data-complete-topic]').forEach(button => {
      button.onclick = () => {
        toggleCompleted(id);
        updateActions();
      };
    });
  }

  function render() {
    document.querySelector('.topic-hero .eyebrow').textContent = t(module.title_en, module.title_bn);
    document.querySelector('.topic-hero h1').textContent = t(topic.title_en, topic.title_bn);
    document.querySelector('.topic-hero p').textContent = t(lesson.plain_en, lesson.plain_bn);

    const peers = adjacentPeers();
    const context = planContext();
    const directLab = topic.lab ? toolMap[topic.lab] : null;
    const recommendedLab = directLab || getRecommendedLab(topic);
    const nextPlan = getNextPlanTopic(id);
    const nextTopic = nextPlan || peers.next;
    const pathPosition = context && context.index >= 0
      ? `${t('Step', 'ধাপ')} ${context.index + 1} / ${context.total} · ${h(t(context.path.title_en, context.path.title_bn))}`
      : t('Not currently in your guided plan', 'বর্তমান guided plan-এর অংশ নয়');
    const currentPercent = context && context.index >= 0 ? Math.round((context.index + 1) / context.total * 100) : 0;
    const objectivesHtml = objectives().map(item => `<li>${h(item)}</li>`).join('');
    const scenarioSteps = t(lesson.scenario.steps_en, lesson.scenario.steps_bn).map(step => `<li>${h(step)}</li>`).join('');
    const recapHtml = lesson.recap.map(item => `<li>${h(t(item.en, item.bn))}</li>`).join('');
    const references = lesson.references.map(ref => `<a href="${h(ref.url)}" target="_blank" rel="noopener noreferrer">${h(ref.label)} ↗</a>`).join('');

    root.innerHTML = `
      <section class="lesson-overview-card">
        <div class="lesson-overview-copy">
          <span class="eyebrow">${t('Comprehensive guided lesson', 'comprehensive guided lesson')}</span>
          <h2>${t('Learn the topic, not just the workflow', 'শুধু workflow নয়, topic-টি শিখুন')}</h2>
          <p>${t('Move through four clear phases. Read the essential content first; open deeper details only when you need them.', 'চারটি clear phase follow করুন। আগে essential content পড়ুন; প্রয়োজন হলে deeper detail খুলুন।')}</p>
        </div>
        <nav class="lesson-phase-nav" aria-label="${t('Lesson sections', 'lesson section')}">
          <a href="#learn"><b>1</b><span>${t('Learn', 'শিখুন')}<small>${t('Meaning and concepts', 'meaning ও concept')}</small></span></a>
          <a href="#explore"><b>2</b><span>${t('Explore', 'অনুসন্ধান')}<small>${t('Worked scenario', 'worked scenario')}</small></span></a>
          <a href="#apply"><b>3</b><span>${t('Apply', 'প্রয়োগ')}<small>${t('Workflow and tools', 'workflow ও tool')}</small></span></a>
          <a href="#check"><b>4</b><span>${t('Check', 'যাচাই')}<small>${t('Quiz and recap', 'quiz ও recap')}</small></span></a>
        </nav>
        <div class="lesson-position-row">
          <span>${pathPosition}</span>
          ${currentPercent ? `<div class="mini-progress" aria-label="${currentPercent}%"><span style="width:${currentPercent}%"></span></div>` : `<a href="/start/">${t('Add to a learning plan', 'learning plan-এ যোগ করুন')} →</a>`}
        </div>
      </section>

      <div class="topic-layout comprehensive-layout">
        <article class="topic-main comprehensive-main">
          <section class="lesson-phase" id="learn">
            <header class="phase-header"><span>01</span><div><p>${t('Phase 1', 'Phase 1')}</p><h2>${t('Learn the idea clearly', 'ধারণাটি পরিষ্কারভাবে শিখুন')}</h2></div></header>

            <section class="topic-card lesson-section simple-explanation">
              <span class="section-kicker">${t('In simple language', 'সহজ ভাষায়')}</span>
              <h3>${h(t(topic.title_en, topic.title_bn))}</h3>
              <p class="lead-copy">${h(t(lesson.plain_en, lesson.plain_bn))}</p>
              <div class="why-box"><strong>${t('Why this matters', 'কেন গুরুত্বপূর্ণ')}</strong><p>${h(t(lesson.why_en, lesson.why_bn))}</p></div>
            </section>

            <section class="topic-card lesson-section">
              <span class="section-kicker">${t('Core vocabulary', 'মূল vocabulary')}</span>
              <h3>${t('Important ideas and definitions', 'গুরুত্বপূর্ণ ধারণা ও definition')}</h3>
              <div class="concept-grid">${renderConcepts()}</div>
            </section>

            <section class="topic-card lesson-section">
              <span class="section-kicker">${t('Learning outcomes', 'learning outcome')}</span>
              <h3>${t('By the end of this lesson, you should be able to', 'lesson শেষে যা করতে পারবেন')}</h3>
              <ul class="objective-list">${objectivesHtml}</ul>
            </section>

            ${topic.formula_en ? `<details class="topic-card disclosure-card formula-disclosure"><summary>${t('Definition, formula or formal rule', 'definition, formula বা formal rule')} <span>＋</span></summary><div><div class="formula-block">${h(t(topic.formula_en, topic.formula_bn))}</div><p class="small">${t('Always state the convention and assumptions used by the formula or procedure.', 'formula বা procedure-এর convention ও assumption সবসময় state করুন।')}</p></div></details>` : ''}
          </section>

          <section class="lesson-phase" id="explore">
            <header class="phase-header"><span>02</span><div><p>${t('Phase 2', 'Phase 2')}</p><h2>${t('Explore a practical example', 'practical example অনুসন্ধান করুন')}</h2></div></header>

            <section class="topic-card lesson-section scenario-card">
              <span class="section-kicker">${t('Real-world scenario', 'real-world scenario')}</span>
              <h3>${h(t(lesson.scenario.title_en, lesson.scenario.title_bn))}</h3>
              <p class="lead-copy">${h(t(lesson.scenario.context_en, lesson.scenario.context_bn))}</p>
              <div class="scenario-question"><strong>${t('Question to answer', 'যে প্রশ্নের উত্তর দিতে হবে')}</strong><p>${h(t(lesson.scenario.question_en, lesson.scenario.question_bn))}</p></div>
              <ol class="worked-example-steps">${scenarioSteps}</ol>
            </section>

            <section class="interpretation-grid">
              <article class="topic-card interpretation-good"><span class="section-kicker">${t('Responsible interpretation', 'responsible interpretation')}</span><h3>${t('What a good explanation includes', 'ভালো explanation-এ যা থাকে')}</h3><p>${h(t(lesson.interpretation.good_en, lesson.interpretation.good_bn))}</p></article>
              <article class="topic-card interpretation-caution"><span class="section-kicker">${t('Do not overclaim', 'overclaim করবেন না')}</span><h3>${t('What this topic cannot guarantee', 'এই topic যা guarantee করে না')}</h3><p>${h(t(lesson.interpretation.caution_en, lesson.interpretation.caution_bn))}</p></article>
            </section>
          </section>

          <section class="lesson-phase" id="apply">
            <header class="phase-header"><span>03</span><div><p>${t('Phase 3', 'Phase 3')}</p><h2>${t('Apply it in a repeatable workflow', 'repeatable workflow-এ apply করুন')}</h2></div></header>

            <section class="topic-card lesson-section">
              <span class="section-kicker">${t('Practical workflow', 'practical workflow')}</span>
              <h3>${t('Use these steps in real analysis', 'real analysis-এ এই step ব্যবহার করুন')}</h3>
              <ol class="workflow-list">${renderWorkflow()}</ol>
            </section>

            <section class="topic-card lesson-section">
              <span class="section-kicker">${t('Implementation', 'implementation')}</span>
              <h3>${t('How this appears in professional work', 'professional work-এ এটি কীভাবে দেখা যায়')}</h3>
              <p>${t('Open the tool or workflow most relevant to you. These are implementation patterns, not a substitute for reading the software documentation.', 'আপনার জন্য relevant tool বা workflow খুলুন। এগুলো implementation pattern; software documentation-এর বিকল্প নয়।')}</p>
              <div class="implementation-list">${renderImplementations()}</div>
            </section>

            ${recommendedLab ? `<section class="topic-card lab-callout lesson-section"><span class="section-kicker">${directLab ? t('Interactive practice', 'interactive practice') : t('Related practice', 'related practice')}</span><h3>${h(t(recommendedLab.title_en, recommendedLab.title_bn))}</h3><p>${h(t(recommendedLab.description_en, recommendedLab.description_bn))}</p><div class="lab-action-row"><a class="button primary" href="/${recommendedLab.url}">${t('Open the lab', 'ল্যাব খুলুন')} →</a><span>${t('Run the example first, then change one input and explain the difference.', 'আগে example run করুন, তারপর একটি input বদলে difference explain করুন।')}</span></div></section>` : ''}

            <section class="topic-card lesson-section practice-task-card">
              <span class="section-kicker">${t('Mini assignment', 'mini assignment')}</span>
              <h3>${t('Implement the idea yourself', 'নিজে ধারণাটি implement করুন')}</h3>
              <p>${h(t(lesson.practice_en, lesson.practice_bn))}</p>
              <div class="assignment-checklist"><span>□ ${t('Data or scenario defined', 'data বা scenario defined')}</span><span>□ ${t('Method and convention stated', 'method ও convention stated')}</span><span>□ ${t('Result interpreted', 'result interpreted')}</span><span>□ ${t('One limitation included', 'একটি limitation included')}</span></div>
            </section>
          </section>

          <section class="lesson-phase" id="check">
            <header class="phase-header"><span>04</span><div><p>${t('Phase 4', 'Phase 4')}</p><h2>${t('Check your understanding', 'বোঝাপড়া যাচাই করুন')}</h2></div></header>

            <section class="topic-card lesson-section">
              <span class="section-kicker">${t('Quick knowledge check', 'quick knowledge check')}</span>
              <h3>${t('Choose the most defensible statement', 'সবচেয়ে defensible statement বাছাই করুন')}</h3>
              ${renderQuiz()}
            </section>

            <details class="topic-card disclosure-card"><summary>${t('Common mistakes and cautions', 'সাধারণ ভুল ও caution')} <span>＋</span></summary><div><p>${h(t(topic.mistakes_en, topic.mistakes_bn))}</p><p class="small">${t('A correct formula can still answer the wrong question when the design, data or assumptions do not match.', 'formula correct হলেও design, data বা assumption না মিললে wrong question-এর answer হতে পারে।')}</p></div></details>

            <section class="topic-card lesson-section recap-card">
              <span class="section-kicker">${t('Lesson recap', 'lesson recap')}</span>
              <h3>${t('Remember these points', 'এই point-গুলো মনে রাখুন')}</h3>
              <ul class="recap-list">${recapHtml}</ul>
            </section>

            <details class="topic-card disclosure-card reference-card"><summary>${t('Sources and further reading', 'source ও further reading')} <span>＋</span></summary><div class="reference-links">${references}</div></details>

            <section class="lesson-complete-card">
              <div><span class="eyebrow">${t('Finish this lesson', 'lesson শেষ করুন')}</span><h2>${isCompleted(id) ? t('This lesson is complete.', 'এই lesson সম্পন্ন।') : t('Can you teach the main idea to someone else?', 'main idea কি অন্য কাউকে শেখাতে পারবেন?')}</h2><p>${t('Mark complete after you can define the topic, work a small example, implement it and state one limitation.', 'topic define, ছোট example work, implement ও একটি limitation state করার পর complete করুন।')}</p></div>
              <div class="lesson-complete-actions"><button class="button ${isCompleted(id) ? 'success' : 'primary'}" data-complete-topic type="button">${isCompleted(id) ? t('Completed ✓', 'সম্পন্ন ✓') : t('Mark complete', 'সম্পন্ন করুন')}</button>${nextTopic ? `<a class="button ghost" href="/${nextTopic.url}">${t('Next:', 'পরবর্তী:')} ${h(t(nextTopic.title_en, nextTopic.title_bn))} →</a>` : `<a class="button ghost" href="/my-learning/">${t('Return to My Learning', 'My Learning-এ ফিরুন')}</a>`}</div>
            </section>
          </section>
        </article>

        <aside class="topic-sidebar comprehensive-sidebar">
          <section class="topic-card focus-card">
            <span class="eyebrow">${t('Study plan', 'study plan')}</span>
            <h2>${topic.minutes} ${t('minutes', 'মিনিট')}</h2>
            <p>${t('Complete one phase at a time. You may pause after any phase and return later.', 'একবারে একটি phase complete করুন। যেকোনো phase-এর পর pause করে পরে ফিরতে পারেন।')}</p>
          </section>
          <nav class="topic-card lesson-toc" aria-label="${t('On this lesson', 'এই lesson-এ')}">
            <h2>${t('On this lesson', 'এই lesson-এ')}</h2>
            <a href="#learn"><span>01</span>${t('Learn', 'শিখুন')}</a>
            <a href="#explore"><span>02</span>${t('Explore', 'অনুসন্ধান')}</a>
            <a href="#apply"><span>03</span>${t('Apply', 'প্রয়োগ')}</a>
            <a href="#check"><span>04</span>${t('Check', 'যাচাই')}</a>
          </nav>
          <section class="topic-card"><h2>${t('Lesson details', 'লেসনের তথ্য')}</h2><div class="meta-list"><div class="meta-row"><span>${t('Module', 'মডিউল')}</span><strong>${h(t(module.title_en, module.title_bn))}</strong></div><div class="meta-row"><span>${t('Level', 'লেভেল')}</span><strong>${h(t(topic.difficulty, ({Beginner:'বিগিনার',Intermediate:'ইন্টারমিডিয়েট',Advanced:'অ্যাডভান্সড'})[topic.difficulty]))}</strong></div><div class="meta-row"><span>${t('Lesson type', 'lesson type')}</span><strong>${h(t(lesson.lesson_type, ({concept:'concept',formula:'formula',method:'method',workflow:'workflow'})[lesson.lesson_type]))}</strong></div></div></section>
          <section class="topic-card"><h2>${t('Nearby lessons', 'কাছাকাছি লেসন')}</h2><div class="related-list">${peers.previous ? `<a href="/${peers.previous.url}">← ${h(t(peers.previous.title_en, peers.previous.title_bn))}</a>` : ''}${peers.next ? `<a href="/${peers.next.url}">${h(t(peers.next.title_en, peers.next.title_bn))} →</a>` : ''}</div></section>
          <a class="button ghost sidebar-back" href="/my-learning/">${t('Back to My Learning', 'My Learning-এ ফিরুন')} →</a>
        </aside>
      </div>`;

    bindQuiz();
    bindComplete();
    updateActions();
  }

  document.getElementById('complete-topic')?.setAttribute('data-complete-topic', '');
  document.getElementById('bookmark-topic')?.addEventListener('click', () => {
    toggleBookmark(id);
    updateActions();
  });
  window.addEventListener('slh:language', render);
  window.addEventListener('slh:profile', render);
  render();
})();
