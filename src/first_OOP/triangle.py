from .figure import Figure

class Triangle(Figure):

    def __init__(self, name, a, b, c):
        self.name = name
        self.a = a
        self.b = b
        self.c = c
    
    @property
    def area(self):
        p = 0.5 * sum((self.a, self.b, self.c))
        return p * (p - self.a) * (p - self.b) * (p - self.c)

    @property
    def perimeter(self):
        return sum((self.a, self.b, self.c))
