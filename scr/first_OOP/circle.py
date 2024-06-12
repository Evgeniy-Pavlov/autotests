from figure import Figure

class Circle(Figure):

    def __init__(self, anme, r):
        self.name = name
        self.r = r

    @property
    def area(self):
        return 3.14 * r ** 2

    @property
    def perimeter(self):
        return 2 * 3.14 * r
