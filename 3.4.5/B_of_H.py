from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

# Экспериментальные координаты крайних точек частных петель, деления
X = [
    [2.5, 2.1, 1.6, 1.4, 1.2, 1.0, 0.8, 0.7],
    [3.9, 3.2, 3.0, 2.8, 2.6, 2.4, 2.4, 2.3],
    [2.1, 1.5, 1.2, 1.1, 1.0, 0.9, 0.8, 0.7],
]
Y = [
    [2.5, 2.4, 2.0, 1.8, 1.6, 1.4, 1.2, 1.0],
    [3.5, 3.0, 2.7, 2.0, 1.4, 1.2, 1.0, 0.6],
    [3.1, 2.6, 2.4, 2.2, 1.6, 1.3, 1.0, 0.8],
]

# Параметры тороидов в СИ
N0 = np.array([35, 35, 45])
Ni = np.array([350, 220, 400])
l = np.array([0.10, 0.24, 0.25])  # м
S = np.array([1.2e-4, 3.8e-4, 3.0e-4])  # м²
R0 = 0.2  # Ом

# Калибровка X: сопротивление измерительного резистора
I_eff = np.array([0.883, 0.115, 0.120])  # А
width_x = np.array([10.0, 9.2, 9.2])  # дел.
kX = 2 * np.sqrt(2) * R0 * I_eff / width_x  # В/дел.

# Калибровка Y: исходные данные, включая 28.2 мВ
U_eff = np.array([0.125, 0.125, 0.0282])  # В
height_y = np.array([7.9, 7.9, 7.8])  # дел.
kY = 2 * np.sqrt(2) * U_eff / height_y  # В/дел.

# Постоянная времени: точная амплитудная формула для RC-цепи
U_in, U_out = 16.0, 0.124  # В
nu = 50.0  # Гц
omega = 2 * np.pi * nu
tau = np.sqrt((U_in / U_out)**2 - 1) / omega

alpha_H = N0 * kX / (l * R0)  # (А/м)/дел.
alpha_B = tau * kY / (Ni * S)  # Тл/дел.

names = [
    "Кремнистое железо Fe-Si",
    "Пермаллой Fe-Ni НП50",
    "Феррит 1000НН",
]

out_dir = Path("images")
out_dir.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})

for i, name in enumerate(names):
    H = alpha_H[i] * np.asarray(X[i], dtype=float)
    B = alpha_B[i] * np.asarray(Y[i], dtype=float)

    fig, ax = plt.subplots(figsize=(7.2, 4.8), layout="constrained")

    # Соединяем соседние измеренные точки отрезками: без МНК и без подгонки.
    ax.plot(H, B, linewidth=1.2, label="Ломаная по измеренным точкам")
    ax.plot(H, B, linestyle="None", marker="+", color="red",
            markersize=13, markeredgewidth=2, label="Эксперимент")

    ax.set_xlim(0, 1.10 * H.max())
    ax.set_ylim(0, 1.10 * B.max())
    ax.set_xlabel("Напряжённость магнитного поля [H], А/м")
    ax.set_ylabel("Магнитная индукция [B], Тл")
    ax.set_title(name)

    # Крупная и мелкая сетка (5 частей между соседними основными делениями)
    ax.xaxis.set_minor_locator(AutoMinorLocator(5))
    ax.yaxis.set_minor_locator(AutoMinorLocator(5))
    ax.grid(which="major", linewidth=0.75, alpha=0.55)
    ax.grid(which="minor", linewidth=0.4, alpha=0.23)
    ax.set_axisbelow(True)
    ax.legend(loc="lower right", frameon=False, fontsize=9)

    path = out_dir / f"B_of_H_{i + 1}.png"
    fig.savefig(path, dpi=200)
    plt.close(fig)
    print(f"{name}: {path}")
    for j, (h, b) in enumerate(zip(H, B), 1):
        print(f"  {j}: H = {h:.2g} А/м; B = {b:.2g} Тл")

# Точки с равным X у пермаллоя дают вертикальный отрезок.
# Это следствие разрешения измерений; он не доказывает скачок индукции.
