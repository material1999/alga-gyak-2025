def binary_search_recursive(arr, target, left, right):
    # Base case: interval is empty → target not found
    if left > right:
        print(f"Interval empty: left={left}, right={right}. {target} not found.")
        return -1

    mid = (left + right) // 2
    print(f"Checking middle index {mid} with value {arr[mid]} (interval {left}-{right})")

    if arr[mid] == target:
        # Target is found
        return mid
    elif target < arr[mid]:
        # Search in the left half
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        # Search in the right half
        return binary_search_recursive(arr, target, mid + 1, right)


# Example usage
arr = [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
target = 37

result = binary_search_recursive(arr, target, 0, len(arr) - 1)

if result != -1:
    print(f"{target} found at index {result}")
else:
    print(f"{target} is not in the list")
