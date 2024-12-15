from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    logo = (By.CSS_SELECTOR, '#header-cart > div > button.btn-lg')
    navbar = (By.CSS_SELECTOR, 'ul.navbar-nav > li.nav-item')
    navbar_item = (By.CSS_SELECTOR, 'ul.navbar-nav > li.nav-item')
    search_field = (By.CSS_SELECTOR, 'input.form-control-lg')
    dropdown_my_account = (By.CSS_SELECTOR, 'li.list-inline-item > div.dropdown')

    def __init__(self, browser):
        self.browser = browser
