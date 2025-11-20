# legkisebbtől legnagyobb helyiértékig megyünk
# minden esetben counting_sort (tudjuk, hogy 0-9ig lesznek a számjegyek)

def counting_sort_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for x in arr:
        index = (x // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for x in reversed(arr):
        index = (x // exp) % 10
        count[index] -= 1
        output[count[index]] = x

    return output

def radix_sort(arr):
    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        arr = counting_sort_digit(arr, exp)
        exp *= 10

    return arr

arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(arr))
