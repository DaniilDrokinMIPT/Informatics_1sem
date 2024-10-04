import numpy as np

x = list(map(float, input().split()))
y = list(map(float, input().split()))
if len(x) == len(y):
    X = np.array(x)
    Y = np.array(y)
    X_P = np.mean(X)
    Y_P = np.mean(Y)
    a = ((np.sum((X - X_P) * (Y - Y_P))) / (np.sum((X - X_P) ** 2)))
    b = Y_P - a * X_P
    print(a, b)
else:
    print('ERROR')