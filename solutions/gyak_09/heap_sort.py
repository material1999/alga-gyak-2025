# tömb mint bináris fa
# heapify
# maximum elem kicserélése a gyökérrel, kivétel, majd ismét heapify

def heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    # Max-heap építése
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # Rendezés
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# Példa
arr = [5, 3, 8, 4, 1, 2]
heapsort(arr)
print(arr)
