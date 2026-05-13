from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

data = np.array(pd.read_csv("inf_cont/t5/5.csv"))

plt.scatter(data[:, 0], data[:, 1], label="set", s=1)
plt.scatter(data[:, 0], data[:, 2], label='map', s=1)
plt.scatter(data[:, 0], data[:, 3], label='multiset', s=1)
plt.scatter(data[:, 0], data[:, 4], label='multimap', s=1)

plt.grid()

plt.legend()

plt.xlabel('i')
plt.ylabel('t, нс')     

plt.title("insert")
    
plt.savefig('inf_cont/t5/5.png')

plt.show()
