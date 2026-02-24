import numpy as np
import random
import time

total = 0

def Partition(l, r):
    if l == r:
        return r
    
    pivot = l + random.randint(0, r - l)
    idx = l

    arr[pivot], arr[r] = arr[r], arr[pivot]
    pivot = arr[r]

    for i in range(l, r):
        if arr[i] <= pivot:
            arr[i], arr[idx] = arr[idx], arr[i]
            idx = idx + 1

    arr[r], arr[idx] = arr[idx], arr[r]

    return idx

def Quick_Sort(l, r): 
    if l >= r:
        return None
    mid = Partition(l, r)
    Quick_Sort(l, mid - 1)
    Quick_Sort(mid + 1, r)

for i in range(5):
    arr = np.fromfile("test_10.inp", sep=' ', dtype=int)
    start_time = time.perf_counter()
    Quick_Sort(0, len(arr) - 1)
    end_time = time.perf_counter()
    total = total + (end_time - start_time)*1000

total = total / 5

print(f"Avg sorting time : {total:.2f} ms")
