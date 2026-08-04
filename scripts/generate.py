from __future__ import annotations

import json
import re
import sys
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from content.datasets.catalog import DATASETS, PROJECTS
from content.platform.config import SITE, STORAGE, TOOL_BASELINES
from content.platform.domains import DOMAINS
from content.platform.glossary import GLOSSARY
from content.platform.legacy_paths import PATHS as LEGACY_PATHS
from content.statistics.comprehensive_content import build_lesson_content
from content.statistics.curriculum import COMMON_MISTAKES, FORMULAS, MODULE_CONTEXT, MODULES
from content.statistics.tools import TOOLS
from content.statistics.topic_details import TOPIC_DETAILS
from content.tracks.career_paths import CAREER_PATHS
from content.tracks.tool_curricula import TOOL_CURRICULA
from content.tutorials import load_tutorials
from scripts.tutorial_generator import write_tutorial_pages

SITE_URL = SITE["site_url"].rstrip("/")

MODULE_DOMAIN = {
    "foundations": "data-foundations",
    "analytics": "data-foundations",
    "descriptive": "statistics",
    "probability": "statistics",
    "inference": "statistics",
    "regression": "statistics",
    "advanced": "statistics",
    "data-science": "data-science",
    "data-engineering": "data-engineering",
}


def slugify(value: str) -> str:
    value = value.lower().strip().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def build_paths() -> list[dict]:
    """Return active local-progress paths plus hidden compatibility paths."""
    paths: list[dict] = []
    for career in CAREER_PATHS:
        topics = career.get("available_topics") or []
        if not topics:
            continue
        paths.append({
            "id": career["id"],
            "title_en": f"{career['title_en']} Path",
            "title_bn": f"{career['title_bn']} পাথ",
            "description_en": career["description_en"],
            "description_bn": career["description_bn"],
            "topics": topics,
            "status": career["status"],
        })

    legacy = {item["id"]: item for item in LEGACY_PATHS}
    foundations = legacy.get("statistics-foundations")
    if foundations:
        paths.append({**foundations, "status": "legacy", "hidden": True})
    # Preserve old profile IDs from v1 without exposing incomplete career routes as active choices.
    for old_id, fallback in (("data-scientist", "data-analyst"), ("data-engineer", "data-analyst"), ("research-business", "research-analyst")):
        old = legacy.get(old_id)
        target = next((p for p in paths if p["id"] == fallback), None)
        if old and target:
            paths.append({**old, "status": "legacy", "hidden": True, "migration_target": fallback})
    return paths


def build_content() -> dict:
    modules: list[dict] = []
    topics: list[dict] = []
    order = 1
    for module in MODULES:
        module_topics: list[str] = []
        context_en, context_bn = MODULE_CONTEXT[module["id"]]
        domain = MODULE_DOMAIN[module["id"]]
        for item in module["topics"]:
            title_en, title_bn, difficulty, kind, *rest = item
            lab = rest[0] if rest else None
            slug = slugify(title_en)
            formula_en, formula_bn = FORMULAS.get(slug, (
                "This topic is primarily conceptual or procedural; no single universal equation defines it.",
                "এটি প্রধানত conceptual বা procedural topic; একক কোনো universal equation দিয়ে পুরো বিষয়টি সংজ্ঞায়িত হয় না।",
            ))
            summary_en, summary_bn = TOPIC_DETAILS[title_en]
            topic = {
                "id": slug,
                "order": order,
                "module": module["id"],
                "domain": domain,
                "title_en": title_en,
                "title_bn": title_bn,
                "summary_en": summary_en,
                "summary_bn": summary_bn,
                "difficulty": difficulty,
                "kind": kind,
                "minutes": 30 if difficulty == "Beginner" else 45 if difficulty == "Intermediate" else 60,
                "formula_en": formula_en,
                "formula_bn": formula_bn,
                "example_en": f"Use {title_en.lower()} in a small {context_en} example, state the convention, and explain what the result supports.",
                "example_bn": f"একটি ছোট {context_bn} উদাহরণে {title_bn} ব্যবহার করুন, convention উল্লেখ করুন এবং ফলাফল কী সমর্থন করে তা ব্যাখ্যা করুন।",
                "mistakes_en": COMMON_MISTAKES[module["id"]][0],
                "mistakes_bn": COMMON_MISTAKES[module["id"]][1],
                "lab": lab,
                "url": f"topics/{slug}/",
                "publication_status": "available",
            }
            topic["lesson"] = build_lesson_content(topic, module)
            topics.append(topic)
            module_topics.append(slug)
            order += 1
        modules.append({k: v for k, v in module.items() if k != "topics"} | {
            "domain": domain,
            "topics": module_topics,
            "publication_status": "available",
        })

    tools = [{
        "id": slug,
        "title_en": en,
        "title_bn": bn,
        "module": module,
        "domain": MODULE_DOMAIN.get(module, "statistics"),
        "description_en": desc_en,
        "description_bn": desc_bn,
        "url": f"tools/{slug}/",
        "publication_status": "available",
    } for slug, en, bn, module, desc_en, desc_bn in TOOLS]

    return {
        "site": SITE,
        "storage": STORAGE,
        "domains": DOMAINS,
        "modules": modules,
        "topics": topics,
        "tools": tools,
        "paths": build_paths(),
        "career_paths": CAREER_PATHS,
        "tool_curricula": TOOL_CURRICULA,
        "tool_baselines": TOOL_BASELINES,
        "datasets": DATASETS,
        "projects": PROJECTS,
        "tutorials": load_tutorials(),
        "glossary": [
            {"term_en": a, "term_bn": b, "definition_en": c, "definition_bn": d}
            for a, b, c, d in GLOSSARY
        ],
        "release_roadmap": [
            {"version": "v2.0.0", "title_en": "Architecture & curriculum foundation", "title_bn": "Architecture ও curriculum foundation", "status": "completed"},
            {"version": "v2.1.0", "title_en": "Tutorial platform core & complete Data Foundations", "title_bn": "Tutorial platform core ও complete Data Foundations", "status": "current"},
            {"version": "v2.2.0", "title_en": "Complete Excel tutorial", "title_bn": "Complete Excel tutorial", "status": "planned"},
            {"version": "v2.3.0", "title_en": "Complete SQL tutorial", "title_bn": "Complete SQL tutorial", "status": "planned"},
            {"version": "v2.4.0", "title_en": "Complete Power BI tutorial", "title_bn": "Complete Power BI tutorial", "status": "planned"},
            {"version": "v2.5.0", "title_en": "Complete Python for Analytics tutorial", "title_bn": "Complete Python for Analytics tutorial", "status": "planned"},
            {"version": "v2.6.0", "title_en": "Data Analytics workflows & portfolio projects", "title_bn": "Data Analytics workflow ও portfolio project", "status": "planned"},
        ],
    }


