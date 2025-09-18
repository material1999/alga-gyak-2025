line = input().split(" ")
n = int(line[0])
target_sum = int(line[1])
numbers = [int(num) for num in input().split(" ")]

# --- O(n²): Double loop
def two_sum_naive(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return str(i + 1) + " " + str(j + 1)
    return "IMPOSSIBLE"

print(two_sum_naive(numbers, target_sum))
