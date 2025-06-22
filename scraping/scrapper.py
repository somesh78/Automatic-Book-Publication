from playwright.sync_api import sync_playwright

def fetch_chapter(url: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")
        content = page.inner_text("body")
        img_bytes = page.screenshot(full_page=True)
        browser.close()
        return content, img_bytes
