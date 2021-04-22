import sys

sys.path += ['/utils', '/pages', '/tests']

from utils import config
from pages.login_page import LoginPage
from tests.base_test import BaseTest
from tests import test_cases

import unittest

# If you want to run it, you should type: python <module-name.py>

class TestLoginInPage(BaseTest):

    def test_sign_in_with_valid_user(self):
        # print("\n" + str(test_cases[1]))
        login_page = LoginPage(self.driver, config.url)
        result = login_page.login_with_user("standard_user")
        self.assertEqual(result, True)

    def test_sign_in_with_invalid_user(self):
    #     # print("\n" + str(test_cases[1]))
        login_page = LoginPage(self.driver,config.url)
        result = login_page.login_with_user("standard_user1")
        self.assertEqual(result,False)
