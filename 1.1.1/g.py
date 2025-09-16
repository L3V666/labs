import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit


data = np.array(pd.read_excel('Измерения.xlsx'))
i20 = data[1:, 1]
u20 = data[1:, 2]
i30 = data[1:, 3]
u30 = data[1:, 4]
i50 = data[1:, 5]
u50 = data[1:, 6]

def linear_func(x, a, b):
    return a * x + b

def lsm(v, u): 
    params, covariance = curve_fit(linear_func, v, u)
    x = np.linspace(0, max(v)*1.15, 100)
    y = params[0] * x + params[1]
    return x, y, params[0], np.sqrt(np.diag(covariance))

x20, y20 = lsm(i20, u20)[0], lsm(i20, u20)[1]
print(lsm(i20, u20)[2:])
plt.plot(x20, y20, label="l=20cm")

x30, y30 = lsm(i30, u30)[0], lsm(i30, u30)[1]
print(lsm(i30, u30)[2:])
plt.plot(x30, y30, label="l=30cm")

x50, y50 = lsm(i50, u50)[0], lsm(i50, u50)[1]
print(lsm(i50, u50)[2:])
plt.plot(x50, y50, label="l=50cm")

plt.legend()

plt.xlabel("I, mA")
plt.ylabel("V, mV")

plt.savefig('g.png')

plt.show()