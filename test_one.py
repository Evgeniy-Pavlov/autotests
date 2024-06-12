import pytest
from src.first_OOP import Square, Rectangle, Circle, Triangle, Figure


def test_figure_create():
    with pytest.raises(AssertionError):
        result = Figure('test_name')

@pytest.mark.parametrize('a', range(1, 5))    
def test_square_create(a):
    result = Square(f'square_{a}', a)
    assert result.name == f'square_{a}'
    assert result.a == a
    assert result.area == a ** 2
    assert result.perimeter == a * 4

@pytest.mark.parametrize('a', range(1, 5))
@pytest.mark.parametrize('b', range(1, 5))
def test_square_add_area(a, b):
    square_1 = Square(f'square_{a}', a)
    square_2 = Square(f'square_{b}', b)
    assert square_1.add_area(square_2) == a ** 2 + b ** 2

