from selenium.webdriver.common.by import By
from src.fifth_page_object.elements.base_class import Base_class_page


class Login_form(Base_class_page):
    EMAIL_INPUT = (By.CSS_SELECTOR, '#input-email')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#form-login > div.text-end > button')

    def __init__(self, browser, base_url):
        super().__init__(browser, base_url)
        self.path = 'en-gb?route=account/login'
