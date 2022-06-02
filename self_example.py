class Vector:
    def __init__(self, x, y):
        try:
            self.x = float(x)
            self.y = float(y)
        except ValueError:
            self.x = 0.0
            self.y = 0.0

    def norm(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __add__(self, other):
        newx = self.x + other.x
        newy = self.y + other.y
        return Vector(newx, newy)

    def __str__(self):
        return "(%f, %f)" %(self.x, self.y)
e = 3
f = 4
print(type(e))
u = Vector(e, f)
v = Vector(3, 6)
print(type(u))
print(u + v)
