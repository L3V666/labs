import numpy as np

from matplotlib import pyplot as plt

from scipy.optimize import curve_fit

import os


# =========================
# Данные
# =========================

R = np.array([
    400, 640, 800, 960, 1200,
    1440, 1600, 1760, 2000
])

U1 = np.array([
    580, 500, 444, 408, 356,
    308, 284, 256, 216
])

U2 = np.array([
    392, 280, 220, 176, 128,
    92, 76, 60, 44
])

R_L = 200.26


# =========================
# Расчёт величин
# =========================

R_sigma = R + R_L

theta = np.log(U1 / U2)

x_data = 1 / (R_sigma ** 2)
y_data = 1 / (theta ** 2)


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
        20 * max(x),
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
    s=400,
    color='red'
)


# Аппроксимация

x, y, a, b, da, db = lsm(
    x_data[-5:],
    y_data[-5:]
)

R_cr = 2 * np.pi * np.sqrt(a)
dR_cr = R_cr * da / (2 * a)

print('a =', a)
print('b =', b)
print('da =', da)
print('db =', db)
print('R_cr =', R_cr)
print('dR_cr =', dR_cr)

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

plt.xlim(0, 1.1 * max(x_data))
plt.ylim(0, 1.1 * max(y_data))


# =========================
# Подписи
# =========================

plt.xlabel(
    r'$1/R_\Sigma^2$, Ом$^{-2}$',
    fontsize=18
)

plt.ylabel(
    r'$1/\Theta^2$',
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
# Научная запись для оси X
# =========================

plt.ticklabel_format(
    axis='x',
    style='sci',
    scilimits=(0, 0)
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

os.makedirs('figures', exist_ok=True)

plt.savefig(
    'figures/inv_theta_inv_r2.png',
    dpi=300,
    bbox_inches='tight'
)

plt.show()