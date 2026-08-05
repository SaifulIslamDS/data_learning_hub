(() => {
  'use strict';
  const T=window.DLHTutorial; if(!T) return;
  const tutorial=T.getTutorial(); const root=document.getElementById('exercise-library-root'); const filter=document.getElementById('exercise-chapter-filter');
  tutorial.chapters.forEach((ch,i)=>filter.insertAdjacentHTML('beforeend',`<option value="${ch.id}">${String(i+1).padStart(2,'0')} · ${ch.title_en}</option>`));
  function render(){
    const chosen=filter.value; const chapters=chosen==='all'?tutorial.chapters:tutorial.chapters.filter(ch=>ch.id===chosen);
    root.innerHTML=chapters.map((ch,ci)=>`<section class="exercise-library-section"><header><span>${String(tutorial.chapters.indexOf(ch)+1).padStart(2,'0')}</span><div><h2>${T.escapeHtml(T.t(ch.title_en,ch.title_bn))}</h2><a href="/tutorials/${tutorial.id}/${ch.id}/">${T.t('Open chapter','Chapter খুলুন')} →</a></div></header><div class="exercise-stack">${ch.exercises.map((x,i)=>T.renderExercise(x,i,`library-${ch.id}`)).join('')}</div></section>`).join('');
    chapters.forEach(ch=>{const section=[...root.querySelectorAll('.exercise-library-section')].find(s=>s.querySelector('h2')?.textContent===T.t(ch.title_en,ch.title_bn));if(section)T.bindExercises(section,ch.exercises);});
  }
  filter.addEventListener('change',render);
  document.getElementById('reset-exercises')?.addEventListener('click',()=>{filter.value='all';render();});
  window.addEventListener('dlh:language',render); render();
})();
