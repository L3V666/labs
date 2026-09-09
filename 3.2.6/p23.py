import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

# Экспериментальные данные
R = np.array([50000, 40000, 30000, 20000, 10000, 2000]) + 610
x_max = np.array([0.215, 0.204, 0.192, 0.176, 0.146, 0.072])

# Аппроксимирующая функция
def approximation(R, a, b, c):
    return a + b / (R + c)

# Находим параметры аппроксимации
popt, pcov = curve_fit(
    approximation,
    R,
    x_max,
    p0=[0.24, -2000, 8000],
    maxfev=100000
)

a, b, c = popt

# Точки для построения гладкой кривой
R_curve = np.linspace(0, R.max(), 1000)
x_curve = approximation(R_curve, a, b, c)

# Критическое отклонение
x0 = 0.183       # м
Theta0 = 0.27

x_free = x0 * np.exp(Theta0 / 4)
x_critical = x_free / np.e

# Находим R+R0, при котором аппроксимация достигает
# критического отклонения
R_sum_critical = -c + b / (x_critical - a)

# Критическое сопротивление
R0 = 610
R_critical = R_sum_critical - R0

# Вывод результатов
print(f'x_free = {x_free:.5f} м')
print(f'x_critical = {x_critical:.5f} м')
print(f'R + R0 = {R_sum_critical:.1f} Ом')
print(f'R_critical = {R_critical:.1f} Ом')
print(f'R_critical = {R_critical / 1000:.2f} кОм')

# График
plt.figure(figsize=(8, 5))

# Экспериментальные точки
plt.scatter(
    R,
    x_max,
    marker='+',
    s=200,
    color='red',
    label='Экспериментальные данные'
)

# Аппроксимирующая кривая
plt.plot(
    R_curve,
    x_curve,
    label='Аппроксимация'
)

# Критическое отклонение
plt.axhline(
    x_critical,
    linestyle='--',
    label=fr'$x_{{\max}}^{{кр}} = {x_critical:.3f}\ м$'
)

# Вертикаль из точки пересечения
plt.axvline(
    R_sum_critical,
    linestyle='--',
    label=fr'$R+R_0 = {R_sum_critical:.0f}\ \Omega$'
)

# Точка критического режима
plt.scatter(
    [R_sum_critical],
    [x_critical],
    s=80,
    zorder=5
)

plt.xlim(0, 53000)
plt.ylim(0, 0.23)

plt.xlabel('$R+R_0$, Ом', fontsize=16)
plt.ylabel('$x_{max}$, м', fontsize=16)

plt.tick_params(axis='both', labelsize=12)

plt.grid(True, which='major', linestyle='-', linewidth=0.5)
plt.grid(True, which='minor', linestyle='-', linewidth=0.3)
plt.minorticks_on()

plt.legend()

plt.tight_layout()
plt.savefig('3.2.6/p23.png', dpi=300)
plt.show()