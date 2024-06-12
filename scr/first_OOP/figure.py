class Figure:

    def __init__(self, name):
        self.name = name
        
    @property
    def area(self):
        pass

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("This object can't be summed")
        return self.area + figure.area
