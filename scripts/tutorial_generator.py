from __future__ import annotations
from html import escape
from pathlib import Path


def attr(value: str) -> str:
    return escape(str(value), quote=True)


def bi(tag: str, en: str, bn: str, class_name: str = '', extra: str = '') -> str:
    cls = f' class="{class_name}"' if class_name else ''
    return f'<{tag}{cls} data-en="{attr(en)}" data-bn="{attr(bn)}" {extra}>{escape(en)}</{tag}>'


def sidebar(tutorial: dict, current: str = '') -> str:
    links = []
    for i, chapter in enumerate(tutorial['chapters'], 1):
        links.append(
            f'<a class="tutorial-chapter-link {"current" if chapter["id"] == current else ""}" '
            f'href="/tutorials/{tutorial["id"]}/{chapter["id"]}/" data-chapter-link="{chapter["id"]}">'
            f'<span>{i:02d}</span><span data-en="{attr(chapter["title_en"])}" data-bn="{attr(chapter["title_bn"])}">{escape(chapter["title_en"])}</span>'
            f'<b class="chapter-state" aria-hidden="true">○</b></a>'
        )
    return f'''<aside class="tutorial-sidebar" id="tutorial-sidebar">
      <div class="tutorial-sidebar-head">
        <a href="/tutorials/{tutorial['id']}/" class="tutorial-course-title">{escape(tutorial['title_en'])}</a>
        <button class="icon-button tutorial-drawer-close" id="tutorial-drawer-close" type="button" aria-label="Close chapter menu">×</button>
      </div>
      <label class="tutorial-sidebar-search"><span class="sr-only">Search chapters</span><input id="tutorial-chapter-search" type="search" placeholder="Search chapters…" data-placeholder-en="Search chapters…" data-placeholder-bn="Chapter খুঁজুন…"></label>
      <div class="tutorial-progress-mini"><div><span data-en="Course progress" data-bn="Course progress">Course progress</span><strong id="tutorial-progress-label">0/{len(tutorial['chapters'])}</strong></div><div class="progress-track"><span id="tutorial-progress-bar" style="width:0"></span></div></div>
      <nav class="tutorial-chapter-nav" aria-label="Course chapters">{''.join(links)}</nav>
      <div class="tutorial-sidebar-links"><a href="/exercises/{tutorial['id']}/">Exercises</a><a href="/quiz/{tutorial['id']}/">Final quiz</a><a href="/examples/{tutorial['id']}/">Examples</a><a href="/references/{tutorial['id']}/">References</a></div>
    </aside>'''


def course_header(tutorial: dict, eyebrow_en: str, eyebrow_bn: str, title_en: str, title_bn: str, summary_en: str, summary_bn: str) -> str:
    return f'''<header class="tutorial-page-header"><div>
      {bi('span', eyebrow_en, eyebrow_bn, 'eyebrow')}
      {bi('h1', title_en, title_bn)}
      {bi('p', summary_en, summary_bn, 'tutorial-lead')}
    </div><div class="tutorial-header-actions"><button class="button ghost tutorial-drawer-open" id="tutorial-drawer-open" type="button">☰ <span data-en="Chapters" data-bn="Chapter">Chapters</span></button><button class="button ghost" type="button" onclick="window.print()">⎙ <span data-en="Print" data-bn="Print">Print</span></button></div></header>'''


def render_terms(terms: list[dict]) -> str:
    cards = []
    for item in terms:
        example = ''
        if item.get('example_en'):
            example = bi('small', item['example_en'], item.get('example_bn', item['example_en']), 'term-example')
        cards.append(f'''<article class="term-card">{bi('h3', item['term_en'], item['term_bn'])}{bi('p', item['definition_en'], item['definition_bn'])}{example}</article>''')
    return ''.join(cards)


def render_worked(worked: dict) -> str:
    steps = ''.join(f'<li><span>{i}</span>{bi("p", en, worked["steps_bn"][i-1])}</li>' for i, en in enumerate(worked['steps_en'], 1))
    return f'''<section class="tutorial-section worked-example" id="worked-example">
      <div class="section-kicker">Example</div>{bi('h2', worked['title_en'], worked['title_bn'])}{bi('p', worked['context_en'], worked['context_bn'], 'example-context')}
      <ol class="worked-steps">{steps}</ol>
      <div class="example-conclusion"><strong data-en="Conclusion" data-bn="Conclusion">Conclusion</strong>{bi('p', worked['conclusion_en'], worked['conclusion_bn'])}</div>
    </section>'''


