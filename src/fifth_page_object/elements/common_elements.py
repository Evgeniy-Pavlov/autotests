from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_class import Base_class_page


class Common_elements(Base_class_page):
    PAGE_TITLE_TEXT = 'Your Store'
    LOGO = (By.CSS_SELECTOR, '#header-cart > div > button.btn-lg')
    DROPDOWN_CURRENCY = (By.CSS_SELECTOR, 'form#form-currency > div.dropdown > a.dropdown-toogle')
    CURRENCIES = (By.CSS_SELECTOR, 'form#form-currency > div.dropdown > ul.dropdown-menu > li > a.dropdown-item')
    INLINE_ITEMS = (By.CSS_SELECTOR, 'div.float-end > ul.list-inline > li.list-inline-item')
    ITEMS_LOGIN_REGISTER = (By.CSS_SELECTOR, 'ul.dropdown-menu-right > li > a.dropdown-item')
    WISHLIST_URL = (By.CSS_SELECTOR, 'a#wishlist-total')
    WISHLIST_COUNT = (By.CSS_SELECTOR, 'a#wishlist-total > span.d-none')
    SHOPPING_CART_URL = (By.CSS_SELECTOR, 'ul > li:nth-child(4) > a')
    SHOPPING_CART_TEXT = (By.CSS_SELECTOR, 'ul > li:nth-child(4) > a > span.d-none')
    CHECKOUT_URL = (By.CSS_SELECTOR, 'ul > li:nth-child(5) > a')
    CHECKOUT_TEXT = (By.CSS_SELECTOR, 'ul > li:nth-child(5) > a > span.d-none')

    def __init__(self):
        super().__init__()
        self.path = '/home'
