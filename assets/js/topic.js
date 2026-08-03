(() => {
  const { DATA, topicMap, moduleMap, toolMap, t, escapeHtml, isCompleted, toggleCompleted, getBookmarks, toggleBookmark } = window.SLH;
  const id=document.body.dataset.topic; const topic=topicMap[id]; if(!topic)return;
  const module=moduleMap[topic.module]; const root=document.getElementById('topic-content');

  function related(){
    const peers=DATA.topics.filter(x=>x.module===topic.module&&x.id!==id);
    const index=peers.findIndex(x=>x.order>topic.order);
    const start=Math.max(0,index<0?peers.length-3:index-1);
    return peers.slice(start,start+3);
  }
  function updateActions(){
    const completed=isCompleted(id); const bookmarked=getBookmarks().has(id);
    const complete=document.getElementById('complete-topic'); const bookmark=document.getElementById('bookmark-topic');
    complete.textContent=completed?t('Completed ✓','সম্পন্ন ✓'):t('Mark complete','সম্পন্ন করুন'); complete.classList.toggle('success',completed);
    bookmark.textContent=bookmarked?'★':'☆'; bookmark.setAttribute('aria-label',bookmarked?t('Remove bookmark','বুকমার্ক সরান'):t('Bookmark lesson','লেসন বুকমার্ক করুন'));
  }
  function render(){
    document.querySelector('.topic-hero .eyebrow').textContent=t(module.title_en,module.title_bn);
    document.querySelector('.topic-hero h1').textContent=t(topic.title_en,topic.title_bn);
    document.querySelector('.topic-hero p').textContent=t(topic.summary_en,topic.summary_bn);
    const objectives=stateObjectives();
    const relatedLinks=related().map(x=>`<a href="/${x.url}">${escapeHtml(t(x.title_en,x.title_bn))}</a>`).join('');
    const lab=topic.lab?toolMap[topic.lab]:null;
    root.innerHTML=`<div class="topic-layout"><article class="topic-main"><section class="topic-card"><h2>${t('Learning objectives','শেখার উদ্দেশ্য')}</h2><ul class="objective-list">${objectives.map(x=>`<li>${escapeHtml(x)}</li>`).join('')}</ul></section><section class="topic-card"><h2>${t('Core idea','মূল ধারণা')}</h2><p>${escapeHtml(t(topic.summary_en,topic.summary_bn))}</p><div class="formula-block">${escapeHtml(t(topic.formula_en,topic.formula_bn))}</div></section><section class="topic-card"><h2>${t('Worked application','প্রয়োগভিত্তিক উদাহরণ')}</h2><p>${escapeHtml(t(topic.example_en,topic.example_bn))}</p><ol class="check-list"><li>${t('Define the analytical question and target quantity before calculating.','হিসাবের আগে analytical question ও target quantity নির্ধারণ করুন।')}</li><li>${t('Check data type, sampling process and method assumptions.','data type, sampling process ও method assumption যাচাই করুন।')}</li><li>${t('Calculate or organize the required quantities using the stated convention.','উল্লেখিত convention অনুযায়ী প্রয়োজনীয় quantity হিসাব বা সংগঠিত করুন।')}</li><li>${t('Interpret magnitude, uncertainty and limitations in context.','context অনুযায়ী magnitude, uncertainty ও limitation ব্যাখ্যা করুন।')}</li></ol></section><section class="topic-card"><h2>${t('Interpretation standard','ব্যাখ্যার স্ট্যান্ডার্ড')}</h2><p>${t('A numerical result is not a decision by itself. Explain the population, units, direction, magnitude, uncertainty, assumptions and practical consequence. For observational data, do not claim causation from association alone.','একটি numerical result নিজে কোনো decision নয়। population, unit, direction, magnitude, uncertainty, assumption ও practical consequence ব্যাখ্যা করুন। observational data থেকে শুধু association দেখে causation দাবি করবেন না।')}</p></section><section class="topic-card"><h2>${t('Common mistakes','সাধারণ ভুল')}</h2><p>${escapeHtml(t(topic.mistakes_en,topic.mistakes_bn))}</p></section>${lab?`<section class="topic-card lab-callout"><span class="eyebrow">${t('Interactive practice','ইন্টারঅ্যাকটিভ প্র্যাকটিস')}</span><h2>${escapeHtml(t(lab.title_en,lab.title_bn))}</h2><p>${escapeHtml(t(lab.description_en,lab.description_bn))}</p><a class="button primary" href="/${lab.url}">${t('Open the lab','ল্যাব খুলুন')} →</a></section>`:''}</article><aside class="topic-sidebar"><section class="topic-card"><h2>${t('Lesson details','লেসনের তথ্য')}</h2><div class="meta-list"><div class="meta-row"><span>${t('Module','মডিউল')}</span><strong>${escapeHtml(t(module.title_en,module.title_bn))}</strong></div><div class="meta-row"><span>${t('Level','লেভেল')}</span><strong>${escapeHtml(t(topic.difficulty,({Beginner:'বিগিনার',Intermediate:'ইন্টারমিডিয়েট',Advanced:'অ্যাডভান্সড'})[topic.difficulty]))}</strong></div><div class="meta-row"><span>${t('Study time','সময়')}</span><strong>${topic.minutes} ${t('minutes','মিনিট')}</strong></div><div class="meta-row"><span>${t('Format','ফরম্যাট')}</span><strong>${topic.kind==='lab'?t('Lesson + lab','লেসন + ল্যাব'):topic.kind==='practice'?t('Practice lesson','প্র্যাকটিস লেসন'):t('Concept lesson','কনসেপ্ট লেসন')}</strong></div></div></section><section class="topic-card"><h2>${t('Related lessons','সম্পর্কিত লেসন')}</h2><div class="related-list">${relatedLinks}</div></section><section class="topic-card"><h2>${t('Accuracy note','অ্যাকুরেসি নোট')}</h2><p class="small">${t('Definitions use standard statistical conventions. A method can still be inappropriate when its data requirements or assumptions are not met.','সংজ্ঞায় standard statistical convention ব্যবহার করা হয়েছে। data requirement বা assumption পূরণ না হলে method অনুপযুক্ত হতে পারে।')}</p></section></aside></div>`;
    updateActions();
  }
  function stateObjectives(){ return [
    t(`Explain what ${topic.title_en} means and why it is used.`,`${topic.title_bn} কী এবং কেন ব্যবহার করা হয় তা ব্যাখ্যা করুন।`),
    t('Recognize the data requirements and assumptions that affect validity.','validity-কে প্রভাবিত করা data requirement ও assumption শনাক্ত করুন।'),
    t('Apply the idea to a small practical example using a stated convention.','উল্লেখিত convention অনুযায়ী ছোট practical example-এ ধারণাটি প্রয়োগ করুন।'),
    t('Interpret the output without overstating certainty or causality.','certainty বা causality অতিরঞ্জিত না করে output ব্যাখ্যা করুন।')
  ]; }
  document.getElementById('complete-topic').addEventListener('click',()=>{toggleCompleted(id);updateActions();});
  document.getElementById('bookmark-topic').addEventListener('click',()=>{toggleBookmark(id);updateActions();});
  window.addEventListener('slh:language',render); render();
})();
