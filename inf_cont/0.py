from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

data = np.array(pd.read_csv("0.csv"))

plt.plot(data[:, 0], data[:, 1], label="size")
plt.plot(data[:, 0], data[:, 2], label='capacity')

plt.grid()

plt.legend()

plt.xlabel('i')
plt.ylabel('capacity(i), size(i)')

plt.savefig('1.png')

plt.show()