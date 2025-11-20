# ha n méretű tömbben maximum k különböző érték van (k kicsi)
# melyik elemből mennyi van, tömb indexére mentjük el
# annyiszor írjuk egymás után az indexet, amennyi az ott lévő érték

def counting_sort(arr, k):
    print("Bemenet:", arr)

    count = [0] * (k+1)

    # Darabszámok
    for x in arr:
        count[x] += 1
    print("Miből mennyi van:", count)

    # Prefix összegek (helyek meghatározása)
    for i in range(1, k+1):
        count[i] += count[i-1]
    print("Eddigi összegek:", count)

    output = [0] * len(arr)

    # Stabil elhelyezés
    for x in reversed(arr):
        count[x] -= 1
        output[count[x]] = x

    return output

arr = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(arr, max(arr)))