def html_shell(*, title: str, description: str, page: str, base: str = "", body_attrs: str = "", extra_scripts: str = "", main_html: str = "") -> str:
    canonical = f"{SITE_URL}/{base}" if base else f"{SITE_URL}/"
    return f"""<!doctype html>
<html lang="en" data-theme="light">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{escape(description)}">
  <meta name="theme-color" content="#6257e8">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{escape(title)}">
  <meta property="og:description" content="{escape(description)}">
  <meta property="og:image" content="{SITE_URL}/assets/icons/social-card.svg">
  <link rel="canonical" href="{canonical}">
  <link rel="icon" href="/assets/icons/favicon.svg" type="image/svg+xml">
  <link rel="manifest" href="/manifest.webmanifest">
  <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
  <script src="/assets/js/theme-init.js"></script>
  <link rel="stylesheet" href="/assets/css/main.css">
  <title>{escape(title)}</title>
</head>
<body data-page="{page}" {body_attrs}>
  <a class="skip-link" href="#main-content">Skip to content</a>
  <div id="site-header"></div>
  <main id="main-content" tabindex="-1">{main_html}</main>
  <div id="site-footer"></div>
  <div id="search-root"></div>
  <button class="scroll-top" id="scroll-top" type="button" aria-label="Scroll to top" title="Scroll to top">↑</button>
  <script src="/assets/js/content.js"></script>
  <script src="/assets/js/site.js" defer></script>
  {extra_scripts}
</body>
</html>
"""


def redirect_page(target: str, title: str) -> str:
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="refresh" content="0; url={target}"><link rel="canonical" href="{SITE_URL}{target}"><title>{escape(title)}</title></head><body><p>Moved to <a href="{target}">{target}</a>.</p><script>location.replace('{target}');</script></body></html>"""


def ensure_dirs(*names: str) -> None:
    for name in names:
        (ROOT / name).mkdir(parents=True, exist_ok=True)


def write_pages(data: dict) -> None:
    ensure_dirs("learn", "practice", "projects", "career-paths", "curriculum", "catalog", "paths", "tools", "about", "start", "my-learning", "glossary")

    home_main = """
<section class="hero home-hero guided-home data-home">
  <div class="container hero-grid">
    <div class="hero-copy reveal">
      <span class="eyebrow" data-en="Data Analytics first · Data Science and Engineering next" data-bn="প্রথমে Data Analytics · পরে Data Science ও Engineering">Data Analytics first · Data Science and Engineering next</span>
      <h1 data-en="Become a Data Analyst—one guided skill at a time." data-bn="একবারে একটি guided skill শিখে Data Analyst হন।">Become a Data Analyst—one guided skill at a time.</h1>
      <p data-en="Start with data foundations and statistics. The curriculum is already mapped for Excel, SQL, Power BI, Python and portfolio projects, and each track will be published without breaking your progress." data-bn="Data Foundations ও Statistics দিয়ে শুরু করুন। Excel, SQL, Power BI, Python ও portfolio project-এর curriculum ইতোমধ্যে mapped; progress না হারিয়ে প্রতিটি track প্রকাশ হবে।">Start with data foundations and statistics. The curriculum is already mapped for Excel, SQL, Power BI, Python and portfolio projects, and each track will be published without breaking your progress.</p>
      <div class="hero-actions"><a class="button primary" id="home-primary-cta" href="/start/">Build my learning plan</a><a class="button ghost" id="home-secondary-cta" href="/learn/">Explore learning domains</a></div>
      <div class="hero-proof" id="hero-stats"></div>
    </div>
    <aside class="home-plan-preview reveal" id="home-plan-preview" aria-live="polite"></aside>
  </div>