def render_chapter(tutorial: dict, chapter: dict, index: int, shell) -> str:
    prev_ch = tutorial['chapters'][index - 1] if index > 0 else None
    next_ch = tutorial['chapters'][index + 1] if index + 1 < len(tutorial['chapters']) else None
    objectives = ''.join(f'<li>{bi("span", o["en"], o["bn"])}</li>' for o in chapter['objectives'])
    sections = []
    for n, item in enumerate(chapter['sections'], 1):
        example = ''
        if item.get('example_en'):
            example = f'<div class="inline-example"><strong data-en="Example" data-bn="উদাহরণ">Example</strong>{bi("p", item["example_en"], item.get("example_bn", item["example_en"]))}</div>'
        sections.append(f'''<section class="tutorial-section" id="concept-{n}"><div class="section-kicker">{n:02d}</div>{bi('h2', item['title_en'], item['title_bn'])}{bi('p', item['body_en'], item['body_bn'])}{example}</section>''')
    recap = ''.join(f'<li>{bi("span", item["en"], item["bn"])}</li>' for item in chapter['recap'])
    refs = ''.join(f'<li><a href="{attr(r["url"])}" target="_blank" rel="noopener noreferrer">{escape(r["title"])} ↗</a></li>' for r in chapter['references'])
    prev_link = f'<a class="tutorial-prev" href="/tutorials/{tutorial["id"]}/{prev_ch["id"]}/"><small>← Previous</small><strong data-en="{attr(prev_ch["title_en"])}" data-bn="{attr(prev_ch["title_bn"])}">{escape(prev_ch["title_en"])}</strong></a>' if prev_ch else '<span></span>'
    next_link = f'<a class="tutorial-next" href="/tutorials/{tutorial["id"]}/{next_ch["id"]}/"><small>Next →</small><strong data-en="{attr(next_ch["title_en"])}" data-bn="{attr(next_ch["title_bn"])}">{escape(next_ch["title_en"])}</strong></a>' if next_ch else f'<a class="tutorial-next" href="/quiz/{tutorial["id"]}/"><small>Finish →</small><strong>Final Quiz</strong></a>'
    main = f'''<div class="tutorial-layout">
      {sidebar(tutorial, chapter['id'])}
      <div class="tutorial-drawer-backdrop" id="tutorial-drawer-backdrop"></div>
      <article class="tutorial-content" data-tutorial="{tutorial['id']}" data-chapter="{chapter['id']}">
        {course_header(tutorial, f'Chapter {index+1} of {len(tutorial["chapters"])}', f'Chapter {index+1} / {len(tutorial["chapters"])}', chapter['title_en'], chapter['title_bn'], chapter['summary_en'], chapter['summary_bn'])}
        <div class="chapter-meta"><span>◷ {chapter['minutes']} min</span><span>Beginner</span><button class="button small primary" id="chapter-complete" type="button">Mark complete</button></div>
        <nav class="chapter-jump" aria-label="On this chapter"><a href="#objectives">Objectives</a><a href="#concept-1">Learn</a><a href="#worked-example">Example</a><a href="#try-it">Try it</a><a href="#exercises">Exercises</a><a href="#summary">Summary</a></nav>
        <section class="tutorial-section tutorial-objectives" id="objectives"><div class="section-kicker">Start here</div>{bi('h2','What you will learn','আপনি যা শিখবেন')}<ul>{objectives}</ul></section>
        {''.join(sections)}
        <section class="tutorial-section key-terms" id="key-terms"><div class="section-kicker">Vocabulary</div>{bi('h2','Key terms','গুরুত্বপূর্ণ শব্দ')}<div class="term-grid">{render_terms(chapter['terms'])}</div></section>
        {render_worked(chapter['worked_example'])}
        <section class="tutorial-section try-it-section" id="try-it"><div class="section-kicker">Try it yourself</div>{bi('h2','Practice the idea','ধারণাটি প্র্যাকটিস করুন')}<div id="tutorial-activity"></div></section>
        <section class="tutorial-section exercise-section" id="exercises"><div class="section-kicker">Check yourself</div>{bi('h2','Chapter exercises','Chapter exercise')}<div id="chapter-exercises"></div><a class="text-link" href="/exercises/{tutorial['id']}/">Open the complete exercise library →</a></section>
        <section class="tutorial-section recap-section" id="summary"><div class="section-kicker">Summary</div>{bi('h2','What to remember','যা মনে রাখবেন')}<ul>{recap}</ul></section>
        <details class="tutorial-references"><summary>Authoritative references</summary><ul>{refs}</ul></details>
        <div class="tutorial-complete-panel"><div>{bi('h2','Ready for the next chapter?','পরবর্তী chapter-এর জন্য প্রস্তুত?')}{bi('p','Mark this chapter complete after you can explain the idea and finish the exercises.','ধারণাটি explain ও exercise finish করতে পারলে chapter complete mark করুন।')}</div><button class="button primary" id="chapter-complete-bottom" type="button">Mark complete</button></div>
        <nav class="tutorial-pager">{prev_link}{next_link}</nav>
      </article>
    </div>'''
    return shell(title=f"{chapter['title_en']} | {tutorial['title_en']}", description=chapter['summary_en'], page='tutorial-chapter', base=f"tutorials/{tutorial['id']}/{chapter['id']}/", body_attrs=f'data-tutorial="{tutorial["id"]}" data-chapter="{chapter["id"]}"', main_html=main, extra_scripts='<script src="/assets/js/tutorial-core.js" defer></script><script src="/assets/js/tutorial.js" defer></script>')


