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


plt.figure(figsize=(16, 9))

coord = np.array([[0.01, 180], [0.02, 100], [0.03, 60], [0.04, 45], [0.05, 45]])

coord[:, 1] = 1 / coord[:, 1]

plt.scatter(coord[:, 0], coord[:, 1], marker='+', s=100, label='$26^\circ C$')
x, y, a, b, da, db = lsm(coord[:12, 0], coord[:12, 1])
plt.plot(x, y)
print(a, b, da)
#-------------------
coord = np.array([[0.01, 120], [0.02, 70], [0.03, 35], [0.04, 25], [0.05, 20]])

coord[:, 1] = 1 / coord[:, 1]

plt.scatter(coord[:, 0], coord[:, 1], marker='+', s=100, color='red', label='$26^\circ C$')
x, y, a, b, da, db = lsm(coord[:12, 0], coord[:12, 1])
plt.plot(x, y, color='red')
print(a, b, da)

plt.xlim(0, 0.06)
plt.ylim(0, 0.06)

plt.xlabel('$c$, л/моль')
plt.ylabel('$v=1\tau$, $c^{-1}$')

plt.grid(True, which='major', linestyle='-', linewidth=0.5)
plt.grid(True, which='minor', linestyle='-', linewidth=0.3)
plt.minorticks_on()

plt.legend()

plt.savefig('chim2/1.png')

plt.show()