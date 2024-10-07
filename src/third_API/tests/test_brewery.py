import pytest
import requests
from models import Brewer

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
        assert Brewer(i)