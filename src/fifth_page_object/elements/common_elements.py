from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    SHOPPING_CART_URL = (By.CSS_SELECTOR, 'ul > li:nth-child(4) > a')
    SHOPPING_CART_TEXT = (By.CSS_SELECTOR, 'ul > li:nth-child(4) > a > span.d-none')
    CHECKOUT_URL = (By.CSS_SELECTOR, 'ul > li:nth-child(5) > a')
    CHECKOUT_TEXT = (By.CSS_SELECTOR, 'ul > li:nth-child(5) > a > span.d-none')
    LOGO_URL = (By.CSS_SELECTOR, 'div#logo > a')
    LOGO = (By.CSS_SELECTOR, 'div#logo > a > img.img-fluid')
    SEARCH = (By.CSS_SELECTOR, 'div#search')
    SEARCH_FIELD = (By.CSS_SELECTOR, 'div#search > input.form-control')
    SEARCH_BTN = (By.CSS_SELECTOR, 'div#search > button.btn-light')
    NAVBAR_MENU = (By.ID, 'MENU')

    def __init__(self, browser, base_url):
        super().__init__(browser, base_url)
        self.path = '/home'

    def change_path(self, path):
        self.path = path
        return self
