from selenium.webdriver.common.by import By
from src.fifth_page_object.elements.base_class import Base_class_page


class Home_page(Base_class_page):
    CAROUSEL = (By.CSS_SELECTOR, '#carousel-banner-0')
    LIST_PRODUCTS = (By.CSS_SELECTOR, '#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4')
    PRODUCT_ITEMS_PICK = (By.CSS_SELECTOR, '#header-cart > div > button')
    LIST_PRDCT_ITEMS = (By.CSS_SELECTOR, '#header-cart > div > ul.p-2')
    LIST_PRDCT_EMPTY_ITEM = (By.CSS_SELECTOR, '#header-cart > div > ul.p-2 > li')
    DELETE_ITEM = (By.CSS_SELECTOR, '#header-cart > div > ul.p-2 > li > table > tbody > tr > td:nth-child(5) > form > button')
    CART_ITEM = (By.CSS_SELECTOR, '#header-cart > div > ul.p-2 > li > table > tbody > tr')
    ITEM_PRODUCT_NAME = (By.CSS_SELECTOR, 'td.text-start > a')
    ITEM_PRODUCT_PRICE = (By.CSS_SELECTOR, 'td:nth-child(4)')
    CAROUSEL_ITEM = (By.CSS_SELECTOR, '#carousel-banner-0 > div.carousel-inner > div.carousel-item')
    FIRST_CAROUSEL_ITEM = (By.CSS_SELECTOR, '#carousel-banner-0 > div.carousel-inner > div.carousel-item:nth-child(1)')
    SECOND_CAROUSEL_ITEM = (By.CSS_SELECTOR, '#carousel-banner-0 > div.carousel-inner > div.carousel-item:nth-child(2)')
    CAROUSEL_BANNER_ITEM = (By.CSS_SELECTOR, '#carousel-banner-1 > div.carousel-inner > div')
    FIRST_BANNER_ITEM = (By.CSS_SELECTOR, '#carousel-banner-1 > div.carousel-inner > div:nth-child(1)')
    SECOND_BANNER_ITEM = (By.CSS_SELECTOR, '#carousel-banner-1 > div.carousel-inner > div:nth-child(2)')
    THIRD_BANNER_ITEM = (By.CSS_SELECTOR, '#carousel-banner-1 > div.carousel-inner > div:nth-child(3)')

    def __init__(self, browser, base_url):
        super().__init__(browser, base_url)
        self.path = '/home'

    def get_info_about_product_in_cart(self):
        result = []
        list_items = self.check_visibility_some_elements(self.CART_ITEM)
        for item in list_items:
            item_name = item.find_element(*self.ITEM_PRODUCT_NAME).text
            item_price = item.find_element(*self.ITEM_PRODUCT_PRICE).text
            result.append({'price': item_price, 'name': item_name})
        return result


class Product_card(Base_class_page):
    PRODUCT_CARD = (
        By.CSS_SELECTOR, '#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div.col > div.product-thumb')
    PRICE_NEW = (By.CSS_SELECTOR, 'span.price-new')
    PRICE_TAX = (By.CSS_SELECTOR, 'span.price-tax')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.content > div > h4 > a')
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, 'div.content > div > p')
    ADD_TO_CART = (By.CSS_SELECTOR, 'div.content > form > div.button-group > button[title="Add to Cart"]')
    ADD_TO_WISHLIST = (By.CSS_SELECTOR,
                   'div.content > form > div.button-group > button[title="Add to Wish List"]')
    COMPARE_THIS_PRODUCT = (By.CSS_SELECTOR,
                    'div.content > form > div > button[aria-label="Compare this Product"]')

    def __init__(self, browser, base_url):
        super().__init__(browser, base_url)
        self.path = '/home'

    def add_to_cart_nth_product(self, number):
        lst_products = self.check_visibility_some_elements(self.PRODUCT_CARD)
        rand_product = lst_products[number - 1]
        rand_product.find_element(*self.ADD_TO_CART).click()

    def add_to_wishlist_nth_product(self, number):
        lst_products = self.check_visibility_some_elements(self.PRODUCT_CARD)
        rand_product = lst_products[number-1]
        rand_product.find_element(*self.ADD_TO_WISHLIST).click()

    def get_info_about_product(self, number):
        number -= 1
        lst_products = self.check_visibility_some_elements(self.PRODUCT_CARD)
        product_name = lst_products[number].find_element(*self.PRODUCT_NAME).text
        product_description = lst_products[number].find_element(*self.PRODUCT_DESCRIPTION).text
        price_new = lst_products[number].find_element(*self.PRICE_NEW).text
        price_tax = lst_products[number].find_element(*self.PRICE_TAX).text
        return {'product_name': product_name, 'product_description': product_description, 'price_new': price_new,
                'price_tax': price_tax}




