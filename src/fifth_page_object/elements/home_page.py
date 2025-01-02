from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.fifth_page_object.elements.base_class import Base_class_page


class Home_page(Base_class_page):
    CAROUSEL = (By.CSS_SELECTOR, '#carousel-banner-0')
    LIST_PRODUCTS = (By.CSS_SELECTOR, '#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4')
    PRODUCT_ITEMS_PICK = (By.CSS_SELECTOR, '#header-cart > div > button')
    LIST_PRDCT_ITEMS = (By.CSS_SELECTOR, '#header-cart > div > ul.p-2')
    LIST_PRDCT_ITEM = (By.CSS_SELECTOR, '#header-cart > div > ul.p-2 > li')
    DELETE_ITEM = (By.CSS_SELECTOR, '#header-cart > div > ul.p-2 > li > table > tbody > tr > td:nth-child(5) > form > button')

    def __init__(self, browser, base_url):
        super().__init__(browser, base_url)
        self.path = '/home'


class Product_card(Base_class_page):
    PRODUCT_CARD = (
        By.CSS_SELECTOR, '#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div.col > div.product-thumb')
    PRICE_NEW = (By.CSS_SELECTOR, 'span.price-new')
    PRICE_TAX = (By.CSS_SELECTOR, 'span.price-tax')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.content > div > h4 > a')
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, 'div.content > div > p')
    ADD_TO_CART = (By.CSS_SELECTOR, 'div.content > form > div.button-group > button[title="Add to Cart"]')
    ADD_TO_WISHLIST = (By.CSS_SELECTOR,
                   'div.content > form > div > button[aria-label="Add to Wish List"]')
    COMPARE_THIS_PRODUCT = (By.CSS_SELECTOR,
                    'div.content > form > div > button[aria-label="Compare this Product"]')


