import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

def linear_func(x, a, b):
    return a * x + b

def lsm(x, y): 
    params, covariance = curve_fit(linear_func, x, y)
    xs = np.linspace(0, 2 * max(x), 1000)
    ys = linear_func(xs, params[0], params[1])
    a, b = params
    da, db = np.sqrt(np.diag(covariance))
    return xs, ys, a, b, da, db

coord = np.array(pd.read_excel("2.5.1/data.ods", sheet_name=0))
print(coord)
plt.scatter(coord[:, 0], coord[:, 1], marker='+', s=100, color='red')
x, y, a, b, da, db = lsm(coord[:8, 0], coord[:8, 1])
plt.plot(x, y)
print(a, b, da)

plt.xlabel('T, К')
plt.ylabel('$\sigma$, мН/м')

plt.xlim(295, 340)
plt.ylim(80, 95)

plt.grid(True, which='major', linestyle='-', linewidth=0.5)
plt.grid(True, which='minor', linestyle='-', linewidth=0.3)
plt.minorticks_on()

plt.savefig('2.5.1/1.png')

plt.show()