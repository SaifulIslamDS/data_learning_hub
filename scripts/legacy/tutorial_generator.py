from __future__ import annotations
from html import escape
from pathlib import Path


def attr(value: str) -> str:
    return escape(str(value), quote=True)


def bi(tag: str, en: str, bn: str, class_name: str = '', extra: str = '') -> str:
    cls = f' class="{class_name}"' if class_name else ''
    return f'<{tag}{cls} data-en="{attr(en)}" data-bn="{attr(bn)}" {extra}>{escape(en)}</{tag}>'


def module_map(tutorial: dict) -> dict:
    return {item['id']: item for item in tutorial.get('modules', [])}


def grouped_chapters(tutorial: dict) -> list[tuple[dict | None, list[tuple[int, dict]]]]:
    modules = module_map(tutorial)
    if not modules:
        return [(None, list(enumerate(tutorial['chapters'], 1)))]
    groups: list[tuple[dict | None, list[tuple[int, dict]]]] = []
    for module in tutorial.get('modules', []):
        rows = [(i, ch) for i, ch in enumerate(tutorial['chapters'], 1) if ch.get('module') == module['id']]
        if rows:
            groups.append((module, rows))
    ungrouped = [(i, ch) for i, ch in enumerate(tutorial['chapters'], 1) if not ch.get('module') or ch.get('module') not in modules]
    if ungrouped:
        groups.append((None, ungrouped))
    return groups


