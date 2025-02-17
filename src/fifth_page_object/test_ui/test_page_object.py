import random
import pytest
from src.fifth_page_object.elements.common_elements import Common_elements
from src.fifth_page_object.elements.home_page import Home_page, Product_card
from src.fifth_page_object.elements.login_form import Login_form
from src.fifth_page_object.elements.personal_page import Personal_page


@pytest.mark.usefixtures('set_currencies', 'set_phone')
def test_common_elem_on_different_pages(base_url, browser, set_currencies, paths, get_phone):
    cmn_elements = Common_elements(browser, base_url)
    cmn_elements.change_path(paths)
    cmn_elements.open_page()
    cmn_elements.currencies_dropdown_click()
    currencies = cmn_elements.check_visibility_some_elements(cmn_elements.CURRENCIES)
    assert len(currencies) == len(set_currencies)
    inline_items = cmn_elements.check_visibility_some_elements(cmn_elements.INLINE_ITEMS)
    assert len(inline_items) == 5
    cmn_elements.my_account_click()
    register_login_items = cmn_elements.check_visibility_some_elements(cmn_elements.ITEMS_LOGIN_REGISTER)
    assert len(register_login_items) == 2
    register, login = register_login_items
    assert register.get_attribute('href') == f'{base_url}/en-gb?route=account/register'
    assert login.get_attribute('href') == f'{base_url}/en-gb?route=account/login'
    cmn_elements.my_account_click()
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
    cmn_elements.input_in_search_field('This is test input')
    cmn_elements.click_elem(cmn_elements.SEARCH_BTN)
    assert cmn_elements.browser.current_url != f'{base_url}{paths}'


@pytest.mark.usefixtures('set_currencies')
def test_change_currency_in_home_page(base_url, browser, set_currencies, curns):
    cmn_elements = Common_elements(browser, base_url)
    cur_name, cur_symb = curns
    cmn_elements.open_page()
    cmn_elements.currencies_dropdown_click()
    cmn_elements.change_currency(cur_name)
    list_products = Home_page(browser, base_url)
    list_products.check_visibility_of_element(list_products.LIST_PRODUCTS)
    products = Product_card(browser, base_url)
    lst_prices_new = products.check_visibility_some_elements(products.PRICE_NEW)
    for new_price in lst_prices_new:
        assert cur_symb in new_price.text
    lst_prices_tax = products.check_visibility_some_elements(products.PRICE_TAX)
    for price_tax in lst_prices_tax:
        assert cur_symb in price_tax.text


def test_product_add_to_cart(base_url, browser):
    home_page = Home_page(browser, base_url)
    home_page.open_page()
    home_page.check_visibility_of_element(home_page.LIST_PRODUCTS)
    product_items_pick = home_page.check_visibility_of_element(home_page.PRODUCT_ITEMS_PICK)
    assert product_items_pick.text == '0 item(s) - $0.00'
    home_page.click_elem(home_page.PRODUCT_ITEMS_PICK)
    lst_add_to_cart = home_page.check_visibility_some_elements(home_page.LIST_PRDCT_EMPTY_ITEM)
    assert len(lst_add_to_cart) == 1
    assert lst_add_to_cart[0].text == 'Your shopping cart is empty!'
    home_page.click_elem(home_page.PRODUCT_ITEMS_PICK)
    products = Product_card(browser, base_url)
    lst_products = products.check_visibility_some_elements(products.PRODUCT_CARD)
    assert len(lst_products) == 4
    rand_num = random.randint(0, len(lst_products) - 1)
    products.add_to_cart_nth_product(rand_num)
    product_info = products.get_info_about_product(rand_num)
    product_items_pick_new = home_page.check_visibility_of_element(home_page.PRODUCT_ITEMS_PICK)
    assert product_items_pick_new.text == f'1 item(s) - {product_info.get("price_new")}'
    home_page.click_elem(home_page.PRODUCT_ITEMS_PICK)
    product_list = home_page.get_info_about_product_in_cart()
    assert len(product_list) == 1
    first_item = product_list[0]
    assert first_item['name'] == product_info['product_name']
    assert first_item['price'] == product_info['price_new']


def test_login_user(base_url, browser, create_random_user):
    cmn_elem = Common_elements(browser, base_url)
    cmn_elem.open_page()
    email, password = create_random_user
    cmn_elem.my_account_click()
    cmn_elem.click_elem(cmn_elem.LOGIN_URL)
    personal_page = Personal_page(browser, base_url)
    login_page = Login_form(browser, base_url)
    login_page.click_elem(login_page.LOGIN_BUTTON)
    personal_page.wait_invisibility_element(personal_page.MY_ACCOUNT_HEADER)
    login_page.input_in_field(login_page.EMAIL_INPUT, email)
    login_page.click_elem(login_page.LOGIN_BUTTON)
    personal_page.wait_invisibility_element(personal_page.MY_ACCOUNT_HEADER)
    login_page.clear_field(login_page.EMAIL_INPUT)
    login_page.input_in_field(login_page.PASSWORD_INPUT, password)
    login_page.click_elem(login_page.LOGIN_BUTTON)
    personal_page.wait_invisibility_element(personal_page.MY_ACCOUNT_HEADER)
    login_page.clear_field(login_page.PASSWORD_INPUT)
    login_page.input_in_field(login_page.EMAIL_INPUT, email)
    login_page.input_in_field(login_page.PASSWORD_INPUT, password)
    login_page.click_elem(login_page.LOGIN_BUTTON)
    personal_page.check_visibility_of_element(personal_page.MY_ACCOUNT_HEADER)
    assert 'account/account&customer_token' in login_page.browser.current_url
    cmn_elem.my_account_click()
    my_account_url = cmn_elem.check_visibility_of_element(cmn_elem.MY_ACCOUNT_URL)
    assert my_account_url.text == 'My Account'
    order_history = cmn_elem.check_visibility_of_element(cmn_elem.ORDER_HISTORY)
    assert order_history.text == 'Order History'
    transactions = cmn_elem.check_visibility_of_element(cmn_elem.TRANSACTIONS)
    assert transactions.text == 'Transactions'
    downloads = cmn_elem.check_visibility_of_element(cmn_elem.MY_ACCOUNT_DOWNLOADS)
    assert downloads.text == 'Downloads'
    logout = cmn_elem.check_visibility_of_element(cmn_elem.LOGOUT_URL)
    assert logout.text == 'Logout'
    cmn_elem.click_elem(cmn_elem.LOGOUT_URL)


def test_add_to_wishlist_without_login(base_url, browser):
    home_page = Home_page(browser, base_url)
    home_page.open_page()
    products = Product_card(browser, base_url)
    lst_products = products.check_visibility_some_elements(products.PRODUCT_CARD)
    assert len(lst_products) == 4
    rand_num = random.randint(1, len(lst_products) - 1)
    products.add_to_wishlist_nth_product(rand_num)
    cmn_elem = Common_elements(browser, base_url)
    wishlist = cmn_elem.check_visibility_of_element(cmn_elem.WISHLIST_TEXT, timeout=4)
    assert wishlist.text == 'Wish List (0)'


def test_change_slide_in_carousel(base_url, browser):
    home_page = Home_page(browser, base_url)
    home_page.open_page()
    carousel_items = home_page.check_presence_some_elements(home_page.CAROUSEL_ITEM)
    assert len(carousel_items) == 2
