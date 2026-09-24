import numpy as np

from matplotlib import pyplot as plt

from scipy.optimize import curve_fit


# =========================
# Данные
# =========================

nu_0 = np.array([
    30, 40, 50, 50, 50, 50, 50
])

T = np.array([
    1, 1, 1, 1, 1, 2, 2
])

N = np.array([
    5, 5, 5, 5, 10, 5, 10
])

delta_nu = np.array([
    6.05, 7.86, 9.98, 9.94, 4.87, 10.09, 5.03
])


# =========================
# Расчёт 1/tau
# =========================

# tau = N / nu_0
# nu_0 задана в кГц, поэтому 1/tau получается в кГц

inv_tau = nu_0 / N


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
    inv_tau,
    delta_nu,
    marker='+',
    s=200,
    color='red'
)


# Линейная аппроксимация

x, y, a, b, da, db = lsm(
    inv_tau,
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

plt.xlim(0, 22)

plt.ylim(0, 12)


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
    '3.6.1/images/delta_nu_1_tau_B.png'
)

plt.show()