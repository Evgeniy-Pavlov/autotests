import pytest
from src.first_OOP import Square, Rectangle, Circle, Triangle, Figure


def test_figure_create():
    with pytest.raises(AssertionError) as err:
        result = Figure('test_name')
    assert err.value.args[0] == 'You cannot create this basic class.'


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
    assert square_1.add_area(square_2) == square_1.area + square_2.area


@pytest.mark.parametrize('a,b,c', [(x, x+1, x+2) for x in range(1,5)])
def test_triangle_create(a, b, c):
    result = Triangle(f'triangle_{a}', a, b, c)
    assert result.name == f'triangle_{a}'
    assert result.a == a
    assert result.b == b
    assert result.c == c
    p = 0.5 * sum((a, b, c))
    assert result.area == p * (p - a) * (p - b) * (p - c)
    assert result.perimeter == a + b + c


@pytest.mark.parametrize('a,b,c', [(x, x+1, x+2) for x in range(1,5)])
def test_triangle_add_area(a, b, c):
    triangle_1 = Triangle(f'triangle_{a}', a, b, c)
    triangle_2 = Triangle(f'triangle_{b}', a, b, c)
    assert triangle_1.add_area(triangle_2) == triangle_1.area + triangle_2.area


@pytest.mark.parametrize('a,b', [(x, x+1) for x in range(1,5)])
def test_rectangle_create(a, b):
    result = Rectangle(f'rectangle_{a}', a, b)
    assert result.name == f'rectangle_{a}'
    assert result.a == a
    assert result.b == b
    assert result.area == a * b
    assert result.perimeter == 2 * (a + b)


@pytest.mark.parametrize('a,b', [(x, x+1) for x in range(1,5)])
def test_rectangle_add_area(a, b):
    rectangle_1 = Rectangle(f'rectangle_{a}', a, b)
    rectangle_2 = Rectangle(f'rectangle_{b}', a, b)
    assert rectangle_1.add_area(rectangle_2) == rectangle_1.area + rectangle_2.area


@pytest.mark.parametrize('r', range(1, 5))    
def test_circle_create(r):
    result = Circle(f'circle_{r}', r)
    assert result.name == f'circle_{r}'
    assert result.r == r
    assert result.area == 3.14 * r ** 2
    assert result.perimeter == 2 * 3.14 * r


@pytest.mark.parametrize('r1', range(1, 5))
@pytest.mark.parametrize('r2', range(1, 5))
def test_circle_add_area(r1, r2):
    circle_1 = Circle(f'circle_{r1}', r1)
    circle_2 = Circle(f'circle_{r2}', r2)
    assert circle_1.add_area(circle_2) == circle_1.area + circle_2.area