</section>
<section class="section method-section"><div class="container"><div class="section-heading center"><div><span class="eyebrow" data-en="A job-ready learning model" data-bn="Job-ready learning model">A job-ready learning model</span><h2 data-en="Learn → Practice → Build → Explain" data-bn="শিখুন → প্র্যাকটিস করুন → তৈরি করুন → ব্যাখ্যা করুন">Learn → Practice → Build → Explain</h2><p class="section-intro" data-en="Every skill should end in an observable output: a calculation, query, report, notebook, project or decision-ready explanation." data-bn="প্রতিটি skill-এর শেষে observable output থাকবে: calculation, query, report, notebook, project বা decision-ready explanation।">Every skill should end in an observable output: a calculation, query, report, notebook, project or decision-ready explanation.</p></div></div><div id="home-method-grid" class="method-grid"></div></div></section>
<section class="section section-muted"><div class="container"><div class="home-next-step" id="home-next-step"></div></div></section>
<section class="section"><div class="container"><div class="section-heading"><div><span class="eyebrow" data-en="The complete Data Analyst route" data-bn="সম্পূর্ণ Data Analyst route">The complete Data Analyst route</span><h2 data-en="One platform, seven connected phases" data-bn="একটি platform, সাতটি connected phase">One platform, seven connected phases</h2><p class="section-intro" data-en="Available content is clearly separated from curriculum-ready and future content—no dead links or pretend lessons." data-bn="Available content-কে curriculum-ready ও future content থেকে পরিষ্কারভাবে আলাদা রাখা হয়েছে—কোনো dead link বা pretend lesson নেই।">Available content is clearly separated from curriculum-ready and future content—no dead links or pretend lessons.</p></div><a href="/curriculum/" class="text-link" data-en="View complete curriculum →" data-bn="সম্পূর্ণ curriculum দেখুন →">View complete curriculum →</a></div><div id="domain-roadmap" class="domain-roadmap"></div></div></section>
<section class="section section-muted"><div class="container"><div class="section-heading"><div><span class="eyebrow" data-en="Practice now" data-bn="এখনই practice করুন">Practice now</span><h2 data-en="Statistics labs and shared practice datasets" data-bn="Statistics lab ও shared practice dataset">Statistics labs and shared practice datasets</h2></div><a href="/practice/" class="text-link" data-en="Open practice center →" data-bn="Practice center খুলুন →">Open practice center →</a></div><div id="featured-tools" class="card-grid featured-tool-grid"></div></div></section>
<section class="section final-cta"><div class="container cta-card"><div><span class="eyebrow">v2.0.0</span><h2 data-en="The architecture is ready for Excel, SQL, Power BI and Python." data-bn="Architecture এখন Excel, SQL, Power BI ও Python-এর জন্য প্রস্তুত।">The architecture is ready for Excel, SQL, Power BI and Python.</h2><p data-en="The current release publishes foundations, statistics, practice datasets and the complete reviewed curriculum map." data-bn="বর্তমান release-এ foundations, statistics, practice dataset এবং complete reviewed curriculum map প্রকাশিত।">The current release publishes foundations, statistics, practice datasets and the complete reviewed curriculum map.</p></div><a class="button primary" href="/curriculum/" data-en="See what comes next" data-bn="পরবর্তী ধাপ দেখুন">See what comes next</a></div></section>
"""
    (ROOT / "index.html").write_text(html_shell(title=SITE["name"], description=SITE["description_en"], page="home", main_html=home_main), encoding="utf-8")

    learn_main = """
<section class="page-hero compact"><div class="container"><span class="eyebrow" data-en="Learn" data-bn="শিখুন">Learn</span><h1 data-en="Start with the active foundation—see the roadmap without being buried by it" data-bn="Active foundation দিয়ে শুরু করুন—চাপ ছাড়াই roadmap দেখুন">Start with the active foundation—see the roadmap without being buried by it</h1><p data-en="Data Foundations and Statistics are available now. Excel, SQL, Power BI and Python are fully mapped and clearly marked for their planned releases." data-bn="Data Foundations ও Statistics এখন available। Excel, SQL, Power BI ও Python সম্পূর্ণ mapped এবং planned release স্পষ্টভাবে দেখানো হয়েছে।">Data Foundations and Statistics are available now. Excel, SQL, Power BI and Python are fully mapped and clearly marked for their planned releases.</p></div></section>
<section class="section"><div class="container"><div id="learning-domain-overview" class="learning-domain-overview"></div><div class="guided-catalog" id="guided-catalog"></div><div class="catalog-toolbar"><button class="button ghost hidden" id="recommended-only" type="button"></button></div><div class="filter-panel"><label class="search-field"><span class="sr-only">Search lessons</span><input id="catalog-search" type="search" placeholder="Search available lessons…" data-placeholder-en="Search available lessons…" data-placeholder-bn="Available lesson খুঁজুন…"><span>⌕</span></label><select id="domain-filter" aria-label="Filter by domain"></select><select id="module-filter" aria-label="Filter by module"></select><select id="difficulty-filter" aria-label="Filter by difficulty"><option value="all">All levels</option><option>Beginner</option><option>Intermediate</option><option>Advanced</option></select><select id="kind-filter" aria-label="Filter by format"><option value="all">All formats</option><option value="lesson">Lesson</option><option value="lab">Lab-linked</option><option value="practice">Practice</option></select></div><div class="result-line"><strong id="catalog-count"></strong><button class="button small ghost" id="clear-filters" type="button" data-en="Clear filters" data-bn="ফিল্টার মুছুন">Clear filters</button></div><div id="catalog-grid" class="card-grid lesson-grid"></div></div></section>
"""
    (ROOT / "learn" / "index.html").write_text(html_shell(title=f"Learn | {SITE['name']}", description="Available data foundations and statistics lessons with a transparent Data Analytics curriculum roadmap.", page="learn", base="learn/", main_html=learn_main, extra_scripts='<script src="/assets/js/catalog.js" defer></script>'), encoding="utf-8")
    (ROOT / "catalog" / "index.html").write_text(redirect_page("/learn/", f"Learn | {SITE['name']}"), encoding="utf-8")

    practice_main = """
