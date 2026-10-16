import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs('figures', exist_ok=True)

L = 1.5e-3
C = 47e-9

nu0 = 1 / (np.pi * np.sqrt(L * C))

nu = np.array([1, 3, 6, 10, 15, 20, 23, 24, 27, 30, 33])
phi = np.array([6.34, 16.77, 32.21, 50.83, 78.44,
                101.2, 118.6, 122.9, 136.0, 154.8, 166.0])

# МНК
a, b = np.polyfit(nu, phi, 1)
phi_fit = a * nu + b
r2 = 1 - np.sum((phi - phi_fit)**2) / np.sum((phi - phi.mean())**2)

# Теоретическая зависимость
x = np.linspace(0, 34, 400)
phi_theory = np.degrees(2 * np.arcsin(x * 1000 / nu0))

plt.figure(figsize=(7, 4.5))

plt.scatter(nu, phi, color='red', marker='+', s=200,
            label='Эксперимент')

plt.plot(x, a*x + b,
         label=fr'МНК: $\Delta\varphi={a:.3f}\nu+{b:.3f}$'
               '\n' + fr'$R^2={r2:.5f}$')

plt.plot(x, phi_theory, '--', label='Теория')

plt.xlabel(r'$\nu$, кГц')
plt.ylabel(r'$\Delta\varphi$, град')

plt.minorticks_on()
plt.grid(which='major', alpha=0.6)
plt.grid(which='minor', alpha=0.25, linestyle=':')
plt.legend()
plt.tight_layout()

plt.savefig('figures/model_phase.png', dpi=300)
plt.show()

print(f'МНК: a = {a:.4f}, b = {b:.4f}')
print(f'R² = {r2:.6f}')