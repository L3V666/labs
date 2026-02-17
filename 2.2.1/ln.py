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


data1 = np.array(pd.read_csv('20260211_1770794006145_44.6.csv'))
data1[:, 1] = np.log(data1[:, 1])
data2 = np.array(pd.read_csv('20260211_1770795592077_74.4.csv'))
data2[:, 1] = np.log(data2[:, 1])
data3 = np.array(pd.read_csv('20260211_1770796734234_104.2.csv'))
data3[:, 1] = np.log(data3[:, 1])
data4 = np.array(pd.read_csv('20260211_1770797789536_137.6.csv'))
data4[:, 1] = np.log(data4[:, 1])

plt.scatter(data1[:, 0], data1[:, 1], s=1, label='44.6 тор')
plt.scatter(data2[:, 0], data2[:, 1], s=1, label='74.4 тор')
plt.scatter(data3[:, 0], data3[:, 1], s=1, label='104.2 тор')
plt.scatter(data4[:, 0], data4[:, 1], s=1, label='137.6 тор')

print(1)
x, y = data1[:, 0], data1[:, 1]
print(out(x, y))
x, y, a, b, da, db = lsm(x, y)
plt.plot(x, y, label='Аппроксимация 44.6 тор')
print(a, b, da)

print(2)
x, y = data2[:, 0], data2[:, 1]
print(out(x, y))
x, y, a, b, da, db = lsm(x, y)
plt.plot(x, y, label='Аппроксимация 74.4 тор')
print(a, b, da)

print(3)
x, y = data3[:, 0], data3[:, 1]
print(out(x, y))
x, y, a, b, da, db = lsm(x, y)
plt.plot(x, y, label='Аппроксимация 104.2 тор')
print(a, b, da)

print(4)
x, y = data4[:, 0], data4[:, 1]
print(out(x, y))
x, y, a, b, da, db = lsm(x, y)
plt.plot(x, y, label='Аппроксимация 137.6 тор')
print(a, b, da)

plt.legend()

plt.grid(True, which='major', linestyle='-', linewidth=0.5)
plt.grid(True, which='minor', linestyle='-', linewidth=0.3)
plt.minorticks_on()

plt.savefig('ln.png')

plt.show()