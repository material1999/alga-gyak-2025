import time
import sys

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

print("##########")
print("Recursion limit:", sys.getrecursionlimit())
print("##########")

n_list = [1, 2, 3, 5, 10, 100, 997, 998, 999, 1000]

for n in n_list:
    print(n)
    start = time.time()
    print(factorial_recursive(n))
    end = time.time()
    print(f"Time taken: {end - start:.6f} seconds")
    print("##########")
