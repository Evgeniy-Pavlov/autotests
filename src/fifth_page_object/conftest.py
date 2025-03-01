import datetime
import socket
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as Firefox_Options
import mariadb
import requests
from helpers import read_conn_params, get_token_admin, generante_random_string, generate_random_password


def pytest_addoption(parser):
    parser.addoption('--url', action='store', default='localhost:8081')
    parser.addoption('--maximized', action='store_true', help='This option\
     allows you to open the browser in full screen.')
    parser.addoption('--headless', action='store_true', help='This is headless mode for the window of browser.')
    parser.addoption('--browser', action='store', default='chrome', choices=['chrome', 'firefox'])
    parser.addoption('--conn_params', action='store', default='conn_params.json', help='This is path db connection\
    parameters')
    parser.addoption('--currencies', action='append', default=["GBP", "USD", "EUR"])
    parser.addoption('--phone', action='store', default='8800853535')
    parser.addoption('--log_level', action='store', default='INFO')


def node_name(request):
    name = request.node.name
    t = str.maketrans({'[': '_', ']': '', '/': ''})
    return name.translate(t)


@pytest.fixture
def base_url(request):
    return request.config.getoption('--url')


@pytest.fixture
def get_phone(request):
    return request.config.getoption('--phone')


@pytest.fixture(scope='session')
def set_currencies(request):
    query = 'SELECT code FROM oc_currency where status = 1'
    conn_params = read_conn_params(request.config.getoption('--conn_params'))
    connection = mariadb.connect(**conn_params)
    cursor = connection.cursor()
    cursor.execute(query)
    result_currencies = tuple([x[0] for x in cursor.fetchall()])
    query_update = f'update oc_currency set status = 1 where code in {tuple(request.config.getoption("--currencies"))}'
    cursor.execute(query_update)
    connection.commit()
    base_url = request.config.getoption('--url')
    token = get_token_admin(base_url)
    requests.post(f'{base_url}/administration/index.php?route=localisation/currency.refresh&user_token={token}')
    requests.get(f'{base_url}/administration/index.php?route=localisation/currency.list&user_token={token}')

    def final():
        cursor.execute(f'update oc_currency set status = 1 where code in {result_currencies}')
        connection.commit()
        cursor.execute(
            f'update oc_currency set status = 0 where code not in {result_currencies}')
        connection.commit()
        cursor.close()
        connection.close()
        requests.post(f'{base_url}/administration/index.php?route=localisation/currency.refresh&user_token={token}')
        requests.get(f'{base_url}/administration/index.php?route=localisation/currency.list&user_token={token}')

    request.addfinalizer(final)
    return request.config.getoption("--currencies")


@pytest.fixture(scope='session')
def set_phone(request):
    phone = request.config.getoption('--phone')
    query = "select value from oc_setting where `key` = 'config_telephone'"
    query_update = f"update oc_setting set value = {phone} where `key` = 'config_telephone'"
    conn_params = read_conn_params(request.config.getoption('--conn_params'))
    connection = mariadb.connect(**conn_params)
    cursor = connection.cursor()
    cursor.execute(query)
    old_phone = str(cursor.fetchall()[0][0])
    cursor.execute(query_update)
    connection.commit()

    def final():
        query_return_phone = f"update oc_setting set value = {old_phone} where `key` = 'config_telephone'"
        cursor.execute(query_return_phone)
        connection.commit()
        cursor.close()
        connection.close()

    request.addfinalizer(final)
    return phone


@pytest.fixture(scope='function')
def create_random_user(request):
    conn_params = read_conn_params(request.config.getoption('--conn_params'))
    connection = mariadb.connect(**conn_params)
    firstname = generante_random_string()
    lastname = generante_random_string()
    email = f'{generante_random_string()}@test.com'
    password, password_encode, salt = generate_random_password()
    ip = socket.gethostbyname(socket.gethostname())
    cursor = connection.cursor()
    query_insert = f'INSERT INTO oc_customer (customer_group_id, store_id, language_id, firstname, lastname, email, telephone,\
    password, custom_field, ip, status, safe, token, code, date_added)\
    VALUES (1, 0, 1, "{firstname}", "{lastname}", "{email}", "", "{str(password_encode)[2:-1]}", "", "{ip}",\
    1, 0,  "", "", NOW())'
    cursor.execute(query_insert)
    connection.commit()
    query_select = f'select customer_id from oc_customer where firstname = "{firstname}" and lastname = "{lastname}"'
    cursor.execute(query_select)
    user_id = str(cursor.fetchall()[0][0])

    def final():
        query_delete = f'delete from oc_customer where customer_id = {user_id}'
        cursor.execute(query_delete)
        connection.commit()
        cursor.close()
        connection.close()

    request.addfinalizer(final)
    return email, password


@pytest.fixture
def browser(request):
    browser_arg = request.config.getoption('--browser')
    headless = request.config.getoption('--headless')
    maximized = request.config.getoption('--maximized')
    log_level = request.config.getoption('--log_level')
    name_node = node_name(request)
    logger = logging.getLogger(name_node)
    file_handler = logging.FileHandler(f'logs/{name_node}.log')
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    options = Chrome_Options() if browser_arg == 'chrome' else Firefox_Options()
    options.page_load_strategy = 'none'
    options.add_argument("--ignore-certificate-errors")
    if headless:
        options.add_argument('--headless=new')
    if browser_arg == 'chrome':
        driver = webdriver.Chrome(options=options)
        options.set_capability('goog:loggingPrefs', {
            'browser': 'ALL',
            'performance': 'ALL',
            'driver': 'ALL'
        })
    elif browser_arg == 'firefox':
        driver = webdriver.Firefox(options=options)
    if maximized:
        driver.maximize_window()
    driver.implicitly_wait(1)
    driver.log_level = log_level
    driver.logger = logger
    driver.name_of_test = name_node
    logger.info(
        f'Test {driver.name_of_test} started at {datetime.datetime.now()}. Browser options: {options}')

    def final():
        log_file = f'logs/browser_logs_{name_node}.log'
        browser_logs = driver.get_log('browser')
        with open(log_file, 'w') as f:
            f.write(str(browser_logs))
        driver.quit()
        logger.info(f'Test {driver.name_of_test} finished at {datetime.datetime.now()}')

    request.addfinalizer(final)
    return driver


def pytest_generate_tests(metafunc):
    if 'curns' in metafunc.fixturenames:
        query = f'select code, case when symbol_left = "" then symbol_right else symbol_left\
         end as symbol from oc_currency oc  where code in {tuple(metafunc.config.getoption("--currencies"))}'
        conn_params = read_conn_params(metafunc.config.getoption('--conn_params'))
        connection = mariadb.connect(**conn_params)
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        metafunc.parametrize('curns', result)
    if 'paths' in metafunc.fixturenames:
        conn_params = read_conn_params(metafunc.config.getoption('--conn_params'))
        connection = mariadb.connect(**conn_params)
        cursor = connection.cursor()
        query = 'select ocd.name from oc_category\
         oc join oc_category_description ocd on oc.category_id = ocd.category_id  where `column` = 1'
        cursor.execute(query)
        categories = [f'/catalog/{(x[0]).lower()}' for x in cursor.fetchall()]
        cursor.close()
        connection.close()
        metafunc.parametrize('paths', ['/home', '/catalog/smartphone', '/catalog/desktops', '/catalog/laptop-notebook'])
