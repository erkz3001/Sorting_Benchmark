import numpy as np
import time

total = 0

def Modify(id, sz):
    left, right, val = id*2 + 1, id*2 + 2, id
    
    if left <= sz and arr[left] > arr[val]:
        val = left
    if right <= sz and arr[right] > arr[val]:
        val = right

    if val != id:
        arr[id], arr[val] = arr[val], arr[id]
        Modify(val, sz)
    

def Heap_Sort():
    n = len(arr) - 1
    for i in range(n // 2, -1, -1):
        Modify(i, n)

    for i in range(n, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        Modify(0, i - 1)

for i in range(5):
    arr = np.fromfile("test_10.inp", sep=' ', dtype=int)
    start_time = time.perf_counter()
    Heap_Sort()
    end_time = time.perf_counter()
    total = total + (end_time - start_time)*1000

total = total / 5

print(f"Avg sorting time : {total:.2f} ms")
