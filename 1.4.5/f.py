import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

m1 = 1087.2
m2 = 1574.6
m3 = 2071.8
m4 = 2566.2
m5 = 3060.1

u1 = 137
u2 = 166.7
u3 = 190
u4 = 209
u5 = 229

m = np.array([m1, m2, m3, m4, m5])
u = np.array([u1, u2, u3, u4, u5])

plt.scatter(m * 1e-3 * 9.81, u ** 2, marker='+')

def linear_func(x, a, b):
    return a * x + b

def lsm(x, y): 
    params, covariance = curve_fit(linear_func, x, y)
    x = np.linspace(min(x), max(x), 1000)
    y = linear_func(x, params[0], params[1])
    return x, y, params[0], np.sqrt(np.diag(covariance))

l = lsm(m * 1e-3 * 9.81, u ** 2)
x, y = l[0:2]
k = l[2]

plt.plot(x, y)

print(k ** -1, l[3] ** -1)

plt.grid(True, which='major', linestyle='-', linewidth=0.5)
plt.grid(True, which='minor', linestyle='-', linewidth=0.3)

plt.minorticks_on()

plt.xlabel('T')
plt.ylabel('u^2')

plt.savefig('3.png')

plt.show()