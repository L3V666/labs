import pandas as pd
import numpy as np

def table(m):
    for i in range(5):
        print(f'{m[i][0]} & {m[i][1]} & {(3.14 * 2 * m[i][0]) / m[i][1] * 1e2:.2f} & {np.pi / m[i][1] / 15 * 1e4:.2f}' + " \\ \hline")
    print()

data = np.array(pd.read_excel("1.2.5.xlsx", header=None))

m1 = data[4:9, 1:3]
m2 = data[13:18, 1:3]
m3 = data[22:27, 1:3]
m4 = data[31:36, 1:3]
m5 = data[40:46, 1:3]
table(m1)
table(m2)
table(m3)
table(m4)
table(m5)