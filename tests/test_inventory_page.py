import sys
sys.path += ['/utils', '/pages', '/tests']

from utils import config
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from tests.base_test import BaseTest
import time

# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class TestInventoryPage(BaseTest):

    def test_addItemsToCart(self):
        login_page = LoginPage(self.driver, config.url)
        result = login_page.login_with_user("standard_user")

        inventory_page = InventoryPage(self.driver, config.url)
        result = inventory_page.dropdownOptionSort(self.driver,config.dropdownOptionSortHighestToLowest)
        time.sleep(10)
        self.assertEqual(result, True,"dropdown option available")
        
        result = inventory_page.addProductToCart(self.driver)
        print("result: "+result)
        self.assertEqual(result, "REMOVE", "added highest price product to cart")
        
        
        result = inventory_page.dropdownOptionSort(self.driver,config.dropdownOptionSortLowestToHeighst)
        time.sleep(10)
        self.assertEqual(result, True)
        
        result = inventory_page.addProductToCart(self.driver)
        self.assertEqual(result, "REMOVE", "added lowest price product to cart")
    
    # def addProductTocart(inventory_page,self.driver,optionDropdownSelector):
    #     result = inventory_page.DropdownOptionSortHighestToLowest(self.driver, config.dropdownOptionSortHighestToLowest)
    #     time.sleep(10)
    #     self.assertEqual(result, True)
        
    #     result = inventory_page.AddHighestPriceProductToCart(self.driver)
    #     self.assertEqual(result, "REMOVE", "added highest price product to cart")

    # def test_addHighestPriceProductToCart(self):
    #     login_page = LoginPage(self.driver, config.url)
    #     result = login_page.login_with_user("standard_user")
    #     self.assertEqual(result, True, "login success")

    #     inventory_page = InventoryPage(self.driver, config.url)
    #     result = inventory_page.DropdownOptionSortHighestToLowest(self.driver, config.dropdownOptionSortHighestToLowest)
    #     self.assertEqual(result, True, "sorted high to low price")

    #     result = inventory_page.AddHighestPriceProductToCart(self.driver)
    #     self.assertEqual(result, "REMOVE", "added highest price product to cart")

    