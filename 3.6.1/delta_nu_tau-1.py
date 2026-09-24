import numpy as np

from matplotlib import pyplot as plt

from scipy.optimize import curve_fit


# =========================
# Данные
# =========================

tau = np.array([
    20, 40, 60, 80, 100,
    120, 140, 160, 180, 200
])

delta_nu = np.array([
    48.62, 24.93, 16.44, 12.52, 9.95,
    7.61, 6.71, 5.50, 5.19, 4.93
])


# =========================
# 1/tau
# =========================

x_data = 1000 / tau


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
        2 * max(x),
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
    delta_nu,
    marker='+',
    s=200,
    color='red'
)


# Аппроксимация

x, y, a, b, da, db = lsm(
    x_data,
    delta_nu
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

plt.xlim(0, 55)

plt.ylim(0, 55)


# =========================
# Подписи
# =========================

plt.xlabel(
    r'$1/\tau$, кГц',
    fontsize=18
)

plt.ylabel(
    r'$\Delta\nu$, кГц',
    fontsize=18
)


# =========================
# Размер подписей осей
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

plt.savefig(
    '3.6.1/images/delta_nu_1_tau.png'
)


plt.show()