def sidebar(tutorial: dict, current: str = '') -> str:
    groups = []
    for module, chapters in grouped_chapters(tutorial):
        heading = ''
        if module:
            heading = f'<div class="tutorial-module-label"><span>{escape(module["id"])}</span><strong data-en="{attr(module["title_en"])}" data-bn="{attr(module["title_bn"])}">{escape(module["title_en"])}</strong></div>'
        links = []
        for i, chapter in chapters:
            links.append(
                f'<a class="tutorial-chapter-link {"current" if chapter["id"] == current else ""}" '
                f'href="/tutorials/{tutorial["id"]}/{chapter["id"]}/" data-chapter-link="{chapter["id"]}">'
                f'<span>{i:02d}</span><span data-en="{attr(chapter["title_en"])}" data-bn="{attr(chapter["title_bn"])}">{escape(chapter["title_en"])}</span>'
                f'<b class="chapter-state" aria-hidden="true">○</b></a>'
            )
        groups.append(f'{heading}<div class="tutorial-module-links">{"".join(links)}</div>')
    return f'''<aside class="tutorial-sidebar" id="tutorial-sidebar">
      <div class="tutorial-sidebar-head">
        <a href="/tutorials/{tutorial['id']}/" class="tutorial-course-title" data-en="{attr(tutorial['short_title_en'])}" data-bn="{attr(tutorial['short_title_bn'])}">{escape(tutorial['short_title_en'])}</a>
        <button class="icon-button tutorial-drawer-close" id="tutorial-drawer-close" type="button" aria-label="Close chapter menu">×</button>
      </div>
      <label class="tutorial-sidebar-search"><span class="sr-only">Search chapters</span><input id="tutorial-chapter-search" type="search" placeholder="Search chapters…" data-placeholder-en="Search chapters…" data-placeholder-bn="Chapter খুঁজুন…"></label>
      <div class="tutorial-progress-mini"><div><span data-en="Course progress" data-bn="Course progress">Course progress</span><strong id="tutorial-progress-label">0/{len(tutorial['chapters'])}</strong></div><div class="progress-track"><span id="tutorial-progress-bar" style="width:0"></span></div></div>
      <nav class="tutorial-chapter-nav" aria-label="Course chapters">{''.join(groups)}</nav>
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


def render_teaching_section(item: dict, n: int) -> str:
    example = ''
    if item.get('example_en'):
        example = f'<div class="inline-example"><strong data-en="Example" data-bn="উদাহরণ">Example</strong>{bi("p", item["example_en"], item.get("example_bn", item["example_en"]))}</div>'
    code = ''
    if item.get('code'):
        label = escape(item.get('code_label', 'Excel'))
        code = f'<div class="formula-block"><span>{label}</span><code>{escape(item["code"])}</code><button type="button" class="copy-code" data-copy-code aria-label="Copy code">Copy</button></div>'
    return f'''<section class="tutorial-section" id="concept-{n}"><div class="section-kicker">{n:02d}</div>{bi('h2', item['title_en'], item['title_bn'])}{bi('p', item['body_en'], item['body_bn'])}{code}{example}</section>'''


def render_downloads(tutorial: dict) -> str:
    downloads = tutorial.get('downloads', [])
    if not downloads:
        return ''
    cards = ''.join(f'<a class="download-card" href="{attr(item["url"])}" download><span>⇩</span><div><strong data-en="{attr(item["title_en"])}" data-bn="{attr(item["title_bn"])}">{escape(item["title_en"])}</strong><small>Download</small></div></a>' for item in downloads)
    return f'<section class="course-downloads"><h2>Practice files</h2><div>{cards}</div></section>'


def render_chapter(tutorial: dict, chapter: dict, index: int, shell) -> str:
    prev_ch = tutorial['chapters'][index - 1] if index > 0 else None
    next_ch = tutorial['chapters'][index + 1] if index + 1 < len(tutorial['chapters']) else None
    sections = [render_teaching_section(item, n) for n, item in enumerate(chapter['sections'], 1)]
    recap = ''.join(f'<li>{bi("span", item["en"], item["bn"])}</li>' for item in chapter['recap'])
    refs = ''.join(f'<li><a href="{attr(r["url"])}" target="_blank" rel="noopener noreferrer">{escape(r["title"])} ↗</a></li>' for r in chapter['references'])
    prev_link = f'<a class="tutorial-prev" href="/tutorials/{tutorial["id"]}/{prev_ch["id"]}/"><small>← Previous</small><strong data-en="{attr(prev_ch["title_en"])}" data-bn="{attr(prev_ch["title_bn"])}">{escape(prev_ch["title_en"])}</strong></a>' if prev_ch else '<span></span>'
    next_link = f'<a class="tutorial-next" href="/tutorials/{tutorial["id"]}/{next_ch["id"]}/"><small>Next →</small><strong data-en="{attr(next_ch["title_en"])}" data-bn="{attr(next_ch["title_bn"])}">{escape(next_ch["title_en"])}</strong></a>' if next_ch else f'<a class="tutorial-next" href="/quiz/{tutorial["id"]}/"><small>Finish →</small><strong>Final Quiz</strong></a>'
    modules = module_map(tutorial)
    module = modules.get(chapter.get('module'))
    module_text = module['title_en'] if module else tutorial['short_title_en']
    level = chapter.get('level', 'Beginner')
    main = f'''<div class="tutorial-layout">
      {sidebar(tutorial, chapter['id'])}
      <div class="tutorial-drawer-backdrop" id="tutorial-drawer-backdrop"></div>
      <article class="tutorial-content" data-tutorial="{tutorial['id']}" data-chapter="{chapter['id']}">
        {course_header(tutorial, f'{module_text} · Chapter {index+1} of {len(tutorial["chapters"])}', f'{module_text} · Chapter {index+1} / {len(tutorial["chapters"])}', chapter['title_en'], chapter['title_bn'], chapter['summary_en'], chapter['summary_bn'])}
        <div class="chapter-meta"><span>◷ {chapter['minutes']} min</span><span>{escape(level)}</span><button class="button small primary" id="chapter-complete" type="button">Mark complete</button></div>
        <nav class="chapter-jump" aria-label="On this chapter"><a href="#concept-1">Learn</a><a href="#worked-example">Example</a><a href="#try-it">Practice</a><a href="#exercises">Exercises</a><a href="#summary">Summary</a></nav>
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
    extra = '<script src="/assets/js/tutorial-core.js" defer></script>' + ('<script src="/assets/js/sql-practice.js" defer></script>' if tutorial['id']=='sql-data-analytics' else '') + ('<script src="/assets/js/python-practice.js" defer></script>' if tutorial['id']=='python-data-analytics' else '') + '<script src="/assets/js/tutorial.js" defer></script>'
    return shell(title=f"{chapter['title_en']} | {tutorial['title_en']}", description=chapter['summary_en'], page='tutorial-chapter', base=f"tutorials/{tutorial['id']}/{chapter['id']}/", body_attrs=f'data-tutorial="{tutorial["id"]}" data-chapter="{chapter["id"]}"', main_html=main, extra_scripts=extra)


