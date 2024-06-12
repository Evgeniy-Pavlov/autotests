from rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, name, a):
        self.name = name
        self.a = a

    @property
    def area(self):
        return a ** 2

    @property
    def perimeter(self):
        return a * 4
