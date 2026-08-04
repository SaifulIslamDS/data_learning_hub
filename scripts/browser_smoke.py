from __future__ import annotations

import re
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
SCREENSHOTS = ROOT / "docs" / "screenshots-v1.2.0"
SCREENSHOTS.mkdir(parents=True, exist_ok=True)


def static_html(slug: str = "statistics-and-data") -> str:
    html = (ROOT / "topics" / slug / "index.html").read_text(encoding="utf-8")
    html = re.sub(r'<link rel="(?:icon|manifest|preconnect)"[^>]*>', '', html)
    html = re.sub(r'<link rel="stylesheet"[^>]*>', '', html)
    html = re.sub(r'<script[^>]*src="[^"]+"[^>]*></script>', '', html)
    return html


def add_assets(page) -> None:
    css = (ROOT / "assets" / "css" / "main.css").read_text(encoding="utf-8")
    page.evaluate("css => { const s = document.createElement('style'); s.textContent = css; document.head.appendChild(s); }", css)
    for path in [
        ROOT / "assets" / "js" / "theme-init.js",
        ROOT / "assets" / "js" / "content.js",
        ROOT / "assets" / "js" / "site.js",
        ROOT / "assets" / "js" / "topic.js",
    ]:
        page.evaluate(path.read_text(encoding="utf-8"))



def smoke_topic(context, slug: str, expected_title: str, expected_scenario: str, expected_type: str) -> None:
    page = context.new_page()
    page.set_default_timeout(30000)
    page.set_content(static_html(slug), wait_until="domcontentloaded")
    add_assets(page)
    page.wait_for_selector(".lesson-phase-nav")
    assert page.locator("h1").first.inner_text().strip() == expected_title
    assert page.locator(".lesson-phase-nav a").count() == 4
    assert page.locator(".concept-card").count() >= 3
    assert page.get_by_text(expected_scenario, exact=True).count() == 1
    assert page.locator(".meta-row").filter(has_text="Lesson type").get_by_text(expected_type, exact=True).count() == 1
    page.close()

def main() -> None:
    html = static_html()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, executable_path="/usr/bin/chromium", args=["--no-sandbox"])
        context = browser.new_context(viewport={"width": 1440, "height": 1100}, device_scale_factor=1)
        page = context.new_page()
        page.set_default_timeout(30000)
        page.set_content(html, wait_until="domcontentloaded")
        add_assets(page)
        page.wait_for_selector(".lesson-phase-nav")

        assert page.locator("h1").first.inner_text().strip() == "Statistics and Data"
        assert page.locator(".lesson-phase-nav a").count() == 4
        assert page.locator(".concept-card").count() >= 4
        assert page.get_by_text("Data", exact=True).count() >= 1
        assert page.get_by_text("Statistics", exact=True).count() >= 1
        assert page.get_by_text("A week of shop sales", exact=True).count() == 1
        assert page.locator(".implementation-card").count() >= 2
        assert page.locator(".quiz-option").count() == 3

        page.screenshot(path=str(SCREENSHOTS / "statistics-and-data-desktop.png"), full_page=False)

        page.locator(".quiz-option input").nth(0).check()
        page.get_by_role("button", name="Check answer").click()
        assert "Correct" in page.locator("#quiz-feedback").inner_text()

        page.get_by_role("button", name="বাংলা").click()
        assert page.locator("h1").first.inner_text().strip() == "পরিসংখ্যান ও ডেটা"
        assert page.get_by_text("এক সপ্তাহের দোকান বিক্রি", exact=True).count() == 1

        page.get_by_role("button", name="English").click()
        page.locator('[data-action="theme"]').first.click()
        assert page.locator("html").get_attribute("data-theme") == "dark"

        mobile = context.new_page()
        mobile.set_viewport_size({"width": 390, "height": 844})
        mobile.set_default_timeout(30000)
        mobile.set_content(html, wait_until="domcontentloaded")
        add_assets(mobile)
        mobile.wait_for_selector(".lesson-phase-nav")
        assert mobile.locator(".lesson-phase-nav a").count() == 4
        mobile.screenshot(path=str(SCREENSHOTS / "statistics-and-data-mobile.png"), full_page=False)
        mobile.close()

        smoke_topic(context, "variance-and-standard-deviation", "Variance and Standard Deviation", "Daily demand variability", "formula")
        smoke_topic(context, "hypothesis-testing-framework", "Hypothesis Testing Framework", "Checking a filling machine", "method")
        smoke_topic(context, "etl-and-elt", "ETL and ELT", "Building a governed transformation flow", "workflow")

        browser.close()
    print("Browser smoke test passed for comprehensive lesson UX, language toggle, quiz, theme and mobile rendering.")


if __name__ == "__main__":
    main()