def render_course_landing(tutorial: dict, shell) -> str:
    cards = []
    for i, ch in enumerate(tutorial['chapters'], 1):
        cards.append(f'''<a class="tutorial-index-card" href="/tutorials/{tutorial['id']}/{ch['id']}/" data-chapter-card="{ch['id']}"><span>{i:02d}</span><div>{bi('h3',ch['title_en'],ch['title_bn'])}{bi('p',ch['summary_en'],ch['summary_bn'])}<small>{ch['minutes']} min</small></div><b>→</b></a>''')
    main = f'''<section class="tutorial-course-hero"><div class="container">
      {bi('span','Complete tutorial','Complete tutorial','eyebrow')}{bi('h1',tutorial['title_en'],tutorial['title_bn'])}{bi('p',tutorial['description_en'],tutorial['description_bn'],'tutorial-lead')}
      <div class="hero-actions"><a class="button primary" href="/tutorials/{tutorial['id']}/{tutorial['chapters'][0]['id']}/">Start tutorial →</a><a class="button ghost" href="/quiz/{tutorial['id']}/">Take final quiz</a></div>
      <div class="tutorial-stat-row"><span><strong>{len(tutorial['chapters'])}</strong> chapters</span><span><strong>{tutorial['estimated_hours']}</strong> estimated hours</span><span><strong>EN/BN</strong> bilingual</span><span><strong>100%</strong> static & private</span></div>
    </div></section>
    <section class="section"><div class="container tutorial-course-grid"><div><div class="section-heading"><div>{bi('span','Course contents','Course contents','eyebrow')}{bi('h2','Learn in a clear sequence','Clear sequence-এ শিখুন')}</div><div class="course-progress-box"><span>Progress</span><strong id="course-landing-progress">0/{len(tutorial['chapters'])}</strong></div></div><div class="tutorial-index-list">{''.join(cards)}</div></div><aside class="course-side-card"><h2>Course tools</h2><a href="/exercises/{tutorial['id']}/">Chapter exercises <span>→</span></a><a href="/examples/{tutorial['id']}/">Worked examples <span>→</span></a><a href="/references/{tutorial['id']}/">Reference library <span>→</span></a><a href="/quiz/{tutorial['id']}/">Final quiz <span>→</span></a><hr><p>This tutorial is the required foundation for Excel, SQL, Power BI, Python, and Data Analytics projects.</p></aside></div></section>'''
    return shell(title=f"{tutorial['title_en']} | Data Learning Hub", description=tutorial['description_en'], page='tutorial-course', base=f"tutorials/{tutorial['id']}/", main_html=main, extra_scripts='<script src="/assets/js/tutorial-core.js" defer></script><script src="/assets/js/tutorial-index.js" defer></script>')


