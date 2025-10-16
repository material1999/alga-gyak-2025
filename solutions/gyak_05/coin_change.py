# Coin Change
# Task: Given a set of coin denominations and a target sum, find the minimum number of coins using a greedy approach.

def greedy_coin_change(coins, amount):
    coins.sort(reverse=True)
    result = []
    remaining = amount

    for coin in coins:
        count = remaining // coin
        if count > 0:
            result.append((coin, count))
            remaining -= coin * count

    return result

# Example 1: canonical coin system
coins = [1, 5, 10, 25]
amount = 87

print("Coins:", coins)
print(f"Target amount: {amount}")
print("Greedy solution:")
for coin, count in greedy_coin_change(coins, amount):
    print(f"  {count} × {coin}")

# Example 2: non-canonical system
coins = [1, 4, 5]
amount = 8

print("\nCoins:", coins)
print(f"Target amount: {amount}")
print("Greedy solution:")
for coin, count in greedy_coin_change(coins, amount):
    print(f"  {count} × {coin}")
