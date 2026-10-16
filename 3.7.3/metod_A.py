import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs('figures', exist_ok=True)

nu = np.array([1, 4, 7, 11, 20, 25, 30, 35, 40])
U0 = np.array([27.8, 28, 27.6, 29, 28.4, 27.2, 26.6, 26.6, 26.1])
Un = np.array([26, 26, 24.6, 25.2, 21.8, 19, 18.5, 17.3, 17.3])

l = 50.085
d = 1.37e-3
R0 = 50
mu0 = 4 * np.pi * 1e-7

alpha = np.log(U0 / Un) / l

x = np.sqrt(nu)
y = alpha * 1e3

# МНК через начало координат
a = np.sum(x * y) / np.sum(x**2)
y_fit = a * x

r2 = 1 - np.sum((y - y_fit)**2) / np.sum((y - y.mean())**2)

# Проводимость в СИ
a_SI = a * 1e-6
sigma = mu0 / (np.pi * (R0 * d * a_SI)**2)

xx = np.linspace(0, 6.8, 300)

plt.figure(figsize=(7, 4.5))
plt.scatter(x, y, color='red', marker='+', s=200,
            label='Эксперимент')
plt.plot(xx, a * xx,
         label=fr'МНК: $y={a:.3f}x$' + '\n'
               + fr'$R^2={r2:.4f}$')

plt.xlabel(r'$\sqrt{\nu/\mathrm{MHz}}$')
plt.ylabel(r'$\alpha$, $10^{-3}$ м$^{-1}$')

plt.xlim(0, 6.8)
plt.ylim(bottom=0)

plt.minorticks_on()
plt.grid(which='major', alpha=0.55)
plt.grid(which='minor', alpha=0.25, linestyle=':')
plt.legend()

plt.tight_layout()
plt.savefig('figures/metod_A.png', dpi=300)
plt.show()

print(f'a = {a_SI:.4e}')
print(f'R² = {r2:.4f}')
print(f'sigma = {sigma:.3e} См/м')