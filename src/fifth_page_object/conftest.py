import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as Firefox_Options
import mariadb
from helpers import read_conn_params



def pytest_addoption(parser):
    parser.addoption('--url', action='store', default='localhost:8081')
    parser.addoption('--maximized', action='store_true', help='This option\
     allows you to open the browser in full screen.')
    parser.addoption('--headless', action='store_true', help='This is headless mode for the window of browser.')
    parser.addoption('--browser', action='store', default='chrome', choices=['chrome', 'firefox'])
    parser.addoption('--conn_params', action='store', default='conn_params.json', help='This is path db connection\
    parameters')
    parser.addoption('--currencies', action='append', default=["GBP", "USD", "EUR", "RUB"])


@pytest.fixture
def base_url(request):
    return request.config.getoption('--url')


@pytest.fixture(scope='session')
def set_currencies(request):
    query = 'SELECT code FROM oc_currency where status = 1'
    conn_params = read_conn_params(request.config.getoption('--conn_params'))
    connection = mariadb.connect(**conn_params)
    cursor = connection.cursor()
    cursor.execute(query)
    result_сurrencies = [x[0] for x in cursor.fetchall()]
    query_update = f'update oc_currency set status = 1 where code in {tuple(request.config.getoption("--currencies"))}'
    cursor.execute(query_update)
    def final():
        query_return = f'update oc_currency set status = 1 where code in {tuple([x[0] for x in result_сurrencies])}'
        cursor.execute(query_return)
        cursor.execute(
            f'update oc_currency set status = 0 where code not in {tuple([x[0] for x in result_сurrencies])}')
        cursor.close()
        connection.close()
    request.addfinalizer(final)
    return request.config.getoption("--currencies")


@pytest.fixture
def browser(request):
    browser_arg = request.config.getoption('--browser')
    headless = request.config.getoption('--headless')
    maximized = request.config.getoption('--maximized')
    options = Chrome_Options() if browser_arg == 'chrome' else Firefox_Options()
    options.page_load_strategy = 'none'
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
