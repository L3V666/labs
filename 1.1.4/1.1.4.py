import numpy as np
import math
from matplotlib import pyplot as plt
import pandas as pd

with open('experiment.txt', 'r') as file:
    data = np.array(list(map(int, file.readlines()[2:-2])))

t10 = np.array([], dtype=int)
t20 = np.array([], dtype=int)
t40 = np.array([], dtype=int)
t80 = np.array([], dtype=int)
for i in range(0, len(data), 10):
    t10 = np.append(t10, np.sum(data[i:i + 10]))
for i in range(0, len(data), 20):
    t20 = np.append(t20, np.sum(data[i:i + 20]))
for i in range(0, len(data), 40):
    t40 = np.append(t40, np.sum(data[i:i + 40]))
for i in range(0, len(data), 80):
    t80 = np.append(t80, np.sum(data[i:i + 80]))


df = pd.DataFrame(t80.reshape(5, 10))
print(t80.reshape(5, 10))
df.to_csv('массив.csv', index=False, encoding='utf-8-sig')


def w(n, t):
    return np.mean(t) ** n / math.factorial(n) * np.exp(1) ** (-np.mean(t))

w10 = np.array([])
w20 = np.array([])
w40 = np.array([])
w80 = np.array([])

x10 = np.array([])
x20 = np.array([])
x40 = np.array([])
x80 = np.array([])

for i in range(0, np.max(t10) + 1):
    w10 = np.append(w10, w(i, t10))
    x10 = np.append(x10, i)
for i in range(0, np.max(t20) + 1):
    w20 = np.append(w20, w(i, t20))
    x20 = np.append(x20, i)
for i in range(0, np.max(t40) + 1):
    w40 = np.append(w40, w(i, t40))
    x40 = np.append(x40, i)
for i in range(0, np.max(t80) + 1):
    x80 = np.append(x80, i)
    w80 = np.append(w80, w(i, t80))

y10 = np.array([])
y20 = np.array([])
y40 = np.array([])
y80 = np.array([])

for i in range(0, np.max(t10) + 1):
    y10 = np.append(y10, np.count_nonzero(t10 == i) / 400)
for i in range(0, np.max(t20) + 1):
    y20 = np.append(y20, np.count_nonzero(t20 == i) / 200)
for i in range(0, np.max(t40) + 1):
    y40 = np.append(y40, np.count_nonzero(t40 == i) / 100)
for i in range(0, np.max(t80) + 1):
    y80 = np.append(y80, np.count_nonzero(t80 == i) / 50)

plt.bar(x20, y20)

plt.show()