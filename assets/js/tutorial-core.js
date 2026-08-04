(() => {
  'use strict';
  const DATA = window.DLH_CONTENT;
  if (!DATA?.tutorials?.length) return;
  const api = window.DLH;
  const lang = () => api?.state?.language === 'bn' ? 'bn' : 'en';
  const t = (en, bn) => lang() === 'bn' ? (bn || en) : en;
  const escapeHtml = api?.escapeHtml || (value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])));
  const safe = api?.safeStorage || {
    json(key, fallback=[]) { try { return JSON.parse(localStorage.getItem(key) || JSON.stringify(fallback)); } catch { return fallback; } },
    set(key, value) { try { localStorage.setItem(key, value); } catch {} },
    get(key, fallback=null) { try { return localStorage.getItem(key) ?? fallback; } catch { return fallback; } },
    remove(key) { try { localStorage.removeItem(key); } catch {} },
  };
  const tutorialMap = Object.fromEntries(DATA.tutorials.map(item => [item.id, item]));
  const getTutorial = (id=document.body.dataset.tutorial) => tutorialMap[id] || DATA.tutorials[0];
  const keyFor = id => `dlh-tutorial-${id}-completed`;
  const getCompleted = id => new Set(safe.json(keyFor(id), []));
  const setCompleted = (id,set) => safe.set(keyFor(id), JSON.stringify([...set]));
  const isComplete = (tutorialId, chapterId) => getCompleted(tutorialId).has(chapterId);
  const toggleComplete = (tutorialId, chapterId) => {
    const set=getCompleted(tutorialId); set.has(chapterId) ? set.delete(chapterId) : set.add(chapterId); setCompleted(tutorialId,set); updateProgress(tutorialId); return set.has(chapterId);
  };
  function updateProgress(tutorialId=document.body.dataset.tutorial) {
    const tutorial=getTutorial(tutorialId); if (!tutorial) return;
    const completed=getCompleted(tutorial.id);
    const total=tutorial.chapters.length;
    const done=tutorial.chapters.filter(ch => completed.has(ch.id)).length;
    document.querySelectorAll('#tutorial-progress-label').forEach(el => el.textContent=`${done}/${total}`);
    document.querySelectorAll('#tutorial-progress-bar').forEach(el => el.style.width=`${total ? Math.round(done/total*100) : 0}%`);
    document.querySelectorAll('[data-chapter-link]').forEach(link => {
      const yes=completed.has(link.dataset.chapterLink); link.classList.toggle('completed',yes);
      const state=link.querySelector('.chapter-state'); if(state) state.textContent=yes?'✓':'○';
    });
    document.querySelectorAll('[data-chapter-card]').forEach(card => card.classList.toggle('completed',completed.has(card.dataset.chapterCard)));
    const landing=document.getElementById('course-landing-progress'); if(landing) landing.textContent=`${done}/${total}`;
  }
  function setupDrawer() {
    const sidebar=document.getElementById('tutorial-sidebar'); const backdrop=document.getElementById('tutorial-drawer-backdrop');
    const open=()=>{sidebar?.classList.add('open');backdrop?.classList.add('open');document.body.classList.add('drawer-open');};
    const close=()=>{sidebar?.classList.remove('open');backdrop?.classList.remove('open');document.body.classList.remove('drawer-open');};
    document.getElementById('tutorial-drawer-open')?.addEventListener('click',open);
    document.getElementById('tutorial-drawer-close')?.addEventListener('click',close);
    backdrop?.addEventListener('click',close);
    document.addEventListener('keydown',e=>{if(e.key==='Escape')close();});
    const input=document.getElementById('tutorial-chapter-search');
    input?.addEventListener('input',()=>{const q=input.value.trim().toLowerCase();document.querySelectorAll('[data-chapter-link]').forEach(link=>{link.hidden=q && !link.textContent.toLowerCase().includes(q);});});
  }
  function feedbackBox(kind,text) { return `<div class="exercise-feedback ${kind}">${escapeHtml(text)}</div>`; }
  function normalize(value) { return String(value??'').trim().toLowerCase().replace(/[.?!,]/g,''); }
  function renderExercise(exercise,index,scope='chapter') {
    const id=`${scope}-exercise-${index}`;
    let control='';
    if(exercise.type==='mcq') {
      control=`<div class="exercise-options">${exercise.options_en.map((opt,i)=>`<label><input type="radio" name="${id}" value="${String.fromCharCode(65+i)}"><span>${escapeHtml(t(opt, exercise.options_bn?.[i]))}</span></label>`).join('')}</div>`;
    } else if(exercise.type==='fill') {
      control=`<label class="exercise-input"><span>${t('Your answer','আপনার উত্তর')}</span><input type="text" data-exercise-input autocomplete="off"></label>`;
    } else {
      control=`<label class="exercise-input"><span>${t('Write your response','আপনার response লিখুন')}</span><textarea data-exercise-input rows="4"></textarea></label>`;
    }
    return `<article class="exercise-card" data-exercise-type="${exercise.type}" data-answer-en="${escapeHtml(exercise.answer_en)}" data-answer-bn="${escapeHtml(exercise.answer_bn)}"><div class="exercise-number">${index+1}</div><h3>${escapeHtml(t(exercise.prompt_en,exercise.prompt_bn))}</h3>${control}<div class="exercise-actions"><button class="button small primary" type="button" data-check-exercise>${exercise.type==='short'?t('Show model answer','Model answer দেখুন'):t('Check answer','Answer check করুন')}</button><button class="button small ghost" type="button" data-reset-exercise>${t('Reset','Reset')}</button></div><div class="exercise-feedback-root" aria-live="polite"></div></article>`;
  }
  function bindExercises(root, exercises) {
    root.querySelectorAll('.exercise-card').forEach((card,index)=>{
      const exercise=exercises[index]; const feedback=card.querySelector('.exercise-feedback-root');
      card.querySelector('[data-check-exercise]')?.addEventListener('click',()=>{
        if(exercise.type==='short') { feedback.innerHTML=feedbackBox('model',`${t('Model answer','Model answer')}: ${t(exercise.answer_en,exercise.answer_bn)}`); return; }
        let value='';
        if(exercise.type==='mcq') value=card.querySelector('input:checked')?.value || '';
        else value=card.querySelector('[data-exercise-input]')?.value || '';
        if(!value) { feedback.innerHTML=feedbackBox('warning',t('Choose or enter an answer first.','প্রথমে answer choose বা enter করুন।')); return; }
        const correct=normalize(value)===normalize(exercise.answer_en) || normalize(value)===normalize(exercise.answer_bn);
        const explanation=t(exercise.explanation_en || exercise.answer_en,exercise.explanation_bn || exercise.answer_bn);
        feedback.innerHTML=feedbackBox(correct?'correct':'incorrect',`${correct?t('Correct','সঠিক'):t('Not yet','এখনও নয়')}. ${explanation}`);
      });
      card.querySelector('[data-reset-exercise]')?.addEventListener('click',()=>{
        card.querySelectorAll('input').forEach(input=>{if(input.type==='radio')input.checked=false;else input.value='';});
        card.querySelectorAll('textarea').forEach(el=>el.value=''); feedback.innerHTML='';
      });
    });
  }
  setupDrawer(); updateProgress();
  window.addEventListener('dlh:language',()=>updateProgress());
  window.DLHTutorial={DATA,t,lang,escapeHtml,safe,getTutorial,tutorialMap,getCompleted,setCompleted,isComplete,toggleComplete,updateProgress,renderExercise,bindExercises,normalize};
})();
