from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    webkit = playwright.webkit
    browser = webkit.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.youtube.com/@LCKglobal/live')
    redirect = page.url
    print(redirect)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
