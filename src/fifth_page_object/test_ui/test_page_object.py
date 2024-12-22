import pytest
from src.fifth_page_object.elements.common_elements import Common_elements


@pytest.mark.usefixtures('set_currencies', 'set_phone')
def test_common_elem_on_different_page(base_url, browser, set_currencies, paths, get_phone):
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
    wishlist = cmn_elements.find_one_elem(cmn_elements.WISHLIST_URL)
    assert wishlist.get_attribute('href') == f'{base_url}/en-gb?route=account/wishlist'
    assert wishlist.get_attribute('title') == 'Wish List (0)'
    phone_elem = cmn_elements.find_one_elem(cmn_elements.PHONE_NUMBER)
    assert phone_elem.text == get_phone
    assert cmn_elements.find_one_elem(cmn_elements.SHOPPING_CART) == inline_items[3]
    shopping_cart_url = cmn_elements.find_one_elem(cmn_elements.SHOPPING_CART_URL)
    shopping_cart_text = cmn_elements.find_one_elem(cmn_elements.SHOPPING_CART_TEXT)
    assert shopping_cart_url.get_attribute('href') == f'{base_url}/en-gb?route=checkout/cart'
    assert shopping_cart_text.text == 'Shopping Cart'
    checkout_url = cmn_elements.find_one_elem(cmn_elements.CHECKOUT_URL)
    checkout_text = cmn_elements.find_one_elem(cmn_elements.CHECKOUT_TEXT)
    assert checkout_url.get_attribute('href') == f'{base_url}/en-gb?route=checkout/checkout'
    assert checkout_text.text == 'Checkout'
    assert cmn_elements.check_visibility_of_element(cmn_elements.LOGO)
    search_field = cmn_elements.find_one_elem(cmn_elements.SEARCH_FIELD)
    assert search_field.get_attribute('type') == 'text'
    search_button = cmn_elements.find_one_elem(cmn_elements.SEARCH_BTN)
    assert search_button.get_attribute('type') == 'button'
    search_field.clear()
    search_field.send_keys('This is test input')
    inline_items[1].click()
    search_button.click()
    assert cmn_elements.browser.current_url != f'{base_url}{paths}'
