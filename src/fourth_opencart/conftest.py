import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as Firefox_Options


def pytest_addoption(parser):
    parser.addoption('--url', action='store', default='localhost:8081')
    parser.addoption('--maximized', action='store_true', help='This option\
     allows you to open the browser in full screen.')
    parser.addoption('--headless', action='store_true', help='This is headless mode for the window of browser.')
    parser.addoption('--browser', action='store', default='chrome', choices=['chrome', 'firefox'])


@pytest.fixture
def base_url(request):
    return request.config.getoption('--url')


@pytest.fixture
def browser(request):
    browser_arg = request.config.getoption('--browser')
    headless = request.config.getoption('--headless')
    maximized = request.config.getoption('--maximized')
    options = Chrome_Options() if browser_arg == 'chrome' else Firefox_Options()
    if headless:
        options.add_argument('--headless=new')
    if browser_arg == 'chrome':
        driver = webdriver.Chrome(options=options)
    elif browser_arg == 'firefox':
        driver = webdriver.Firefox(options=options)
    if maximized:
        driver.maximize_window()
    driver.implicitly_wait(1)

    def final():
        driver.quit()

    request.addfinalizer(final)
    return driver
