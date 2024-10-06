import re
import pytest
import requests

def pytest_addoption(parser):
    parser.addoption(
        '--url',
        default = 'https://ya.ru',
        action = 'store',
        type = str,
        help = 'You need to write here the url the service being tested.'
    )
    parser.addoption(
        '--status_code',
        default = 200,
        action = 'store',
        type = int,
        choices = [200, 201, 400, 401, 403, 404, 500, 501, 502, 503, 504],
        help = 'It is the list of status codes.'
    )

@pytest.fixture
def base_url(request):
    return request.config.getoption('--url')

@pytest.fixture
def status_code(request):
    return request.config.getoption('--status_code')

@pytest.fixture
def pattern_url_dogs():
    return re.compile(r'https:\/\/images.dog.ceo\/breeds\/[a-z-]{1,30}\/[a-zA-Z0-9~.,_()-]{1,60}.jpg')


def pytest_generate_tests(metafunc):
    if 'breed' in metafunc.fixturenames:
        url = metafunc.config.getoption('--url')
        metafunc.parametrize('breed', [x if x != 'pinscher' else pytest.param(x, 
                            marks=pytest.mark.xfail(reason='For the pinscher breed, returns\
                            the MD file in the message list. For example https://images.dog.ceo/breeds/pinscher/README.MD')) 
                            for x in requests.get(f'{url}/api/breeds/list/all').json()['message'].keys()])


