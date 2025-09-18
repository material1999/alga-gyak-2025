# CSES - Missing Number
# https://cses.fi/problemset/task/1083

length = int(input())
numbers = [int(num) for num in input().split(" ")]

# --- O(n): Hash set
def missing_number_set(arr, n):
    full = set(range(1, n+1))
    return (full - set(arr)).pop()

print(missing_number_set(numbers, length))
