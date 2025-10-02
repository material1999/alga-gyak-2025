import time

def climb_stairs_recursive(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return climb_stairs_recursive(n - 1) + climb_stairs_recursive(n - 2)


def climb_stairs_dp(n: int) -> int:
    if n == 0 or n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

n_list = [0, 1, 2, 5, 10, 20, 30, 35]

print("=== Recursive vs DP Comparison ===")
for n in n_list:
    print(f"\nStairs: {n}")

    # Recursive
    start = time.time()
    result_rec = climb_stairs_recursive(n)
    end = time.time()
    print(f"Recursive result: {result_rec}, time: {end - start:.6f} sec")

    # DP
    start = time.time()
    result_dp = climb_stairs_dp(n)
    end = time.time()
    print(f"Dynamic P result: {result_dp}, time: {end - start:.6f} sec")

n_list = [1000, 10000, 20000]

print("=== DP Comparison ===")
for n in n_list:
    print(f"\nStairs: {n}")
    start = time.time()
    result_dp = climb_stairs_dp(n)
    end = time.time()
    print(f"DP result: {result_dp}, time: {end - start:.6f} sec")