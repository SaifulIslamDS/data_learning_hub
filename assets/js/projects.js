(() => {
  'use strict';
  const { DATA, t, escapeHtml, statusLabel } = window.DLH;
  const root = document.getElementById('projects-root');
  if (!root) return;

  function render() {
    const available = DATA.projects.filter(project => project.status === 'available');
    const roadmap = DATA.projects.filter(project => project.status !== 'available');
    root.innerHTML = `<section class="project-foundation-grid">${available.map(project => {
      const dataset = DATA.datasets.find(item => item.id === project.dataset);
      return `<article class="project-card featured"><span class="status-chip available">${t('Available now', 'এখন available')}</span><h2>${escapeHtml(t(project.title_en, project.title_bn))}</h2><p>${escapeHtml(t(project.description_en, project.description_bn))}</p><div class="project-meta"><span>${project.level}</span><span>${dataset?.rows || 0} ${t('dataset rows', 'dataset row')}</span><span>${t('Statistics foundation', 'Statistics foundation')}</span></div><div class="hero-actions"><a class="button primary" href="${project.url}">${t('Open project', 'Project খুলুন')} →</a><a class="button ghost" href="${dataset.file}" download>${t('Download dataset', 'Dataset download')}</a></div></article>`;
    }).join('')}<article class="project-card"><span class="status-chip foundation-ready">${t('Architecture ready', 'Architecture ready')}</span><h2>${t('One dataset across four tools', 'এক dataset চারটি tool-এ')}</h2><p>${t('Future projects will reuse the same business data in Excel, SQL, Power BI and Python so the learner sees how analytical reasoning transfers between tools.', 'Future project একই business data Excel, SQL, Power BI ও Python-এ reuse করবে, যাতে analytical reasoning tool-এর মধ্যে কীভাবে transfer হয় বোঝা যায়।')}</p><a class="button ghost" href="/curriculum/">${t('View tool sequence', 'Tool sequence দেখুন')} →</a></article></section><section class="curriculum-section"><div class="section-heading"><div><span class="eyebrow">${t('Portfolio roadmap', 'Portfolio roadmap')}</span><h2>${t('Projects become deeper as tool tracks arrive', 'Tool track আসার সঙ্গে project deeper হবে')}</h2></div></div><div class="project-roadmap">${roadmap.map(project => `<article class="project-card roadmap"><span class="status-chip roadmap">${statusLabel(project.status)}</span><h3>${escapeHtml(t(project.title_en, project.title_bn))}</h3><p>${escapeHtml(t(project.description_en, project.description_bn))}</p><small>${t('Not yet published as a project page', 'এখনও project page হিসেবে publish হয়নি')}</small></article>`).join('')}</div></section><section class="curriculum-section"><div class="section-heading"><div><span class="eyebrow">${t('Dataset library', 'Dataset library')}</span><h2>${t('Documented synthetic data available now', 'Documented synthetic data এখন available')}</h2></div></div><div class="dataset-grid">${DATA.datasets.map(dataset => `<article class="dataset-card"><div class="dataset-card-top"><span class="dataset-icon">CSV</span><span class="status-chip available">${dataset.rows} ${t('rows', 'row')}</span></div><h3>${escapeHtml(t(dataset.title_en, dataset.title_bn))}</h3><p>${escapeHtml(t(dataset.description_en, dataset.description_bn))}</p><div class="dataset-actions"><a class="button small primary" href="${dataset.file}" download>${t('Download data', 'Data download')}</a><a class="button small ghost" href="${dataset.dictionary}" download>${t('Dictionary', 'Dictionary')}</a></div></article>`).join('')}</div></section>`;
  }

  window.addEventListener('dlh:language', render);
  render();
})();
