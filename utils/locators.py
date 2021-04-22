from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    USERNAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    BTN_LOGIN = (By.ID, 'login-button')
    INVENTORY_DROPDOWN = (By.CLASS_NAME, 'product_sort_container')


class InventoryPageLocators(object):
    HighestToLowestDropdownOption = (By.CLASS_NAME, 'product_sort_container')
    INVENTORY_CONTAINER = (By.ID, 'inventory_container')
    INVENTORY_CONTAINER_HighestItem = (By.CSS_SELECTOR, '#inventory_container > div > div:nth-child(1) > div.inventory_item_description > div.pricebar>button')
