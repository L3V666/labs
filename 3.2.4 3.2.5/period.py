
import numpy as np

from matplotlib import pyplot as plt

from scipy.optimize import curve_fit

from pathlib import Path


# =========================
# Данные
# =========================

L = 0.1           # Гн
C0 = 0.00107      # мкФ

C = np.array([
    0.001, 0.002, 0.003,
    0.004, 0.005, 0.006,
    0.007, 0.008, 0.009
])

T_exp = np.array([
    90, 110, 128, 146, 156,
    166, 180, 190, 200
])


# =========================
# Теоретический период
# =========================

T_theor = 2 * np.pi * np.sqrt(
    L * (C + C0) * 1e-6
) * 1e6

x_data = T_theor
y_data = T_exp


# =========================
# Линейная функция
# =========================

def linear_func(x, a, b):

    return a * x + b


# =========================
# Метод наименьших квадратов
# =========================

def lsm(x, y):

    params, covariance = curve_fit(
        linear_func,
        x,
        y
    )

    xs = np.linspace(
        0,
        210,
        1000
    )

    ys = linear_func(
        xs,
        params[0],
        params[1]
    )

    a, b = params

    da, db = np.sqrt(
        np.diag(covariance)
    )

    return xs, ys, a, b, da, db


# =========================
# График
# =========================

plt.figure(figsize=(16, 9))


# Экспериментальные точки

plt.scatter(
    x_data,
    y_data,
    marker='+',
    s=200,
    color='red'
)


# Аппроксимация

x, y, a, b, da, db = lsm(
    x_data,
    y_data
)

plt.plot(
    x,
    y
)


# =========================
# Результаты
# =========================

print('a =', a)
print('b =', b)
print('da =', da)
print('db =', db)


# =========================
# Оси
# =========================

plt.xlim(0, 210)

plt.ylim(0, 210)


# =========================
# Подписи
# =========================

plt.xlabel(
    r'$T_{\mathrm{теор}}$, мкс',
    fontsize=18
)

plt.ylabel(
    r'$T_{\mathrm{эксп}}$, мкс',
    fontsize=18
)


# =========================
# Размер подписей
# =========================

plt.tick_params(
    axis='both',
    labelsize=12
)


# =========================
# Сетка
# =========================

plt.grid(
    True,
    which='major',
    linestyle='-',
    linewidth=0.5
)

plt.grid(
    True,
    which='minor',
    linestyle='-',
    linewidth=0.3
)

plt.minorticks_on()


# =========================
# Сохранение
# =========================

Path('figures').mkdir(exist_ok=True)

plt.savefig(
    '3.2.4 3.2.5/figures/period.png',
    bbox_inches='tight'
)

plt.show()
