import math


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __abs__(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def __plus__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __rplus__(self, other1, other2, other3):
        return Vector(self.x + other1, self.y + other2, self.z + other3)

    def __minus__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __rminus__(self, other1, other2, other3):
        return Vector(self.x - other1, self.y - other2, self.z - other3)

    def __scalar__(self, other):
        return Vector(self.x * other.x, self.y * other.y, self.z * other.z)

    def __vect2__(self, a):
        return Vector(self.x * a, self.y * a, self.z * a)

    def __str__(self):
        return f'x = {self.x} y = {self.y} z = {self.z}'


A = Vector(1, 0, 1)
print(A)
B = A.__scalar__(A.__vect2__(2))
print(B)
C = A.__rplus__(1, 2, 3)
print(C)
D = A.__plus__(Vector(-1, -2, -3))
print(D)