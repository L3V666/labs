from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


omega = np.array([4.6, 5.7, 7.07, 8.41, 10.59])
M = np.array([0.9, 1.1, 1.38, 1.64, 2.07])

plt.scatter(M, omega, marker='+', color='red', s=200)

def linear_func(x, a, b):
    return a * x + b

def lsm(x, y): 
    params, covariance = curve_fit(linear_func, x, y)
    x = np.linspace(0, 2 * max(x), 1000)
    y = linear_func(x, params[0], params[1])
    return x, y, params[0], np.sqrt(np.diag(covariance))

l = lsm(M, omega)
x, y = l[0:2]
k = l[2]

print(k)

plt.plot(x, y, ls='--', lw=1)

plt.xlabel('$M, 10^{-1}$ Н$\cdot$м')
plt.ylabel('$\Omega, 10^{-2}$ с')

plt.grid(True, which='major', linestyle='-', linewidth=0.5)
plt.grid(True, which='minor', linestyle='-', linewidth=0.3)

plt.minorticks_on()

plt.xlim(0, 2.5)
plt.ylim(0, 12)

plt.savefig("1.png")

plt.show()