def render_course_landing(tutorial: dict, shell) -> str:
    groups = []
    for module, chapters in grouped_chapters(tutorial):
        title = ''
        if module:
            title = f'<div class="tutorial-module-heading"><span>{escape(module["id"])}</span>{bi("h2", module["title_en"], module["title_bn"])}</div>'
        cards = []
        for i, ch in chapters:
            cards.append(f'''<a class="tutorial-index-card" href="/tutorials/{tutorial['id']}/{ch['id']}/" data-chapter-card="{ch['id']}"><span>{i:02d}</span><div>{bi('h3',ch['title_en'],ch['title_bn'])}{bi('p',ch['summary_en'],ch['summary_bn'])}<small>{ch['minutes']} min · {escape(ch.get('level','Beginner'))}</small></div><b>→</b></a>''')
        groups.append(f'<section class="tutorial-index-module">{title}<div class="tutorial-index-list">{"".join(cards)}</div></section>')
    main = f'''<section class="tutorial-course-hero"><div class="container">
      {bi('span','Complete tutorial','Complete tutorial','eyebrow')}{bi('h1',tutorial['title_en'],tutorial['title_bn'])}{bi('p',tutorial['description_en'],tutorial['description_bn'],'tutorial-lead')}
      <div class="hero-actions"><a class="button primary" href="/tutorials/{tutorial['id']}/{tutorial['chapters'][0]['id']}/">Start tutorial →</a><a class="button ghost" href="/quiz/{tutorial['id']}/">Take final quiz</a></div>
      <div class="tutorial-stat-row"><span><strong>{len(tutorial['chapters'])}</strong> chapters</span><span><strong>{tutorial['estimated_hours']}</strong> estimated hours</span><span><strong>English</strong> tutorial</span><span><strong>100%</strong> static & private</span></div>
    </div></section>
    <section class="section"><div class="container tutorial-course-grid"><div><div class="section-heading"><div>{bi('span','Course contents','Course contents','eyebrow')}{bi('h2','Learn in a clear sequence','Clear sequence-এ শিখুন')}</div><div class="course-progress-box"><span>Progress</span><strong id="course-landing-progress">0/{len(tutorial['chapters'])}</strong></div></div>{''.join(groups)}</div><aside class="course-side-card"><h2>Course tools</h2><a href="/exercises/{tutorial['id']}/">Chapter exercises <span>→</span></a>{'<a href="/playground/sql/">SQL Playground <span>→</span></a>' if tutorial['id']=='sql-data-analytics' else ""}{'<a href="/playground/python/">Python Playground <span>→</span></a>' if tutorial['id']=='python-data-analytics' else ""}<a href="/examples/{tutorial['id']}/">Worked examples <span>→</span></a><a href="/references/{tutorial['id']}/">Reference library <span>→</span></a><a href="/quiz/{tutorial['id']}/">Final quiz <span>→</span></a><hr><p>This tutorial contains complete learning content, practice, assessment, and project work.</p>{render_downloads(tutorial)}</aside></div></section>'''
    return shell(title=f"{tutorial['title_en']} | Data Learning Hub", description=tutorial['description_en'], page='tutorial-course', base=f"tutorials/{tutorial['id']}/", body_attrs=f'data-tutorial="{tutorial["id"]}"', main_html=main, extra_scripts='<script src="/assets/js/tutorial-core.js" defer></script><script src="/assets/js/tutorial-index.js" defer></script>')


