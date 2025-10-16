# CSES - Two Sets
# https://cses.fi/problemset/task/1092

n = int(input())

def two_sets(n):

    total_sum = n * (n + 1) // 2
    if total_sum % 2 != 0:
        return "NO"

    set1 = []
    set2 = []
    target = total_sum // 2

    for i in range(n, 0, -1):
        if target >= i:
            set1.append(i)
            target -= i
        else:
            set2.append(i)

    result = "YES\n"
    result += f"{len(set1)}\n" + " ".join(map(str, set1)) + "\n"
    result += f"{len(set2)}\n" + " ".join(map(str, set2))
    return result

print(two_sets(n))