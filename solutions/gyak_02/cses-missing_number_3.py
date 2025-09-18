length = int(input())
numbers = [int(num) for num in input().split(" ")]

# --- O(1): Sum formula
def missing_number_sum(arr, n):
    return n*(n+1)//2 - sum(arr)

print(missing_number_sum(numbers, length))
