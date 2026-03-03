from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

fig, ax = plt.subplots(nrows=3, ncols=1, figsize=(10, 10))

data1 = np.array(pd.read_excel('data.xlsx', sheet_name=0))

ax[0].scatter(data1[:, 14], data1[:, 13], s=50, marker='+', c='red')

ax[0].plot(np.array([0, 13]), np.array([0, 13]) * (-0.22) + 1.55)

ax[0].set_xlim(0, 13)

ax[0].set_ylabel('$ln(P-P_{пр})$, $10^{-4}$ торр')
ax[0].set_xlabel('t, с')

ax[0].grid(True, which='major', linestyle='-', linewidth=0.5)
ax[0].grid(True, which='minor', linestyle='-', linewidth=0.3)
ax[0].minorticks_on()

ax[0].set_title('1 Серия')

data1 = np.array(pd.read_excel('data.xlsx', sheet_name=1))

ax[1].scatter(data1[:, 14], data1[:, 13], s=50, marker='+', c='red')

ax[1].plot(np.array([0, 13]), np.array([0, 13]) * (-0.22) + 1.69)

ax[1].set_xlim(0, 13)

ax[1].set_ylabel('$ln(P-P_{пр})$, $10^{-4}$ торр')
ax[1].set_xlabel('t, с')

ax[1].grid(True, which='major', linestyle='-', linewidth=0.5)
ax[1].grid(True, which='minor', linestyle='-', linewidth=0.3)
ax[1].minorticks_on()

ax[1].set_title('2 Серия')

data1 = np.array(pd.read_excel('data.xlsx', sheet_name=2))

ax[2].scatter(data1[:, 14], data1[:, 13], s=50, marker='+', c='red')

ax[2].plot(np.array([0, 13]), np.array([0, 13]) * (-0.24) + 1.53)

ax[2].set_xlim(0, 13)

ax[2].set_ylabel('$ln(P-P_{пр})$, $10^{-4}$ торр')
ax[2].set_xlabel('t, с')

ax[2].grid(True, which='major', linestyle='-', linewidth=0.5)
ax[2].grid(True, which='minor', linestyle='-', linewidth=0.3)
ax[2].minorticks_on()

ax[2].set_title('3 Серия')

plt.tight_layout()

plt.savefig('exp.png')

plt.show()