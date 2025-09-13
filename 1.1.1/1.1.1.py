import numpy as np
import pandas as pd

N = 10
d = 0.01
data = np.array(pd.read_excel('измерения диаметра.xlsx'))
avg_d = np.mean(data[:, 1])
sigma_d = np.sqrt(1 / (N - 1) * np.sum((data[:, 1] - avg_d) ** 2))
sigma_avg = sigma_d / np.sqrt(N)
sigma_all = np.sqrt(sigma_avg ** 2 + d ** 2)
print(sigma_all)