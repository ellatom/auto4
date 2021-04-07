from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    USERNAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    BTN_LOGIN = (By.ID, 'login-button')
    INVENTORY_DROPDOWN = (By.CLASS_NAME, 'product_sort_container')

#class AnotherPageLocators(object):