import numpy as np
import pandas as pd

N = 10
d = 0.01
data = np.array(pd.read_excel('измерения диаметра.xlsx'))
avg_d = np.mean(data[:, 1])
print(f'avg_d {avg_d}')
sigma_d = np.sqrt(1 / (N - 1) * np.sum((data[:, 1] - avg_d) ** 2))
print(f'sigma_d {sigma_d}')
sigma_avg = sigma_d / np.sqrt(N)
print(f'sigma_avg {sigma_avg}')
sigma_all = np.sqrt(sigma_avg ** 2 + d ** 2)
print(f'sigma_all {sigma_all}')

print(sigma_d / 0.365)