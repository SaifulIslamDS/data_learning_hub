(() => {
  'use strict';
  const { DATA, t, escapeHtml } = window.DLH;
  const root = document.getElementById('projects-root');
  if (!root) return;

  function card(project) {
    const tools = project.tools.map(tool => `<span>${escapeHtml(tool)}</span>`).join('');
    const download = project.downloads?.[0];
    return `<article class="portfolio-project-card">
      <div class="project-card-top"><span class="status-chip available">${t('Complete project', 'Complete project')}</span><span>${project.estimated_hours} ${t('hours', 'ঘণ্টা')}</span></div>
      <h2>${escapeHtml(t(project.title_en, project.title_bn))}</h2>
      <p>${escapeHtml(t(project.summary_en, project.summary_bn))}</p>
      <div class="project-tools">${tools}</div>
      <div class="project-stat-row"><span>${escapeHtml(project.level)}</span><span>8 ${t('workflow phases', 'workflow phase')}</span><span>${project.deliverables.length} ${t('deliverables', 'deliverable')}</span></div>
      <div class="hero-actions"><a class="button primary" href="${project.url}">${t('Open project', 'Project খুলুন')} →</a>${download ? `<a class="button ghost" href="${download.url}" download>${t('Download package', 'Package download')}</a>` : ''}</div>
    </article>`;
  }

  function render() {
    const projects = DATA.projects.filter(project => project.status === 'available');
    root.innerHTML = `<section class="project-hub-intro"><div><span class="eyebrow">${t('Six complete case studies', 'ছয়টি complete case study')}</span><h2>${t('Choose a business problem and build the evidence', 'Business problem বেছে evidence তৈরি করুন')}</h2><p>${t('Every project uses the same eight-phase workflow, downloadable synthetic data, validation gates and portfolio templates.', 'প্রতিটি project একই আট-phase workflow, downloadable synthetic data, validation gate ও portfolio template ব্যবহার করে।')}</p></div><div class="project-toolkit-card"><strong>${t('Portfolio toolkit', 'Portfolio toolkit')}</strong><p>${t('Reusable charter, analysis plan, README, presentation, QA and insight-log templates.', 'Reusable charter, analysis plan, README, presentation, QA ও insight-log template।')}</p><a class="button ghost" href="/assets/downloads/portfolio/data-analytics-portfolio-toolkit.zip" download>${t('Download toolkit', 'Toolkit download')} ↓</a></div></section><div class="portfolio-project-grid">${projects.map(card).join('')}</div><section class="project-path-panel"><div><span class="eyebrow">${t('Learn the workflow first', 'আগে workflow শিখুন')}</span><h2>${t('Need step-by-step guidance?', 'Step-by-step guidance প্রয়োজন?')}</h2><p>${t('The complete Analytics Workflows tutorial teaches framing, data understanding, preparation, analysis, validation, communication and portfolio delivery.', 'Complete Analytics Workflows tutorial framing, data understanding, preparation, analysis, validation, communication ও portfolio delivery শেখায়।')}</p></div><a class="button primary" href="/tutorials/data-analytics-workflows/">${t('Open workflow tutorial', 'Workflow tutorial খুলুন')} →</a></section>`;
  }

  window.addEventListener('dlh:language', render);
  render();
})();
