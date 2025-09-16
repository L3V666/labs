import pandas as pd
import numpy as np

n = 10

data = np.array(pd.read_excel('Измерения.xlsx'))
i20 = data[1:, 1]
u20 = data[1:, 2]
i30 = data[1:, 3]
u30 = data[1:, 4]
i50 = data[1:, 5]
u50 = data[1:, 6]

r20 = np.mean(i20 * u20) / np.mean(i20 ** 2)
print(f'r20 {r20}')
sigma_sl_20 = np.sqrt((1 / (n - 1)) * (np.mean(u20 ** 2) / np.mean(i20 ** 2) - r20 ** 2))
print(f'sigma_sl_20 {sigma_sl_20}')
delta_sist_20 = r20 * np.sqrt((2 / np.max(u20)) ** 2 + ((0.002 * np.max(i20) + 0.02) / np.max(i20)) ** 2)
print(f'delta_sist_20 {delta_sist_20}')
sigma_poln_20 = np.sqrt(sigma_sl_20 ** 2 + delta_sist_20 ** 2)
print(f'sigma_poln_20 {sigma_poln_20}')

r30 = np.mean(i30 * u30) / np.mean(i30 ** 2)
print(f'r30 {r30}')
sigma_sl_30 = np.sqrt((1 / (n - 1)) * (np.mean(u30 ** 2) / np.mean(i30 ** 2) - r30 ** 2))
print(f'sigma_sl_30 {sigma_sl_30}')
delta_sist_30 = r30 * np.sqrt((2 / np.max(u30)) ** 2 + ((0.002 * np.max(i30) + 0.02) / np.max(i30)) ** 2)
print(f'delta_sist_30 {delta_sist_30}')
sigma_poln_30 = np.sqrt(sigma_sl_30 ** 2 + delta_sist_30 ** 2)
print(f'sigma_poln_30 {sigma_poln_30}')

r50 = np.mean(i50 * u50) / np.mean(i50 ** 2)
print(f'r50 {r50}')
sigma_sl_50 = np.sqrt((1 / (n - 1)) * (np.mean(u50 ** 2) / np.mean(i50 ** 2) - r50 ** 2))
print(f'sigma_sl_50 {sigma_sl_50}')
delta_sist_50 = r50 * np.sqrt((2 / np.max(u50)) ** 2 + ((0.002 * np.max(i50) + 0.02) / np.max(i50)) ** 2)
print(f'delta_sist_50 {delta_sist_50}')
sigma_poln_50 = np.sqrt(sigma_sl_50 ** 2 + delta_sist_50 ** 2)
print(f'sigma_poln_50 {sigma_poln_50}')


d = 0.365

r20 = 2.012
ro20 = r20 * 3.14 * d ** 2 / 4 / 0.2
print(f'ro20 {ro20} {ro20 * 0.014}')

r30 = 3.01
ro30 = r30 * 3.14 * d ** 2 / 4 / 0.3
print(f'ro30 {ro30} {ro30 * 0.014}')

r50 = 5.03
ro50 = r50 * 3.14 * d ** 2 / 4 / 0.5
print(f'ro50 {ro50} {ro50 * 0.014}')