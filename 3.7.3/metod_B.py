import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs('figures', exist_ok=True)

nu = np.array([1, 4, 7, 11, 20, 25, 30, 35, 40])
U0 = np.array([27.8, 28.0, 27.6, 29.0, 28.4, 27.2, 26.6, 26.6, 26.1])
Un = np.array([26.0, 26.0, 24.6, 25.2, 21.8, 19.0, 18.5, 17.3, 17.3])
dt = np.array([252, 7, 31, 12, 5.4, 15, 12, 3.2, 4.6])

m = np.array([0, 1, 2, 3, 5, 6, 8, 9, 10])
sign = np.array([1, 1, -1, -1, 1, 1, -1, -1, 1])

l = 50.085
Cx = 101.5e-12
d = 1.37e-3
mu0 = 4 * np.pi * 1e-7

phi = 2 * np.pi * (m + sign * nu * dt / 1000)
alpha = np.log(U0 / Un) / l
k = phi / l

x = nu**1.5
y = alpha * k * 1e3

# МНК через начало координат
a = np.sum(x * y) / np.sum(x**2)
y_fit = a * x
r2 = 1 - np.sum((y - y_fit)**2) / np.sum((y - y.mean())**2)

# Проводимость
a_SI = a * 1e-12
sigma = 4 * np.pi * mu0 * Cx**2 / (d**2 * a_SI**2)

xx = np.linspace(0, x.max() * 1.05, 300)

plt.figure(figsize=(7, 4.5))
plt.scatter(x, y, color='red', marker='+', s=200,
            label='Эксперимент')
plt.plot(xx, a * xx,
         label=fr'МНК: $y={a:.5f}x$' + '\n'
               + fr'$R^2={r2:.5f}$')

plt.xlabel(r'$(\nu/\mathrm{МГц})^{3/2}$')
plt.ylabel(r'$\alpha k$, $10^{-3}$ м$^{-2}$')

plt.xlim(0, xx.max())
plt.ylim(bottom=0)
plt.minorticks_on()
plt.grid(which='major', alpha=0.55)
plt.grid(which='minor', alpha=0.25, linestyle=':')
plt.legend()

plt.tight_layout()
plt.savefig('figures/metod_B.png', dpi=300)
plt.show()

print(f'a = {a_SI:.5e}')
print(f'R² = {r2:.5f}')
print(f'sigma = {sigma:.3e} См/м')