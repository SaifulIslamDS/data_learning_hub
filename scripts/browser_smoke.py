from __future__ import annotations

import re
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
SCREENSHOTS = ROOT / "docs" / "screenshots-v2.0.0"
SCREENSHOTS.mkdir(parents=True, exist_ok=True)

SCRIPT_MAP = {
    "home": [],
    "start": ["start.js"],
    "learn": ["catalog.js"],
    "curriculum": ["curriculum.js"],
    "projects": ["projects.js"],
    "topic": ["topic.js"],
}


def stripped_html(relative: str) -> str:
    html = (ROOT / relative).read_text(encoding="utf-8")
    html = re.sub(r'<link rel="(?:icon|manifest|preconnect)"[^>]*>', '', html)
    html = re.sub(r'<link rel="stylesheet"[^>]*>', '', html)
    html = re.sub(r'<script[^>]*src="[^"]+"[^>]*></script>', '', html)
    return html


def install_storage(page, initial: dict[str, str] | None = None) -> None:
    initial = initial or {}
    page.evaluate("""initial => {
      const store = new Map(Object.entries(initial));
      Object.defineProperty(window, 'localStorage', {
        configurable: true,
        value: {
          getItem: key => store.has(String(key)) ? store.get(String(key)) : null,
          setItem: (key, value) => store.set(String(key), String(value)),
          removeItem: key => store.delete(String(key)),
          clear: () => store.clear(),
          key: index => Array.from(store.keys())[index] ?? null,
          get length() { return store.size; }
        }
      });
    }""", initial)


def inject(page, page_type: str, initial_storage: dict[str, str] | None = None) -> None:
    install_storage(page, initial_storage)
    css = (ROOT / "assets/css/main.css").read_text(encoding="utf-8")
    page.evaluate("css => { const style=document.createElement('style'); style.textContent=css; document.head.appendChild(style); }", css)
    for filename in ["theme-init.js", "content.js", "site.js", *SCRIPT_MAP.get(page_type, [])]:
        page.evaluate((ROOT / "assets/js" / filename).read_text(encoding="utf-8"))


def load(page, relative: str, page_type: str, storage: dict[str, str] | None = None) -> None:
    page.set_content(stripped_html(relative), wait_until="domcontentloaded")
    inject(page, page_type, storage)


def main() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, executable_path="/usr/bin/chromium", args=["--no-sandbox"])
        context = browser.new_context(viewport={"width": 1440, "height": 1000}, device_scale_factor=1)
        page = context.new_page()
        page.set_default_timeout(30000)

        legacy = {
            "slh-theme": "dark",
            "slh-language": "bn",
            "slh-completed": '["statistics-and-data"]',
            "slh-profile": '{"goal":"data-analyst","level":"beginner","mode":"balanced"}',
        }
        load(page, "index.html", "home", legacy)
        page.wait_for_selector(".site-header")
        assert page.locator("html").get_attribute("data-theme") == "dark"
        assert page.locator("html").get_attribute("lang") == "bn"
        assert page.evaluate("localStorage.getItem('dlh-theme')") == "dark"
        assert page.evaluate("localStorage.getItem('slh-theme')") == "dark"
        assert "statistics-and-data" in page.evaluate("localStorage.getItem('dlh-completed')")
        page.get_by_role("button", name="English").click()
        assert "Data Analyst" in page.locator("h1").first.inner_text()
        assert page.get_by_text("Excel for Data Analytics", exact=True).count() >= 1
        page.screenshot(path=str(SCREENSHOTS / "home-desktop.png"), full_page=False)

        load(page, "start/index.html", "start")
        page.wait_for_selector("#guide-wizard .choice-card")
        assert page.get_by_text("What are you learning for?", exact=True).count() == 1
        assert page.locator(".choice-card").count() == 2
        page.screenshot(path=str(SCREENSHOTS / "guided-setup-desktop.png"), full_page=False)

        load(page, "learn/index.html", "learn")
        page.wait_for_selector("#catalog-grid .lesson-card")
        assert page.locator(".learning-domain-card").count() >= 2
        assert page.locator("#catalog-grid .lesson-card").count() > 0
        assert page.get_by_text("Curriculum ready", exact=False).count() >= 1

        load(page, "curriculum/index.html", "curriculum")
        page.wait_for_selector(".curriculum-track")
        assert page.locator(".curriculum-track").count() == 4
        assert page.get_by_text("Excel for Data Analytics", exact=True).count() == 1
        assert page.get_by_text("SQL for Data Analytics", exact=True).count() == 1
        assert page.get_by_text("No planned lesson is presented as already published.", exact=True).count() == 1
        page.screenshot(path=str(SCREENSHOTS / "curriculum-desktop.png"), full_page=False)

        load(page, "projects/index.html", "projects")
        page.wait_for_selector(".project-card")
        assert page.get_by_text("Retail Sales Foundations Project", exact=True).count() == 1
        assert page.locator(".dataset-card").count() == 3

        # Project detail is generated HTML and needs only the shared shell.
        load(page, "projects/retail-sales-foundations/index.html", "project")
        page.wait_for_selector(".project-shell")
        assert page.get_by_text("Retail Sales Foundations Project", exact=True).count() >= 1
        assert page.get_by_role("link", name="Download CSV").count() == 1

        load(page, "topics/statistics-and-data/index.html", "topic")
        page.wait_for_selector(".lesson-phase-nav")
        assert page.locator(".lesson-phase-nav a").count() == 4
        assert page.get_by_text("A week of shop sales", exact=True).count() == 1
        assert page.locator(".quiz-option").count() == 3

        mobile = browser.new_page(viewport={"width": 390, "height": 844})
        load(mobile, "index.html", "home")
        mobile.wait_for_selector(".site-header")
        assert mobile.locator(".menu-button").count() == 1
        mobile.screenshot(path=str(SCREENSHOTS / "home-mobile.png"), full_page=False)
        mobile.close()

        browser.close()
    print("Browser smoke test passed for v2 identity, v1 progress migration, guided setup, learning catalog, curriculum honesty, datasets, project and comprehensive lesson UX.")


if __name__ == "__main__":
    main()
