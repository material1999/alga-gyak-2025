# CSES - Longest Common Subsequence
# https://cses.fi/problemset/task/3403

def longest_common_subsequence(arr1, arr2):
    n, m = len(arr1), len(arr2)

    # DP table: dp[i][j] = LCS length of arr1[0..i-1] and arr2[0..j-1]
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if arr1[i - 1] == arr2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct LCS from DP table
    i, j = n, m
    lcs = []
    while i > 0 and j > 0:
        if arr1[i - 1] == arr2[j - 1]:
            lcs.append(arr1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    lcs.reverse()  # reverse because we traced from the end

    return dp[n][m], lcs


# Read input
n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

length, sequence = longest_common_subsequence(arr1, arr2)

# Output
print(length)
print(*sequence)
