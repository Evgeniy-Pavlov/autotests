import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--url', action='store', default='localhost:8081')
    parser.addoption('--maximized', action='store_true', help='This option allows you to open the browser in full screen.')
    parser.addoption('--headless', action='store_true', help='This is headless mode for the window of browser.')
    parser.addoption('--browser', action='store', default = 'chrome', choices=['chrome', 'firefox'])


@pytest.fixture
def base_url(request):
    return request.config.getoption('--url')


@pytest.fixture
def browser(request):
    browser = request.config.getoption('--browser')
    headless = request.config.getoption('--headless')
    maximized = request.config.getoption('--maximized')
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    return driver
