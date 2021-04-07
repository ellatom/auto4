from locators import *

from base_page import BasePage
import config
import users

class LoginPage(BasePage):
    def __init__(self, driver,base_url):
        
        self.locator = LoginPageLocators
        super().__init__(driver,base_url)

    def enter_username(self, username):
        self.find_element(*self.locator.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.find_element(*self.locator.PASSWORD).send_keys(password)
    
    def click_btn_login(self):
        self.find_element(*self.locator.BTN_LOGIN).click()
    
    def timeout_to_load(self):
        self.find_element(*self.locator.INVENTORY_DROPDOWN)

    def login(self,username):
        user = users.get_user(username)
        self.enter_username(user["username"])
        self.enter_password(user["password"])
        self.click_btn_login()
        # self.timeout_to_load()
    
    def login_with_valid_user(self, user):
        self.login(user)
        return LoginPage(self.driver,self.base_url)
