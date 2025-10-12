import time
import random
import csv

data = []
for n in range(10000, 50001, 10000):
    a = [0] * n
    for i in range(len(a)):
        a[i] = random.randint(0, 1000)
    s = time.time()
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if a[j + 1] < a[j]:
                a[j], a[j + 1] = a[j + 1], a[j]
    e = time.time()
    print(n)
    data.append([str(n), str(e - s)])

with open("bubble_py_csv.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)