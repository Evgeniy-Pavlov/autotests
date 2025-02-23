import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException


class Base_class_page:

    def __init__(self, browser, base_url):
        self.browser = browser
        self.path = '/'
        self.base_url = base_url
        self.logger = browser.logger

    def check_presence_of_element(self, elem, timeout=1):
        try:
            self.logger.info(f'Check presence of the element {elem}, timeout = {timeout}')
            return WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(elem))
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as err:
            self.logger.error(f'The element {elem} not in DOM or the timeout is not enough. Error: {err}')
            self.browser.save_screenshot(f'logs/{self.browser.session_id}-{datetime.datetime.now()}.png')
            raise AssertionError(err)

    def check_presence_some_elements(self, elem, timeout=1):
        try:
            self.logger.info(f'Check presense of some elements {elem}, timeout = {timeout}')
            return WebDriverWait(self.browser, timeout).until(EC.presence_of_all_elements_located(elem))
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as err:
            self.logger.error(f'The elements {elem} not in DOM or the timeout is not enough. Error: {err}')
            self.browser.save_screenshot(f'logs/{self.browser.session_id}-{datetime.datetime.now()}.png')
            raise AssertionError(err)

    def check_visibility_of_element(self, elem, timeout=1):
        try:
            self.logger.info(f'Check visibility of the element {elem}, timeout = {timeout}')
            return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(elem))
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as err:
            self.logger.error(f'The element {elem} is not visible or the timeout is not enough. Error: {err}')
            self.browser.save_screenshot(f'logs/{self.browser.session_id}-{datetime.datetime.now()}.png')
            raise AssertionError(err)

    def wait_invisibility_element(self, elem, timeout=1):
        try:
            self.logger.info(f'Check invisibility of the element {elem}, timeout = {timeout}')
            return WebDriverWait(self.browser, timeout).until(EC.invisibility_of_element_located(elem))
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as err:
            self.logger.error(f'The element {elem} is visible or the timeout is not enough. Error: {err}')
            self.browser.save_screenshot(f'logs/{self.browser.session_id}-{datetime.datetime.now()}.png')
            raise AssertionError(err)

    def check_visibility_some_elements(self, elem, timeout=1):
        try:
            self.logger.info(f'Check visibility of some elements {elem}, timeout = {timeout}')
            return WebDriverWait(self.browser, timeout).until(EC.visibility_of_all_elements_located(elem))
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as err:
            self.logger.error(f'The elements {elem} is not visible or the timeout is not enough. Error: {err}')
            self.browser.save_screenshot(f'logs/{self.browser.session_id}-{datetime.datetime.now()}.png')
            raise AssertionError(err)

    def title_wait(self, title, timeout=1):
        try:
            self.logger.info(f'Waiting title of page {title}, timeout = {timeout}')
            return WebDriverWait(self.browser, timeout).until((EC.title_is(title)))
        except TimeoutException as err:
            self.logger.error(f'Title is not found. Error: {err}')
            raise AssertionError(err)

    def open_page(self):
        self.logger.info(f'Open page: {self.base_url}{self.path}')
        self.browser.get(f'{self.base_url}{self.path}')

    def click_elem(self, elem):
        self.logger.info(f'Click the element {elem}')
        find_elem = self.check_visibility_of_element(elem)
        find_elem.click()

    def input_in_field(self, elem, value):
        self.logger.info(f'Entering "{value}" into the field {elem}')
        find_field = self.check_visibility_of_element(elem)
        find_field.clear()
        find_field.send_keys(value)

    def clear_field(self, elem):
        self.logger.info(f'Clear field {elem}')
        find_elem = self.check_visibility_of_element(elem)
        find_elem.clear()
