class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __add__(self, v):
        x = self.x + v.x
        y = self.y + v.y
        return Vector(x, y)

    def __sub__(self, v):
        x = self.x - v.x
        y = self.y - v.y
        return Vector(x, y)

    def __mul__(self, scalar):
        x = self.x * scalar
        y = self.y * scalar
        return Vector(x, y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def tuple(self):
        return (self.x, self.y)

    def normalized(self):
        return Vector(self.x, self.y) * (1 / self.magnitude())

    def asint(self):
        x = round(self.x)
        y = round(self.y)
        return Vector(x, y)