<section class="page-hero compact"><div class="container"><span class="eyebrow" data-en="Practice" data-bn="প্র্যাকটিস">Practice</span><h1 data-en="Experiment with statistics and download reusable analytical datasets" data-bn="Statistics experiment করুন এবং reusable analytical dataset download করুন">Experiment with statistics and download reusable analytical datasets</h1><p data-en="All labs run locally in the browser. All downloadable datasets are synthetic and documented for educational use." data-bn="সব lab browser-এ locally run করে। সব downloadable dataset synthetic এবং educational use-এর জন্য documented।">All labs run locally in the browser. All downloadable datasets are synthetic and documented for educational use.</p></div></section>
<section class="section"><div class="container"><div class="practice-tabs"><a class="active" href="#labs" data-en="Interactive labs" data-bn="Interactive lab">Interactive labs</a><a href="#datasets" data-en="Practice datasets" data-bn="Practice dataset">Practice datasets</a></div><div id="labs"><div class="section-heading"><div><h2 data-en="Statistics laboratories" data-bn="Statistics laboratory">Statistics laboratories</h2><p class="section-intro" data-en="Calculate, visualize and interpret with stated methods and input validation." data-bn="Stated method ও input validation-সহ calculate, visualize ও interpret করুন।">Calculate, visualize and interpret with stated methods and input validation.</p></div></div><div class="filter-panel compact-filter"><label class="search-field"><span class="sr-only">Search labs</span><input id="tool-search" type="search" placeholder="Search labs…" data-placeholder-en="Search labs…" data-placeholder-bn="ল্যাব খুঁজুন…"><span>⌕</span></label><select id="tool-module-filter" aria-label="Filter labs by module"></select></div><div class="result-line"><strong id="tool-count"></strong></div><div id="tool-grid" class="card-grid tool-grid"></div></div><div id="datasets" class="dataset-section"><div class="section-heading"><div><h2 data-en="Shared synthetic datasets" data-bn="Shared synthetic dataset">Shared synthetic datasets</h2><p class="section-intro" data-en="The same datasets will connect future Excel, SQL, Power BI and Python lessons." data-bn="একই dataset future Excel, SQL, Power BI ও Python lesson-কে connect করবে।">The same datasets will connect future Excel, SQL, Power BI and Python lessons.</p></div></div><div id="dataset-grid" class="card-grid dataset-grid"></div></div></div></section>
"""
    (ROOT / "practice" / "index.html").write_text(html_shell(title=f"Practice | {SITE['name']}", description="Interactive statistical labs and documented synthetic practice datasets.", page="practice", base="practice/", main_html=practice_main, extra_scripts='<script src="/assets/js/tools-index.js" defer></script>'), encoding="utf-8")
    (ROOT / "tools" / "index.html").write_text(redirect_page("/practice/", f"Practice | {SITE['name']}"), encoding="utf-8")

    career_main = """
<section class="page-hero compact"><div class="container"><span class="eyebrow" data-en="Career paths" data-bn="Career path">Career paths</span><h1 data-en="Data Analyst is active; future roles build on the same foundation" data-bn="Data Analyst active; future role একই foundation-এর ওপর তৈরি হবে">Data Analyst is active; future roles build on the same foundation</h1><p data-en="The platform will complete Data Analytics first. Data Science and Data Engineering remain honest roadmaps until their full learning experiences are implemented." data-bn="Platform প্রথমে Data Analytics complete করবে। Full learning experience implement না হওয়া পর্যন্ত Data Science ও Data Engineering honest roadmap হিসেবে থাকবে।">The platform will complete Data Analytics first. Data Science and Data Engineering remain honest roadmaps until their full learning experiences are implemented.</p></div></section>
<section class="section"><div class="container"><div id="career-paths-root"></div></div></section>
"""
    (ROOT / "career-paths" / "index.html").write_text(html_shell(title=f"Career Paths | {SITE['name']}", description="Active Data Analyst path and transparent future Data Science and Data Engineering roadmaps.", page="career-paths", base="career-paths/", main_html=career_main, extra_scripts='<script src="/assets/js/career-paths.js" defer></script>'), encoding="utf-8")
    (ROOT / "paths" / "index.html").write_text(redirect_page("/career-paths/", f"Career Paths | {SITE['name']}"), encoding="utf-8")

    curriculum_main = """
