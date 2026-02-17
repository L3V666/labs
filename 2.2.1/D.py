import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
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

def out(x, y):
    print(f'Среднее значение x: {np.mean(x)}')
    print(f'Средний квадрат x: {np.mean(x ** 2)}')
    print(f'Квадрат среднего x: {np.mean(x) ** 2}')
    print(f'Среднее произведения xy: {np.mean(x * y)}')
    print(f'Среднее значение y: {np.mean(y)}')
    print(f'Средний квадрат y: {np.mean(y ** 2)}')
    print(f'Квадрат среднего y: {np.mean(y) ** 2}')


y = np.array([6.22, 4.97, 3.48, 3.33])
x = 1 / np.array([44.6, 74.4, 104.2, 137.6])

plt.scatter(x, y, marker='+', c='red', s=100)

print(out(x, y))
x, y, a, b, da, db = lsm(x, y)
plt.plot(x, y)
print(a, b, da)

plt.xlim(0, 0.025)
plt.ylim(0, 7)

plt.xlabel('1/T, 1/Па')

plt.ylabel('D, ${см}^2 / c$')

plt.grid(True, which='major', linestyle='-', linewidth=0.5)
plt.grid(True, which='minor', linestyle='-', linewidth=0.3)
plt.minorticks_on()

plt.savefig('D.png')

plt.show()