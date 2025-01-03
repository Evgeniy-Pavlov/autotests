import random
import pytest
from selenium.webdriver.common.by import By
from src.fifth_page_object.elements.common_elements import Common_elements
from src.fifth_page_object.elements.home_page import Home_page, Product_card
from src.fifth_page_object.elements.alerts import Home_page_alerts


@pytest.mark.usefixtures('set_currencies', 'set_phone')
def test_common_elem_on_different_pages(base_url, browser, set_currencies, paths, get_phone):
    cmn_elements = Common_elements(browser, base_url)
    cmn_elements.change_path(paths)
    cmn_elements.open_page()
    currencies_dropdown = cmn_elements.check_visibility_of_element(cmn_elements.DROPDOWN_CURRENCY, 5)
    currencies_dropdown.click()
    currencies = cmn_elements.find_some_elem(cmn_elements.CURRENCIES)
    assert len(currencies) == len(set_currencies)
    inline_items = cmn_elements.find_some_elem(cmn_elements.INLINE_ITEMS)
    assert len(inline_items) == 5
    inline_items[1].click()
    register_login_items = inline_items[1].find_elements(*cmn_elements.ITEMS_LOGIN_REGISTER)
    assert len(register_login_items) == 2
    register, login = register_login_items
    assert register.get_attribute('href') == f'{base_url}/en-gb?route=account/register'
    assert login.get_attribute('href') == f'{base_url}/en-gb?route=account/login'
    wishlist = cmn_elements.check_visibility_of_element(cmn_elements.WISHLIST_URL)
    assert wishlist.get_attribute('href') == f'{base_url}/en-gb?route=account/wishlist'
    assert wishlist.get_attribute('title') == 'Wish List (0)'
    phone_elem = cmn_elements.check_visibility_of_element(cmn_elements.PHONE_NUMBER)
    assert phone_elem.text == get_phone
    assert cmn_elements.check_visibility_of_element(cmn_elements.SHOPPING_CART) == inline_items[3]
    shopping_cart_url = cmn_elements.check_visibility_of_element(cmn_elements.SHOPPING_CART_URL)
    shopping_cart_text = cmn_elements.check_visibility_of_element(cmn_elements.SHOPPING_CART_TEXT)
    assert shopping_cart_url.get_attribute('href') == f'{base_url}/en-gb?route=checkout/cart'
    assert shopping_cart_text.text == 'Shopping Cart'
    checkout_url = cmn_elements.check_visibility_of_element(cmn_elements.CHECKOUT_URL)
    checkout_text = cmn_elements.check_visibility_of_element(cmn_elements.CHECKOUT_TEXT)
    assert checkout_url.get_attribute('href') == f'{base_url}/en-gb?route=checkout/checkout'
    assert checkout_text.text == 'Checkout'
    assert cmn_elements.check_visibility_of_element(cmn_elements.LOGO)
    search_field = cmn_elements.check_visibility_of_element(cmn_elements.SEARCH_FIELD)
    assert search_field.get_attribute('type') == 'text'
    search_button = cmn_elements.check_visibility_of_element(cmn_elements.SEARCH_BTN)
    assert search_button.get_attribute('type') == 'button'
    search_field.clear()
    search_field.send_keys('This is test input')
    inline_items[1].click()
    search_button.click()
    assert cmn_elements.browser.current_url != f'{base_url}{paths}'


@pytest.mark.usefixtures('set_currencies')
def test_change_currency_in_home_page(base_url, browser, set_currencies, curns):
    cmn_elements = Common_elements(browser, base_url)
    cur_name, cur_symb = curns
    cmn_elements.open_page()
    dropdown_currency = cmn_elements.check_visibility_of_element(cmn_elements.DROPDOWN_CURRENCY, 5)
    dropdown_currency.click()
    cmn_elements.check_visibility_of_element(cmn_elements.CURRENCY_DICT.get(cur_name)).click()
    list_products = Home_page(browser, base_url)
    list_products.check_visibility_of_element(list_products.LIST_PRODUCTS)
    products = Product_card(browser, base_url)
    lst_prices_new = products.find_some_elem(products.PRICE_NEW)
    for new_price in lst_prices_new:
        assert cur_symb in new_price.text
    lst_prices_tax = products.find_some_elem(products.PRICE_TAX)
    for price_tax in lst_prices_tax:
        assert cur_symb in price_tax.text


def test_product_add_to_cart(base_url, browser):
    home_page = Home_page(browser, base_url)
    home_page.open_page()
    home_page.check_visibility_of_element(home_page.LIST_PRODUCTS)
    product_items_pick = home_page.check_visibility_of_element(home_page.PRODUCT_ITEMS_PICK)
    product_items_pick.click()
    lst_add_to_cart = home_page.find_some_elem(home_page.LIST_PRDCT_ITEM)
    assert len(lst_add_to_cart) == 1
    assert lst_add_to_cart[0].text == 'Your shopping cart is empty!'
    product_items_pick.click()
    products = Product_card(browser, base_url)
    lst_products = home_page.find_some_elem(products.PRODUCT_CARD)
    assert len(lst_products) == 4
    rand_product = lst_products[random.randint(1, len(lst_products)) - 1]
    rand_product.find_element(*products.ADD_TO_CART).click()
    alerts = Home_page_alerts(browser, base_url)
    text_alert_add_to_cart = alerts.check_visibility_of_element(alerts.ALERT_SUCCESS, timeout=3)
    assert 'Success: You have added' in text_alert_add_to_cart.text





