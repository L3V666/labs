import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

a1 = np.array([[1, 136.99],
                [2, 263.16],
                [3, 434.78],
                [4, 555.56],
                [5, 689.66],
                [6, 869.57],
                [7, 1000],
                [8, 1111.11],
                [9, 1250],
                [10, 1428.57]])

a2 = np.array([[1, 166.67],
                [2, 336.40],
                [3, 504.70],
                [4, 674],
                [5, 843.80],
                [6, 1012.20],
                [7,  1183.50],
                [8, 1354.90],
                [9, 1526],
                [10, 1698.50]])

a3 = np.array([[1, 190],
                [2, 381],
                [3, 572.4],
                [4, 763],
                [5, 954.6],
                [6, 1146],
                [7,  1338.7],
                [8, 1533],
                [9, 1725],
                [10, 1920]])

a4 = np.array([[1, 209],
                [2, 419],
                [3, 629],
                [4, 839],
                [5, 1049],
                [6, 1259],
                [7, 1472],
                [8, 1683],
                [9, 1895],
                [10, 2108]])

a5 = np.array([[1, 229],
                [2, 458],
                [3, 688],
                [4, 917],
                [5, 1147],
                [6, 1377],
                [7, 1608],
                [8, 1840],
                [9, 2071],
                [10, 2303]])

plt.scatter(a1[:, 0], a1[:, 1], marker='+')
plt.scatter(a2[:, 0], a2[:, 1], marker='+')
plt.scatter(a3[:, 0], a3[:, 1], marker='+')
plt.scatter(a4[:, 0], a4[:, 1], marker='+')
plt.scatter(a5[:, 0], a5[:, 1], marker='+')

def linear_func(x, a, b):
    return a * x + b

def lsm(x, y): 
    params, covariance = curve_fit(linear_func, x, y)
    x = np.linspace(min(x), max(x), 1000)
    y = linear_func(x, params[0], params[1])
    return x, y, params[0], np.sqrt(np.diag(covariance))

for a in [a1, a2, a3, a4, a5]:
    a = np.array(a)
    l = lsm(a[:, 0], a[:, 1])
    x, y = l[0:2]
    print(l[2::])
    if np.all(a == a1):
        plt.plot(x, y, label='m = 1087,2 г')
    if np.all(a == a2):
        plt.plot(x, y, label='m = 1574,6 г')
    if np.all(a == a3):
        plt.plot(x, y, label='m = 2071,8 г')  
    if np.all(a == a4):
        plt.plot(x, y, label='m = 2566,2 г')  
    if np.all(a == a5):
        plt.plot(x, y, label='m = 3060,1 г')


plt.grid(True, which='major', linestyle='-', linewidth=0.5)
plt.grid(True, which='minor', linestyle='-', linewidth=0.3)

plt.minorticks_on()

plt.legend()

plt.xlabel('n')
plt.ylabel('nu')

plt.savefig('2.png')

plt.show()