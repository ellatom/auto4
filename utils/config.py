
url= "https://www.saucedemo.com/"
timeout =10
user = "standard_user"
password = "secret_sauce"
finish_order_msg ="Your order has been dispatched, and will arrive just as fast as the pony can get there!"
finish_order = '#checkout_complete_container > div'
finish_btn ='#checkout_summary_container > div > div.summary_info > div.cart_footer > a.btn_action.cart_button'
quantity = '#checkout_summary_container > div > div.cart_list > div.cart_item > div.summary_quantity'
sum_totals ='#checkout_summary_container > div > div.summary_info > div.summary_subtotal_label'
checkout_btn='#cart_contents_container > div > div.cart_footer > a.btn_action.checkout_button'
cart_items='#shopping_cart_container > a > span'
highest_product_remove='#cart_contents_container > div > div.cart_list > div:nth-child(3) > div.cart_item_label > div.item_pricebar > button'
cart_icon ='#shopping_cart_container > a'
inventory_prices='#inventory_container > div > div:nth-child(n) > div.pricebar > div'
add_to_cart='#inventory_container > div > div:nth-child(1) > div.pricebar > button'
summary_cart='#checkout_summary_container > div > div.cart_list > div.cart_item > div.summary_quantity'
expected_price='7.99'