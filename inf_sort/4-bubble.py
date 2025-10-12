import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


data = np.array(pd.read_csv('bubble_sort_csv.csv', header=None))

plt.plot(data[:, 0], data[:, 1], label='default')
plt.plot(data[:, 0], data[:, 2], label='best')
plt.plot(data[:, 0], data[:, 3], label='worst')

plt.legend()

plt.savefig("4bubble.png")

plt.show()