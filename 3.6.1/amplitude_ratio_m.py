import numpy as np

from matplotlib import pyplot as plt

from scipy.optimize import curve_fit


# =========================
# Данные
# =========================

m = np.array([
    10, 20, 30, 40, 50, 80, 100
])

a_exp = np.array([
    0.05, 0.10, 0.16, 0.21, 0.27, 0.42, 0.51
])


# =========================
# Перевод m из процентов
# =========================

m = m / 100


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
        1.1,
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
    m,
    a_exp,
    marker='+',
    s=200,
    color='red'
)


# Линейная аппроксимация

x, y, a, b, da, db = lsm(
    m,
    a_exp
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

plt.xlim(0, 1.1)

plt.ylim(0, 0.6)


# =========================
# Подписи
# =========================

plt.xlabel(
    r'$m$',
    fontsize=18
)

plt.ylabel(
    r'$a_{\mathrm{бок}}/a_{\mathrm{осн}}$',
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
    '3.6.1/images/amplitude_ratio_m.png'
)

plt.show()