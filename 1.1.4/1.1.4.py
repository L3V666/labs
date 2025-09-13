import numpy as np
import math
from matplotlib import pyplot as plt
import pandas as pd

with open('experiment.txt', 'r') as file:
    data = np.array(list(map(int, file.readlines()[2:-2])))

tau = 80

t = np.array([], dtype=int)
for i in range(0, len(data), tau):
    t = np.append(t, np.sum(data[i:i + tau]))


pd.DataFrame(t.reshape(5, 10)).to_csv('t80.csv', index=False, encoding='utf-8-sig')


def w_n(n, t):
    return np.mean(t) ** n / math.factorial(n) * np.exp(1) ** (-np.mean(t))

w = np.array([])

x = np.array([])

for i in range(0, np.max(t) + 1):
    w = np.append(w, w_n(i, t))
    x = np.append(x, i)

y = np.array([])

for i in range(0, np.max(t) + 1):
    y = np.append(y, np.count_nonzero(t == i) / (4000 / tau))

plt.bar(x, y)
plt.plot(x, w, color='red')

avg_n = np.sum(t) / len(t) 
print(f'avg_n {avg_n}')

sigma_n = np.sqrt(np.sum((t - avg_n) ** 2) / len(t))
print(f'sigma_n {sigma_n}')

sigma_avg_n = sigma_n / np.sqrt(len(t))
print(f'sigma_avg_n {sigma_avg_n}')

j = avg_n / tau
print(f'j {j}')

plt.savefig('80.png')

plt.show()