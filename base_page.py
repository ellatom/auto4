
import config

# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

class BasePage(object):
    def __init__(self, driver,base_url=config.url):
        self.base_url = base_url
        self.driver = driver
    
    def find_element(self, *locator):
        return self.driver.find_element(*locator)
    
    # def timeoutById(self, *locator):
    #     timeout = config.timeout
    #     try:
    #         element_present = EC.presence_of_element_located(*locator)
    #         WebDriverWait(self.driver, timeout).until(element_present)
    #     except TimeoutException:
    #         print("Timed out waiting for page to load")
        