import sys  
sys.path += ['/utils','/pages','/tests'] 

from utils import config 
from pages.login_page import LoginPage
from tests.base_test import BaseTest
from tests import test_cases

import unittest

# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class TestLoginInPage(BaseTest):

    def test_sign_in_with_valid_user(self):
        # print("\n" + str(test_cases[1]))
        login_page = LoginPage(self.driver,config.url)
        result = login_page.login_with_valid_user("standard_user")
        self.assertIn("1", "1")
    
    # def test_dropdown(self):
    #     pagetest.dropdownOptions('product_sort_container','hilo',self.driver)


