(() => {
  'use strict';
  const { pathMap, t, escapeHtml, getProfile, setProfile, levelStartIndex } = window.DLH;
  const root = document.getElementById('guide-wizard');
  if (!root) return;

  const existing = getProfile();
  const choices = {
    goal: existing?.goal || 'data-analyst',
    level: existing?.level || '',
    time: existing?.time || '',
    mode: existing?.mode || '',
    knowledge: Array.isArray(existing?.knowledge) ? [...existing.knowledge] : [],
  };
  let step = 0;

  const steps = [
    {
      key: 'goal', type: 'single', eyebrow: ['Step 1 of 5', 'ধাপ ১ / ৫'],
      title: ['What are you learning for?', 'আপনি কোন উদ্দেশ্যে শিখছেন?'],
      copy: ['Data Analyst is the primary v2 route. Research remains a statistics-heavy supporting route.', 'Data Analyst হলো primary v2 route। Research একটি statistics-heavy supporting route।'],
      options: [
        { value:'data-analyst', en:'Become a Data Analyst', bn:'Data Analyst হতে চাই', descEn:'Foundations → Statistics → Excel → SQL → Power BI → Python → Projects', descBn:'Foundation → Statistics → Excel → SQL → Power BI → Python → Project', icon:'DA' },
        { value:'research-analyst', en:'Research & Decision Analysis', bn:'Research ও Decision Analysis', descEn:'Sampling, inference, experiments, regression and defensible communication.', descBn:'Sampling, inference, experiment, regression ও defensible communication।', icon:'RA' },
      ],
    },
    {
      key: 'level', type: 'single', eyebrow: ['Step 2 of 5', 'ধাপ ২ / ৫'],
      title: ['Where should the active foundation begin?', 'Active foundation কোথা থেকে শুরু হবে?'],
      copy: ['This changes the recommended starting point, not access to the full library.', 'এটি recommended starting point বদলায়; full library access বদলায় না।'],
      options: [
        { value:'beginner', en:'Complete beginner', bn:'Complete beginner', descEn:'Start with data, variables, quality and first statistical ideas.', descBn:'Data, variable, quality ও প্রথম statistical idea থেকে শুরু করুন।', icon:'01' },
        { value:'intermediate', en:'Some experience', bn:'কিছু অভিজ্ঞতা আছে', descEn:'Begin near descriptive analysis and practical interpretation.', descBn:'Descriptive analysis ও practical interpretation-এর কাছ থেকে শুরু করুন।', icon:'02' },
        { value:'advanced', en:'Strong foundation', bn:'ভালো foundation আছে', descEn:'Begin later and use prerequisites as optional review.', descBn:'পরে শুরু করুন এবং prerequisite optional review হিসেবে ব্যবহার করুন।', icon:'03' },
      ],
    },
    {
      key: 'time', type: 'single', eyebrow: ['Step 3 of 5', 'ধাপ ৩ / ৫'],
      title: ['How much time can you study per session?', 'প্রতি session কত সময় পড়তে পারবেন?'],
      copy: ['The dashboard will keep each session inside this approximate time box.', 'Dashboard প্রতিটি session এই approximate time-এর মধ্যে রাখবে।'],
      options: [
        { value:'20', en:'20 minutes', bn:'২০ মিনিট', descEn:'One focused concept or a short review.', descBn:'একটি focused concept বা short review।', icon:'20' },
        { value:'40', en:'40 minutes', bn:'৪০ মিনিট', descEn:'Lesson, small practice and interpretation.', descBn:'Lesson, small practice ও interpretation।', icon:'40' },
        { value:'60', en:'60 minutes', bn:'৬০ মিনিট', descEn:'A full lesson plus lab or project work.', descBn:'Full lesson এবং lab বা project work।', icon:'60' },
      ],
    },
    {
      key: 'mode', type: 'single', eyebrow: ['Step 4 of 5', 'ধাপ ৪ / ৫'],
      title: ['How do you prefer to learn?', 'আপনি কীভাবে শিখতে পছন্দ করেন?'],
      copy: ['This changes the order of reading, practice and interpretation—not the curriculum.', 'এটি reading, practice ও interpretation-এর order বদলায়; curriculum নয়।'],
      options: [
        { value:'concepts', en:'Concept-first', bn:'Concept-first', descEn:'Understand definitions and reasoning before practice.', descBn:'Practice-এর আগে definition ও reasoning বুঝুন।', icon:'A' },
        { value:'balanced', en:'Balanced', bn:'Balanced', descEn:'Combine explanation, example, practice and interpretation.', descBn:'Explanation, example, practice ও interpretation একত্র করুন।', icon:'A+B' },
        { value:'practice', en:'Practice-first', bn:'Practice-first', descEn:'Start with an example or lab, then explain the theory.', descBn:'Example বা lab দিয়ে শুরু করে theory explain করুন।', icon:'B' },
      ],
    },
    {
      key: 'knowledge', type: 'multi', eyebrow: ['Step 5 of 5', 'ধাপ ৫ / ৫'],
      title: ['Which tools have you used before?', 'আগে কোন tool ব্যবহার করেছেন?'],
      copy: ['Select any that apply. This is saved for future tool-track recommendations; it does not skip unpublished lessons.', 'যা প্রযোজ্য select করুন। Future tool-track recommendation-এর জন্য save হবে; unpublished lesson skip করবে না।'],
      options: [
        { value:'excel', en:'Excel', bn:'Excel', descEn:'Formulas, tables or PivotTables', descBn:'Formula, table বা PivotTable', icon:'X' },
        { value:'sql', en:'SQL', bn:'SQL', descEn:'Queries or relational databases', descBn:'Query বা relational database', icon:'S' },
        { value:'power-bi', en:'Power BI', bn:'Power BI', descEn:'Power Query, models or reports', descBn:'Power Query, model বা report', icon:'P' },
        { value:'python', en:'Python', bn:'Python', descEn:'Python, notebooks or pandas', descBn:'Python, notebook বা pandas', icon:'Py' },
      ],
    },
  ];

  function hasSelection(config) {
    return config.type === 'multi' ? true : Boolean(choices[config.key]);
  }

  function render() {
    const config = steps[step];
    const selected = choices[config.key];
    root.innerHTML = `<div class="wizard-progress" aria-label="${t('Setup progress', 'Setup progress')}"><span style="width:${((step + 1) / steps.length) * 100}%"></span></div><div class="wizard-heading"><span class="eyebrow">${t(...config.eyebrow)}</span><h1>${t(...config.title)}</h1><p>${t(...config.copy)}</p></div><div class="choice-grid ${config.key === 'goal' ? 'goal-choice-grid' : ''}" role="${config.type === 'multi' ? 'group' : 'radiogroup'}">${config.options.map(option => {
      const active = config.type === 'multi' ? choices.knowledge.includes(option.value) : selected === option.value;
      return `<button class="choice-card ${active ? 'selected' : ''}" type="button" ${config.type === 'multi' ? `aria-pressed="${active}"` : `role="radio" aria-checked="${active}"`} data-value="${option.value}"><span class="choice-icon">${escapeHtml(option.icon)}</span><span><strong>${escapeHtml(t(option.en, option.bn))}</strong><small>${escapeHtml(t(option.descEn, option.descBn))}</small></span><span class="choice-check">✓</span></button>`;
    }).join('')}</div>${config.type === 'multi' ? `<p class="wizard-helper">${t('No previous tool experience is also a valid starting point.', 'আগে কোনো tool experience না থাকাও valid starting point।')}</p>` : ''}<div class="wizard-actions"><button class="button ghost" id="wizard-back" type="button" ${step === 0 ? 'disabled' : ''}>← ${t('Back', 'পেছনে')}</button><span class="wizard-note">${t('Saved only in this browser', 'শুধু এই browser-এ save হবে')}</span><button class="button primary" id="wizard-next" type="button" ${hasSelection(config) ? '' : 'disabled'}>${step === steps.length - 1 ? t('Create my plan', 'আমার plan তৈরি করুন') : t('Continue', 'চালিয়ে যান')} →</button></div>`;

    root.querySelectorAll('.choice-card').forEach(button => button.addEventListener('click', () => {
      if (config.type === 'multi') {
        const value = button.dataset.value;
        choices.knowledge = choices.knowledge.includes(value) ? choices.knowledge.filter(item => item !== value) : [...choices.knowledge, value];
      } else {
        choices[config.key] = button.dataset.value;
      }
      render();
    }));
    document.getElementById('wizard-back')?.addEventListener('click', () => { if (step > 0) { step -= 1; render(); } });
    document.getElementById('wizard-next')?.addEventListener('click', () => {
      if (!hasSelection(config)) return;
      if (step < steps.length - 1) { step += 1; render(); return; }
      const path = pathMap[choices.goal] || pathMap['data-analyst'];
      setProfile({
        goal: path.id,
        level: choices.level,
        time: Number(choices.time || 40),
        mode: choices.mode,
        knowledge: choices.knowledge,
        startIndex: levelStartIndex(path, choices.level),
        createdAt: existing?.createdAt || new Date().toISOString(),
        updatedAt: new Date().toISOString(),
      });
      location.href = '/my-learning/?new=1';
    });
  }

  window.addEventListener('dlh:language', render);
  render();
})();
