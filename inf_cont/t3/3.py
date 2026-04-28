from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

data = np.array(pd.read_csv("inf_cont/t3/3.csv"))

plt.scatter(data[:, 0], data[:, 1], label="stl_list", s=1)
plt.scatter(data[:, 0], data[:, 2], label='stl_forward_list', s=1)
plt.scatter(data[:, 0], data[:, 3], label='sub_forward_list', s=1)

plt.grid()

plt.legend()

plt.xlabel('i')
plt.ylabel('t, нс')     

plt.title("push_front")
    
plt.savefig('inf_cont/t3/3.png')

plt.show()
