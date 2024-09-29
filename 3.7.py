import numpy as np

x = []
n, m = list(map(int, input().split()))
if n == m:
    A = [list(map(int, input().split())) for i in range(n)]
    b = np.array(list(map(int, input().split())), dtype=np.float64)
    D = np.linalg.det(A)
    if D == 0:
        print('ERROR: DET == 0')
    else:
        for i in range(len(b)):
            m1 = np.copy(A)
            m1[:, i] = b
            d = np.linalg.det(m1) / D
            x.append(d)
        print(*x)
else:
    print('ERROR: n != m')


