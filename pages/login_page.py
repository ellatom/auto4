from locators import *

from base_page import BasePage
import config
from users import users

class LoginPage(BasePage):
    
    def __init__(self, driver):
        
        self.locator = LoginPageLocators
        super(LoginPage,self).__init__(driver)

    def enter_username(self, username):
        self.find_element(*self.locator.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.find_element(*self.locator.PASSWORD).send_keys(password)

    def login(self,username):
        user = users.get_user(username)
        self.enter_username(user["username"])
        self.enter_password(user["password"])
    
    def login_with_valid_user(self, user):
        self.login(user)
        return LoginPage(self.driver)
        
        # username= pagetest.findElementById('user-name',_init_driver)
        # pagetest.insertText(username, config.user)
        # password= pagetest.findElementById('password',_init_driver)
        # pagetest.insertText(password,config.password) 

