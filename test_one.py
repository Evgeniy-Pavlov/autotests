import pytest

@pytest.mark.parametrize('a', [1, 2])
@pytest.mark.parametrize('b', [3, 4])
def test_first(a, b):
    result = a * b
    assert isinstance(result, int)
