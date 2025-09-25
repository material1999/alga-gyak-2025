# CSES - Fibonacci Numbers
# https://cses.fi/problemset/task/1722

import time

def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)

n_list = [1, 2, 3, 4, 5, 10, 20, 30, 35, 40]

for n in n_list:
    print(n)
    start = time.time()
    print(fib_naive(n))
    end = time.time()
    print(f"Time taken: {end - start:.6f} seconds")
    print("##########")
