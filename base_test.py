import unittest
from selenium import webdriver
from base_page import BasePage
import config

#python -m unittest
# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>
class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(config.url)
        

    def tearDown(self):
        self.driver.close()
        pass
        

if __name__  ==  "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLoginInPage)
    unittest.TextTestRunner(verbosity=1).run(suite)

