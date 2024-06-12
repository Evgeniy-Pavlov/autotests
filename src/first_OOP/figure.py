class Figure:
    _instances = {}

    def __init__(self, name):
        self.name = name
    
    def __new__(cls, *args):
        if cls is Figure:
            raise AssertionError('You cannot create this basic class.')
        cls._instances[cls] = super(Figure, cls).__new__(cls)
        return cls._instances[cls]
        
    @property
    def area(self):
        pass

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("This object can't be summed")
        return self.area + figure.area
