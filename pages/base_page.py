from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    def __init__(self, browser):
        self.browser = browser
        self.url = "https://hb-eta.stage.sirenltd.dev/siding"

    def go_to_site(self):
        return self.browser.get(self.url)

    def find_element(self, locator, time=20):
        return WebDriverWait(self.browser, time).until(expected_conditions.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=20):
        return WebDriverWait(self.browser, time).until(expected_conditions.presence_of_all_elements_located(locator),
                                                     message=f"Can't find elements by locator {locator}")
