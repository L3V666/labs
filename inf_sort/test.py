import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# --- Замените эти массивы на ваши данные ---
data = np.array(pd.read_csv("merge_sort_csv.csv", header=None))

N = data[:, 0]
times = data[:, 1]
# ------------------------------------------------

# 1) Подготовка модели t ≈ c * N * log(N)
# используем натуральный лог — база логарифма только меняет c, не форму
x = N * np.log(N)
# наилучший коэффициент c по МНК (одна переменная, без свободного члена)
c = np.dot(times, x) / np.dot(x, x)
t_pred = c * x

# R^2 для оценки качества аппроксимации
residuals = times - t_pred
SSE = np.sum(residuals**2)
SST = np.sum((times - np.mean(times))**2)
R2 = 1 - SSE / SST

print(f"Коэффициент c = {c:.6e}, R^2 = {R2:.4f}")

# 2) График: исходные точки + кривая c * N log N
plt.figure(figsize=(8,5))
plt.scatter(N, times, label='Измерения', zorder=5)
N_smooth = np.linspace(N.min(), N.max(), 300)
plt.plot(N_smooth, c * N_smooth * np.log(N_smooth), label=f'c·N·log(N), c={c:.3e}')
plt.xlabel('N (длина массива)')
plt.ylabel('Время (сек)')
plt.title('Сравнение времени с моделью N·log(N)')
plt.legend()
plt.grid(True)
plt.show()

# 3) Нормировочный график: t / (N log N) — если зависимость ~N log N, отношение должно быть ≈ const
plt.figure(figsize=(8,4))
ratio = times / x
plt.scatter(N, ratio, label='t / (N log N)')
plt.hlines(np.mean(ratio), N.min(), N.max(), linestyles='dashed', label=f'среднее = {np.mean(ratio):.3e}')
plt.xlabel('N')
plt.ylabel('t / (N log N)')
plt.title('Нормированное время — должно быть примерно const при N log N')
plt.legend()
plt.grid(True)
plt.show()

# 4) (опционально) Лог-лог аппроксимация степени: t ≈ A * N^b
# если b ≈ 1 и в нормировке видна медленная лог-функция, это тоже согласуется с N log N
coeffs = np.polyfit(np.log(N), np.log(times), 1)
b = coeffs[0]; A = np.exp(coeffs[1])
print(f"Лог-лог аппроксимация: t ≈ {A:.3e} * N^{b:.3f}")
