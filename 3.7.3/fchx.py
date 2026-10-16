import numpy as np
import matplotlib.pyplot as plt

nu = np.array([1, 4, 7, 11, 20, 25, 30, 35, 40])
U0 = np.array([27.8, 28.0, 27.6, 29.0, 28.4, 27.2, 26.6, 26.6, 26.1])
Un = np.array([26.0, 26.0, 24.6, 25.2, 21.8, 19.0, 18.5, 17.3, 17.3])
dt = np.array([252, 7, 31, 12, 5.4, 15, 12, 3.2, 4.6])

m = np.array([0, 1, 2, 3, 5, 6, 8, 9, 10])
sign = np.array([1, 1, -1, -1, 1, 1, -1, -1, 1])

A = Un / U0
phi = 2 * np.pi * (m + sign * nu * dt / 1000)

# АЧХ
plt.figure(figsize=(7, 4.5))
plt.scatter(nu, A, color='red', marker='+', s=200)
plt.xlabel(r'$\nu$, МГц')
plt.ylabel(r'$U_{\mathrm{н}}/U_0$')
plt.minorticks_on()
plt.grid(which='major', alpha=0.6)
plt.grid(which='minor', alpha=0.25, linestyle=':')
plt.tight_layout()
plt.savefig('figures/achx.png', dpi=300)
plt.show()

# ФЧХ
a, b = np.polyfit(nu, phi, 1)

phi_fit = a * nu + b
r2 = 1 - np.sum((phi - phi_fit)**2) / np.sum((phi - phi.mean())**2)

x = np.linspace(nu.min(), nu.max(), 300)

plt.figure(figsize=(7, 4.5))

plt.scatter(nu, phi, color='red', marker='+',
            s=200, label='Эксперимент')

plt.plot(x, a*x + b,
         label=fr'МНК: $\Delta\varphi={a:.3f}\nu+{b:.3f}$'
               '\n'
               fr'$R^2={r2:.5f}$')

plt.xlabel(r'$\nu$, МГц')
plt.ylabel(r'$\Delta\varphi$, рад')

plt.minorticks_on()
plt.grid(which='major', alpha=0.6)
plt.grid(which='minor', alpha=0.25, linestyle=':')
plt.legend()

plt.tight_layout()
plt.savefig('figures/fchx.png', dpi=300)
plt.show()

# Проверка линейности ФЧХ
a, b = np.polyfit(nu, phi, 1)
r2 = 1 - np.sum((phi - (a * nu + b))**2) / np.sum((phi - phi.mean())**2)

l = 50.085
v = 2 * np.pi * l * 1e6 / a

print(f"Наклон ФЧХ: {a:.4f} рад/МГц")
print(f"R² = {r2:.6f}")
print(f"Фазовая скорость: {v:.3e} м/с")