from selenium.webdriver.common.by import By
from src.fourth_opencart.find_elements import title_wait, wait_visibility_element, wait_invisibility_element


def test_base_page(browser, base_url):
    browser.get(base_url)
    title_wait('Your Store', browser, 3)
    assert browser.title == 'Your Store'
    assert browser.find_element(By.CSS_SELECTOR, '#header-cart > div > button.btn-lg')
    assert wait_visibility_element('ul.navbar-nav > li.nav-item', browser)
    list_categories = browser.find_elements(By.CSS_SELECTOR, 'ul.navbar-nav > li.nav-item')
    assert len(list_categories) == 8
    assert wait_visibility_element('input.form-control-lg', browser)
    search_field = browser.find_element(By.CSS_SELECTOR, 'input.form-control-lg')
    assert search_field.get_attribute('placeholder') == 'Search'
    assert search_field.get_attribute('type') == 'text'
    assert wait_visibility_element('nav#top', browser)
    assert wait_visibility_element('#top > div > div.nav.float-end > ul > li:nth-child(2) > div > a > span', browser)
    dropdown_my_account_name = browser.find_element(
        By.CSS_SELECTOR, '#top > div > div.nav.float-end > ul > li:nth-child(2) > div > a > span')
    assert dropdown_my_account_name.text == 'My Account'
    assert wait_invisibility_element(
        '#top > div > div.nav.float-end > ul > li:nth-child(2) > div > ul > li:nth-child(1) > a', browser)
    assert wait_invisibility_element(
        '#top > div > div.nav.float-end > ul > li:nth-child(2) > div > ul > li:nth-child(2) > a', browser)
    dropdown_my_account = browser.find_element(
        By.CSS_SELECTOR, '#top > div > div.nav.float-end > ul > li:nth-child(2)')
    dropdown_my_account.click()
    wait_visibility_element('#top > div > div.nav.float-end > ul > li:nth-child(2) > div > ul > li:nth-child(1) > a', browser, 2)
    li_register = browser.find_element(By.CSS_SELECTOR, '#top > div > div.nav.float-end > ul > li:nth-child(2) > div > ul > li:nth-child(1) > a')
    assert li_register.text == 'Register'
    assert li_register.get_attribute('href') == f'{base_url}/en-gb?route=account/register'
    wait_visibility_element('#top > div > div.nav.float-end > ul > li:nth-child(2) > div > ul > li:nth-child(2) > a', browser)
    li_login = browser.find_element(By.CSS_SELECTOR, '#top > div > div.nav.float-end > ul > li:nth-child(2) > div > ul > li:nth-child(2) > a')
    assert li_login.text == 'Login'
    assert li_login.get_attribute('href') == f'{base_url}/en-gb?route=account/login'


def test_catalog(browser, base_url):
    browser.get(f'{base_url}/en-gb/catalog/desktops')
    assert wait_visibility_element('aside#column-left', browser)
    list_categories = browser.find_elements(By.CSS_SELECTOR, 'a.list-group-item')
    assert len(list_categories) == 10
    assert wait_visibility_element('div.btn-group', browser)
    assert wait_visibility_element('button#button-list', browser)
    btn_list = browser.find_element(By.CSS_SELECTOR, 'button#button-list')
    assert wait_visibility_element('button#button-grid', browser)
    btn_grid = browser.find_element(By.CSS_SELECTOR, 'button#button-grid')
    assert btn_list.get_attribute('class') == 'btn btn-light'
    assert btn_grid.get_attribute('class') == 'btn btn-light active'
    assert wait_visibility_element('div#product-list', browser)


def test_card_of_product(browser, base_url):
    browser.get(f'{base_url}/en-gb/product/desktops/apple-cinema')
    assert wait_visibility_element('ul.breadcrumb', browser)
    list_breadcrum = browser.find_elements(By.CSS_SELECTOR, 'li.breadcrumb-item > a')
    assert len(list_breadcrum) == 3
    lst_urls = ['/en-gb?route=common/home', '/en-gb/catalog/desktops', '/en-gb/product/desktops/apple-cinema']
    for elem, url in zip(list_breadcrum, lst_urls):
        assert elem.get_attribute('href') == f'{base_url}{url}'
    assert wait_visibility_element('div.magnific-popup', browser)
    assert wait_visibility_element('#content > div.row.mb-3 > div:nth-child(2)', browser)
    assert wait_visibility_element('div.btn-group', browser)
    assert wait_visibility_element('form#form-product', browser)
    list_required_fields = browser.find_elements(By.CSS_SELECTOR, '#form-product > div > div.required')
    assert len(list_required_fields) == 9


def test_page_login_administation(browser, base_url):
    browser.get(f'{base_url}/administration')