<section class="page-hero compact"><div class="container"><span class="eyebrow" data-en="Curriculum foundation" data-bn="Curriculum foundation">Curriculum foundation</span><h1 data-en="A complete, sequenced Data Analytics curriculum—published in controlled releases" data-bn="Complete, sequenced Data Analytics curriculum—controlled release-এ প্রকাশিত হবে">A complete, sequenced Data Analytics curriculum—published in controlled releases</h1><p data-en="This map defines prerequisites, outcomes, modules and authoritative tool baselines before lesson production begins." data-bn="Lesson production-এর আগে এই map prerequisite, outcome, module ও authoritative tool baseline define করে।">This map defines prerequisites, outcomes, modules and authoritative tool baselines before lesson production begins.</p></div></section>
<section class="section"><div class="container"><div id="curriculum-root"></div></div></section>
"""
    (ROOT / "curriculum" / "index.html").write_text(html_shell(title=f"Curriculum | {SITE['name']}", description="The reviewed curriculum architecture for Data Foundations, Statistics, Excel, SQL, Power BI, Python and projects.", page="curriculum", base="curriculum/", main_html=curriculum_main, extra_scripts='<script src="/assets/js/curriculum.js" defer></script>'), encoding="utf-8")

    projects_main = """
<section class="page-hero compact"><div class="container"><span class="eyebrow" data-en="Projects" data-bn="প্রজেক্ট">Projects</span><h1 data-en="Apply multiple skills to one consistent business problem" data-bn="একটি consistent business problem-এ multiple skill apply করুন">Apply multiple skills to one consistent business problem</h1><p data-en="v2.0.0 establishes the shared dataset and project architecture. The first foundation project is available now; cross-tool capstones arrive after the tool tracks." data-bn="v2.0.0 shared dataset ও project architecture স্থাপন করেছে। প্রথম foundation project এখন available; tool track-এর পর cross-tool capstone আসবে।">v2.0.0 establishes the shared dataset and project architecture. The first foundation project is available now; cross-tool capstones arrive after the tool tracks.</p></div></section>
<section class="section"><div class="container"><div id="projects-root"></div></div></section>
"""
    (ROOT / "projects" / "index.html").write_text(html_shell(title=f"Projects | {SITE['name']}", description="Data Analytics project and portfolio architecture using shared synthetic datasets.", page="projects", base="projects/", main_html=projects_main, extra_scripts='<script src="/assets/js/projects.js" defer></script>'), encoding="utf-8")

    project = next(item for item in PROJECTS if item["id"] == "retail-sales-foundations")
    project_dir = ROOT / "projects" / project["id"]
    project_dir.mkdir(parents=True, exist_ok=True)
    project_main = """
