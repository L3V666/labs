import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data1 = np.array(pd.read_csv('20260211_1770794006145_44.6.csv'))
data2 = np.array(pd.read_csv('20260211_1770795592077_74.4.csv'))
data3 = np.array(pd.read_csv('20260211_1770796734234_104.2.csv'))
data4 = np.array(pd.read_csv('20260211_1770797789536_137.6.csv'))


plt.scatter(data1[:, 0], data1[:, 1], s=3, label='44.6 тор')
plt.scatter(data2[:, 0], data2[:, 1], s=3, label='74.4 тор')
plt.scatter(data3[:, 0], data3[:, 1], s=3, label='104.2 тор')
plt.scatter(data4[:, 0], data4[:, 1], s=3, label='137.6 тор')

plt.legend()

plt.grid(True, which='major', linestyle='-', linewidth=0.5)
plt.grid(True, which='minor', linestyle='-', linewidth=0.3)
plt.minorticks_on()

plt.xlabel('t, с')
plt.ylabel('V, мВ')

plt.ylim(0, 25)
plt.xlim(0, 300)

plt.title('V(t)')

plt.savefig('V(t).png')

plt.show()