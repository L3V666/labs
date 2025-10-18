from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

fig, ax = plt.subplots(2, 1, figsize=(7, 10))

x = np.linspace(0, 1, 1000)
ax[0].plot(x, x)
ax[0].plot(x, x ** 2 / 2)

ax[0].set_xlabel('x')
ax[0].set_ylabel('y')

data = np.array(pd.read_csv("4_float.csv", header=None))

ax[1].plot(data[:, 0], data[:, 1], label='float')

data = np.array(pd.read_csv("4_double.csv", header=None))

ax[1].plot(data[:, 0], data[:, 1], label='double')

ax[1].set_xlabel('Кол-во прямоугольников')
ax[1].set_ylabel('Суммарная площадь')

ax[1].legend()

plt.savefig('4.png')

plt.show()