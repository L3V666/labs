import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs('figures', exist_ok=True)

nu = np.array([1, 4, 7, 11, 20, 25, 30, 35, 40])
U0 = np.array([27.8, 28.0, 27.6, 29.0, 28.4,
               27.2, 26.6, 26.6, 26.1])
Un = np.array([26.0, 26.0, 24.6, 25.2, 21.8,
               19.0, 18.5, 17.3, 17.3])
dt = np.array([252, 7, 31, 12, 5.4, 15, 12, 3.2, 4.6])

m = np.array([0, 1, 2, 3, 5, 6, 8, 9, 10])
sign = np.array([1, 1, -1, -1, 1, 1, -1, -1, 1])

l = 50.085
R0 = 50

phi = 2 * np.pi * (m + sign * nu * dt / 1000)

alpha = np.log(U0 / Un) / l
k = phi / l
omega = 2 * np.pi * nu * 1e6

x = omega**2 / 1e16
y = k**2 - alpha**2

# МНК
a, b = np.polyfit(x, y, 1)
y_fit = a * x + b
r2 = 1 - np.sum((y - y_fit)**2) / np.sum((y - y.mean())**2)

# Погонные параметры в СИ
slope = a / 1e16
Lx = R0 * np.sqrt(slope)
Cx = np.sqrt(slope) / R0
v = 1 / np.sqrt(slope)

# График
xx = np.linspace(0, x.max() * 1.05, 300)

plt.figure(figsize=(7, 4.5))
plt.scatter(x, y, color='red', marker='+', s=200,
            label='Эксперимент')

plt.plot(xx, a * xx + b,
         label=fr'МНК: $y={a:.4f}x+{b:.4f}$'
               '\n'
               fr'$R^2={r2:.5f}$')

plt.xlabel(r'$\omega^2$, $10^{16}$ с$^{-2}$')
plt.ylabel(r'$k^2-\alpha^2$, м$^{-2}$')

plt.minorticks_on()
plt.grid(which='major', alpha=0.6)
plt.grid(which='minor', alpha=0.25, linestyle=':')
plt.legend()

plt.tight_layout()
plt.savefig('figures/line_params.png', dpi=300)
plt.show()

print(f'a = {slope:.5e} с²/м²')
print(f'b = {b:.6f} м⁻²')
print(f'R² = {r2:.6f}')
print(f'Lx = {Lx * 1e9:.2f} нГн/м')
print(f'Cx = {Cx * 1e12:.2f} пФ/м')
print(f'V = {v:.3e} м/с')