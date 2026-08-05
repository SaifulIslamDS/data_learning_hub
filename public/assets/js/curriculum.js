(() => {
  'use strict';
  const { DATA, t, escapeHtml, statusLabel } = window.DLH;
  const root = document.getElementById('curriculum-root');
  if (!root) return;

  function baselineTable() {
    return `<section class="curriculum-section"><div class="section-heading"><div><span class="eyebrow">${t('Teaching baselines', 'Teaching baseline')}</span><h2>${t('Tool-specific behavior is anchored to official documentation', 'Tool-specific behavior official documentation-এ anchored')}</h2></div></div><div class="baseline-grid">${DATA.tool_baselines.map(item => `<a class="baseline-card" href="${item.official_url}" target="_blank" rel="noopener noreferrer"><span>${escapeHtml(item.name)}</span><p>${escapeHtml(t(item.baseline_en, item.baseline_bn))}</p><strong>${t('Official documentation', 'Official documentation')} ↗</strong></a>`).join('')}</div></section>`;
  }

  function track(trackItem) {
    const lessonCount = trackItem.modules.reduce((sum, module) => sum + module.lessons.length, 0);
    return `<article class="curriculum-track" id="${trackItem.id}"><header class="curriculum-track-header"><div><span class="status-chip curriculum-ready">${statusLabel(trackItem.status)} · ${trackItem.target_release}</span><h2>${escapeHtml(t(trackItem.title_en, trackItem.title_bn))}</h2><p>${escapeHtml(t(trackItem.outcome_en, trackItem.outcome_bn))}</p></div><div class="curriculum-count"><strong>${trackItem.modules.length}</strong><span>${t('modules', 'module')}</span><strong>${lessonCount}</strong><span>${t('planned lessons', 'planned lesson')}</span></div></header><div class="prerequisite-row"><strong>${t('Prerequisites', 'Prerequisite')}</strong>${trackItem.prerequisites.map(item => `<span>${escapeHtml(item)}</span>`).join('')}</div><div class="curriculum-module-list">${trackItem.modules.map((module, index) => `<details class="curriculum-module" ${index === 0 ? 'open' : ''}><summary><span>${String(index + 1).padStart(2, '0')}</span><strong>${escapeHtml(t(module.title_en, module.title_bn))}</strong><small>${module.lessons.length} ${t('planned lessons', 'planned lesson')}</small><b>＋</b></summary><ol>${module.lessons.map(lesson => `<li>${escapeHtml(lesson)}</li>`).join('')}</ol></details>`).join('')}</div><footer class="curriculum-track-footer"><p>${t('These entries define reviewed scope and sequence. They are not counted as published lessons until their complete bilingual pages, examples, exercises and quality checks exist.', 'এই entry reviewed scope ও sequence define করে। Complete bilingual page, example, exercise ও quality check না হওয়া পর্যন্ত published lesson হিসেবে count হবে না।')}</p><a href="${trackItem.reference_url}" target="_blank" rel="noopener noreferrer">${t('Primary reference', 'Primary reference')} ↗</a></footer></article>`;
  }

  function roadmap() {
    return `<section class="curriculum-section"><div class="section-heading"><div><span class="eyebrow">${t('Release sequence', 'Release sequence')}</span><h2>${t('One complete track at a time', 'একবারে একটি complete track')}</h2></div></div><div class="release-roadmap">${DATA.release_roadmap.map((item, index) => `<div class="release-step ${item.status}"><span>${String(index + 1).padStart(2, '0')}</span><div><small>${item.version}</small><strong>${escapeHtml(t(item.title_en, item.title_bn))}</strong></div><b>${item.status === 'current' ? '●' : '○'}</b></div>`).join('')}</div></section>`;
  }

  function render() {
    root.innerHTML = `<section class="curriculum-intro-grid"><article class="topic-card"><span class="section-kicker">${t('Available now', 'এখন available')}</span><h2>${t('Data Foundations and Statistics', 'Data Foundations ও Statistics')}</h2><p>${t(`${DATA.topics.length} comprehensive lessons and ${DATA.tools.length} browser labs remain fully available, now positioned as the first two phases of the Data Analyst journey.`, `${DATA.topics.length} comprehensive lesson ও ${DATA.tools.length} browser lab এখন Data Analyst journey-এর প্রথম দুই phase হিসেবে available।`)}</p><a class="button primary" href="/learn/">${t('Open available learning', 'Available learning খুলুন')}</a></article><article class="topic-card"><span class="section-kicker">${t('Curriculum-ready', 'Curriculum-ready')}</span><h2>Excel → SQL → Power BI → Python</h2><p>${t('Each tool track has defined prerequisites, outcomes, modules, lesson scope and authoritative references before content production.', 'Content production-এর আগে প্রতিটি tool track-এর prerequisite, outcome, module, lesson scope ও authoritative reference defined।')}</p><p class="small">${t('No planned lesson is presented as already published.', 'কোনো planned lesson-কে published হিসেবে দেখানো হয় না।')}</p></article></section>${roadmap()}${baselineTable()}<section class="curriculum-section tool-track-stack"><div class="section-heading"><div><span class="eyebrow">${t('Tool curricula', 'Tool curriculum')}</span><h2>${t('Reviewed scope and sequence', 'Reviewed scope ও sequence')}</h2></div></div>${DATA.tool_curricula.map(track).join('')}</section>`;
    root.querySelectorAll('.curriculum-module').forEach(details => details.addEventListener('toggle', () => {
      const marker = details.querySelector('summary b');
      if (marker) marker.textContent = details.open ? '−' : '＋';
    }));
  }

  window.addEventListener('dlh:language', render);
  render();
})();
