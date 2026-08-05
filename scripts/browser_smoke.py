from __future__ import annotations
import re
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
SCREENSHOTS=ROOT/'docs'/'screenshots-v2.6.0'
SCREENSHOTS.mkdir(parents=True,exist_ok=True)
SCRIPT_MAP={
 'home':[], 'tutorials':[], 'resources':[], 'projects':['projects.js'], 'portfolio-project':['portfolio-project.js'],
 'tutorial-course':['tutorial-core.js','tutorial-index.js'],
 'tutorial-chapter':['tutorial-core.js','tutorial.js'],
 'tutorial-sql-chapter':['tutorial-core.js','sql-practice.js','tutorial.js'],
 'tutorial-python-chapter':['tutorial-core.js','python-practice.js','tutorial.js'],
 'tutorial-exercises':['tutorial-core.js','tutorial-exercises.js'],
 'tutorial-quiz':['tutorial-core.js','tutorial-quiz.js'],
 'tool':[],
}

def stripped_html(relative:str)->str:
    html=(ROOT/relative).read_text(encoding='utf-8')
    html=re.sub(r'<link rel="(?:icon|manifest|preconnect)"[^>]*>','',html)
    html=re.sub(r'<link rel="stylesheet"[^>]*>','',html)
    html=re.sub(r'<script[^>]*src="[^"]+"[^>]*></script>','',html)
    return html

def install_storage(page,initial=None):
    page.evaluate("""initial=>{const store=new Map(Object.entries(initial||{}));Object.defineProperty(window,'localStorage',{configurable:true,value:{getItem:k=>store.has(String(k))?store.get(String(k)):null,setItem:(k,v)=>store.set(String(k),String(v)),removeItem:k=>store.delete(String(k)),clear:()=>store.clear(),key:i=>Array.from(store.keys())[i]??null,get length(){return store.size}}});}""",initial or {})

def inject(page,page_type,storage=None):
    install_storage(page,storage)
    css=(ROOT/'assets/css/main.css').read_text(encoding='utf-8')
    page.evaluate("css=>{const s=document.createElement('style');s.textContent=css;document.head.appendChild(s)}",css)
    for filename in ['theme-init.js','content.js','site.js',*SCRIPT_MAP.get(page_type,[])]:
        page.evaluate((ROOT/'assets/js'/filename).read_text(encoding='utf-8'))

def load(page,relative,page_type,storage=None):
    page.set_content(stripped_html(relative),wait_until='domcontentloaded')
    inject(page,page_type,storage)

def assert_sticky(page):
    page.wait_for_selector('#site-header .site-header')
    before=page.locator('#site-header').evaluate('el=>el.getBoundingClientRect().top')
    page.evaluate('window.scrollTo(0, Math.min(1000, document.body.scrollHeight-300))')
    page.wait_for_timeout(60)
    after=page.locator('#site-header').evaluate('el=>el.getBoundingClientRect().top')
    assert abs(before)<1.5 and abs(after)<1.5
    assert page.locator('#site-header').evaluate("el=>getComputedStyle(el).position")=='sticky'

