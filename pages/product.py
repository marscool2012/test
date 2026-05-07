from selenium.webdriver.common.by import By


class ProdustPage:
    def __init__(self, browser):
        self.browser = browser

    def check_titile_is(self, title):
        page_title = self.browser.find_element(By.CSS_SELECTOR, "h2")
        assert page_title.text == title
