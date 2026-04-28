from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

data = np.array(pd.read_csv("inf_cont/t0/0.csv"))

plt.plot(data[:, 0], data[:, 1], label="size")
plt.plot(data[:, 0], data[:, 2], label='capacity')

plt.grid()

plt.legend()

plt.xlabel('i')
plt.ylabel('capacity(i), size(i)')

plt.savefig('inf_cont/t0/0.png')

plt.show()