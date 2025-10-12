import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


data = np.array(pd.read_csv('merge_sort_csv.csv', header=None))

plt.plot(data[:, 0][::40], data[:, 1][::40], label='default')
plt.plot(data[:, 0][::40], data[:, 2][::40], label='best')
plt.plot(data[:, 0][::40], data[:, 3][::40], label='worst')

plt.legend()

plt.savefig("4merge.png")

plt.show()