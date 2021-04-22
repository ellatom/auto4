import sys
sys.path += ['/utils', '/pages']

import time
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from utils.locators import InventoryPageLocators


class InventoryPage(BasePage):

    def __init__(self, driver, base_url):
        self.locator = InventoryPageLocators
        super().__init__(driver, base_url)

    # select by value -highest
    def dropdownOptionSort(self, driver,value) -> bool:
        try:
            select = Select(self.driver.find_element(*self.locator.HighestToLowestDropdownOption))
            select.select_by_value(value)
            return True
        except Exception as err:
            print("dropdown option not found")
            return False

    def addProductToCart(self, driver) -> str:
        try:
            inventory_container = self.driver.find_element(*self.locator.INVENTORY_CONTAINER)
            inventory_container.find_elements(*self.locator.INVENTORY_CONTAINER_HighestItem)[0].click()
            time.sleep(10)
            return inventory_container.find_elements(*self.locator.INVENTORY_CONTAINER_HighestItem)[0].text 
        except Exception as err:
            return "adding highest price failed"
