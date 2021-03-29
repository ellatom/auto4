# from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pagetest
import config


browser = pagetest.init_driver()
pagetest.navigateToUrl(browser)

pagetest.timeoutById('user-name',browser)
    
username= pagetest.findElementById('user-name',browser)
pagetest.insertText(username, config.user)


password= pagetest.findElementById('password',browser)
pagetest.insertText(password,config.password)


pagetest.timeoutByClass('product_sort_container',browser)

pagetest.dropdownOptions('product_sort_container','hilo',browser)


inventory_container = pagetest.findElementById('inventory_container',browser)
inventory_container.find_elements_by_css_selector('#inventory_container > div > div:nth-child(1) > div.pricebar > button')[0].click()
assert inventory_container.find_elements_by_css_selector('#inventory_container > div > div:nth-child(1) > div.pricebar > button')[0].text == "REMOVE"
print("highest added")

pagetest.dropdownOptions('product_sort_container','lohi',browser)
# select by value -lowest


inventory_container = pagetest.findElementById('inventory_container',browser)
inventory_prices =inventory_container.find_elements_by_css_selector('#inventory_container > div > div:nth-child(n) > div.pricebar > div')

prices_list = pagetest.addItemPrices(inventory_prices)
    
assert pagetest.is_sorted(prices_list) == True
print("as expected sorted lowest to highest")



inventory_container.find_elements_by_css_selector('#inventory_container > div > div:nth-child(1) > div.pricebar > button')[0].click()
assert inventory_container.find_elements_by_css_selector('#inventory_container > div > div:nth-child(1) > div.pricebar > button')[0].text == "REMOVE"
print("lowest added")

cart_items =browser.find_elements_by_css_selector('#shopping_cart_container > a > span')[0].text
assert cart_items == '2'
print("added 2 items to cart")


cart_icon =browser.find_elements_by_css_selector('#shopping_cart_container > a')[0]
cart_icon.click()

highest_product_remove = browser.find_element_by_css_selector('#cart_contents_container > div > div.cart_list > div:nth-child(3) > div.cart_item_label > div.item_pricebar > button').click()

cart_items =browser.find_elements_by_css_selector('#shopping_cart_container > a > span')[0].text
assert cart_items == '1'
print("removed 1 items from cart")

checkout_btn = browser.find_elements_by_css_selector('#cart_contents_container > div > div.cart_footer > a.btn_action.checkout_button')[0].click()

firstname = pagetest.findElementByCSS('#first-name',browser)
lastname = pagetest.findElementByCSS('#last-name',browser)
postalcode = pagetest.findElementByCSS('#postal-code',browser)

pagetest.insertText(firstname,"Ella")
pagetest.insertText(lastname,"Tomilin")
pagetest.insertText(postalcode,"421")

pagetest.timeoutByCSS('#checkout_summary_container > div > div.cart_list > div.cart_item > div.summary_quantity',browser)


sum_total = pagetest.findElementByCSS('#checkout_summary_container > div > div.summary_info > div.summary_subtotal_label',browser).text
assert sum_total.split("$")[1] == '7.99'
print("as expected price 7.99")

quantity = pagetest.findElementByCSS('#checkout_summary_container > div > div.cart_list > div.cart_item > div.summary_quantity',browser).text    
assert quantity == "1"
print("as expected quantity 1")


finish_btn = pagetest.findElementByCSS('#checkout_summary_container > div > div.summary_info > div.cart_footer > a.btn_action.cart_button',browser).click()

finish_order_msg = pagetest.findElementByCSS('#checkout_complete_container > div',browser).text
assert finish_order_msg == "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
print("message order dispatched as expected")

pagetest.closeBrowser(browser)

