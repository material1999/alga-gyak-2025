# elejétől indulunk, megyünk jobbra
# minden új elemet oda szúrunk be, ahova való

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Elemet toljuk hátra, hogy helyet csináljunk
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


# Példa
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print(arr)
