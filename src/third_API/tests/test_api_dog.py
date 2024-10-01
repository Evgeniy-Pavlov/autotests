import re
import pytest
import requests


@pytest.mark.dogsapi
def test_breeds_list_all(base_url, status_code):
    response = requests.get(f'{base_url}/api/breeds/list/all')
    assert response.status_code == status_code
    result = response.json()
    assert result['status'] == 'success'
    assert isinstance(result['message'], dict)
    assert not [x for x in result['message'].keys() if not isinstance(result['message'][x], list)]


@pytest.mark.dogsapi
def test_breeds_image_random(base_url, pattern_url_dogs, status_code):
    response = requests.get(f'{base_url}/api/breeds/image/random')
    assert response.status_code == status_code
    result = response.json()
    assert isinstance(result['message'], str)
    assert result['status'] == 'success'
    assert re.match(pattern_url_dogs, result['message'])


@pytest.mark.dogsapi
@pytest.mark.parametrize('num', [x for x in range(1, 51)])
def test_breeds_image_random_multiple_valid_num(base_url, status_code, pattern_url_dogs, num):
    response = requests.get(f'{base_url}/api/breeds/image/random/{num}')
    assert response.status_code == status_code
    result = response.json()
    assert isinstance(result['message'], list)
    assert result['status'] == 'success'
    assert len(result['message']) == num
    assert len([x for x in result['message'] if not re.match(pattern_url_dogs, x)]) == 0


@pytest.mark.dogsapi
@pytest.mark.parametrize('num', [pytest.param(-1, id='negative', marks=pytest.mark.xfail(reason='With this value returns 1, should be error')), 
    pytest.param(0, id='zero', marks=pytest.mark.xfail(reason='With this value returns 1, should be error')), 
    pytest.param(51, id='more_than_max', marks=pytest.mark.xfail(reason='With this value returns 50, should be error')),
    pytest.param('a', id='str', marks=pytest.mark.xfail(reason='With this value returns 1, should be error'))])
def test_breeds_image_random_multiple_invalid_num(base_url, status_code, num):
    response = requests.get(f'{base_url}/api/breeds/image/random/{num}')
    assert response.status_code == status_code
    result = response.json()
    assert result['status'] == 'error'
    assert isinstance(result['message'], list)
