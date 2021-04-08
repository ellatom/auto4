from selenium import webdriver
import pagetest
import config
import pytest

#pytest run command:pytest -s test_all.py -m TestCase
#pytest run command:python3 -m pytest -s test_all.py -m TestCase
#website is mark
#update file pytest.init with other marks

#python3 -m pytest

def _init_driver():
    browser = pagetest.init_driver()
    return browser


@pytest.fixture   
def test_open_browser(_init_driver):
    pagetest.navigateToUrl(_init_driver)
    pagetest.timeoutById('user-name',_init_driver)
   
@pytest.fixture 
def test_login():
    #  pytest.set_trace() 
    username= pagetest.findElementById('user-name',_init_driver)
    pagetest.insertText(username, config.user)
    password= pagetest.findElementById('password',_init_driver)
    pagetest.insertText(password,config.password) 

class TestClass:
    def test_order(self, _init_driver, test_open_browser,test_login):
        assert order == ["_init_driver", "test_open_browser","test_login"]




# #pagetest.timeoutByClass('product_sort_container',browser)

# pagetest.dropdownOptions('product_sort_container','hilo',browser)


# inventory_container = pagetest.findElementById('inventory_container',browser)
# inventory_container.find_elements_by_css_selector(config.add_to_cart)[0].click()
# assert inventory_container.find_elements_by_css_selector(config.add_to_cart)[0].text == "REMOVE"
# print("highest added")

# pagetest.dropdownOptions('product_sort_container','lohi',browser)
# # select by value -lowest


# inventory_container = pagetest.findElementById('inventory_container',browser)
# inventory_prices =inventory_container.find_elements_by_css_selector(config.inventory_prices)

# prices_list = pagetest.addItemPrices(inventory_prices)
    
# assert pagetest.is_sorted(prices_list) == True
# print("as expected sorted lowest to highest")



# inventory_container.find_elements_by_css_selector(config.add_to_cart)[0].click()
# assert inventory_container.find_elements_by_css_selector(config.add_to_cart)[0].text == "REMOVE"
# print("lowest added")

# cart_items =browser.find_elements_by_css_selector(config.cart_items)[0].text
# assert cart_items == '2'
# print("added 2 items to cart")


# cart_icon =browser.find_elements_by_css_selector(config.cart_icon)[0]
# cart_icon.click()

# highest_product_remove = browser.find_element_by_css_selector(config.highest_product_remove).click()

# cart_items =browser.find_elements_by_css_selector(config.cart_items)[0].text
# assert cart_items == '1'
# print("removed 1 items from cart")

# checkout_btn = browser.find_elements_by_css_selector(config.checkout_btn)[0].click()

# firstname = pagetest.findElementByCSS('#first-name',browser)
# lastname = pagetest.findElementByCSS('#last-name',browser)
# postalcode = pagetest.findElementByCSS('#postal-code',browser)

# pagetest.insertText(firstname,"Ella")
# pagetest.insertText(lastname,"Tomilin")
# pagetest.insertText(postalcode,"421")

# pagetest.timeoutByCSS(config.summary_cart,browser)


# sum_total = pagetest.findElementByCSS(config.sum_totals,browser).text
# assert sum_total.split("$")[1] == config.expected_price
# print("as expected price 7.99")

# quantity = pagetest.findElementByCSS(config.quantity,browser).text    
# assert quantity == "1"
# print("as expected quantity 1")


# finish_btn = pagetest.findElementByCSS(config.finish_btn,browser).click()

# finish_order_msg = pagetest.findElementByCSS(config.finish_order,browser).text
# assert finish_order_msg == config.finish_order_msg
# print("message order dispatched as expected")

# pagetest.closeBrowser(browser)

