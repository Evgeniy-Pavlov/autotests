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
def pattern_url_dogs():
    return re.compile(r'https:\/\/images.dog.ceo\/breeds\/[a-z-]{1,30}\/[a-zA-Z0-9._()-]{1,50}.jpg')
