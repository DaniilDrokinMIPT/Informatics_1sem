from matplotlib import pyplot as plt
import numpy as np

plt.figure(figsize=(16, 9), dpi=100)
plt.title('Моя лаба', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
x = np.arange(0, 11, 1)
y = [0.050, 0.054, 0.045, 0.047, 0.049, 0.056, 0.046, 0.050, 0.051, 0.049, 0.047]
plt.plot(x, y, 'r-.', label='график')
plt.xlabel('Т, с')
plt.ylabel('N')
X = np.array(x)
Y = np.array(y)
X_P = np.mean(X)
Y_P = np.mean(Y)
a = ((np.sum((X - X_P) * (Y - Y_P))) / (np.sum((X - X_P) ** 2)))
b = Y_P - a * X_P
plt.plot(x, a * x + b, 'b-', label=f'МНК, y = {round(a, 5)}x+{round(b, 5)}')
plt.legend()
plt.savefig('mygraph.png', dpi=300)
plt.show()
