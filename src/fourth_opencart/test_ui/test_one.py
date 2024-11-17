from selenium.webdriver.common.by import By
from src.fourth_opencart.find_elements import title_wait, wait_visibility_element, wait_invisibility_element
import time


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



