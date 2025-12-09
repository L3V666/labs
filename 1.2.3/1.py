import numpy as np

m = 0.9347 + 0.8817
k = 4.04 * 1e-4
T = np.array([74.02, 74.21, 73.97, 74.28, 74.14]) / 20
print(k * m * T ** 2 - 7.3 * 1e-3)