<section class="project-shell"><div class="container"><nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a><span>/</span><a href="/projects/">Projects</a><span>/</span><span>Retail Sales Foundations</span></nav><header class="project-hero"><div><span class="eyebrow" data-en="Available foundation project" data-bn="Available foundation project">Available foundation project</span><h1 data-en="Retail Sales Foundations Project" data-bn="রিটেইল সেলস ফাউন্ডেশন প্রজেক্ট">Retail Sales Foundations Project</h1><p data-en="Audit a synthetic transaction dataset, define defensible metrics, summarize variation and write a short decision-ready finding." data-bn="Synthetic transaction dataset audit, defensible metric define, variation summarize এবং short decision-ready finding লিখুন।">Audit a synthetic transaction dataset, define defensible metrics, summarize variation and write a short decision-ready finding.</p></div><span class="status-chip available" data-en="Available now" data-bn="এখন available">Available now</span></header><div class="project-layout"><article class="topic-main"><section class="topic-card"><span class="section-kicker">01 · Download</span><h2 data-en="Get the dataset and dictionary" data-bn="Dataset ও dictionary নিন">Get the dataset and dictionary</h2><p data-en="The files are synthetic and contain no real customer or company data." data-bn="File synthetic; কোনো real customer বা company data নেই।">The files are synthetic and contain no real customer or company data.</p><div class="hero-actions"><a class="button primary" href="/assets/datasets/retail_sales.csv" download>Download CSV</a><a class="button ghost" href="/assets/datasets/retail_sales_dictionary.csv" download>Download dictionary</a></div></section><section class="topic-card"><span class="section-kicker">02 · Frame</span><h2 data-en="Define the analytical question" data-bn="Analytical question define করুন">Define the analytical question</h2><ul class="objective-list"><li data-en="Which regions and channels produce the most revenue and profit?" data-bn="কোন region ও channel সবচেয়ে বেশি revenue ও profit তৈরি করে?">Which regions and channels produce the most revenue and profit?</li><li data-en="How variable are daily sales?" data-bn="Daily sales কতটা variable?">How variable are daily sales?</li><li data-en="Which products deserve further investigation?" data-bn="কোন product further investigation প্রয়োজন?">Which products deserve further investigation?</li></ul></section><section class="topic-card"><span class="section-kicker">03 · Audit</span><h2 data-en="Check data quality before analysis" data-bn="Analysis-এর আগে data quality check করুন">Check data quality before analysis</h2><ol class="workflow-list"><li><strong>Grain</strong><span data-en="Confirm that one row represents one transaction line." data-bn="এক row একটি transaction line represent করে কিনা confirm করুন।">Confirm that one row represents one transaction line.</span></li><li><strong>Types</strong><span data-en="Check dates, categories, integer quantities and numeric amounts." data-bn="Date, category, integer quantity ও numeric amount check করুন।">Check dates, categories, integer quantities and numeric amounts.</span></li><li><strong>Reconciliation</strong><span data-en="Verify profit equals revenue minus cost." data-bn="Profit = revenue − cost verify করুন।">Verify profit equals revenue minus cost.</span></li><li><strong>Duplicates</strong><span data-en="Confirm transaction IDs are unique." data-bn="Transaction ID unique কিনা confirm করুন।">Confirm transaction IDs are unique.</span></li></ol></section><section class="topic-card"><span class="section-kicker">04 · Analyze</span><h2 data-en="Produce a minimum evidence set" data-bn="Minimum evidence set তৈরি করুন">Produce a minimum evidence set</h2><ul class="objective-list"><li data-en="Total revenue, cost and profit" data-bn="Total revenue, cost ও profit">Total revenue, cost and profit</li><li data-en="Average and median transaction revenue" data-bn="Average ও median transaction revenue">Average and median transaction revenue</li><li data-en="Revenue and profit by region, channel and product" data-bn="Region, channel ও product অনুযায়ী revenue ও profit">Revenue and profit by region, channel and product</li><li data-en="A histogram or box plot of transaction revenue" data-bn="Transaction revenue-এর histogram বা box plot">A histogram or box plot of transaction revenue</li></ul><div class="hero-actions"><a class="button ghost" href="/tools/summary-statistics/">Summary lab</a><a class="button ghost" href="/tools/histogram/">Histogram lab</a><a class="button ghost" href="/tools/box-plot/">Box plot lab</a></div></section><section class="topic-card"><span class="section-kicker">05 · Communicate</span><h2 data-en="Write the final finding" data-bn="Final finding লিখুন">Write the final finding</h2><p data-en="Write three short sections: what happened, what evidence supports it, and what limitation or next check remains. Do not claim that a product or channel caused performance differences from this observational dataset alone." data-bn="তিনটি short section লিখুন: কী ঘটেছে, কোন evidence সমর্থন করে এবং কোন limitation বা next check বাকি। Observational dataset থেকে product বা channel performance difference cause করেছে—এমন claim করবেন না।">Write three short sections: what happened, what evidence supports it, and what limitation or next check remains. Do not claim that a product or channel caused performance differences from this observational dataset alone.</p></section></article><aside class="topic-aside"><div class="aside-card"><h3 data-en="Deliverables" data-bn="Deliverable">Deliverables</h3><ul><li>Data-quality checklist</li><li>Metric table</li><li>Two useful charts</li><li>Three-paragraph finding</li><li>One limitation</li></ul></div><div class="aside-card"><h3 data-en="Future reuse" data-bn="Future reuse">Future reuse</h3><p data-en="This same dataset will return in Excel, SQL, Power BI and Python projects." data-bn="একই dataset Excel, SQL, Power BI ও Python project-এ আবার ব্যবহার হবে।">This same dataset will return in Excel, SQL, Power BI and Python projects.</p></div></aside></div></div></section>
"""
    (project_dir / "index.html").write_text(html_shell(title=f"Retail Sales Foundations Project | {SITE['name']}", description=project["description_en"], page="project", base="projects/retail-sales-foundations/", main_html=project_main), encoding="utf-8")

    glossary_main = """
<section class="page-hero compact"><div class="container"><span class="eyebrow" data-en="Glossary" data-bn="গ্লসারি">Glossary</span><h1 data-en="Plain-language data and statistics definitions" data-bn="সহজ ভাষায় data ও statistics definition">Plain-language data and statistics definitions</h1><p data-en="Search bilingual terms used across the available lessons and future tool tracks." data-bn="Available lesson ও future tool track-এ ব্যবহৃত bilingual term খুঁজুন।">Search bilingual terms used across the available lessons and future tool tracks.</p></div></section><section class="section"><div class="container"><label class="search-field glossary-search"><input id="glossary-search" type="search" placeholder="Search terms…" data-placeholder-en="Search terms…" data-placeholder-bn="টার্ম খুঁজুন…"><span>⌕</span></label><div id="glossary-grid" class="glossary-grid"></div></div></section>
"""
    (ROOT / "glossary" / "index.html").write_text(html_shell(title=f"Glossary | {SITE['name']}", description="Bilingual data, analytics and statistics glossary.", page="glossary", base="glossary/", main_html=glossary_main, extra_scripts='<script src="/assets/js/glossary.js" defer></script>'), encoding="utf-8")

    about_main = f"""
