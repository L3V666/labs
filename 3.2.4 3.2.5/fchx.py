
import numpy as np
from matplotlib import pyplot as plt
from pathlib import Path


# =========================
# Данные
# =========================

nu = np.array([
    5.30, 5.37, 5.44, 5.51, 5.58,
    5.65, 5.72, 5.79, 5.86, 5.93,
    6.00, 6.07, 6.14, 6.21, 6.28,
    6.35, 6.42, 6.49, 6.56, 6.63, 6.70
])

# R1 = 400 Ом

U1 = np.array([
    3.35, 3.75, 4.10, 4.45, 5.15,
    5.70, 6.45, 7.15, 7.75, 8.25,
    8.30, 8.25, 8.00, 7.55, 7.00,
    6.45, 5.90, 5.40, 5.10, 4.80, 4.55
])

dt1 = np.array([
    75.6, 75.6, 73.2, 69.2, 66.8,
    62.8, 58.8, 54.8, 49.2, 43.2,
    38.4, 33.4, 28.4, 24.5, 21.2,
    18.6, 16.0, 14.1, 12.4, 10.1, 8.8
])

# R2 = 2000 Ом

U2 = np.array([
    1.91, 1.95, 1.98, 2.02, 2.05,
    2.08, 2.11, 2.14, 2.16, 2.18,
    2.20, 2.19, 2.18, 2.16, 2.14,
    2.12, 2.09, 2.06, 2.03, 2.00, 1.97
])

dt2 = np.array([
    48.8, 47.3, 45.5, 43.5, 41.5,
    39.7, 37.7, 35.7, 33.9, 32.2,
    30.5, 28.9, 27.4, 25.9, 24.6,
    23.3, 22.1, 20.9, 19.8, 18.7, 17.7
])

R1 = 400
R2 = 2000

nu01 = 6.012
nu02 = 6.000

U01 = 8.35
U02 = 2.20

L = 0.1
C = 7.07e-9
R_L = 200.26

Path('figures').mkdir(exist_ok=True)


# =========================
# Теоретическая АЧХ
# =========================

def achx_theor(x, Q):

    return 1 / np.sqrt(
        1 + Q**2 * (x - 1/x)**2
    )


Q1_theor = np.sqrt(L / C) / (R1 + R_L)
Q2_theor = np.sqrt(L / C) / (R2 + R_L)

print('Q1_theor =', Q1_theor)
print('Q2_theor =', Q2_theor)


# =========================
# Поиск пересечений
# =========================

def intersections(x, y, level):

    result = []

    for i in range(len(x) - 1):

        if (y[i] - level) * (y[i+1] - level) < 0:

            xc = x[i] + (
                (level - y[i]) *
                (x[i+1] - x[i]) /
                (y[i+1] - y[i])
            )

            result.append(xc)

    return result


# =========================
# Оформление графиков
# =========================

def graph_style():

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


# =========================
# 7. Нормированные АЧХ
# =========================

x1 = nu / nu01
y1 = U1 / U01

x2 = nu / nu02
y2 = U2 / U02

x_theor = np.linspace(0.85, 1.15, 1000)

plt.figure(figsize=(16, 9))

line1, = plt.plot(
    x1, y1,
    linewidth=1.5,
    label=r'$R=400$ Ом'
)

line2, = plt.plot(
    x2, y2,
    linewidth=1.5,
    label=r'$R=2000$ Ом'
)

# Экспериментальные точки

plt.scatter(
    x1, y1,
    marker='+',
    s=200,
    color='red'
)

plt.scatter(
    x2, y2,
    marker='+',
    s=200,
    color='red'
)

# Теоретические кривые

plt.plot(
    x_theor,
    achx_theor(x_theor, Q1_theor),
    '--',
    color=line1.get_color(),
    label=r'Теория, $R=400$ Ом'
)

plt.plot(
    x_theor,
    achx_theor(x_theor, Q2_theor),
    '--',
    color=line2.get_color(),
    label=r'Теория, $R=2000$ Ом'
)

plt.xlim(0.85, 1.15)
plt.ylim(0, 1.1)

plt.xlabel(
    r'Нормированная частота ($\nu/\nu_0$)',
    fontsize=18
)

plt.ylabel(
    r'Нормированная амплитуда ($U_C/U_0$)',
    fontsize=18
)

plt.legend(fontsize=13)