def render_tutorials_index(tutorials: list[dict], domains: list[dict], shell) -> str:
    published = ''.join(f'''<article class="subject-course-card published"><div><span class="badge">Published · {t['version']}</span>{bi('h2',t['title_en'],t['title_bn'])}{bi('p',t['description_en'],t['description_bn'])}</div><div class="subject-meta"><span>{len(t['chapters'])} chapters</span><span>{t['estimated_hours']} hours</span></div><a class="button primary" href="/tutorials/{t['id']}/">Start tutorial →</a></article>''' for t in tutorials)
    published_ids = {t['id'] for t in tutorials}
    upcoming = []
    for d in domains:
        tutorial_id = {'excel':'excel-data-analytics','sql':'sql-data-analytics','power-bi':'power-bi-data-analytics','python':'python-data-analytics'}.get(d['id'], d['id'])
        if tutorial_id in published_ids or d['id'] == 'data-foundations':
            continue
        if d['id'] in {'sql','power-bi','python','statistics'}:
            status = 'Lesson library available' if d['id']=='statistics' else f"Planned · {d['release']}"
            href = '/learn/?domain=statistics' if d['id']=='statistics' else d['url']
            upcoming.append(f'''<a class="subject-course-card upcoming" href="{href}"><div><span class="badge muted">{status}</span>{bi('h3',d['title_en'],d['title_bn'])}{bi('p',d['description_en'],d['description_bn'])}</div><span class="text-link">View details →</span></a>''')
    main=f'''<section class="page-hero tutorial-hub-hero"><div class="container">{bi('span','Tutorials','Tutorial','eyebrow')}{bi('h1','Learn Data Analytics one complete chapter at a time','একটি complete chapter করে Data Analytics শিখুন')}{bi('p','Read the explanation, study a worked example, try the concept, complete exercises, and continue to the next chapter. No study-plan setup is required.','Explanation পড়ুন, worked example দেখুন, concept try করুন, exercise complete করে next chapter-এ যান। Study-plan setup প্রয়োজন নেই।')}</div></section><section class="section"><div class="container"><div class="section-heading"><div>{bi('h2','Published tutorials','Published tutorial')}{bi('p','Complete learning content available now.','এখন available complete learning content।','section-intro')}</div></div><div class="published-subjects">{published}</div>{f'<div class="section-heading top-gap"><div>{bi("h2","Growing tutorial library","Growing tutorial library")}{bi("p","Additional complete tool tutorials will be published in sequence.","Additional complete tool tutorial sequence-এ publish হবে।","section-intro")}</div></div><div class="upcoming-subjects">{"".join(upcoming)}</div>' if upcoming else ''}</div></section>'''
    return shell(title='Tutorials | Data Learning Hub',description='Complete chapter-based Data Analytics tutorials with examples, exercises and references.',page='tutorials',base='tutorials/',main_html=main)


def render_exercises(tutorial: dict, shell) -> str:
    count = sum(len(ch['exercises']) for ch in tutorial['chapters'])
    main=f'''<div class="tutorial-layout">{sidebar(tutorial)}<div class="tutorial-drawer-backdrop" id="tutorial-drawer-backdrop"></div><article class="tutorial-content exercise-library">{course_header(tutorial,'Exercise library','Exercise library',f'{tutorial["short_title_en"]} Exercises',f'{tutorial["short_title_bn"]} Exercise',f'Practice all {len(tutorial["chapters"])} chapters with {count} multiple-choice, fill-in, and application questions.',f'{len(tutorial["chapters"])} chapter-এর {count}টি multiple-choice, fill-in ও application question practice করুন।')}<div class="exercise-toolbar"><select id="exercise-chapter-filter"><option value="all">All chapters</option></select><button class="button ghost" id="reset-exercises" type="button">Reset answers</button></div><div id="exercise-library-root"></div></article></div>'''
    return shell(title=f'{tutorial["short_title_en"]} Exercises | Data Learning Hub',description=f'{tutorial["short_title_en"]} chapter exercises with answers and explanations.',page='tutorial-exercises',base=f'exercises/{tutorial["id"]}/',body_attrs=f'data-tutorial="{tutorial["id"]}"',main_html=main,extra_scripts='<script src="/assets/js/tutorial-core.js" defer></script><script src="/assets/js/tutorial-exercises.js" defer></script>')


def render_quiz(tutorial: dict, shell) -> str:
    main=f'''<div class="tutorial-layout">{sidebar(tutorial)}<div class="tutorial-drawer-backdrop" id="tutorial-drawer-backdrop"></div><article class="tutorial-content quiz-page">{course_header(tutorial,'Final assessment','Final assessment',tutorial['final_quiz']['title_en'],tutorial['final_quiz']['title_bn'],f'Test essential ideas from all {len(tutorial["chapters"])} chapters. Your score is stored only in this browser.',f'{len(tutorial["chapters"])} chapter-এর essential idea test করুন। Score শুধু browser-এ store হয়।')}<div class="quiz-intro"><strong>Pass target: {tutorial['final_quiz']['pass_percent']}%</strong><p>Answer the automatically scored multiple-choice and fill-in questions. Short-response prompts remain available in the exercise library.</p><button class="button primary" id="start-final-quiz" type="button">Start quiz</button></div><div id="final-quiz-root"></div></article></div>'''
    return shell(title=f'{tutorial["short_title_en"]} Final Quiz | Data Learning Hub',description=f'Final assessment for the complete {tutorial["short_title_en"]} tutorial.',page='tutorial-quiz',base=f'quiz/{tutorial["id"]}/',body_attrs=f'data-tutorial="{tutorial["id"]}"',main_html=main,extra_scripts='<script src="/assets/js/tutorial-core.js" defer></script><script src="/assets/js/tutorial-quiz.js" defer></script>')


