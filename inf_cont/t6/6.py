from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

data = np.array(pd.read_csv("inf_cont/t6/6.csv"))

plt.scatter(data[:, 0], data[:, 1], label="vector", s=1)
plt.scatter(data[:, 0], data[:, 2], label='forward_list', s=1)
plt.scatter(data[:, 0], data[:, 3], label='list', s=1)
plt.scatter(data[:, 0], data[:, 4], label='map', s=1)
plt.scatter(data[:, 0], data[:, 5], label='set', c='pink', s=1)

plt.grid()

plt.legend()

plt.xlabel('i')
plt.ylabel('t, нс')     

plt.title("обход контейнера")
    
plt.savefig('inf_cont/t6/6.png')

plt.show()