graph_style()

plt.savefig(
    'figures/achx.png',
    dpi=300,
    bbox_inches='tight'
)

plt.show()


# =========================
# 8. Добротность по АЧХ
# =========================

for R, U, nu0, U0 in [
    (R1, U1, nu01, U01),
    (R2, U2, nu02, U02)
]:

    level = U0 / np.sqrt(2)

    cross = intersections(
        nu, U, level
    )

    print(f'\nАЧХ: R = {R} Ом')
    print('U0/sqrt(2) =', level)

    if len(cross) == 2:

        nu_minus, nu_plus = cross

        delta_nu = nu_plus - nu_minus

        width_omega = (
            2 * np.pi * delta_nu * 1000
        )

        Q = nu0 / delta_nu

        print('nu_minus =', nu_minus)
        print('nu_plus =', nu_plus)
        print('2DeltaOmega =', width_omega)
        print('Q_achx =', Q)

    else:

        print('Обе границы АЧХ не найдены')


# =========================
# 9. Определение Q по ФЧХ
# =========================

# nu — кГц, dt — мкс
# Минус соответствует запаздыванию

phi1 = -2 * np.pi * nu * dt1 / 1000
phi2 = -2 * np.pi * nu * dt2 / 1000

omega = 2 * np.pi * nu * 1000


# Отражение нижней части ФЧХ
# относительно -pi/2

phi_reflected = np.where(
    phi1 < -np.pi / 2,
    -np.pi - phi1,
    np.nan
)

plt.figure(figsize=(16, 9))

plt.plot(
    omega,
    phi1,
    linewidth=1.5,
    label='ФЧХ при R = 400 Ом'
)

plt.scatter(
    omega,
    phi1,
    marker='+',
    s=200,
    color='red'
)

plt.plot(
    omega,
    phi_reflected,
    '--',
    linewidth=1.5,
    label='Отражённая часть'
)

plt.axhline(
    -np.pi / 2,
    linestyle='--',
    color='gray'
)

plt.axhline(
    -np.pi / 4,
    linestyle='--',
    color='gray'
)

plt.xlabel(
    r'Циклическая частота ($\omega$), рад/с',
    fontsize=18
)

plt.ylabel(
    r'Разность фаз ($\Delta\varphi$), рад',
    fontsize=18
)

plt.legend(fontsize=14)

graph_style()

plt.savefig(
    'figures/fchx_Q.png',
    dpi=300,
    bbox_inches='tight'
)

plt.show()


# =========================
# Расчёт Q по ФЧХ
# =========================

for R, phi, nu0 in [
    (R1, phi1, nu01),
    (R2, phi2, nu02)
]:

    # Уровни -3pi/4 и -pi/4
    # соответствуют ширине после отражения

    left = intersections(
        nu,
        phi,
        -3 * np.pi / 4
    )

    right = intersections(
        nu,
        phi,
        -np.pi / 4
    )

    print(f'\nФЧХ: R = {R} Ом')

    if left and right:

        nu_minus = left[0]
        nu_plus = right[0]

        delta_nu = nu_plus - nu_minus

        delta_omega = (
            2 * np.pi * delta_nu * 1000
        )

        Q = nu0 / delta_nu

        print('nu_minus =', nu_minus)
        print('nu_plus =', nu_plus)
        print('DeltaOmega =', delta_omega)
        print('Q_fchx =', Q)

    else:

        print('Обе границы ФЧХ не найдены')


# =========================
# 10. ФЧХ при двух R
# =========================

plt.figure(figsize=(16, 9))

plt.plot(
    omega,
    phi1,
    linewidth=1.5,
    label=r'$R=400$ Ом'
)

plt.plot(
    omega,
    phi2,
    linewidth=1.5,
    label=r'$R=2000$ Ом'
)

plt.scatter(
    omega,
    phi1,
    marker='+',
    s=200,
    color='red'
)

plt.scatter(
    omega,
    phi2,
    marker='+',
    s=200,
    color='red'
)

plt.xlabel(
    r'Циклическая частота ($\omega$), рад/с',
    fontsize=18
)

plt.ylabel(
    r'Разность фаз ($\Delta\varphi$), рад',
    fontsize=18
)

plt.legend(fontsize=14)

graph_style()

plt.savefig(
    'figures/fchx.png',
    dpi=300,
    bbox_inches='tight'
)

plt.show()
