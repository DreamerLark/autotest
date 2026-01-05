from __future__ import annotations

from playwright.sync_api import sync_playwright

from ui_click_tests.html_samples import COUNTER_APP_HTML


def main() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 900, "height": 700})
        page = context.new_page()

        page.set_content(COUNTER_APP_HTML)

        page.click("#inc")
        page.click("#inc")
        page.click("#dec")
        page.check("#agree")
        page.click("#toggle")

        page.wait_for_timeout(1500)

        context.close()
        browser.close()


if __name__ == "__main__":
    main()
