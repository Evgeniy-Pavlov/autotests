import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class Base_class_page:

    def __init__(self, browser, base_url):
        self.browser = browser
        self.path = '/'
        self.base_url = base_url

    def check_visibility_of_element(self, elem, timeout=1):
        try:
            return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(elem))
        except (TimeoutException, NoSuchElementException) as err:
            self.browser.save_screenshot(f'{self.browser.session_id}-{datetime.datetime.now()}.png')
            raise AssertionError(err)

    def wait_invisibility_element(self, elem, timeout=1):
        try:
            return WebDriverWait(self.browser, timeout).until(EC.invisibility_of_element_located(elem))
        except (TimeoutException, NoSuchElementException) as err:
            self.browser.save_screenshot(f'{self.browser.session_id}-{datetime.datetime.now()}.png')
            raise AssertionError(err)

    def title_wait(self, title, timeout=1):
        try:
            return WebDriverWait(self.browser, timeout).until((EC.title_is(title)))
        except TimeoutException as err:
            raise AssertionError(err)

    def open_page(self):
        self.browser.get(f'{self.base_url}{self.path}')

    def find_some_elem(self, elem):
        return self.browser.find_elements(*elem)

    def find_one_elem(self, elem):
        return self.browser.find_element(*elem)

