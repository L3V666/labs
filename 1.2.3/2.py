from matplotlib import pyplot as plt
import numpy as np
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

x = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) ** 2
y = np.array([1.58, 1.61, 1.71, 1.86, 2.06, 2.34, 2.75, 3.21, 3.66, 4.24, 4.88])

plt.scatter(x, y, marker='+', s=100, color='red')

plt.xlim(0, 2600)
plt.ylim(0, 5)

x, y, a, b, da, db = lsm(x, y)
plt.plot(x, y)
print(a, da)

plt.xlabel(r'$h^2$, мм$^2$')
plt.ylabel(r'$I, 10^{-3} \text{ кг}\cdot\text{м}^2$')

plt.grid(True, which='major', linestyle='-', linewidth=0.5)
plt.grid(True, which='minor', linestyle='-', linewidth=0.3)

plt.minorticks_on()

plt.show()