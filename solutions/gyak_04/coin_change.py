def min_coins_steps(coins, x):
    # Print task description
    print("=== Coin Change / Minimum Coins Problem ===")
    print(f"Goal: Find the minimum number of coins to make sum {x} using coins {coins}\n")

    INF = float('inf')
    dp = [INF] * (x + 1)
    dp[0] = 0  # base case

    print(f"Initial dp: {dp}\n")

    # Fill DP table
    for i in range(1, x + 1):
        print(f"Calculating dp[{i}]:")
        for coin in coins:
            if i - coin >= 0:
                new_val = dp[i - coin] + 1
                if new_val < dp[i]:
                    dp[i] = new_val
                    print(f"  Using coin {coin}: dp[{i}] = dp[{i}-{coin}] + 1 = {dp[i - coin]} + 1 -> {dp[i]}")
                else:
                    print(f"  Using coin {coin}: dp[{i}] not improved (current dp[{i}] = {dp[i]})")
        print(f"dp after sum {i}: {dp}\n")

    if dp[x] == INF:
        print(f"Target sum {x} is not reachable.")
        return -1
    else:
        print(f"Minimum coins to make {x}: {dp[x]}")
        return dp[x]


# Example usage
coins = [1, 3, 4]
x = 6
min_coins_steps(coins, x)
