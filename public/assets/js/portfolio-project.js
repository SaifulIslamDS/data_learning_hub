(() => {
  'use strict';
  const projectId = document.body.dataset.project;
  if (!projectId) return;
  const boxes = [...document.querySelectorAll('[data-project-task]')];
  const progress = document.querySelector('[data-project-progress]');
  const bar = document.querySelector('[data-project-progress-bar]');
  const reset = document.querySelector('[data-reset-project]');
  const key = `dlh-project-${projectId}-tasks`;

  function read() {
    try { return new Set(JSON.parse(localStorage.getItem(key) || '[]')); }
    catch { return new Set(); }
  }
  function update() {
    const done = boxes.filter(box => box.checked).length;
    if (progress) progress.textContent = `${done}/${boxes.length} phases`;
    if (bar) bar.style.width = `${boxes.length ? (done / boxes.length) * 100 : 0}%`;
  }
  function save() {
    localStorage.setItem(key, JSON.stringify(boxes.filter(box => box.checked).map(box => box.dataset.projectTask)));
    update();
  }
  const saved = read();
  boxes.forEach(box => {
    box.checked = saved.has(box.dataset.projectTask);
    box.addEventListener('change', save);
  });
  reset?.addEventListener('click', () => {
    boxes.forEach(box => { box.checked = false; });
    localStorage.removeItem(key);
    update();
  });
  update();
})();
