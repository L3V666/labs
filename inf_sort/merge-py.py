from typing import List, TypeVar, Callable, Optional
import time
import random
import csv

T = TypeVar("T")

def merge(left: List[T], right: List[T]) -> List[T]:
    i = j = 0
    out: List[T] = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out

def merge_sort(arr: List[T]) -> List[T]:
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

if __name__ == "__main__":
    data = []
    for n in range(10000, 50001, 10000):
        a = [0] * n
        for i in range(len(a)):
            a[i] = random.randint(0, 1000)
        s = time.time()
        sorted_a = merge_sort(a)
        e = time.time()
        assert sorted_a == sorted(a)
        print(n)
        data.append([str(n), str(e - s)])

    with open("merge_py_csv.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)
