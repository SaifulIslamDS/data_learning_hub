(() => {
  'use strict';
  const T=window.DLHTutorial; if(!T) return;
  T.updateProgress();
  const input=document.getElementById('example-search');
  input?.addEventListener('input',()=>{const q=input.value.trim().toLowerCase();document.querySelectorAll('.example-library-card').forEach(card=>card.hidden=q && !card.textContent.toLowerCase().includes(q));});
})();
