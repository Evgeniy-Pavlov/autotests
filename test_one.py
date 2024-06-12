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


@pytest.mark.parametrize('a', range(1, 5))
@pytest.mark.parametrize('b', range(2, 6))
@pytest.mark.parametrize('c', range(3, 7))
def test_triangle_create(a, b, c):
    result = Triangle(f'triangle_{a}', a, b, c)
    assert result.name == f'triangle_{a}'
    assert result.a == a
    assert result.b == b
    assert result.c == c
    p = 0.5 * sum((a, b, c))
    assert result.area == p * (p - a) * (p - b) * (p - c)
    assert result.perimeter == a + b + c

@pytest.mark.parametrize('a', range(1, 5))
@pytest.mark.parametrize('b', range(2, 6))
@pytest.mark.parametrize('c', range(3, 7))
def test_triangle_add_area(a, b, c):
    triangle_1 = Triangle(f'triangle_{a}', a, b, c)
    triangle_2 = Triangle(f'triangle_{b}', a, b, c)
    assert triangle_1.add_area(triangle_2) == triangle_1.area + triangle_2.area
