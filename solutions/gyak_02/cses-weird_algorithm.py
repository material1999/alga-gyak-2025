# CSES - Weird Algorithm
# https://cses.fi/problemset/task/1068/

import time

def weird_algorithm(n):
    seq = []
    while n != 1:
        seq.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    seq.append(1)
    return seq


n = 100
start = time.time()
result = weird_algorithm(n)
end = time.time()
print(f"Weird Algorithm steps for n={n}: {len(result)} steps, time: {end-start:.6f} sec")

n = 10**6
start = time.time()
result = weird_algorithm(n)
end = time.time()
print(f"Weird Algorithm steps for n={n}: {len(result)} steps, time: {end-start:.6f} sec")

n = 10**16
start = time.time()
result = weird_algorithm(n)
end = time.time()
print(f"Weird Algorithm steps for n={n}: {len(result)} steps, time: {end-start:.6f} sec")