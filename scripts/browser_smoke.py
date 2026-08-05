from __future__ import annotations
import re
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
SCREENSHOTS=ROOT/'docs'/'screenshots-v2.5.0'
SCREENSHOTS.mkdir(parents=True,exist_ok=True)
SCRIPT_MAP={
 'home':[], 'tutorials':[], 'resources':[],
 'tutorial-course':['tutorial-core.js','tutorial-index.js'],
 'tutorial-chapter':['tutorial-core.js','tutorial.js'],
 'tutorial-sql-chapter':['tutorial-core.js','sql-practice.js','tutorial.js'],
 'tutorial-python-chapter':['tutorial-core.js','python-practice.js','tutorial.js'],
 'sql-playground':['sql-practice.js'],
 'python-playground':['python-practice.js'],
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
    page.evaluate('window.scrollTo(0, Math.min(1400, document.body.scrollHeight-300))')
    page.wait_for_timeout(100)
    after=page.locator('#site-header').evaluate('el=>el.getBoundingClientRect().top')
    assert abs(before) < 1.5, before
    assert abs(after) < 1.5, after
    assert page.locator('#site-header').evaluate("el=>getComputedStyle(el).position")=='sticky'

def main():
  with sync_playwright() as p:
    browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
    context=browser.new_context(viewport={'width':1440,'height':1000},device_scale_factor=1)
    page=context.new_page(); page.set_default_timeout(30000)

    print('stage home',flush=True)
    load(page,'index.html','home',{'dlh-language':'en','dlh-theme':'light'})
    page.wait_for_selector('.site-header')
    assert page.get_by_role('link',name='Tutorials',exact=True).count()==1
    assert 'Learn Data Analytics here' in page.locator('h1').first.inner_text()
    assert page.get_by_text('Excel for Data Analytics',exact=True).count()>=1
    assert page.get_by_text('314',exact=True).count()>=1
    assert page.get_by_text('Python Analytics',exact=True).count()>=1
    assert_sticky(page)
    footer_links=page.locator('.footer-bottom-links a')
    assert footer_links.count()==1
    assert footer_links.first.inner_text().strip()=='About'
    assert page.locator('.footer-bottom-links a[href*="tafshir027"]').count()==0
    page.evaluate('window.scrollTo(0,0)')
    page.wait_for_timeout(100)
    page.screenshot(path=str(SCREENSHOTS/'home-desktop.png'),full_page=False)

    print('stage tutorials',flush=True)
    load(page,'tutorials/index.html','tutorials')
    page.wait_for_selector('.subject-course-card.published')
    assert page.locator('.subject-course-card.published').count()==5
    assert page.get_by_text('Excel for Data Analytics',exact=True).count()>=1

    print('stage excel course',flush=True)
    load(page,'tutorials/excel-data-analytics/index.html','tutorial-course')
    page.wait_for_selector('.tutorial-index-card')
    assert page.locator('.tutorial-index-card').count()==56
    assert page.locator('.tutorial-index-module').count()==8
    assert page.get_by_text('Welcome to Excel for Data Analytics',exact=True).count()>=1
    assert page.get_by_role('link',name=re.compile('Practice Workbook')).count()>=1
    assert_sticky(page)
    page.evaluate('window.scrollTo(0,0)')
    page.wait_for_timeout(100)
    page.screenshot(path=str(SCREENSHOTS/'excel-course-desktop.png'),full_page=False)

    print('stage excel chapter',flush=True)
    load(page,'tutorials/excel-data-analytics/xlookup/index.html','tutorial-chapter')
    page.wait_for_selector('#tutorial-activity .try-panel')
    assert page.get_by_text('XLOOKUP',exact=True).count()>=1
    assert page.locator('.formula-block code').filter(has_text='XLOOKUP').count()>=1
    assert page.locator('.term-card').count()==4
    assert page.locator('.exercise-card').count()==3
    page.locator('[data-lookup]').select_option('P103')
    page.get_by_role('button',name='Run lookup').click()
    assert 'Trousers' in page.locator('.activity-result').inner_text()
    page.get_by_role('button',name='Mark complete').first.click()
    stored=page.evaluate("localStorage.getItem('dlh-tutorial-excel-data-analytics-completed')")
    assert 'xlookup' in stored
    page.get_by_role('button',name='বাংলা').click()
    assert page.locator('html').get_attribute('lang')=='bn'
    assert 'XLOOKUP' in page.locator('h1').first.inner_text()
    page.get_by_role('button',name='English').click()
    assert_sticky(page)
    page.evaluate('window.scrollTo(0,0)')
    page.wait_for_timeout(100)
    page.screenshot(path=str(SCREENSHOTS/'excel-xlookup-desktop.png'),full_page=False)

    print('stage resources',flush=True)
    load(page,'exercises/index.html','resources')
    page.wait_for_selector('.resource-subject-card')
    assert page.locator('.resource-subject-card').count()==5
    load(page,'exercises/excel-data-analytics/index.html','tutorial-exercises')
    page.wait_for_selector('.exercise-library-section')
    assert page.locator('.exercise-library-section').count()==56
    assert page.locator('.exercise-card').count()==168
    page.locator('#exercise-chapter-filter').select_option('sumif-and-sumifs')
    assert page.locator('.exercise-library-section').count()==1

    load(page,'quiz/excel-data-analytics/index.html','tutorial-quiz')
    page.get_by_role('button',name='Start quiz').click()
    page.wait_for_selector('.quiz-question')
    assert page.locator('.quiz-question').count()==30


    print('stage sql course',flush=True)
    load(page,'tutorials/sql-data-analytics/index.html','tutorial-course')
    page.wait_for_selector('.tutorial-index-card')
    assert page.locator('.tutorial-index-card').count()==66
    assert page.locator('.tutorial-index-module').count()==9
    assert page.get_by_text('SQL for Data Analytics Tutorial',exact=True).count()>=1
    assert page.get_by_role('link',name=re.compile('SQL Playground')).count()>=1
    assert_sticky(page)
    page.evaluate('window.scrollTo(0,0)')
    page.screenshot(path=str(SCREENSHOTS/'sql-course-desktop.png'),full_page=False)

    print('stage sql chapter',flush=True)
    load(page,'tutorials/sql-data-analytics/inner-join/index.html','tutorial-sql-chapter')
    page.wait_for_selector('#tutorial-activity .sql-editor')
    assert 'JOIN' in page.locator('.sql-editor').input_value().upper()
    assert page.locator('.exercise-card').count()==3
    assert page.locator('.tutorial-chapter-link').count()==66
    assert page.get_by_role('button',name='Run query').count()==1
    assert_sticky(page)
    page.evaluate('window.scrollTo(0,0)')
    page.screenshot(path=str(SCREENSHOTS/'sql-inner-join-desktop.png'),full_page=False)

    print('stage playground',flush=True)
    load(page,'playground/sql/index.html','sql-playground')
    page.evaluate('window.DLHSQLPractice.mountStandalone()')
    page.wait_for_selector('#sql-playground-root .sql-editor')
    assert 'SELECT' in page.locator('.sql-editor').input_value().upper()
    assert page.get_by_role('button',name='Run query').count()==1

    print('stage power bi course',flush=True)
    load(page,'tutorials/power-bi-data-analytics/index.html','tutorial-course')
    page.wait_for_selector('.tutorial-index-card')
    assert page.locator('.tutorial-index-card').count()==77
    assert page.locator('.tutorial-index-module').count()==9
    assert page.get_by_text('Power BI for Data Analytics Tutorial',exact=True).count()>=1
    assert page.get_by_role('link',name=re.compile('Power BI Retail Practice Data')).count()>=1
    assert_sticky(page)
    page.evaluate('window.scrollTo(0,0)')
    page.screenshot(path=str(SCREENSHOTS/'power-bi-course-desktop.png'),full_page=False)

    print('stage power bi chapter',flush=True)
    load(page,'tutorials/power-bi-data-analytics/dax-overview/index.html','tutorial-chapter')
    page.wait_for_selector('#tutorial-activity .powerbi-sim')
    assert page.locator('.tutorial-chapter-link').count()==77
    assert page.locator('.exercise-card').count()==3
    assert page.get_by_role('button',name='Run simulation').count()==1
    page.get_by_role('button',name='Run simulation').click()
    assert page.locator('.activity-result').inner_text().strip()!=''
    page.get_by_role('button',name='Mark complete').first.click()
    stored=page.evaluate("localStorage.getItem('dlh-tutorial-power-bi-data-analytics-completed')")
    assert 'dax-overview' in stored
    page.get_by_role('button',name='বাংলা').click()
    assert page.locator('html').get_attribute('lang')=='bn'
    page.get_by_role('button',name='English').click()
    assert_sticky(page)
    page.evaluate('window.scrollTo(0,0)')
    page.screenshot(path=str(SCREENSHOTS/'power-bi-dax-overview-desktop.png'),full_page=False)

    load(page,'exercises/power-bi-data-analytics/index.html','tutorial-exercises')
    page.wait_for_selector('.exercise-library-section')
    assert page.locator('.exercise-library-section').count()==77
    assert page.locator('.exercise-card').count()==231
    load(page,'quiz/power-bi-data-analytics/index.html','tutorial-quiz')
    page.get_by_role('button',name='Start quiz').click()
    page.wait_for_selector('.quiz-question')
    assert page.locator('.quiz-question').count()==30

    print('stage python course',flush=True)
    load(page,'tutorials/python-data-analytics/index.html','tutorial-course')
    page.wait_for_selector('.tutorial-index-card')
    assert page.locator('.tutorial-index-card').count()==94
    assert page.locator('.tutorial-index-module').count()==9
    assert page.get_by_text('Python for Data Analytics Tutorial',exact=True).count()>=1
    assert page.get_by_role('link',name=re.compile('Python Retail Practice Package')).count()>=1
    assert page.locator('a[href="/playground/python/"]').count()>=1
    assert_sticky(page)
    page.evaluate('window.scrollTo(0,0)')
    page.screenshot(path=str(SCREENSHOTS/'python-course-desktop.png'),full_page=False)

    print('stage python chapter',flush=True)
    load(page,'tutorials/python-data-analytics/groupby-and-aggregation/index.html','tutorial-python-chapter')
    page.wait_for_selector('#tutorial-activity .python-editor')
    assert page.locator('.tutorial-chapter-link').count()==94
    assert page.locator('.exercise-card').count()==3
    assert 'groupby' in page.locator('.python-editor').input_value().lower()
    assert page.get_by_role('button',name='Run Python').count()==1
    page.get_by_role('button',name='Mark complete').first.click()
    stored=page.evaluate("localStorage.getItem('dlh-tutorial-python-data-analytics-completed')")
    assert 'groupby-and-aggregation' in stored
    page.get_by_role('button',name='বাংলা').click()
    assert page.locator('html').get_attribute('lang')=='bn'
    page.get_by_role('button',name='English').click()
    assert_sticky(page)
    page.evaluate('window.scrollTo(0,0)')
    page.screenshot(path=str(SCREENSHOTS/'python-groupby-desktop.png'),full_page=False)

    load(page,'exercises/python-data-analytics/index.html','tutorial-exercises')
    page.wait_for_selector('.exercise-library-section')
    assert page.locator('.exercise-library-section').count()==94
    assert page.locator('.exercise-card').count()==282
    load(page,'quiz/python-data-analytics/index.html','tutorial-quiz')
    page.get_by_role('button',name='Start quiz').click()
    page.wait_for_selector('.quiz-question')
    assert page.locator('.quiz-question').count()==30

    print('stage python playground',flush=True)
    load(page,'playground/python/index.html','python-playground')
    page.evaluate("window.DLHPythonPractice.renderStandalone(document.getElementById(\'python-playground-root\'))")
    page.wait_for_selector('#python-playground-root .python-editor')
    assert 'pandas' in page.locator('.python-editor').input_value().lower()
    assert page.get_by_role('button',name='Run Python').count()==1
    page.screenshot(path=str(SCREENSHOTS/'python-playground-desktop.png'),full_page=False)

    print('stage regression',flush=True)
    # Regression: the old Data Foundations course and a retained statistical lab still use the sticky shared header.
    load(page,'tutorials/data-foundations/data-and-statistics/index.html','tutorial-chapter')
    page.wait_for_selector('#tutorial-activity .try-panel')
    assert page.locator('.tutorial-chapter-link').count()==21
    assert_sticky(page)
    load(page,'tools/summary-statistics/index.html','tool')
    page.wait_for_selector('.site-header')
    assert_sticky(page)

    print('stage mobile',flush=True)
    mobile=browser.new_page(viewport={'width':390,'height':844})
    load(mobile,'tutorials/python-data-analytics/groupby-and-aggregation/index.html','tutorial-python-chapter')
    mobile.wait_for_selector('#tutorial-activity .python-editor')
    assert mobile.locator('#tutorial-drawer-open').is_visible()
    mobile.locator('#tutorial-drawer-open').click(force=True)
    assert mobile.locator('[data-chapter-link]').count()==94
    mobile.screenshot(path=str(SCREENSHOTS/'python-groupby-mobile.png'),full_page=False)
    mobile.close()
    context.close()
    browser.close()
  print('Browser smoke test passed for sticky headers, five-course tutorial navigation, 56-chapter Excel, 66-chapter SQL, 77-chapter Power BI, 94-chapter Python, SQL and Python playground UIs, Power BI simulations, bilingual state, exercises, quizzes, retained Data Foundations, statistical lab, footer adjustments, and mobile drawer.')

if __name__=='__main__': main()
