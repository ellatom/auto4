import sys

sys.path += ['/utils', '/pages']
from utils.locators import LoginPageLocators
from pages.base_page import BasePage
from utils import users
import time


class LoginPage(BasePage):
    def __init__(self, driver, base_url):

        self.locator = LoginPageLocators
        super().__init__(driver, base_url)

    def enter_username(self, username):
        self.find_element(*self.locator.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.find_element(*self.locator.PASSWORD).send_keys(password)

    def click_btn_login(self):
        self.find_element(*self.locator.BTN_LOGIN).click()

    def timeout_to_load(self):
        self.timeoutLoad(*self.locator.INVENTORY_DROPDOWN)

    def login(self, username) -> bool:
        try:
            user = users.get_user(username)
            self.enter_username(user["username"])
            self.enter_password(user["password"])
            self.click_btn_login()
            time.sleep(10)
            # self.timeout_to_load()
            return True
        except:
            return False

    def login_with_user(self, user) -> bool:
        result = self.login(user)
        return result
