import numpy as np

from matplotlib import pyplot as plt

from scipy.optimize import curve_fit


# =========================
# Данные
# =========================

T = np.array([
    200, 800, 1400, 2000, 2600,
    3200, 3800, 4400, 5000
])

delta_nu = np.array([
    4.98, 1.32, 0.72, 0.47, 0.40,
    0.31, 0.27, 0.22, 0.20
])


# =========================
# 1/T
# =========================

x_data = 1000 / T


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

plt.xlim(0, 5.5)

plt.ylim(0, 5.5)


# =========================
# Подписи
# =========================

plt.xlabel(
    r'$1/T$, кГц',
    fontsize=18
)

plt.ylabel(
    r'$\delta\nu$, кГц',
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

plt.savefig(
    '3.6.1/images/delta_nu_1_T.png'
)

plt.show()