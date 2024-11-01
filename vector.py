import math


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __abs__(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def __add__(self, other):
        if type(other) != Vector:
            return 'ERROR'
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def scalar(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def vect2(self, a):
        if type(a) != float and type(a) != int:
            return 'ERROR'
        return Vector(self.x * a, self.y * a, self.z * a)

    def __str__(self):
        return f'x = {self.x} y = {self.y} z = {self.z}'


A = Vector(1, 0, 1)
print(A)
B = A + Vector(1, 1, 1)
print(B)
C = A.scalar(B)
print(C)
D = A + 1
print(D)
F = A + 'р'
print(F)
C = Vector(-1, -1, -2)
print(A + C)
print(A.vect2(3))
print(A.vect2('р'))
print(abs(C))