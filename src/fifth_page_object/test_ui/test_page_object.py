import pytest
from src.fifth_page_object.elements.common_elements import Common_elements


@pytest.mark.usefixtures('set_currencies')
def test_one(base_url, browser, set_currencies):
    cmn_elements = Common_elements(browser, base_url)
    cmn_elements.open_page()
    assert cmn_elements.title_wait(cmn_elements.PAGE_TITLE_TEXT)
    currencies_dropdown = cmn_elements.check_visibility_of_element(cmn_elements.DROPDOWN_CURRENCY, 5)
    currencies_dropdown.click()
    currencies = cmn_elements.find_some_elem(cmn_elements.CURRENCIES)
    assert len(currencies) == len(set_currencies)
