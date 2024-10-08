import pytest
import requests
from models import Brewery, Brewery_meta


@pytest.mark.brewery
@pytest.mark.parametrize('num', range(1, 5))
def test_list_breweries(base_url, status_code, num):
    response = requests.get(f'{base_url}/v1/breweries?per_page={num}')
    assert response.status_code == status_code
    result = response.json()
    assert isinstance(result, list)
    assert len(result) == num
    for i in result:
        assert isinstance(i, dict)
        assert Brewery.model_validate(i)


@pytest.mark.brewery
def test_simple_brewery(base_url, status_code, brewery_id):
    response = requests.get(f'{base_url}/v1/breweries/{brewery_id}')
    assert response.status_code == status_code
    result = response.json()
    assert isinstance(result, dict)
    assert result['id'] == brewery_id
    assert Brewery.model_validate(result)


@pytest.mark.brewery
def test_breweries_by_city(base_url, status_code, brewery_city):
    response = requests.get(f'{base_url}/v1/breweries?by_city={brewery_city}')
    assert response.status_code == status_code
    result = response.json()
    assert isinstance(result, list)
    for i in result:
        assert Brewery.model_validate(i)
        assert brewery_city in i['city']  


@pytest.mark.brewery
def test_breweries_by_country(base_url, status_code, brewery_country):
    response = requests.get(f'{base_url}/v1/breweries?by_country={brewery_country}')
    assert response.status_code == status_code
    result = response.json()
    assert isinstance(result, list)
    for i in result:
        assert Brewery.model_validate(i)
        assert brewery_country in i['country']  


@pytest.mark.brewery
def test_breweries_by_dist(base_url, status_code):
    response = requests.get(f'{base_url}/v1/breweries?by_dist=32.88313237,-117.1649842&per_page=3')
    assert response.status_code == status_code
    result = response.json()
    assert isinstance(result, list)
    assert len(result) == 3
    for i in result:
        assert Brewery.model_validate(i)


@pytest.mark.brewery
def test_breweries_by_ids(base_url, status_code, brewery_ids):
    ids = ','.join(brewery_ids)
    response = requests.get(f'{base_url}/v1/breweries?by_ids={ids}')
    assert response.status_code == status_code
    result = response.json()
    assert isinstance(result, list)
    assert len(result) == 3
    for i in result:
        assert Brewery.model_validate(i)


@pytest.mark.brewery
@pytest.mark.parametrize('param,value', [('name', 'san_diego'), ('state', 'california'), ('postal', '92101')])
def test_breweries_by_name_state_postal(base_url, status_code, param, value):
    response = requests.get(f'{base_url}/v1/breweries?by_{param}={value}&per_page=3')
    assert response.status_code == status_code
    result = response.json()
    assert isinstance(result, list)
    assert len(result) == 3
    for i in result:
        assert Brewery.model_validate(i)


@pytest.mark.brewery
@pytest.mark.parametrize('type_brewery', ['micro', 'nano', 'regional', 'brewpub', 'large', 'planning', 'bar', 'contract', 'proprietor', 'closed'])
def test_breweries_by_type(base_url, status_code, type_brewery):
    response = requests.get(f'{base_url}/v1/breweries?by_bype={type_brewery}&per_page=5')
    assert response.status_code == status_code
    result = response.json()
    assert isinstance(result, list)
    assert len(result) == 5
    for i in result:
        assert Brewery.model_validate(i)


@pytest.mark.brewery
def test_random_brewery(base_url, status_code):
    response = requests.get(f'{base_url}/v1/breweries/random')
    assert response.status_code == status_code
    result = response.json()
    assert isinstance(result, list)
    assert Brewery.model_validate(result[0])


@pytest.mark.brewery
@pytest.mark.parametrize('num', range(1,5))
def test_random_brewery_size(base_url, status_code, num):
    response = requests.get(f'{base_url}/v1/breweries/random?size={num}')
    assert response.status_code == status_code
    result = response.json()
    assert isinstance(result, list)
    assert len(result) == num
    for i in result:
        assert Brewery.model_validate(i)


@pytest.mark.brewery
def test_breweries_meta(base_url, status_code):
    response = requests.get(f'{base_url}/v1/breweries/meta')
    assert response.status_code == status_code
    result = response.json()
    assert isinstance(result, dict)
    assert Brewery_meta.model_validate(result)