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
    wait_visibility_element(
        '#top > div > div.nav.float-end > ul > li:nth-child(2) > div > ul > li:nth-child(1) > a', browser, 2)
    li_register = browser.find_element(
        By.CSS_SELECTOR, '#top > div > div.nav.float-end > ul > li:nth-child(2) > div > ul > li:nth-child(1) > a')
    assert li_register.text == 'Register'
    assert li_register.get_attribute('href') == f'{base_url}/en-gb?route=account/register'
    wait_visibility_element(
        '#top > div > div.nav.float-end > ul > li:nth-child(2) > div > ul > li:nth-child(2) > a', browser)
    li_login = browser.find_element(
        By.CSS_SELECTOR, '#top > div > div.nav.float-end > ul > li:nth-child(2) > div > ul > li:nth-child(2) > a')
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
    assert wait_visibility_element('header#header > div.container-fluid > a.navbar-brand > img', browser)
    logo = browser.find_element(By.CSS_SELECTOR, 'header#header > div.container-fluid > a.navbar-brand > img')
    assert logo.get_attribute('src') == f'{base_url}/administration/view/image/logo.png'
    assert logo.get_attribute('title') == 'OpenCart'
    assert wait_visibility_element('div.card-header > i.fa-solid', browser)
    div_header_form = browser.find_element(By.CSS_SELECTOR, 'div.card-header')
    assert div_header_form.text == 'Please enter your login details.'
    label_login_input = browser.find_element(By.CSS_SELECTOR, '#form-login > div:nth-child(1) > label')
    assert label_login_input.text == 'Username'
    label_password_input = browser.find_element(By.CSS_SELECTOR, '#form-login > div:nth-child(2) > label')
    assert label_password_input.text == 'Password'
    input_login = browser.find_element(By.CSS_SELECTOR, 'input#input-username')
    input_password = browser.find_element(By.CSS_SELECTOR, 'input#input-password')
    assert input_login.get_attribute('placeholder') == 'Username'
    assert input_password.get_attribute('placeholder') == 'Password'
    assert input_login.get_attribute('type') == 'text'
    assert input_password.get_attribute('type') == 'password'


def test_registration_page(browser, base_url):
    browser.get(f'{base_url}/index.php?route=account/register')
    assert wait_visibility_element('div#content > h1', browser)
    header_form = browser.find_element(By.CSS_SELECTOR, 'div#content > h1')
    assert header_form.text == 'Register Account'
    required_fields = browser.find_elements(By.CSS_SELECTOR, 'div.required')
    assert len(required_fields) == 4
    first_name_label = browser.find_element(By.CSS_SELECTOR, '#account > div:nth-child(2) > label.col-form-label')
    assert first_name_label.text == 'First Name'
    first_name_field = browser.find_element(By.CSS_SELECTOR, '#input-firstname')
    assert first_name_field.get_attribute('placeholder') == 'First Name'
    assert first_name_field.get_attribute('type') == 'text'
    last_name_label = browser.find_element(By.CSS_SELECTOR, '#account > div:nth-child(3) > label.col-form-label')
    assert last_name_label.text == 'Last Name'
    last_name_field = browser.find_element(By.CSS_SELECTOR, '#input-lastname')
    assert last_name_field.get_attribute('placeholder') == 'Last Name'
    assert last_name_field.get_attribute('type') == 'text'
    email_label = browser.find_element(By.CSS_SELECTOR, '#account > div:nth-child(4) > label.col-form-label')
    assert email_label.text == 'E-Mail'
    email_field = browser.find_element(By.CSS_SELECTOR, '#input-email')
    assert email_field.get_attribute('placeholder') == 'E-Mail'
    assert email_field.get_attribute('type') == 'email'
    password_label = browser.find_element(
        By.CSS_SELECTOR, '#form-register > fieldset:nth-child(2) > div > label.col-form-label')
    assert password_label.text == 'Password'
    password_field = browser.find_element(By.CSS_SELECTOR, '#input-password')
    assert password_field.get_attribute('placeholder') == 'Password'
    assert password_field.get_attribute('type') == 'password'
    btn_form = browser.find_element(By.CSS_SELECTOR, '#form-register > div > button.btn-primary')
    assert btn_form.get_attribute('type') == 'submit'
