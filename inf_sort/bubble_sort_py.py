from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

file = 'bubble_sort_csv.csv'

data = np.array(pd.read_csv(file, header=None))

n = data[:, 0]
t = data[:, 1]

fig, ax = plt.subplots(1, 2, figsize=(12, 6))

ax[0].scatter(n, t, s=5)
ax[0].set_title("Обычные оси")
ax[0].set_xlabel("n")
ax[0].set_ylabel("t")

def linear_func(x, a, b):
    return a * x + b

def lsm(n, t): 
    params, covariance = curve_fit(linear_func, n, t)
    x = np.linspace(min(n), max(n), 1000)
    y = linear_func(x, params[0], params[1])
    return x, y, params[0], np.sqrt(np.diag(covariance))

n_log = np.log(n)
t_log = np.log(t)
x, y = lsm(n_log, t_log)[0: 2]
print(lsm(n_log, t_log)[2])

ax[1].plot(x, y, color='red')
ax[1].scatter(n_log, t_log, s=5)
ax[1].set_title("Логарифмические оси")
ax[1].set_xlabel("ln(n)")
ax[1].set_ylabel("ln(t)")


plt.show()