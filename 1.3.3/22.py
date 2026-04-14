import numpy as np
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

coord = np.array(pd.read_excel("11.ods", sheet_name=3))
plt.plot(coord[:, 1], coord[:, 0])
#x, y, a, b, da, db = lsm(coord[:12, 0], coord[:12, 1])
#plt.plot(x, y)
#print(a, b, da)

#plt.xlim(0, 0.6)
plt.ylim(0, 230)

plt.xlabel('x, м')
plt.ylabel('$\Delta$P/l, Па/м')

plt.grid(True, which='major', linestyle='-', linewidth=0.5)
plt.grid(True, which='minor', linestyle='-', linewidth=0.3)
plt.minorticks_on()

plt.savefig('4.png')

plt.show() 