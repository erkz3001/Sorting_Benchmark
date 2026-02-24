import numpy as np
import time

total = 0

for i in range(5):
    arr = np.fromfile("test_2.inp", sep=' ', dtype=float)
    start_time = time.perf_counter()
    arr.sort()
    end_time = time.perf_counter()
    total = total + (end_time - start_time)*1000

total = total / 5

print(f"Avg sorting time : {total:.2f} ms")
