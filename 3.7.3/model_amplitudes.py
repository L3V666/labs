import numpy as np
import matplotlib.pyplot as plt

N = np.array([4, 5, 6, 7, 8, 9, 10])

U_10 = np.array([32.7, 66.5, 39.0, 28.0, 26.0, 33.0, 36.0])
U_19 = np.array([43.0, 64.5, 45.0, 43.3, 42.5, 36.0, 38.0])
U_266 = np.array([51.5, 45.6, 37.5, 35.0, 32.5, 30.5, 29.0])

plt.figure(figsize=(7, 4.5))

plt.plot(N, U_10, marker='+', markersize=10, label='10 кГц')
plt.plot(N, U_19, marker='+', markersize=10, label='19.2 кГц')
plt.plot(N, U_266, marker='+', markersize=10, label='26.6 кГц')

plt.xlabel('Номер ячейки')
plt.ylabel('U, В')

plt.minorticks_on()
plt.grid(which='major', alpha=0.6)
plt.grid(which='minor', alpha=0.25, linestyle=':')
plt.legend()

plt.tight_layout()
plt.savefig('figures/model_amplitudes.png', dpi=300)
plt.show()