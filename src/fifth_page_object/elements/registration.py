from selenium.webdriver.common.by import By
from src.fifth_page_object.elements.base_class import Base_class_page


class Registration_page(Base_class_page):
    HEADER = (By.CSS_SELECTOR, '#content > h1')
    PERSONAL_DETAILS_LEGEND = (By.CSS_SELECTOR, '#account > legend')
    FIRST_NAME_LABEL = (By.CSS_SELECTOR, '#account > div.required > label[for="input-firstname"]')
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '#input-firstname')
    ERROR_FIRST_NAME = (By.CSS_SELECTOR, '#error-firstname')
    LAST_NAME_LABEL = (By.CSS_SELECTOR, '#account > div.required > label[for="input-lastname"]')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '#input-lastname')
    ERROR_LAST_NAME = (By.CSS_SELECTOR, '#error-lastname')
    EMAIL_LABEL = (By.CSS_SELECTOR, '#account > div.required > label[for="input-email"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#input-email')
    ERROR_EMAIL = (By.CSS_SELECTOR, '#error-email')
    PASSWORD_LEGEND = (By.CSS_SELECTOR, '#form-register > fieldset:nth-child(2) > legend')
    PASSWORD_LABER = (By.CSS_SELECTOR, '#form-register > fieldset > div.required > label[for="input-password"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    ERROR_PASSWORD = (By.CSS_SELECTOR, '#error-password')
    NEWLETTER_LEGEND = (By.CSS_SELECTOR, '#form-register > fieldset:nth-child(3) > legend')
    SUBSCRIBE_LABEL = (By.CSS_SELECTOR, '#form-register > fieldset:nth-child(3) > div > label')
    SUBSCRIBE_SWITCH = (By.CSS_SELECTOR, '#input-newsletter')
    POLICY_LABEL = (By.CSS_SELECTOR, '#form-register > div > div > label.form-check-label')
    POLICY_SWITCH = (By.CSS_SELECTOR, '#form-register > div > div > input.form-check-input')
    CONTINUE_BTN = (By.CSS_SELECTOR, '#form-register > div > button')

    def __init__(self, browser, base_url):
        super().__init__(browser, base_url)
        self.path = '/en-gb?route=account/register'