def render_examples(tutorial: dict, shell) -> str:
    cards=[]
    for i,ch in enumerate(tutorial['chapters'],1):
        w=ch['worked_example']
        cards.append(f'''<article class="example-library-card" data-example-module="{attr(ch.get('module',''))}"><div class="example-library-head"><span>{i:02d}</span>{bi('h2',w['title_en'],w['title_bn'])}</div>{bi('p',w['context_en'],w['context_bn'])}<ol>{''.join(f'<li>{bi("span",en,w["steps_bn"][j])}</li>' for j,en in enumerate(w['steps_en']))}</ol><div class="example-conclusion">{bi('p',w['conclusion_en'],w['conclusion_bn'])}</div><a class="text-link" href="/tutorials/{tutorial['id']}/{ch['id']}/#worked-example">Open chapter →</a></article>''')
    main=f'''<div class="tutorial-layout">{sidebar(tutorial)}<div class="tutorial-drawer-backdrop" id="tutorial-drawer-backdrop"></div><article class="tutorial-content">{course_header(tutorial,'Example library','Example library',f'{tutorial["short_title_en"]} Worked Examples',f'{tutorial["short_title_bn"]} Worked Example','Review every scenario and step-by-step workflow in one searchable collection.','সব scenario ও step-by-step workflow একটি searchable collection-এ review করুন।')}<label class="example-search"><input id="example-search" type="search" placeholder="Search examples…"></label><div class="example-library" id="example-library">{''.join(cards)}</div></article></div>'''
    return shell(title=f'{tutorial["short_title_en"]} Examples | Data Learning Hub',description=f'Worked examples for every chapter of the {tutorial["short_title_en"]} tutorial.',page='tutorial-examples',base=f'examples/{tutorial["id"]}/',body_attrs=f'data-tutorial="{tutorial["id"]}"',main_html=main,extra_scripts='<script src="/assets/js/tutorial-core.js" defer></script><script src="/assets/js/tutorial-index.js" defer></script>')


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
    main=f'''<div class="tutorial-layout">{sidebar(tutorial)}<div class="tutorial-drawer-backdrop" id="tutorial-drawer-backdrop"></div><article class="tutorial-content">{course_header(tutorial,'References','Reference',f'{tutorial["short_title_en"]} Reference',f'{tutorial["short_title_bn"]} Reference','Definitions, official sources, downloads, and quick links used throughout the course.','Course জুড়ে ব্যবহৃত definition, official source, download ও quick link।')}<section class="reference-source-grid">{''.join(groups)}</section>{render_downloads(tutorial)}<section class="tutorial-section"><div class="section-kicker">Quick reference</div>{bi('h2','Course glossary','Course glossary')}<div class="reference-term-grid">{glossary}</div></section></article></div>'''
    return shell(title=f'{tutorial["short_title_en"]} Reference | Data Learning Hub',description=f'Official references and glossary for {tutorial["short_title_en"]}.',page='tutorial-references',base=f'references/{tutorial["id"]}/',body_attrs=f'data-tutorial="{tutorial["id"]}"',main_html=main,extra_scripts='<script src="/assets/js/tutorial-core.js" defer></script>')


