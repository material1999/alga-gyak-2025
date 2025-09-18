# CSES - Distinct Numbers
# https://cses.fi/problemset/task/1621

length = int(input())
numbers = [int(num) for num in input().split(" ")]

# --- O(n²): Nested check
def distinct_naive(arr):
    distinct = []
    for x in arr:
        if x not in distinct:
            distinct.append(x)
    return len(distinct)

print(distinct_naive(numbers))