def render_tutorials_index(tutorials: list[dict], domains: list[dict], shell) -> str:
    published = ''.join(f'''<article class="subject-course-card published"><div><span class="badge">Published · {t['version']}</span>{bi('h2',t['title_en'],t['title_bn'])}{bi('p',t['description_en'],t['description_bn'])}</div><div class="subject-meta"><span>{len(t['chapters'])} chapters</span><span>{t['estimated_hours']} hours</span></div><a class="button primary" href="/tutorials/{t['id']}/">Start tutorial →</a></article>''' for t in tutorials)
    upcoming = []
    for d in domains:
        if d['id'] in {'excel','sql','power-bi','python','statistics'}:
            status = 'Lesson library available' if d['id']=='statistics' else f"Planned · {d['release']}"
            href = '/learn/?domain=statistics' if d['id']=='statistics' else d['url']
            upcoming.append(f'''<a class="subject-course-card upcoming" href="{href}"><div><span class="badge muted">{status}</span>{bi('h3',d['title_en'],d['title_bn'])}{bi('p',d['description_en'],d['description_bn'])}</div><span class="text-link">View details →</span></a>''')
    main=f'''<section class="page-hero tutorial-hub-hero"><div class="container">{bi('span','Tutorials','Tutorial','eyebrow')}{bi('h1','Learn Data Analytics one complete chapter at a time','একটি complete chapter করে Data Analytics শিখুন')}{bi('p','Read the explanation, study a worked example, try the concept, complete exercises, and continue to the next chapter. No study-plan setup is required.','Explanation পড়ুন, worked example দেখুন, concept try করুন, exercise complete করে next chapter-এ যান। Study-plan setup প্রয়োজন নেই।')}</div></section><section class="section"><div class="container"><div class="section-heading"><div>{bi('h2','Published tutorials','Published tutorial')}{bi('p','Complete learning content available now.','এখন available complete learning content।','section-intro')}</div></div><div class="published-subjects">{published}</div><div class="section-heading top-gap"><div>{bi('h2','Growing tutorial library','Growing tutorial library')}{bi('p','Statistics remains available as a comprehensive lesson library while tool tutorials are built in sequence.','Statistics comprehensive lesson library হিসেবে available; tool tutorial sequence-এ তৈরি হবে।','section-intro')}</div></div><div class="upcoming-subjects">{''.join(upcoming)}</div></div></section>'''
    return shell(title='Tutorials | Data Learning Hub',description='Complete chapter-based Data Analytics tutorials with examples, exercises and references.',page='tutorials',base='tutorials/',main_html=main)


def render_exercises(tutorial: dict, shell) -> str:
    main=f'''<div class="tutorial-layout">{sidebar(tutorial)}<div class="tutorial-drawer-backdrop" id="tutorial-drawer-backdrop"></div><article class="tutorial-content exercise-library">{course_header(tutorial,'Exercise library','Exercise library','Data Foundations Exercises','ডেটা ফাউন্ডেশন Exercise','Practice every chapter with multiple choice, fill-in-the-blank, and explanation questions.','Multiple choice, fill-in-the-blank ও explanation question দিয়ে প্রতিটি chapter practice করুন।')}<div class="exercise-toolbar"><select id="exercise-chapter-filter"><option value="all">All chapters</option></select><button class="button ghost" id="reset-exercises" type="button">Reset answers</button></div><div id="exercise-library-root"></div></article></div>'''
    return shell(title='Data Foundations Exercises | Data Learning Hub',description='Data Foundations chapter exercises with answers and explanations.',page='tutorial-exercises',base=f'exercises/{tutorial["id"]}/',body_attrs=f'data-tutorial="{tutorial["id"]}"',main_html=main,extra_scripts='<script src="/assets/js/tutorial-core.js" defer></script><script src="/assets/js/tutorial-exercises.js" defer></script>')


def render_quiz(tutorial: dict, shell) -> str:
    main=f'''<div class="tutorial-layout">{sidebar(tutorial)}<div class="tutorial-drawer-backdrop" id="tutorial-drawer-backdrop"></div><article class="tutorial-content quiz-page">{course_header(tutorial,'Final assessment','Final assessment',tutorial['final_quiz']['title_en'],tutorial['final_quiz']['title_bn'],'Test the essential ideas from all 21 chapters. Your score is stored only in this browser.','২১ chapter-এর essential idea test করুন। Score শুধু এই browser-এ store হয়।')}<div class="quiz-intro"><strong>Pass target: {tutorial['final_quiz']['pass_percent']}%</strong><p>Answer the automatically scored multiple-choice and fill-in questions. Short-response prompts remain available in the exercise library.</p><button class="button primary" id="start-final-quiz" type="button">Start quiz</button></div><div id="final-quiz-root"></div></article></div>'''
    return shell(title='Data Foundations Final Quiz | Data Learning Hub',description='Final assessment for the complete Data Foundations tutorial.',page='tutorial-quiz',base=f'quiz/{tutorial["id"]}/',body_attrs=f'data-tutorial="{tutorial["id"]}"',main_html=main,extra_scripts='<script src="/assets/js/tutorial-core.js" defer></script><script src="/assets/js/tutorial-quiz.js" defer></script>')


