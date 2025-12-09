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


def mlsm(x, y): 
    params, covariance = curve_fit(linear_func, x, y)
    xs = np.linspace(2 * min(x), 0, 1000)
    ys = linear_func(xs, params[0], params[1])
    a, b = params
    da, db = np.sqrt(np.diag(covariance))
    return xs, ys, a, b, da, db


data_a = []
data_da = []

d1 = np.array([[0, 0],
                [4.46, 0.67],
                [9.11, 1.35],
                [13.99, 2.06],
                [18.9, 2.77],
                [13.99, 2.2],
                [9.11, 1.41],
                [4.46, 0.69], 
                [0, 0.02]])

d1_r = np.array([[0, 0],
                [4.46, 0.65],
                [9.11, 1.35],
                [13.99, 2.07],
                [18.9, 2.81],
                [13.99, 2.11],
                [9.11, 1.43],
                [4.46, 0.74], 
                [0, 0.03]])

d2 = np.array([[0, 0],
                [4.46, 0.40],
                [9.11, 0.79],
                [13.99, 1.06],
                [18.9, 1.44],
                [13.99, 1.04],
                [9.11, 0.62],
                [4.46, 0.30], 
                [0, 0.00]])

d2_r = np.array([[0, 0],
                [4.46, 0.41],
                [9.11, 0.82],
                [13.99, 1.25],
                [18.9, 1.68],
                [13.99, 1.28],
                [9.11, 0.95],
                [4.46, 0.44], 
                [0, 0.05]])

s = np.array([[0, 0],
                [4.46, 0.66],
                [9.11, 1.3],
                [13.99, 1.97],
                [18.9, 2.67],
                [13.99, 1.98],
                [9.11, 1.29],
                [4.46, 0.65], 
                [0, 0.04]])

s_r = np.array([[0, 0],
                [4.46, 0.59],
                [9.11, 1.25],
                [13.99, 1.93],
                [18.9, 2.66],
                [13.99, 1.97],
                [9.11, 1.28],
                [4.46, 0.64], 
                [0, 0.03]])

data1 = d1
data2 = d1_r

fig, axs = plt.subplots(1, 2, figsize=(11, 6))

axs[0].set_title("Увеличение нагрузки")

axs[0].scatter(data1[:5, 1], data1[:5, 0], label='Обычное', marker='+', s=200)
axs[0].scatter(data2[:5, 1], data2[:5, 0], label='Перевёрнутое', marker='+', s=200)

x, y, a, b, da, db = lsm(data1[:5, 1], data1[:5, 0])
axs[0].plot(x, y, label='Аппроксимация обычная')

data_a.append(a)
data_da.append(da)

x, y, a, b, da, db = lsm(data2[:5, 1], data2[:5, 0])
axs[0].plot(x, y, label='Аппроксимация перевёрнутая')

data_a.append(a)
data_da.append(da)

axs[0].grid(True, which='major', linestyle='-', linewidth=0.5)
axs[0].grid(True, which='minor', linestyle='-', linewidth=0.3)

axs[0].minorticks_on()

axs[0].set_xlim(0, 3)
axs[0].set_ylim(0, 19.5)

axs[0].set_xlabel('$y_{max}$, мм')
axs[0].set_ylabel('$P$, Н')

axs[0].legend()

###############33

axs[1].set_title("Уменьшение нагрузки")

axs[1].scatter(-data1[4:, 1], data1[4:, 0], label='Обычное', marker='+', s=200)
axs[1].scatter(-data2[4:, 1], data2[4:, 0], label='Перевёрнутое', marker='+', s=200)

x, y, a, b, da, db = mlsm(-data1[4:, 1], data1[4:, 0])
axs[1].plot(x, y, label='Аппроксимация обычная')

data_a.append(a)
data_da.append(da)

x, y, a, b, da, db = mlsm(-data2[4:, 1], data2[4:, 0])
axs[1].plot(x, y, label='Аппроксимация перевёрнутая')

data_a.append(a)
data_da.append(da)

axs[1].grid(True, which='major', linestyle='-', linewidth=0.5)
axs[1].grid(True, which='minor', linestyle='-', linewidth=0.3)

axs[1].minorticks_on()

axs[1].set_xlim(-3, 0)
axs[1].set_ylim(0, 19.5)

axs[1].set_xlabel('$y_{max}$, мм')
axs[1].set_ylabel('$P$, Н')

axs[1].legend()

plt.show()

data_a = np.array(data_a)
data_da = np.array(data_da)

print(np.mean(np.abs(data_a)), np.mean(data_da))