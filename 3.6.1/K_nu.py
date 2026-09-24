import numpy as np

from matplotlib import pyplot as plt


# =========================
# Экспериментальные данные
# =========================

nu = np.array([
    100, 200, 300, 400,
    500, 600, 700, 800
])  # кГц

K = np.array([
    695 / 4452,
    295.4 / 3768,
    166.6 / 3151,
    82.2 / 1991,
    27.8 / 891,
    18.9 / 683,
    15.6 / 647,
    12.3 / 297
])


# =========================
# Параметры RC-цепочки
# =========================

R = 3 * 10**3       # Ом
C = 1000 * 10**-12  # Ф

tau_RC = R * C


# =========================
# Теоретическая зависимость
# =========================

tau_RC = 10 * 10**-6

nu_theory = np.linspace(0, 800, 1000)

K_theory = 1 / np.sqrt(
    1 + (2 * np.pi * nu_theory * 10**3 * tau_RC)**2
)


# =========================
# График
# =========================

plt.figure(figsize=(16, 9))


# Экспериментальные точки

plt.scatter(
    nu,
    K,
    s=200,
    color='red',
    label='Эксперимент'
)


# Теоретическая кривая

plt.plot(
    nu_theory,
    K_theory,
    label='Теория'
)


# =========================
# Оси
# =========================

plt.xlim(0, 850)

plt.ylim(0, 1.05)


# =========================
# Подписи
# =========================

plt.xlabel(
    r'$\nu$, кГц',
    fontsize=18
)

plt.ylabel(
    r'$K(\nu)$',
    fontsize=18
)


# =========================
# Оформление
# =========================

plt.tick_params(
    axis='both',
    labelsize=12
)

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

plt.legend(
    fontsize=14
)


# =========================
# Сохранение
# =========================

plt.savefig(
    '3.6.1/images/K_nu.png',
    dpi=300,
    bbox_inches='tight'
)

plt.show()