def resource_index(tutorials: list[dict], kind: str, shell) -> str:
    labels = {'exercises':('Exercise Libraries','Practice every published tutorial by chapter.'),'examples':('Worked Example Libraries','Review complete worked scenarios and analytical workflows.'),'references':('Reference Libraries','Open official sources, course glossaries, and downloads.'),'quiz':('Final Assessments','Test your knowledge after completing a tutorial.')}
    title, summary = labels[kind]
    cards=[]
    for t in tutorials:
        count = sum(len(ch['exercises']) for ch in t['chapters']) if kind == 'exercises' else len(t['chapters'])
        cards.append(f'<article class="resource-subject-card"><span class="badge">{t["version"]}</span>{bi("h2",t["short_title_en"],t["short_title_bn"])}<p>{escape(summary)}</p><div class="subject-meta"><span>{count} {"exercises" if kind=="exercises" else "chapters"}</span></div><a class="button primary" href="/{kind}/{t["id"]}/">Open {kind} →</a></article>')
    main=f'<section class="page-hero"><div class="container"><span class="eyebrow">{escape(kind.title())}</span><h1>{escape(title)}</h1><p>{escape(summary)}</p></div></section><section class="section"><div class="container resource-subject-grid">{"".join(cards)}</div></section>'
    return shell(title=f'{title} | Data Learning Hub',description=summary,page=f'{kind}-index',base=f'{kind}/',main_html=main)


def render_home(tutorials: list[dict], shell) -> str:
    primary=tutorials[-1] if len(tutorials)>1 else tutorials[0]
    course_cards=''.join(f'''<article class="home-course-card"><span class="badge">Complete · {t['version']}</span>{bi('h2',t['short_title_en'],t['short_title_bn'])}{bi('p',t['description_en'],t['description_bn'])}<div class="subject-meta"><span>{len(t['chapters'])} chapters</span><span>{t['estimated_hours']} hours</span></div><a class="button primary" href="/tutorials/{t['id']}/">Open tutorial →</a></article>''' for t in tutorials)
    total_chapters=sum(len(t['chapters']) for t in tutorials)
    total_exercises=sum(len(ch['exercises']) for t in tutorials for ch in t['chapters'])
    main=f'''<section class="hero tutorial-first-home"><div class="container hero-grid"><div class="hero-copy"><span class="eyebrow">Data Analytics Tutorial Platform</span><h1>Learn Data Analytics here—chapter by chapter.</h1><p>Study complete Data Foundations, Excel, SQL, Power BI, Python, and Analytics Workflows tutorials with clear explanations, browser practice, exercises, assessments, references, and portfolio projects.</p><div class="hero-actions"><a class="button primary" href="/tutorials/{primary['id']}/">Start {escape(primary['short_title_en'])} →</a><a class="button ghost" href="/tutorials/">Browse tutorials</a></div><div class="hero-stats"><span class="stat-chip"><strong>{total_chapters}</strong> complete chapters</span><span class="stat-chip"><strong>{total_exercises}</strong> chapter exercises</span><span class="stat-chip"><strong>Practice</strong> built in</span></div></div><div class="home-tutorial-preview"><span class="guide-kicker">Latest complete course</span><h2>{escape(primary['title_en'])}</h2><ol>{''.join(f'<li><span>{i:02d}</span><a href="/tutorials/{primary["id"]}/{ch["id"]}/">{escape(ch["title_en"])}</a></li>' for i,ch in enumerate(primary['chapters'][:5],1))}</ol><a class="text-link" href="/tutorials/{primary['id']}/">View all {len(primary['chapters'])} chapters →</a></div></div></section><section class="section"><div class="container"><div class="section-heading"><div><span class="eyebrow">Published tutorials</span><h2>Complete learning content—not curriculum placeholders</h2></div></div><div class="home-course-grid">{course_cards}</div></div></section><section class="section tutorial-value-section"><div class="container"><div class="section-heading"><div><span class="eyebrow">How learning works</span><h2>A complete tutorial loop inside every chapter</h2></div></div><div class="method-grid"><article class="method-card"><span>01</span><h3>Learn</h3><p>Definitions and easy explanations build the concept from zero.</p></article><article class="method-card"><span>02</span><h3>Explore</h3><p>Worked scenarios connect the concept to analytical work.</p></article><article class="method-card"><span>03</span><h3>Try it</h3><p>Interactive activities let you calculate, transform, inspect, and decide.</p></article><article class="method-card"><span>04</span><h3>Check</h3><p>Exercises, answers, final quizzes, and projects verify learning.</p></article></div></div></section>'''
    return shell(title='Data Learning Hub — Complete Data Analytics Tutorials',description='A tutorial-first bilingual Data Analytics learning platform with complete Data Foundations, Excel, SQL, Power BI, Python, Analytics Workflows, and portfolio projects.',page='home',main_html=main)



