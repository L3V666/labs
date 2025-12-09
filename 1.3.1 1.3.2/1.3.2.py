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

data = np.array([[0, 0, 0, 0],
            [150, 2.9, 2.7, 2.8],
            [300, 5.6, 5.8, 5.6],
            [450, 8.9, 8.5, 8.4],
            [600, 11.7, 11.1, 11.3],
            [750, 14.4, 14.1, 14.0],
            [900, 16.9, 17.4, 17.8],
            [750, 14.6, 14.5, 14.6],
            [600, 11.6, 11.6, 11.6],
            [450, 8.6, 8.7, 8.6],
            [300, 5.8, 5.8, 5.9],
            [150, 2.9, 2.8, 2.8],
            [0, 0, 0, 0]])


M = (np.concatenate((data[:, 0], data[:, 0],data[:, 0])) + 0) * 1e-3 * 9.81 * 4.1 * 1e-2
phi = np.concatenate((data[:, 1], data[:, 2], data[:, 3])) * 1e-2 / 1.3

plt.scatter(M, phi, marker='+', s=100, color='red')

x, y, a, b, da, db = lsm(M, phi)
plt.plot(x, y)
print(a, da)

plt.grid(True, which='major', linestyle='-', linewidth=0.5)
plt.grid(True, which='minor', linestyle='-', linewidth=0.3)

plt.minorticks_on()

plt.xlim(0, 0.4)
plt.ylim(0, 0.15)

plt.xlabel('$M$, Н $\cdot$ м')
plt.ylabel(r'$\varphi$, рад')

plt.show()