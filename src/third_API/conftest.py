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

@pytest.fixture
def pattern_url_jsonplaceholder():
    return re.compile(r'https:\/\/via.placeholder.com\/[0-9]{1,3}\/[a-z0-9]{1,6}')


def pytest_generate_tests(metafunc):
    url = metafunc.config.getoption('--url')
    if 'breed' in metafunc.fixturenames:
        metafunc.parametrize('breed', [x if x != 'pinscher' else pytest.param(x, 
                            marks=pytest.mark.xfail(reason='For the pinscher breed, returns\
                            the MD file in the message list. For example https://images.dog.ceo/breeds/pinscher/README.MD')) 
                            for x in requests.get(f'{url}/api/breeds/list/all').json()['message'].keys()])
    if 'sub_breed' in metafunc.fixturenames:
        metafunc.parametrize('sub_breed', [{'key': key, 'value': value, 'len': len(value)} for key, value in requests.get(f'{url}/api/breeds/list/all').json()['message'].items() if value])
    if 'sub_breed_img' in metafunc.fixturenames:
        lst_breeds = [(key,value) for key, value in requests.get(f'{url}/api/breeds/list/all').json()['message'].items() if value]
        result = []
        for key, value in lst_breeds:
            for sub_breed in value:
                result.append((key, sub_breed))
        metafunc.parametrize('sub_breed_img', result)
    if 'brewery_id' in metafunc.fixturenames:
        metafunc.parametrize('brewery_id', [x['id'] for x in requests.get(f'{url}/v1/breweries?per_page=10').json()]) 
    if 'brewery_city' in metafunc.fixturenames:
        metafunc.parametrize('brewery_city', sorted(list(set([x['city'] for x in requests.get(f'{url}/v1/breweries?per_page=40').json() if x['city']])))) 
    if 'brewery_country' in metafunc.fixturenames:
        metafunc.parametrize('brewery_country', sorted(list(set([x['country'] for x in requests.get(f'{url}/v1/breweries?per_page=40').json() if x['country']])))) 
    if 'brewery_ids' in metafunc.fixturenames:
        lst_breweries = [x['id'] for x in requests.get(f'{url}/v1/breweries?per_page=10').json()]
        metafunc.parametrize('brewery_ids', [lst_breweries[x-3:x] for x in range(3, len(lst_breweries), 3)]) 
    if 'post_id' in metafunc.fixturenames:
        metafunc.parametrize('post_id', [int(x['id']) for x in requests.get(f'{url}/posts').json()])
    if 'post_data' in metafunc.fixturenames:
        data_list = [{'title': f'test_{num}', 'body': f'body_{num}', 'userId': 1} for num in range(1,5)]
        metafunc.parametrize('post_data', [requests.post(url=f'{url}/posts', data=data).json() for data in data_list])
