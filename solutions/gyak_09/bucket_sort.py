# ha egyenletes az eloszlása az értékeknek 0 és 1 között
# annyi bucket, amennyi elem
# elemeket megszorozzuk az elemszámmal, majd int-re konvertáljuk
# bucket-ok külön rendezése, majd összefűzés

def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]

    # Elem elhelyezése bucketekbe
    for x in arr:
        index = int(x * n)
        buckets[index].append(x)

    # Bucketek rendezése
    for b in buckets:
        b.sort()

    # Összefűzés
    result = []
    for b in buckets:
        result.extend(b)

    return result

arr = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47]
print(bucket_sort(arr))
