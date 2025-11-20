# oszd meg és uralkodj, rekurzió
# felez ameddig 1 elem nem marad, majd rendezve összefésül

def merge_sort(arr):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr

    # Divide: split the array into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Conquer: merge the two sorted halves
    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    # Merge the arrays by choosing the smallest element each time
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


# ---- Example usage ----
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original:", arr)

sorted_arr = merge_sort(arr)
print("Sorted:", sorted_arr)
