# oszd meg és uralkodj, rekurzió
# pivot elem választása, majd rendezés (nála kisebb tőle balra, nála nagyobb tőle jobbra)
# ekkor a pivot helye megvan a végső rendezésben


def quicksort(arr, left, right):
    if left < right:
        p = partition(arr, left, right)
        quicksort(arr, left, p - 1)
        quicksort(arr, p + 1, right)

def partition(arr, left, right):
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i

# Példa
arr = [8, 3, 1, 7, 0, 10, 2]
quicksort(arr, 0, len(arr) - 1)
print(arr)