def render_examples(tutorial: dict, shell) -> str:
    cards=[]
    for i,ch in enumerate(tutorial['chapters'],1):
        w=ch['worked_example']
        cards.append(f'''<article class="example-library-card"><div class="example-library-head"><span>{i:02d}</span>{bi('h2',w['title_en'],w['title_bn'])}</div>{bi('p',w['context_en'],w['context_bn'])}<ol>{''.join(f'<li>{bi("span",en,w["steps_bn"][j])}</li>' for j,en in enumerate(w['steps_en']))}</ol><div class="example-conclusion">{bi('p',w['conclusion_en'],w['conclusion_bn'])}</div><a class="text-link" href="/tutorials/{tutorial['id']}/{ch['id']}/#worked-example">Open chapter →</a></article>''')
    main=f'''<div class="tutorial-layout">{sidebar(tutorial)}<div class="tutorial-drawer-backdrop" id="tutorial-drawer-backdrop"></div><article class="tutorial-content">{course_header(tutorial,'Example library','Example library','Data Foundations Worked Examples','ডেটা ফাউন্ডেশন Worked Example','Review every scenario and step-by-step reasoning in one searchable collection.','সব scenario ও step-by-step reasoning একটি searchable collection-এ review করুন।')}<label class="example-search"><input id="example-search" type="search" placeholder="Search examples…"></label><div class="example-library" id="example-library">{''.join(cards)}</div></article></div>'''
    return shell(title='Data Foundations Examples | Data Learning Hub',description='Worked examples for every chapter of the Data Foundations tutorial.',page='tutorial-examples',base=f'examples/{tutorial["id"]}/',body_attrs=f'data-tutorial="{tutorial["id"]}"',main_html=main,extra_scripts='<script src="/assets/js/tutorial-core.js" defer></script><script src="/assets/js/tutorial-index.js" defer></script>')


def render_references(tutorial: dict, shell) -> str:
    groups=[]
    for group in tutorial['reference_groups']:
        links=''.join(f'<li><a href="{attr(r["url"])}" target="_blank" rel="noopener noreferrer"><strong>{escape(r["title"])}</strong><span>{escape(r["url"])}</span></a></li>' for r in group['references'])
        groups.append(f'''<section class="reference-group">{bi('h2',group['title_en'],group['title_bn'])}<ul>{links}</ul></section>''')
    terms=[]
    seen=set()
    for ch in tutorial['chapters']:
        for item in ch['terms']:
            if item['term_en'] not in seen:
                seen.add(item['term_en']); terms.append(item)
    glossary=''.join(f'''<article class="reference-term">{bi('h3',t['term_en'],t['term_bn'])}{bi('p',t['definition_en'],t['definition_bn'])}</article>''' for t in sorted(terms,key=lambda x:x['term_en']))
    main=f'''<div class="tutorial-layout">{sidebar(tutorial)}<div class="tutorial-drawer-backdrop" id="tutorial-drawer-backdrop"></div><article class="tutorial-content">{course_header(tutorial,'References','Reference','Data Foundations Reference','ডেটা ফাউন্ডেশন Reference','Definitions, authoritative sources, and quick links used throughout the course.','Course জুড়ে ব্যবহৃত definition, authoritative source ও quick link।')}<section class="reference-source-grid">{''.join(groups)}</section><section class="tutorial-section"><div class="section-kicker">Quick reference</div>{bi('h2','Course glossary','Course glossary')}<div class="reference-term-grid">{glossary}</div></section></article></div>'''
    return shell(title='Data Foundations Reference | Data Learning Hub',description='Authoritative references and glossary for Data Foundations.',page='tutorial-references',base=f'references/{tutorial["id"]}/',body_attrs=f'data-tutorial="{tutorial["id"]}"',main_html=main,extra_scripts='<script src="/assets/js/tutorial-core.js" defer></script>')


