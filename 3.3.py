import math

a, b = list(map(int, input().split()))
d = math.gcd(a, b)
j = 100000000000000000000000000
p = (0, 0)
for x in range(-10000, 10000):
    if (d - x * a) % b == 0:
        y = (d - x * a) // b
        if j > abs(x) + abs(y):
            j = abs(x) + abs(y)
            p = (x, y)
print(*p, d)
