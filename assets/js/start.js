(() => {
  'use strict';
  const { pathMap, t, escapeHtml, getProfile, setProfile, levelStartIndex } = window.SLH;
  const root = document.getElementById('guide-wizard');
  if (!root) return;

  const existing = getProfile();
  const queryGoal = new URLSearchParams(location.search).get('goal');
  const choices = {
    goal: existing?.goal || (pathMap[queryGoal] ? queryGoal : ''),
    level: existing?.level || '',
    mode: existing?.mode || '',
  };
  let step = 0;

  const goalMeta = {
    'statistics-foundations': ['Foundations', 'ভিত্তি', 'Build confidence before choosing a specialist career route.', 'বিশেষায়িত career route-এর আগে আত্মবিশ্বাসী ভিত্তি তৈরি করুন।', 'μ'],
    'data-analyst': ['Data Analyst', 'ডেটা অ্যানালিস্ট', 'Describe data, test business questions and communicate decisions.', 'ডেটা বর্ণনা, business question test ও decision communicate করুন।', '↗'],
    'data-scientist': ['Data Scientist', 'ডেটা সায়েন্টিস্ট', 'Develop probability, modeling and model-evaluation foundations.', 'probability, modeling ও model-evaluation ভিত্তি তৈরি করুন।', 'ƒ'],
    'data-engineer': ['Data Engineer', 'ডেটা ইঞ্জিনিয়ার', 'Connect statistical literacy with reliable analytical data systems.', 'statistical literacy-কে reliable analytical data system-এর সঙ্গে যুক্ত করুন।', '⌁'],
    'research-business': ['Research & Decisions', 'রিসার্চ ও সিদ্ধান্ত', 'Design evidence, compare groups and communicate uncertainty.', 'evidence design, group comparison ও uncertainty communicate করুন।', '∵'],
  };

  const steps = [
    {
      key: 'goal',
      eyebrow: ['Step 1 of 3', 'ধাপ ১ / ৩'],
      title: ['What are you learning for?', 'আপনি কোন উদ্দেশ্যে শিখছেন?'],
      copy: ['Choose the route closest to your current goal. You can change it later.', 'আপনার বর্তমান লক্ষ্যের সবচেয়ে কাছের route বেছে নিন। পরে পরিবর্তন করতে পারবেন।'],
      options: Object.entries(goalMeta).map(([value, [en, bn, descEn, descBn, icon]]) => ({ value, en, bn, descEn, descBn, icon })),
    },
    {
      key: 'level',
      eyebrow: ['Step 2 of 3', 'ধাপ ২ / ৩'],
      title: ['Where should the route begin?', 'Route কোথা থেকে শুরু হবে?'],
      copy: ['This changes the recommended starting point, not access to the full library.', 'এটি শুধু recommended starting point বদলাবে; পুরো library সবসময় খোলা থাকবে।'],
      options: [
        { value:'beginner', en:'Beginner', bn:'বিগিনার', descEn:'Start with vocabulary, data types and first principles.', descBn:'পরিভাষা, data type ও first principle থেকে শুরু করুন।', icon:'01' },
        { value:'intermediate', en:'Some experience', bn:'কিছু অভিজ্ঞতা আছে', descEn:'Begin near the first applied and inferential concepts.', descBn:'প্রথম applied ও inferential concept-এর কাছ থেকে শুরু করুন।', icon:'02' },
        { value:'advanced', en:'Strong foundation', bn:'ভালো ভিত্তি আছে', descEn:'Begin later in the route with optional prerequisite review.', descBn:'optional prerequisite review-সহ route-এর পরের অংশ থেকে শুরু করুন।', icon:'03' },
      ],
    },
    {
      key: 'mode',
      eyebrow: ['Step 3 of 3', 'ধাপ ৩ / ৩'],
      title: ['How do you learn best?', 'আপনি কীভাবে ভালো শিখেন?'],
      copy: ['Your dashboard will shape each session around this preference.', 'আপনার dashboard প্রতিটি session এই preference অনুযায়ী সাজাবে।'],
      options: [
        { value:'concepts', en:'Concept-first', bn:'কনসেপ্ট-ফার্স্ট', descEn:'Read, connect ideas and summarize before using a lab.', descBn:'lab ব্যবহারের আগে পড়ুন, ধারণা যুক্ত করুন ও summarize করুন।', icon:'A' },
        { value:'balanced', en:'Balanced', bn:'ব্যালান্সড', descEn:'Combine a short lesson, a practical action and interpretation.', descBn:'short lesson, practical action ও interpretation একত্র করুন।', icon:'A+B' },
        { value:'practice', en:'Practice-first', bn:'প্র্যাকটিস-ফার্স্ট', descEn:'Start with examples and labs, then return to the underlying idea.', descBn:'example ও lab দিয়ে শুরু করে পরে underlying idea-তে ফিরুন।', icon:'B' },
      ],
    },
  ];

  function render() {
    const config = steps[step];
    const selected = choices[config.key];
    root.innerHTML = `<div class="wizard-progress" aria-label="${t('Setup progress','সেটআপ অগ্রগতি')}"><span style="width:${((step + 1) / steps.length) * 100}%"></span></div><div class="wizard-heading"><span class="eyebrow">${t(...config.eyebrow)}</span><h1>${t(...config.title)}</h1><p>${t(...config.copy)}</p></div><div class="choice-grid ${config.key === 'goal' ? 'goal-choice-grid' : ''}" role="radiogroup">${config.options.map(option => `<button class="choice-card ${selected === option.value ? 'selected' : ''}" type="button" role="radio" aria-checked="${selected === option.value}" data-value="${option.value}"><span class="choice-icon">${escapeHtml(option.icon)}</span><span><strong>${escapeHtml(t(option.en, option.bn))}</strong><small>${escapeHtml(t(option.descEn, option.descBn))}</small></span><span class="choice-check">✓</span></button>`).join('')}</div><div class="wizard-actions"><button class="button ghost" id="wizard-back" type="button" ${step === 0 ? 'disabled' : ''}>← ${t('Back','পেছনে')}</button><span class="wizard-note">${t('Saved only in this browser','শুধু এই ব্রাউজারে সংরক্ষিত হবে')}</span><button class="button primary" id="wizard-next" type="button" ${selected ? '' : 'disabled'}>${step === steps.length - 1 ? t('Create my plan','আমার প্ল্যান তৈরি করুন') : t('Continue','চালিয়ে যান')} →</button></div>`;

    root.querySelectorAll('.choice-card').forEach(button => button.addEventListener('click', () => {
      choices[config.key] = button.dataset.value;
      render();
    }));
    document.getElementById('wizard-back')?.addEventListener('click', () => { if (step > 0) { step -= 1; render(); } });
    document.getElementById('wizard-next')?.addEventListener('click', () => {
      if (!choices[config.key]) return;
      if (step < steps.length - 1) { step += 1; render(); return; }
      const path = pathMap[choices.goal];
      const profile = {
        goal: choices.goal,
        level: choices.level,
        mode: choices.mode,
        startIndex: levelStartIndex(path, choices.level),
        createdAt: existing?.createdAt || new Date().toISOString(),
        updatedAt: new Date().toISOString(),
      };
      setProfile(profile);
      location.href = '/my-learning/?new=1';
    });
  }

  window.addEventListener('slh:language', render);
  render();
})();