def render_home(tutorial: dict, shell) -> str:
    first=tutorial['chapters'][0]
    main=f'''<section class="hero tutorial-first-home"><div class="container hero-grid"><div class="hero-copy"><span class="eyebrow">Data Analytics Tutorial Platform</span><h1>Learn the subject here—not just the study plan.</h1><p>Start with complete Data Foundations chapters. Read clear explanations, study practical examples, try the concept, complete exercises, and move forward one chapter at a time.</p><div class="hero-actions"><a class="button primary" href="/tutorials/{tutorial['id']}/{first['id']}/">Start Data Foundations →</a><a class="button ghost" href="/tutorials/">Browse tutorials</a></div><div class="hero-stats"><span class="stat-chip"><strong>{len(tutorial['chapters'])}</strong> complete chapters</span><span class="stat-chip"><strong>{sum(len(c['exercises']) for c in tutorial['chapters'])}</strong> chapter exercises</span><span class="stat-chip"><strong>EN/BN</strong> bilingual</span></div></div><div class="home-tutorial-preview"><span class="guide-kicker">Your first course</span><h2>{escape(tutorial['title_en'])}</h2><ol>{''.join(f'<li><span>{i:02d}</span><a href="/tutorials/{tutorial["id"]}/{ch["id"]}/">{escape(ch["title_en"])}</a></li>' for i,ch in enumerate(tutorial['chapters'][:5],1))}</ol><a class="text-link" href="/tutorials/{tutorial['id']}/">View all {len(tutorial['chapters'])} chapters →</a></div></div></section><section class="section tutorial-value-section"><div class="container"><div class="section-heading"><div><span class="eyebrow">How learning works</span><h2>A complete tutorial loop inside every chapter</h2></div></div><div class="method-grid"><article class="method-card"><span>01</span><h3>Learn</h3><p>Definitions and easy explanations build the concept from zero.</p></article><article class="method-card"><span>02</span><h3>Explore</h3><p>Worked scenarios connect the concept to real analytical work.</p></article><article class="method-card"><span>03</span><h3>Try it</h3><p>Interactive activities let you classify, calculate, inspect, and decide.</p></article><article class="method-card"><span>04</span><h3>Check</h3><p>Exercises, answers, and a final quiz verify understanding.</p></article></div></div></section><section class="section"><div class="container cta-card"><div><span class="eyebrow">Tutorial-first release</span><h2>Roadmaps still exist, but tutorials are now the primary product.</h2><p>My Learning, career paths, statistics labs, datasets, and projects remain available as optional supporting tools.</p></div><a class="button primary" href="/tutorials/">Open tutorials →</a></div></section>'''
    return shell(title='Data Learning Hub — Complete Data Analytics Tutorials',description='A tutorial-first bilingual Data Analytics learning platform with complete chapters, examples, exercises and projects.',page='home',main_html=main)


def write_tutorial_pages(root: Path, data: dict, shell) -> list[str]:
    tutorials=data['tutorials']
    for path in ['tutorials','exercises','quiz','examples','references']:
        (root/path).mkdir(parents=True,exist_ok=True)
    (root/'tutorials'/'index.html').write_text(render_tutorials_index(tutorials,data['domains'],shell),encoding='utf-8')
    urls=['/tutorials/']
    for tutorial in tutorials:
        tid=tutorial['id']
        for base in ['tutorials','exercises','quiz','examples','references']:
            (root/base/tid).mkdir(parents=True,exist_ok=True)
        (root/'tutorials'/tid/'index.html').write_text(render_course_landing(tutorial,shell),encoding='utf-8')
        (root/'exercises'/tid/'index.html').write_text(render_exercises(tutorial,shell),encoding='utf-8')
        (root/'quiz'/tid/'index.html').write_text(render_quiz(tutorial,shell),encoding='utf-8')
        (root/'examples'/tid/'index.html').write_text(render_examples(tutorial,shell),encoding='utf-8')
        (root/'references'/tid/'index.html').write_text(render_references(tutorial,shell),encoding='utf-8')
        urls += [f'/tutorials/{tid}/',f'/exercises/{tid}/',f'/quiz/{tid}/',f'/examples/{tid}/',f'/references/{tid}/']
        for i,ch in enumerate(tutorial['chapters']):
            out=root/'tutorials'/tid/ch['id']; out.mkdir(parents=True,exist_ok=True)
            (out/'index.html').write_text(render_chapter(tutorial,ch,i,shell),encoding='utf-8')
            urls.append(f'/tutorials/{tid}/{ch["id"]}/')
    (root/'index.html').write_text(render_home(tutorials[0],shell),encoding='utf-8')
    return urls
