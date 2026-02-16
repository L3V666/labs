from matplotlib import pyplot as plt
import numpy as np

nx = np.linspace(296, 312, 17)
ny = np.array([52, 54.3, 57.2, 61, 64.4, 68.4, 71.9, 75.3, 80.6, 86.1, 90.9, 95.1, 101.2, 106.7, 111.4, 118.5, 124.4]) * 133.3

ox = np.array([312, 311, 310, 308, 306, 304, 302, 300, 298, 296])
oy = np.array([121.6, 116.5, 110.9, 99.1, 90.7, 74.6, 71.9, 64.7, 58.6, 53.8]) * 133.3

plt.scatter(nx, ny, marker='+', c='red', s=50)

plt.scatter(ox, oy, marker='+', c='blue', s=50)

plt.xlabel('$T, K$')
plt.ylabel('$P, Па$')

plt.grid(True, which='major', linestyle='-', linewidth=0.5)
plt.grid(True, which='minor', linestyle='-', linewidth=0.3)
plt.minorticks_on()

print(f'Среднее значение x при нагреве: {np.mean(nx)}')
print(f'Средний квадрат x при нагреве: {np.mean(nx ** 2)}')
print(f'Квадрат среднего x при нагреве: {np.mean(nx) ** 2}')
print(f'Среднее произведения xy: {np.mean(nx * ny)}')
print(f'Среднее значение y при нагреве: {np.mean(ny)}')
print(f'Средний квадрат y при нагреве: {np.mean(ny ** 2)}')
print(f'Квадрат среднего y при нагреве: {np.mean(ny) ** 2}')
print()
nb = (np.mean(nx * ny) - np.mean(nx) * np.mean(ny)) / (np.mean(nx ** 2) - np.mean(nx) ** 2)
print(nb)
print(f'Среднее значение x при охлаждении: {np.mean(ox)}')
print(f'Средний квадрат x при охлаждении: {np.mean(ox ** 2)}')
print(f'Квадрат среднего x при охлаждении: {np.mean(ox) ** 2}')
print(f'Среднее произведения xy: {np.mean(ox * oy)}')
print(f'Среднее значение y при охлаждении: {np.mean(oy)}')
print(f'Средний квадрат y при охлаждении: {np.mean(oy ** 2)}')
print(f'Квадрат среднего y при охлаждении: {np.mean(oy) ** 2}')

#y = a + bx
nb = (np.mean(nx * ny) - np.mean(nx) * np.mean(ny)) / (np.mean(nx ** 2) - np.mean(nx) ** 2)
na = np.mean(ny) - nb * np.mean(nx)
plt.plot([min(nx), max(nx)], [na + nb * min(nx), na + nb * max(nx)], label='Апроксимация прямой нагрева', c='red', ls='--')

ob = (np.mean(ox * oy) - np.mean(ox) * np.mean(oy)) / (np.mean(ox ** 2) - np.mean(ox) ** 2)
oa = np.mean(oy) - ob * np.mean(ox)
plt.plot([min(ox), max(ox)], [oa + ob * min(ox), oa + ob * max(ox)], label='Апроксимация прямой охлаждения', c='blue', ls='--')

plt.legend()

plt.savefig('P.png')

print(oy[7])

plt.show()