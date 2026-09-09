import numpy as np

R1_R2 = 1 / 1000
U_0 = 1.4
R_0 = 610
R = np.array([i for i in range(4000, 22001, 2000)])
I = R1_R2 * U_0 / (R + R_0)
print(I)
I = I * 10 ** 8

X = np.array([20, 14, 10.8, 8.8, 7.4, 6.5, 5.7, 5.1, 4.6, 4.3])

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

plt.scatter(X, I, marker='+', s=200, color='red')
x, y, a, b, da, db = lsm(X, I)
plt.plot(x, y)
print(a, b, da)
A = 1.34
print(2 * A * a / (10 ** 8) / 10)

plt.xlim(0, 25)
plt.ylim(0, 32)

plt.xlabel('$x$, см', fontsize=18)
plt.ylabel('$I$, $10^{-8}$ A', fontsize=18)

plt.tick_params(axis='both', labelsize=12)

plt.grid(True, which='major', linestyle='-', linewidth=0.5)
plt.grid(True, which='minor', linestyle='-', linewidth=0.3)
plt.minorticks_on()

plt.savefig('3.2.6/p20.png')

plt.show()