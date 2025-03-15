import allure
from selenium.webdriver.common.by import By
from src.fifth_page_object.elements.base_class import Base_class_page


class Common_elements(Base_class_page):
    PAGE_TITLE_TEXT = 'Your Store'
    DROPDOWN_CURRENCY = (By.CSS_SELECTOR, 'form#form-currency')
    CURRENCIES = (By.CSS_SELECTOR, 'form#form-currency > div.dropdown > ul.dropdown-menu > li > a.dropdown-item')
    PHONE_NUMBER = (By.CSS_SELECTOR, '#top > div > div.nav.float-end > ul > li:nth-child(1) > span')
    INLINE_ITEMS = (By.CSS_SELECTOR, 'div.float-end > ul.list-inline > li.list-inline-item')
    ITEMS_LOGIN_REGISTER = (By.CSS_SELECTOR, 'ul.dropdown-menu-right > li > a.dropdown-item')
    WISHLIST_URL = (By.CSS_SELECTOR, 'a#wishlist-total')
    WISHLIST_COUNT = (By.CSS_SELECTOR, 'a#wishlist-total > span.d-none')
    SHOPPING_CART = (By.CSS_SELECTOR, 'ul > li:nth-child(4)')
    SHOPPING_CART_URL = (By.CSS_SELECTOR, 'ul > li:nth-child(4) > a')
    SHOPPING_CART_TEXT = (By.CSS_SELECTOR, 'ul > li:nth-child(4) > a > span.d-none')
    CHECKOUT_URL = (By.CSS_SELECTOR, 'ul > li:nth-child(5) > a')
    CHECKOUT_TEXT = (By.CSS_SELECTOR, 'ul > li:nth-child(5) > a > span.d-none')
    LOGO_URL = (By.CSS_SELECTOR, 'div#logo > a')
    LOGIN_URL = (By.CSS_SELECTOR,
                 '#top > div > div.nav.float-end > ul > li:nth-child(2) > div > ul > li:nth-child(2) > a')
    REGISTRATION_URL = (By.CSS_SELECTOR,
                  '#top > div > div.nav.float-end > ul > li:nth-child(2) > div > ul > li:nth-child(1) > a')
    MY_ACCOUNT_URL = (By.CSS_SELECTOR,
                      '#top > div > div.nav.float-end > ul > li:nth-child(2) > div > ul > li:nth-child(1) > a')
    ORDER_HISTORY = (By.CSS_SELECTOR,
                     '#top > div > div.nav.float-end > ul > li:nth-child(2) > div > ul > li:nth-child(2) > a')
    TRANSACTIONS = (By.CSS_SELECTOR,
                    '#top > div > div.nav.float-end > ul > li:nth-child(2) > div > ul > li:nth-child(3) > a')
    MY_ACCOUNT_DOWNLOADS = (By.CSS_SELECTOR,
                            '#top > div > div.nav.float-end > ul > li:nth-child(2) > div > ul > li:nth-child(4) > a')
    LOGOUT_URL = (By.CSS_SELECTOR,
                  '#top > div > div.nav.float-end > ul > li:nth-child(2) > div > ul > li:nth-child(5) > a')
    LOGO = (By.CSS_SELECTOR, 'div#logo > a > img.img-fluid')
    SEARCH = (By.CSS_SELECTOR, 'div#search')
    SEARCH_FIELD = (By.CSS_SELECTOR, 'div#search > input.form-control')
    SEARCH_BTN = (By.CSS_SELECTOR, '#search > button')
    NAVBAR_MENU = (By.ID, 'MENU')
    CURRENCY_EURO = (By.CSS_SELECTOR, '#form-currency > div > ul > li > a[href="EUR"]')
    CURRENCY_USD = (By.CSS_SELECTOR, '#form-currency > div > ul > li > a[href="USD"]')
    CURRENCY_GBP = (By.CSS_SELECTOR, '#form-currency > div > ul > li > a[href="GBP"]')
    WISHLIST_TEXT = (By.CSS_SELECTOR, '#wishlist-total > span')
    CURRENCY_DICT = {'EUR': CURRENCY_EURO, 'USD': CURRENCY_USD, 'GBP': CURRENCY_GBP}

    def __init__(self, browser, base_url):
        super().__init__(browser, base_url)
        self.path = '/home'

    def change_path(self, path):
        self.path = path
        return self

    @allure.step('Открытие списка доступных валют')
    def currencies_dropdown_click(self):
        self.logger.info('Open a dropdown of currencies')
        currencies_dropdown = self.check_visibility_of_element(self.DROPDOWN_CURRENCY, 5)
        currencies_dropdown.click()

    @allure.step('Открытие списка доступных опций моего аккаунта')
    def my_account_click(self):
        self.logger.info('Clicking on My account')
        inline_items = self.check_visibility_some_elements(self.INLINE_ITEMS, timeout=5)
        inline_items[1].click()

    @allure.step('Ввод в поле поиска значения {text}')
    def input_in_search_field(self, text=''):
        self.logger.info(f'Entering into a search field value "{text}"')
        search_field = self.check_visibility_of_element(self.SEARCH_FIELD)
        search_field.clear()
        search_field.send_keys(text)

    @allure.step('Изменение валюты на {currency}')
    def change_currency(self, currency):
        self.logger.info(f'Change currency to {currency}')
        self.check_visibility_of_element(self.CURRENCY_DICT.get(currency)).click()

    @allure.step('Логаут пользователя')
    def logout_user(self):
        self.logger.info('User logout')
        self.my_account_click()
        find_elem = self.check_visibility_of_element(self.LOGOUT_URL)
        find_elem.click()
