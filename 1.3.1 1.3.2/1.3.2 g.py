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

lx = np.array([4.9, 7.3, 9.7, 12.1, 14.5])
ly1 = np.array([13.5, 16.1, 18.6, 21.8, 24.4])
ly2 = np.array([15.8, 18.9, 21.3, 24.2, 26.8])

plt.scatter(lx, ly1, label='$n_1$', marker='+', s=200)
plt.scatter(lx, ly2, label='$n_2$', marker='+', s=200)

x, y, a, b, da, db = lsm(lx, ly1)
plt.plot(x, y, label='Аппроксимация о')

x, y, a, b, da, db = lsm(lx, ly2)
plt.plot(x, y, label='Аппроксимация о')

plt.xlim(0, 17)
plt.ylim(0, 30)

plt.xlabel('$P$, Н')
plt.ylabel('$n$, см')

plt.grid(True, which='major', linestyle='-', linewidth=0.5)
plt.grid(True, which='minor', linestyle='-', linewidth=0.3)

plt.minorticks_on()


plt.show()