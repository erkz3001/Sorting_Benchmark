import numpy as np
import time

tmp = np.zeros(10**6, dtype=float) 
total = 0

def Merge_Sort(l, r):
    if l >= r:
        return
    
    mid = (l + r) // 2 
    Merge_Sort(l, mid)
    Merge_Sort(mid + 1, r)
    
    p1, p2, idx = l, mid + 1, 0  
    
    while p1 <= mid or p2 <= r:
        if p1 > mid:
            tmp[l + idx] = arr[p2]
            idx += 1
            p2 += 1
        elif p2 > r:
            tmp[l + idx] = arr[p1]
            idx += 1
            p1 += 1
        elif arr[p1] < arr[p2]:
            tmp[l + idx] = arr[p1]
            p1 += 1
            idx += 1
        else:
            tmp[l + idx] = arr[p2]
            p2 += 1
            idx += 1

    arr[l:r+1] = tmp[l:r+1]


for i in range(5):
    arr = np.fromfile("test_1.inp", sep=' ', dtype=float)
    
    start_time = time.perf_counter()
    Merge_Sort(0, len(arr) - 1)
    end_time = time.perf_counter()
    
    run_time = (end_time - start_time) * 1000
    total += run_time

total = total / 5

print(f"Avg sorting time : {total:.2f} ms")