def render_sql_playground(tutorial: dict, shell) -> str:
    main = f'''<section class="page-hero compact"><div class="container"><span class="eyebrow">Browser SQL Playground</span><h1>Run SQL against the course database</h1><p>Edit and run SQLite-compatible queries entirely in your browser. The practice database is recreated locally and no query or data is sent to a backend.</p></div></section><section class="section"><div class="container sql-playground-page"><div id="sql-playground-root" data-seed="/assets/downloads/sql-analytics-practice-database.sql"></div><aside class="sql-playground-help"><h2>Practice database</h2><p>Customers, products, employees, orders, order items, and web events.</p><a class="button ghost" href="/tutorials/{tutorial['id']}/">Open SQL tutorial</a><a class="text-link" href="/assets/downloads/sql-analytics-practice-database.sql" download>Download database script ↓</a><p class="small">Teaching baseline: PostgreSQL concepts. Browser engine: SQLite-compatible sql.js. Dialect differences are identified in the relevant chapters.</p></aside></div></section>'''
    return shell(title='SQL Playground | Data Learning Hub', description='Run SQL queries in the browser against the Data Learning Hub retail practice database.', page='sql-playground', base='playground/sql/', body_attrs='data-tutorial="sql-data-analytics"', main_html=main, extra_scripts='<script src="/assets/js/sql-practice.js" defer></script>')

def render_python_playground(tutorial: dict, shell) -> str:
    main = f'''<section class="page-hero compact"><div class="container"><span class="eyebrow">Browser Python Playground</span><h1>Run Python analytics code in your browser</h1><p>Edit and run Python, NumPy, pandas, Matplotlib, and SciPy examples locally with Pyodide. The supplied synthetic retail data is loaded into browser memory and no code is sent to a backend.</p></div></section><section class="section"><div class="container python-playground-page"><div id="python-playground-root"></div><aside class="python-playground-help"><h2>Practice files</h2><p>Retail sales, customer, and deliberately messy order data are available inside the browser runtime.</p><a class="button ghost" href="/tutorials/{tutorial['id']}/">Open Python tutorial</a><a class="text-link" href="/assets/downloads/python-retail-analytics-practice-package.zip" download>Download practice package ↓</a><p class="small">Teaching baseline: stable Python 3.14 with current NumPy, pandas, Matplotlib, and SciPy. Browser engine: pinned Pyodide 314.0.2.</p></aside></div></section>'''
    return shell(title='Python Playground | Data Learning Hub', description='Run Python analytics code in the browser with Pyodide and the Data Learning Hub retail practice data.', page='python-playground', base='playground/python/', body_attrs='data-tutorial="python-data-analytics"', main_html=main, extra_scripts='<script src="/assets/js/python-practice.js" defer></script>')


def write_tutorial_pages(root: Path, data: dict, shell) -> list[str]:
    tutorials=data['tutorials']
    for path in ['tutorials','exercises','quiz','examples','references','playground/sql','playground/python']:
        (root/path).mkdir(parents=True,exist_ok=True)
    (root/'tutorials'/'index.html').write_text(render_tutorials_index(tutorials,data['domains'],shell),encoding='utf-8')
    for kind in ['exercises','quiz','examples','references']:
        (root/kind/'index.html').write_text(resource_index(tutorials,kind,shell),encoding='utf-8')
    urls=['/tutorials/','/exercises/','/quiz/','/examples/','/references/']
    sql_tutorial=next((t for t in tutorials if t['id']=='sql-data-analytics'),None)
    if sql_tutorial:
        (root/'playground'/'sql'/'index.html').write_text(render_sql_playground(sql_tutorial,shell),encoding='utf-8')
        urls.append('/playground/sql/')
    python_tutorial=next((t for t in tutorials if t['id']=='python-data-analytics'),None)
    if python_tutorial:
        (root/'playground'/'python'/'index.html').write_text(render_python_playground(python_tutorial,shell),encoding='utf-8')
        urls.append('/playground/python/')
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
    (root/'index.html').write_text(render_home(tutorials,shell),encoding='utf-8')
    return urls
