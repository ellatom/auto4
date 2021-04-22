import sys

sys.path += ['/utils', '/tests']

# from tests.test_sign_in_page import TestLoginInPage

from utils import config
from unittest import TestLoader, TestSuite, TextTestRunner, TestCase
from selenium import webdriver


# python -m unittest #I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>
class BaseTest(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(config.url)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    # # run more than 1 test
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(TestLoginInPage),
        # loader.loadTestsFromTestCase(TestInventoryPage)
    ))
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)

    # suite = unittest.TestLoader().loadTestsFromTestCase(TestInventoryPage)
    # unittest.TextTestRunner(verbosity=2).run(suite)
