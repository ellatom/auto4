
import config

class BasePage(object):
    def __init__(self, driver,base_url):
        self.base_url = base_url
        self.driver = driver
    
    def find_element(self, *locator):
        return self.driver.find_element(*locator)
        
    def navigateToUrl(self,driver):
        self.driver.get(config.url)