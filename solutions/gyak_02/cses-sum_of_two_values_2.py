# CSES - Sum of Two Values
# https://cses.fi/problemset/task/1640

line = input().split(" ")
n = int(line[0])
target_sum = int(line[1])
numbers = [int(num) for num in input().split(" ")]

# --- O(n): Hash map
def two_sum_map(n, numbers, target_sum):
    looking_for = dict()
    for i in range(n):
        if numbers[i] not in looking_for:
            looking_for[target_sum - numbers[i]] = i + 1
        else:
            return str(looking_for[numbers[i]]) + " " + str(i + 1)
    return "IMPOSSIBLE"

print(two_sum_map(n, numbers, target_sum))
