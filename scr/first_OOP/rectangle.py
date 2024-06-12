from figure import Figure

class Rectangle(Figure):

    def __init__(self, name, a, b):
        self.name = name
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    @property
    def perimeter(self):
        return 2 * (self.a + self.b)
