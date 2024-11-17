import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def title_wait(title, driver, timeout=1):
    try:
        WebDriverWait(driver, timeout).until((EC.title_is(title)))
    except TimeoutException as err:
        raise AssertionError(err)

def wait_visibility_element(selector, driver, timeout=1):
    try:
        return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
    except (TimeoutException, NoSuchElementException) as err:
        driver.save_screenshot(f'{driver.session_id}-{datetime.datetime.now()}.png')
        raise AssertionError(err)

def wait_invisibility_element(selector, driver, timeout=1):
    try:
        return WebDriverWait(driver, timeout).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, selector)))
    except (TimeoutException, NoSuchElementException) as err:
        driver.save_screenshot(f'{driver.session_id}-{datetime.datetime.now()}.png')
        raise AssertionError(err)

