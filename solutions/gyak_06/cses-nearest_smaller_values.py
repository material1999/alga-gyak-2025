# CSES - Nearest Smaller Values
# https://cses.fi/problemset/task/1645/

def nearest_smaller_values(arr):
    n = len(arr)
    result = [0] * n
    stack = []  # stores indices

    for i in range(n):
        # Pop indices whose value >= arr[i]
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()

        # If stack is not empty, top is nearest smaller
        if stack:
            result[i] = stack[-1] + 1  # +1 for 1-based index
        else:
            result[i] = 0

        # Push current index onto stack
        stack.append(i)

    return result


n = int(input())
arr = list(map(int, input().split()))
print(*nearest_smaller_values(arr))