<section class="page-hero compact"><div class="container"><span class="eyebrow" data-en="About the platform" data-bn="Platform সম্পর্কে">About the platform</span><h1 data-en="A static, tutorial-first and transparent Data Analytics learning platform" data-bn="Static, tutorial-first ও transparent Data Analytics learning platform">A static, tutorial-first and transparent Data Analytics learning platform</h1><p data-en="Data Learning Hub teaches Data Analytics first, then extends the same architecture into Data Science and Data Engineering." data-bn="Data Learning Hub প্রথমে Data Analytics শেখায়, পরে একই architecture-কে Data Science ও Data Engineering-এ extend করবে।">Data Learning Hub teaches Data Analytics first, then extends the same architecture into Data Science and Data Engineering.</p></div></section><section class="section"><div class="container about-layout"><article class="prose-card"><h2 data-en="What v2.1.0 provides" data-bn="v2.1.0 যা দেয়">What v2.1.0 provides</h2><p data-en="A complete 21-chapter Data Foundations Tutorial, tutorial navigation, interactive activities, chapter exercises, final quiz, example and reference libraries—alongside 108 retained comprehensive lessons, 20 browser labs, datasets, projects, and reviewed tool curricula." data-bn="Complete 21-chapter Data Foundations Tutorial, tutorial navigation, interactive activity, chapter exercise, final quiz, example ও reference library—এর সঙ্গে 108 retained lesson, 20 browser lab, dataset, project ও reviewed tool curriculum।">A complete 21-chapter Data Foundations Tutorial, tutorial navigation, interactive activities, chapter exercises, final quiz, example and reference libraries—alongside 108 retained comprehensive lessons, 20 browser labs, datasets, projects, and reviewed tool curricula.</p><h2 data-en="Publication honesty" data-bn="Publication honesty">Publication honesty</h2><p data-en="Only complete tutorials are labeled published. Curriculum-ready modules show scope and target release, but never pretend to be complete tutorial pages." data-bn="শুধু complete tutorial published label পায়। Curriculum-ready module scope ও target release দেখায়, কিন্তু complete tutorial page হিসেবে pretend করে না।">Only complete tutorials are labeled published. Curriculum-ready modules show scope and target release, but never pretend to be complete tutorial pages.</p><h2 data-en="Privacy" data-bn="Privacy">Privacy</h2><p data-en="No backend, API, database or account is required. Language, theme, progress, bookmarks and plan preferences remain optional browser-local data." data-bn="Backend, API, database বা account প্রয়োজন নেই। Language, theme, progress, bookmark ও plan preference optional browser-local data হিসেবে থাকে।">No backend, API, database or account is required. Language, theme, progress, bookmarks and plan preferences remain optional browser-local data.</p><h2 data-en="Progress migration" data-bn="Progress migration">Progress migration</h2><p data-en="On first load, v2 copies compatible v1 browser preferences from the old slh-* keys into versioned dlh-* keys. The original keys are not deleted." data-bn="First load-এ v2 পুরোনো slh-* key থেকে compatible browser preference versioned dlh-* key-এ copy করে। Original key delete করা হয় না।">On first load, v2 copies compatible v1 browser preferences from the old slh-* keys into versioned dlh-* keys. The original keys are not deleted.</p></article><aside class="credit-card"><span class="eyebrow">Credits</span><h2>{escape(SITE['creator'])}</h2><p data-en="Idea and developed by Saiful Islam." data-bn="Idea and developed by Saiful Islam.">Idea and developed by Saiful Islam.</p><div class="credit-links"><a href="{SITE['website']}" target="_blank" rel="noopener noreferrer">Website ↗</a><a href="{SITE['github']}" target="_blank" rel="noopener noreferrer">GitHub ↗</a><a href="{SITE['linkedin']}" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a></div><hr><p class="small" data-en="Conceptually inspired by a public statistics learning repository. This rebuild uses original architecture, interface and educational copy." data-bn="একটি public statistics learning repository থেকে conceptually inspired। এই rebuild-এর architecture, interface ও educational copy original।">Conceptually inspired by a public statistics learning repository. This rebuild uses original architecture, interface and educational copy.</p><a href="{SITE['inspiration']}" target="_blank" rel="noopener noreferrer">Original inspiration ↗</a></aside></div></section>
"""
    (ROOT / "about" / "index.html").write_text(html_shell(title=f"About | {SITE['name']}", description="About Data Learning Hub, its phased curriculum, privacy model and credits.", page="about", base="about/", main_html=about_main), encoding="utf-8")

    start_main = """
<section class="wizard-shell"><div class="container wizard-layout"><aside class="wizard-aside"><a class="brand" href="/"><span class="brand-mark">D</span><span class="brand-text">Data Learning Hub<small data-en="Guided Data Analyst setup" data-bn="Guided Data Analyst setup">Guided Data Analyst setup</small></span></a><div><span class="eyebrow" data-en="A focused route" data-bn="Focused route">A focused route</span><h2 data-en="See only the next useful step." data-bn="শুধু পরবর্তী useful step দেখুন।">See only the next useful step.</h2><p data-en="The setup personalizes the available foundation while preserving access to the curriculum and full statistics library." data-bn="Setup available foundation personalize করে; curriculum ও full statistics library access খোলা থাকে।">The setup personalizes the available foundation while preserving access to the curriculum and full statistics library.</p></div><ul class="wizard-benefits"><li data-en="Data Analyst is the active career route" data-bn="Data Analyst active career route">Data Analyst is the active career route</li><li data-en="Your v1 progress is migrated automatically" data-bn="v1 progress automatically migrate হয়">Your v1 progress is migrated automatically</li><li data-en="Everything remains in your browser" data-bn="সবকিছু browser-এ থাকে">Everything remains in your browser</li></ul></aside><section class="wizard-card" id="guide-wizard"></section></div></section>
"""
    (ROOT / "start" / "index.html").write_text(html_shell(title=f"Start Here | {SITE['name']}", description="Create a private Data Analyst learning plan based on experience, study time and learning style.", page="start", base="start/", main_html=start_main, extra_scripts='<script src="/assets/js/start.js" defer></script>'), encoding="utf-8")

    dashboard_main = '<section class="dashboard-shell"><div class="container" id="learning-dashboard"></div></section>'
    (ROOT / "my-learning" / "index.html").write_text(html_shell(title=f"My Learning | {SITE['name']}", description="Private browser-local Data Analyst learning dashboard.", page="my-learning", base="my-learning/", main_html=dashboard_main, extra_scripts='<script src="/assets/js/dashboard.js" defer></script>'), encoding="utf-8")

    module_by_id = {m["id"]: m for m in data["modules"]}
    for topic in data["topics"]:
        module = module_by_id[topic["module"]]
        topic_dir = ROOT / "topics" / topic["id"]
        topic_dir.mkdir(parents=True, exist_ok=True)
        static_main = f"""
