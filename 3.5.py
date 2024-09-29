import numpy as np

m, n = list(map(int, input().split()))
a = np.array([[0] * m] * n)
nach = 0

def kontur(m, n, count, nach):
    for i in range(nach, m):
        a[nach][i] = count
        count += 1
    for j in range(nach + 1, n):
        a[j][m - 1] = count
        count += 1
    for i in range(m - 2, nach - 1, -1):
        a[-1 - nach][i] = count
        count += 1
    for j in range(n - 2, nach, -1):
        a[j][nach] = count
        count += 1
    return a


kontur(m, n, 1, 0)
while np.min(a) == 0:
    m -= 1
    n -= 1
    nach += 1
    count = np.max(a)
    kontur(m, n, count + 1, nach)
print(a)
summa = 0
for i in range(n):
    for j in range(m):
        summa += i * a[i][j]
print(summa)