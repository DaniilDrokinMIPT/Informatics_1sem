import math


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __abs__(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            B = Vector(other, other, other)
            return Vector(self.x + B.x, self.y + B.y, self.z + B.z)
        if type(other) == Vector:
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return 'ERROR'

    def __radd__(self, other):
        if type(other) != Vector:
            return 'ERROR'
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        if type(other) == float or type(other) == int:
            return Vector(self.x * other, self.y * other, self.z * other)
        if type(other) == Vector:
            return self.x * other.x + self.y * other.y + self.z * other.z
        return 'ERROR'


    def __str__(self):
        return f'x = {self.x} y = {self.y} z = {self.z}'


A = Vector(1, 0, 1)
print(A)
B = A + Vector(1, 1, 1)
print(B)
C = A * B
print(C)
D = A + 1
print(D)
F = A + 'р'
print(F)
C = Vector(-1, -1, -2)
print(A + C)
print(A * 3)
print(A * 'р')
print(abs(C))
print(1 + A)
print(A + B)