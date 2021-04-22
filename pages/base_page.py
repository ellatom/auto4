import sys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
sys.path.insert(0, '/utils')
from utils import config


class BasePage(object):
    def __init__(self, driver, base_url=config.url):
        self.base_url = base_url
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def timeoutLoad(self, *locator):
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'product_sort_container'))#HighestToLowestDropdownOption
            return WebDriverWait(self.driver, config.timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
            return print("Time out")
