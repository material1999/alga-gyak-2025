# CSES - Distinct Numbers
# https://cses.fi/problemset/task/1621

length = int(input())
numbers = {num for num in input().split(" ")}

# --- O(n): Hash set
def distinct_set(arr):
    return len(arr)

print(distinct_set(numbers))
