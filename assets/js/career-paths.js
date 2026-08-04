(() => {
  'use strict';
  const { DATA, pathMap, t, escapeHtml, pathProgress, statusLabel, setProfile, getProfile, levelStartIndex } = window.DLH;
  const root = document.getElementById('career-paths-root');
  if (!root) return;

  function phaseGrid(career) {
    if (!career.phases?.length) return '';
    return `<div class="journey-phase-grid">${career.phases.map((phase, index) => `<div class="journey-phase ${phase.status}"><span>${String(index + 1).padStart(2, '0')}</span><div><small>${statusLabel(phase.status)} · ${phase.release}</small><strong>${escapeHtml(t(phase.title_en, phase.title_bn))}</strong></div></div>`).join('')}</div>`;
  }

  function render() {
    const activeProfile = getProfile();
    root.innerHTML = DATA.career_paths.map(career => {
      const path = pathMap[career.id];
      const progress = path ? pathProgress(path) : { done:0, total:0, percent:0 };
      const active = activeProfile?.goal === career.id;
      const available = Boolean(path);
      return `<article class="career-card ${career.status} ${active ? 'selected' : ''}" id="${career.id}"><div class="career-card-header"><div><span class="status-chip ${career.status === 'active' || career.status === 'supporting' ? 'available' : 'roadmap'}">${career.status === 'active' ? t('Primary active path', 'Primary active path') : career.status === 'supporting' ? t('Supporting path', 'Supporting path') : t('Future roadmap', 'Future roadmap')}</span><h2>${escapeHtml(t(career.title_en, career.title_bn))}</h2><p>${escapeHtml(t(career.description_en, career.description_bn))}</p></div>${active ? `<span class="badge completed-badge">✓ ${t('Your plan', 'আপনার plan')}</span>` : ''}</div>${available ? `<div class="career-progress"><div class="progress-track"><span style="width:${progress.percent}%"></span></div><span>${progress.done}/${progress.total} ${t('available lessons complete', 'available lesson complete')}</span></div>` : ''}${phaseGrid(career)}<div class="career-card-actions">${available ? `<button class="button ${active ? 'ghost' : 'primary'}" type="button" data-select-path="${career.id}">${active ? t('Keep this path', 'এই path রাখুন') : t('Use this path', 'এই path ব্যবহার করুন')}</button><a class="button ghost" href="/learn/?all=0">${t('View available lessons', 'Available lesson দেখুন')}</a>` : `<a class="button ghost" href="/curriculum/">${t('See shared foundation', 'Shared foundation দেখুন')}</a>`}<span class="career-note">${available ? t('Only implemented lessons are added to My Learning.', 'শুধু implemented lesson My Learning-এ যোগ হয়।') : t('This route will not become selectable until its curriculum is fully implemented.', 'Curriculum fully implement না হওয়া পর্যন্ত এই route selectable হবে না।')}</span></div></article>`;
    }).join('');

    root.querySelectorAll('[data-select-path]').forEach(button => button.addEventListener('click', () => {
      const goal = button.dataset.selectPath;
      const path = pathMap[goal];
      const current = getProfile();
      setProfile({
        ...(current || {}),
        goal,
        level: current?.level || 'beginner',
        time: current?.time || 40,
        mode: current?.mode || 'balanced',
        knowledge: current?.knowledge || [],
        startIndex: levelStartIndex(path, current?.level || 'beginner'),
        updatedAt: new Date().toISOString(),
        createdAt: current?.createdAt || new Date().toISOString(),
      });
      location.href = '/my-learning/';
    }));
  }

  window.addEventListener('dlh:language', render);
  window.addEventListener('dlh:profile', render);
  window.addEventListener('dlh:progress', render);
  render();
})();
