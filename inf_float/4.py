from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

fig, ax = plt.subplots(2, 1, figsize=(6, 10))

# x = np.linspace(0, 1, 1000)
# ax[0].plot(x, x)
# ax[0].plot(x, x ** 2 / 2)

# ax[0].set_xlabel('x')
# ax[0].set_ylabel('y')

data = np.array(pd.read_csv("4_float.csv", header=None))

ax[0].set_title('float')
ax[0].set_xlabel('Кол-во столбцов')
ax[0].set_ylabel('Значение')

ax[0].plot(data[:, 0], data[:, 1])

data = np.array(pd.read_csv("4_double.csv", header=None))

ax[1].set_title('double')
ax[1].set_xlabel('Кол-во столбцов')
ax[1].set_ylabel('Значение')

ax[1].plot(data[:, 0], data[:, 1])

plt.savefig('4.png')

plt.show()