def main():
  with sync_playwright() as p:
    browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
    page=browser.new_page(viewport={'width':1440,'height':1000}); page.set_default_timeout(15000)

    print('stage home',flush=True)
    load(page,'index.html','home',{'dlh-language':'en','dlh-theme':'light'})
    assert 'Learn Data Analytics here' in page.locator('h1').first.inner_text()
    assert page.get_by_text('363',exact=True).count()>=1
    assert page.get_by_text('Analytics Workflows',exact=True).count()>=1
    assert page.locator('.home-course-card').count()==6
    assert page.locator('.footer-bottom-links a').count()==1
    assert page.locator('.footer-bottom-links a').first.inner_text().strip()=='About'
    assert_sticky(page); page.evaluate('window.scrollTo(0,0)')
    page.screenshot(path=str(SCREENSHOTS/'home-desktop.png'),full_page=False)

    print('stage tutorial library',flush=True)
    load(page,'tutorials/index.html','tutorials')
    assert page.locator('.subject-course-card.published').count()==6

    print('stage workflow course',flush=True)
    load(page,'tutorials/data-analytics-workflows/index.html','tutorial-course')
    page.wait_for_selector('.tutorial-index-card')
    assert page.locator('.tutorial-index-card').count()==49
    assert page.locator('.tutorial-index-module').count()==8
    assert page.get_by_role('link',name=re.compile('Analytics Portfolio Toolkit')).count()>=1
    assert_sticky(page); page.evaluate('window.scrollTo(0,0)')
    page.screenshot(path=str(SCREENSHOTS/'workflow-course-desktop.png'),full_page=False)

    print('stage workflow chapter',flush=True)
    load(page,'tutorials/data-analytics-workflows/cross-tool-reconciliation/index.html','tutorial-chapter')
    page.wait_for_selector('#tutorial-activity .try-panel')
    assert page.locator('.tutorial-chapter-link').count()==49
    assert page.locator('.exercise-card').count()==3
    assert page.locator('#tutorial-activity input[type="checkbox"]').count()>=3
    page.get_by_role('button',name='Mark complete').first.click()
    assert 'cross-tool-reconciliation' in page.evaluate("localStorage.getItem('dlh-tutorial-data-analytics-workflows-completed')")
    page.get_by_role('button',name='বাংলা').click(); assert page.locator('html').get_attribute('lang')=='bn'
    page.get_by_role('button',name='English').click(); assert_sticky(page); page.evaluate('window.scrollTo(0,0)')
    page.screenshot(path=str(SCREENSHOTS/'workflow-reconciliation-desktop.png'),full_page=False)

    print('stage exercises and quiz',flush=True)
    load(page,'exercises/data-analytics-workflows/index.html','tutorial-exercises')
    assert page.locator('.exercise-library-section').count()==49
    assert page.locator('.exercise-card').count()==147
    load(page,'quiz/data-analytics-workflows/index.html','tutorial-quiz')
    page.get_by_role('button',name='Start quiz').click(); page.wait_for_selector('.quiz-question')
    assert page.locator('.quiz-question').count()==30

    print('stage project center',flush=True)
    load(page,'projects/index.html','projects')
    page.wait_for_selector('.portfolio-project-card')
    assert page.locator('.portfolio-project-card').count()==6
    assert page.get_by_role('link',name='Open project').count()==6
    assert_sticky(page); page.evaluate('window.scrollTo(0,0)')
    page.screenshot(path=str(SCREENSHOTS/'portfolio-projects-desktop.png'),full_page=False)

    print('stage project page',flush=True)
    load(page,'projects/retail-sales-360/index.html','portfolio-project')
    assert page.locator('.project-phase-card').count()==8
    assert page.locator('[data-project-task]').count()==8
    page.locator('[data-project-task]').first.check()
    assert page.locator('[data-project-progress]').inner_text().startswith('1/8')
    assert 'retail-sales-360-01' in page.evaluate("localStorage.getItem('dlh-project-retail-sales-360-tasks')")
    assert page.get_by_role('link',name=re.compile('Complete project package')).count()==1
    assert_sticky(page); page.evaluate('window.scrollTo(0,0)')
    page.screenshot(path=str(SCREENSHOTS/'retail-project-desktop.png'),full_page=False)

    print('stage retained course regression',flush=True)
    for path,ptype,selector,count in [
      ('tutorials/data-foundations/data-and-statistics/index.html','tutorial-chapter','.tutorial-chapter-link',21),
      ('tutorials/excel-data-analytics/xlookup/index.html','tutorial-chapter','.tutorial-chapter-link',56),
      ('tutorials/sql-data-analytics/inner-join/index.html','tutorial-sql-chapter','.tutorial-chapter-link',66),
      ('tutorials/power-bi-data-analytics/dax-overview/index.html','tutorial-chapter','.tutorial-chapter-link',77),
      ('tutorials/python-data-analytics/groupby-and-aggregation/index.html','tutorial-python-chapter','.tutorial-chapter-link',94),
    ]:
      load(page,path,ptype); assert page.locator(selector).count()==count; assert_sticky(page)
    load(page,'tools/summary-statistics/index.html','tool'); assert_sticky(page)

    print('stage mobile',flush=True)
    mobile=browser.new_page(viewport={'width':390,'height':844}); mobile.set_default_timeout(15000)
    load(mobile,'tutorials/data-analytics-workflows/cross-tool-reconciliation/index.html','tutorial-chapter')
    mobile.locator('#tutorial-drawer-open').click(force=True)
    assert mobile.locator('[data-chapter-link]').count()==49
    mobile.screenshot(path=str(SCREENSHOTS/'workflow-reconciliation-mobile.png'),full_page=False)
    mobile.close(); browser.close()
  print('Browser smoke test passed for sticky headers, six-course tutorial navigation, Analytics Workflows, exercises, quiz, six portfolio projects, project progress, bilingual state, retained courses, statistical lab, exact footer behavior, and mobile drawer.')

if __name__=='__main__': main()