<section class="topic-shell" id="topic-app"><div class="container"><nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a><span>/</span><a href="/learn/">Learn</a><span>/</span><span>{escape(topic['title_en'])}</span></nav><header class="topic-hero"><div><span class="eyebrow">{escape(module['title_en'])}</span><h1>{escape(topic['title_en'])}</h1><p>{escape(topic['summary_en'])}</p></div><div class="topic-actions"><button class="icon-action" id="bookmark-topic" type="button" aria-label="Bookmark lesson" title="Bookmark">☆</button><button class="button primary" id="complete-topic" type="button">Mark complete</button></div></header><div id="topic-content"></div></div></section>"""
        (topic_dir / "index.html").write_text(html_shell(title=f"{topic['title_en']} | {SITE['name']}", description=topic["summary_en"], page="topic", base=f"topics/{topic['id']}/", body_attrs=f'data-topic="{topic["id"]}"', main_html=static_main, extra_scripts='<script src="/assets/js/topic.js" defer></script>'), encoding="utf-8")

    for tool in data["tools"]:
        tool_dir = ROOT / "tools" / tool["id"]
        tool_dir.mkdir(parents=True, exist_ok=True)
        static_main = f"""
<section class="tool-shell"><div class="container"><nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a><span>/</span><a href="/practice/">Practice</a><span>/</span><span>{escape(tool['title_en'])}</span></nav><header class="tool-hero"><div><span class="eyebrow">Interactive statistics lab</span><h1>{escape(tool['title_en'])}</h1><p>{escape(tool['description_en'])}</p></div><span class="privacy-pill">Runs locally</span></header><div id="tool-app" data-tool="{tool['id']}"></div></div></section>"""
        extra = '<script src="https://cdn.jsdelivr.net/npm/chart.js@4.5.1/dist/chart.umd.min.js" defer></script><script type="module" src="/assets/js/tools.js"></script>'
        (tool_dir / "index.html").write_text(html_shell(title=f"{tool['title_en']} | {SITE['name']}", description=tool["description_en"], page="tool", base=f"tools/{tool['id']}/", body_attrs=f'data-tool="{tool["id"]}"', main_html=static_main, extra_scripts=extra), encoding="utf-8")

    not_found = """
<section class="page-hero error-page"><div class="container"><span class="error-code">404</span><h1 data-en="This page is not published." data-bn="এই page publish করা হয়নি।">This page is not published.</h1><p data-en="Use Learn, Practice, Projects or Curriculum to find available and planned content." data-bn="Available ও planned content খুঁজতে Learn, Practice, Projects বা Curriculum ব্যবহার করুন।">Use Learn, Practice, Projects or Curriculum to find available and planned content.</p><div class="hero-actions"><a class="button primary" href="/learn/" data-en="Open Learn" data-bn="Learn খুলুন">Open Learn</a><a class="button ghost" href="/curriculum/" data-en="View curriculum" data-bn="Curriculum দেখুন">View curriculum</a></div></div></section>"""
    (ROOT / "404.html").write_text(html_shell(title=f"Page not found | {SITE['name']}", description="The requested page is not published.", page="404", base="404.html", main_html=not_found), encoding="utf-8")

    urls = ["/", "/start/", "/my-learning/", "/learn/", "/practice/", "/projects/", "/projects/retail-sales-foundations/", "/career-paths/", "/curriculum/", "/glossary/", "/about/"]
    urls += [f"/{t['url']}" for t in data["topics"]]
    urls += [f"/{t['url']}" for t in data["tools"]]
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(f"  <url><loc>{SITE_URL}{u}</loc></url>" for u in urls) + "\n</urlset>\n"
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")


def main() -> None:
    data = build_content()
    content_js = "window.DLH_CONTENT = " + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n"
    (ROOT / "assets" / "js" / "content.js").write_text(content_js, encoding="utf-8")
    write_pages(data)
    tutorial_urls = write_tutorial_pages(ROOT, data, html_shell)
    sitemap_path = ROOT / "sitemap.xml"
    sitemap = sitemap_path.read_text(encoding="utf-8")
    additions = "\n".join(f"  <url><loc>{SITE_URL}{url}</loc></url>" for url in tutorial_urls)
    sitemap = sitemap.replace("\n</urlset>", f"\n{additions}\n</urlset>")
    sitemap_path.write_text(sitemap, encoding="utf-8")
    chapter_count = sum(len(t['chapters']) for t in data['tutorials'])
    print(
        f"Generated Data Learning Hub {SITE['version']}: {len(data['topics'])} retained lessons, "
        f"{len(data['tools'])} labs, {len(data['tutorials'])} published tutorials, "
        f"{chapter_count} tutorial chapters and {len(data['projects'])} projects."
    )


if __name__ == "__main__":
    main()
