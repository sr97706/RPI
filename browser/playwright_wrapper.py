from playwright.sync_api import sync_playwright

class Browser:
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()

    def login(self, url, username, password):
        self.page.goto(url)

    def close(self):
        self.browser.close()
        self.playwright.stop()


