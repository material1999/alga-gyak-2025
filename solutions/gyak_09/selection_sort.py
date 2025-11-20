# elejére szúrogatunk be rendezve
# első helyre a legkisebbet
# másodikra maradékból a legkisebbet...

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        # Rendezetlen rész minimumának keresése
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Csere
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Példa
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print(arr)
