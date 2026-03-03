from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

fig, ax = plt.subplots(nrows=3, ncols=1, figsize=(10, 10))

data1 = np.array(pd.read_excel('data.xlsx', sheet_name=0))

ax[0].scatter(data1[:, 1], data1[:, 0], s=1)

ax[0].set_xlim(0, 110)
ax[0].set_ylim(0, 7.5)

ax[0].set_ylabel('P, $10^{-4}$ торр')
ax[0].set_xlabel('t, с')

ax[0].grid(True, which='major', linestyle='-', linewidth=0.5)
ax[0].grid(True, which='minor', linestyle='-', linewidth=0.3)
ax[0].minorticks_on()

ax[0].set_title('1 Серия')

data2 = np.array(pd.read_excel('data.xlsx', sheet_name=1))

ax[1].scatter(data2[:, 1], data2[:, 0], s=1)

ax[1].set_xlim(0, 110)
ax[1].set_ylim(0, 7.5)

ax[1].set_ylabel('P, $10^{-4}$ торр')
ax[1].set_xlabel('t, с')

ax[1].grid(True, which='major', linestyle='-', linewidth=0.5)
ax[1].grid(True, which='minor', linestyle='-', linewidth=0.3)
ax[1].minorticks_on()

ax[1].set_title('2 Серия')

data3 = np.array(pd.read_excel('data.xlsx', sheet_name=2))

ax[2].scatter(data3[:, 1], data3[:, 0], s=1)

ax[2].set_xlim(0, 110)
ax[2].set_ylim(0, 7.5)

ax[2].set_ylabel('P, $10^{-4}$ торр')
ax[2].set_xlabel('t, с')

ax[2].grid(True, which='major', linestyle='-', linewidth=0.5)
ax[2].grid(True, which='minor', linestyle='-', linewidth=0.3)
ax[2].minorticks_on()

ax[2].set_title('3 Серия')

plt.tight_layout()

plt.savefig('1.png')

plt.show()