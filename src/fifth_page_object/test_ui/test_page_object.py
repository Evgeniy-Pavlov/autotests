import pytest
from src.fifth_page_object.elements.common_elements import Common_elements


@pytest.mark.usefixtures('set_currencies')
def test_one(base_url, browser):
    cmn_elements = Common_elements(browser, base_url)
    cmn_elements.open_page()
    assert cmn_elements.title_wait(cmn_elements.PAGE_TITLE_TEXT)
