import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class Base_class_page:

    def __init__(self, browser, base_url):
        self.browser = browser
        self.path = '/'
        self.base_url = base_url

    def check_presence_of_element(self, elem, timeout=1):
        try:
            return WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(elem))
        except (TimeoutException, NoSuchElementException) as err:
            self.browser.save_screenshot(f'{self.browser.session_id}-{datetime.datetime.now()}.png')
            raise AssertionError(err)

    def check_presence_some_elements(self, elem, timeout=1):
        try:
            return WebDriverWait(self.browser, timeout).until(EC.presence_of_all_elements_located(elem))
        except (TimeoutException, NoSuchElementException) as err:
            self.browser.save_screenshot(f'{self.browser.session_id}-{datetime.datetime.now()}.png')
            raise AssertionError(err)

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

    def check_visibility_some_elements(self, elem, timeout=1):
        try:
            return WebDriverWait(self.browser, timeout).until(EC.visibility_of_all_elements_located(elem))
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

    def click_elem(self, elem):
        find_elem = self.check_visibility_of_element(elem)
        find_elem.click()

    def input_in_field(self, elem, value):
        find_field = self.check_visibility_of_element(elem)
        find_field.clear()
        find_field.send_keys(value)

    def clear_field(self, elem):
        find_elem = self.check_visibility_of_element(elem)
        find_elem.clear()
