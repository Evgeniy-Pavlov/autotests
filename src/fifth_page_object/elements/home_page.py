from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.fifth_page_object.elements.base_class import Base_class_page


class Home_page(Base_class_page):
    CAROUSEL = (By.CSS_SELECTOR, '#carousel-banner-0')
    PRICE_NEW = (By.CSS_SELECTOR, 'span.price-new')
    PRICE_TAX = (By.CSS_SELECTOR, 'span.price-tax')