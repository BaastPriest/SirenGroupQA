import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

link = "https://hb-eta.stage.sirenltd.dev/"

@pytest.yield_fixture(scope='session')
def browser():
    "pytest fixture for browser"
    print("\nstart browser for test...")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser...")
    driver.quit()

@pytest.fixture(scope='session')
def wait_element(my_locator):
    "Wait element"
    delay = 7
    try:
        WebDriverWait(browser, delay).until(expected_conditions.visibility_of_element_located(my_locator))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")
