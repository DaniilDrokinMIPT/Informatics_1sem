a = [0] * 1000000
a[1] = 1
a[2] = 1
for i in range(3, 100000):
    a[i] = a[i - 1] + a[i - 2]
print(a[20577])