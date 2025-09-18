length = int(input())
numbers = [int(num) for num in input().split(" ")]

# --- O(n log n): Sort + scan
def missing_number_sort(arr, n):
    arr.sort()
    for i, x in enumerate(arr, start=1):
        if i != x:
            return i
    return n

print(missing_number_sort(numbers, length))
