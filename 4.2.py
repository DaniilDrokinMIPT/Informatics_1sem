import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure(figsize=(16, 9))
axs1 = fig.add_subplot(311)
axs2 = fig.add_subplot(312)
axs3 = fig.add_subplot(313)

x = [i for i in range(0, 200, 50)]
y = [j for j in range(0, 200, 50)]
S = [i + j for i in x for j in y]
axs1.hist(S)

x = [i for i in range(0, 200, 25)]
y= [j for j in range(0, 200, 25)]
S = [i + j for i in x for j in y]
axs2.hist(S)

x = [i for i in range(0, 200, 1)]
y = [j for j in range(0, 200, 1)]
S = [i + j for i in x for j in y]
axs3.hist(S)


plt.show()