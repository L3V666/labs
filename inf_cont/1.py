from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

data = np.array(pd.read_csv("1.csv"))

plt.scatter(data[:, 0], data[:, 1], label="stl_vector", s=1)
plt.scatter(data[:, 0], data[:, 2], label='sub_vetor', s=1)

plt.grid()

plt.legend()

plt.xlabel('i')
plt.ylabel('t, нс')

plt.title("insert")
    
plt.savefig('1.png')

plt.show()
