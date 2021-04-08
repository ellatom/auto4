
import config
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def init_driver():
    browser = webdriver.Chrome()
    return browser

def navigateToUrl(browser):
    return browser.get(config.url)

def timeoutById(element_selector,browser):
    timeout = config.timeout
    try:
        element_present = EC.presence_of_element_located((By.ID,element_selector ))
        WebDriverWait(browser, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
        
def findElementById(id_,browser):
    element = browser().find_element_by_id(id_)
    return element

def findElementByCSS(css,browser):
     element = browser.find_element_by_css_selector(css)
     return element

def insertText(element,text):    
    element.send_keys(text)
    element.submit()
    

def timeoutByClass(element_selector,browser):

    timeout= config.timeout
    try:
        element_present = EC.presence_of_element_located((By.CLASS_NAME, element_selector ))
        WebDriverWait(browser, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")

def timeoutByCSS(element_selector,browser):

    timeout = config.timeout
    try:
        element_present = EC.presence_of_element_located((By.CSS_SELECTOR,element_selector))
        WebDriverWait(browser, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
        
def dropdownOptions(selector_name,value_o, browser):
    select = Select(browser.find_element_by_class_name(selector_name))
    # select by value -highest
    select.select_by_value(value_o)
    

def is_sorted(prices_list):
    return all(prices_list[i] <= prices_list[i+1] for i in range(len(prices_list)-1))

def addItemPrices(inventory_prices):
    prices_list = []

    for item in inventory_prices:
        prices_list.append(int(float(item.text.split("$")[1])))
        
    return prices_list

def closeBrowser(browser):
    return browser.quit()