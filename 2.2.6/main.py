from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

def linear_func(x, a, b):
    return a * x + b

def lsm(x, y): 
    params, covariance = curve_fit(linear_func, x, y)
    xs = np.linspace(0, 1.2 * max(x), 1000)
    ys = linear_func(xs, params[0], params[1])
    a, b = params
    da, db = np.sqrt(np.diag(covariance))
    return xs, ys, a, b, da, db

coord = np.array(pd.read_excel('data.xlsx'))[:, 3:5]

plt.scatter(coord[:, 0], coord[:, 1], marker='+', s=100)

x, y, a, b, da, db = lsm(coord[:, 0], coord[:, 1])
plt.plot(x, y)
print(a, b, da)

plt.xlim(0.0025, 0.00375)
plt.ylim(-10, 5)

plt.xlabel('1/T, $K^{-1}$')
plt.ylabel('ln$\eta$, Па $\cdot$ с')

plt.grid(True, which='major', linestyle='-', linewidth=0.5)
plt.grid(True, which='minor', linestyle='-', linewidth=0.3)
plt.minorticks_on()

plt.savefig('1.png')

plt.show()