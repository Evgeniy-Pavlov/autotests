import pytest
from src.fifth_page_object.elements.common_elements import Common_elements


@pytest.mark.usefixtures('set_currencies')
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
