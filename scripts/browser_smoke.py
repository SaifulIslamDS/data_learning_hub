from __future__ import annotations
import re
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
SCREENSHOTS=ROOT/'docs'/'screenshots-v2.1.0'
SCREENSHOTS.mkdir(parents=True,exist_ok=True)
SCRIPT_MAP={
 'home':[], 'tutorials':[],
 'tutorial-course':['tutorial-core.js','tutorial-index.js'],
 'tutorial-chapter':['tutorial-core.js','tutorial.js'],
 'tutorial-exercises':['tutorial-core.js','tutorial-exercises.js'],
 'tutorial-quiz':['tutorial-core.js','tutorial-quiz.js'],
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

def main():
  with sync_playwright() as p:
    browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
    context=browser.new_context(viewport={'width':1440,'height':1000},device_scale_factor=1)
    page=context.new_page(); page.set_default_timeout(30000)

    load(page,'index.html','home',{'dlh-language':'en','dlh-theme':'light'})
    page.wait_for_selector('.site-header')
    assert page.get_by_role('link',name='Tutorials',exact=True).count()==1
    assert 'Learn the subject here' in page.locator('h1').first.inner_text()
    assert page.get_by_text('21 complete chapters',exact=True).count()==1
    page.screenshot(path=str(SCREENSHOTS/'home-desktop.png'),full_page=False)

    load(page,'tutorials/index.html','tutorials')
    page.wait_for_selector('.subject-course-card.published')
    assert page.get_by_text('Data Foundations Tutorial',exact=True).count()>=1
    assert page.get_by_text('Complete learning content available now.',exact=True).count()==1

    load(page,'tutorials/data-foundations/index.html','tutorial-course')
    page.wait_for_selector('.tutorial-index-card')
    assert page.locator('.tutorial-index-card').count()==21
    assert page.get_by_text('Welcome to Data Analytics',exact=True).count()>=1
    page.screenshot(path=str(SCREENSHOTS/'data-foundations-course-desktop.png'),full_page=False)

    load(page,'tutorials/data-foundations/data-and-statistics/index.html','tutorial-chapter')
    page.wait_for_selector('#tutorial-activity .try-panel')
    assert page.get_by_text('What is data?',exact=True).count()==1
    assert page.get_by_text('What is statistics?',exact=True).count()==1
    assert page.locator('.term-card').count()==4
    assert page.locator('.worked-steps li').count()==4
    assert page.locator('.exercise-card').count()==3
    page.locator('.classify-row select').nth(0).select_option('data')
    page.locator('.classify-row select').nth(1).select_option('descriptive')
    page.locator('.classify-row select').nth(2).select_option('inference')
    page.get_by_role('button',name='Check classification').click()
    assert '3/3' in page.locator('.activity-result').inner_text()
    page.get_by_role('button',name='Mark complete').first.click()
    assert 'data-and-statistics' in page.evaluate("localStorage.getItem('dlh-tutorial-data-foundations-completed')")
    page.get_by_role('button',name='বাংলা').click()
    assert page.locator('html').get_attribute('lang')=='bn'
    assert 'ডেটা ও স্ট্যাটিস্টিকস' in page.locator('h1').first.inner_text()
    page.get_by_role('button',name='English').click()
    page.screenshot(path=str(SCREENSHOTS/'data-and-statistics-desktop.png'),full_page=False)

    load(page,'exercises/data-foundations/index.html','tutorial-exercises')
    page.wait_for_selector('.exercise-library-section')
    assert page.locator('.exercise-library-section').count()==21
    assert page.locator('.exercise-card').count()==63
    page.locator('#exercise-chapter-filter').select_option('measurement-scales')
    assert page.locator('.exercise-library-section').count()==1

    load(page,'quiz/data-foundations/index.html','tutorial-quiz')
    page.get_by_role('button',name='Start quiz').click()
    page.wait_for_selector('.quiz-question')
    assert page.locator('.quiz-question').count()==30

    mobile=browser.new_page(viewport={'width':390,'height':844})
    load(mobile,'tutorials/data-foundations/data-and-statistics/index.html','tutorial-chapter')
    mobile.wait_for_selector('#tutorial-activity .try-panel')
    assert mobile.locator('#tutorial-drawer-open').is_visible()
    mobile.locator('#tutorial-drawer-open').click()
    assert mobile.locator('#tutorial-sidebar').get_attribute('class').find('open')>=0
    assert mobile.locator('[data-chapter-link]').count()==21
    mobile.screenshot(path=str(SCREENSHOTS/'data-and-statistics-mobile.png'),full_page=False)
    mobile.close(); browser.close()
  print('Browser smoke test passed for tutorial-first homepage, 21-chapter course, bilingual chapter content, activity, exercises, progress, final quiz and mobile drawer.')

if __name__=='__main__': main()
