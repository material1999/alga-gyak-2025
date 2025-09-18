# CSES - Distinct Numbers
# https://cses.fi/problemset/task/1621

length = int(input())
numbers = [int(num) for num in input().split(" ")]

# --- O(n log n): Sort + unique
def distinct_sort(arr):
    arr = sorted(arr)
    count = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            count += 1
    return count

print(distinct_sort(numbers))
