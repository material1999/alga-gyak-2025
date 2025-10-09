def grid_paths_top_left(n, m):
    # Create dp table
    dp = [[0] * m for _ in range(n)]

    # Start at top-left
    dp[0][0] = 1

    # Fill table
    for i in range(n):  # top to bottom
        for j in range(m):  # left to right
            if i - 1 >= 0:
                dp[i][j] += dp[i - 1][j]  # coming from above
            if j - 1 >= 0:
                dp[i][j] += dp[i][j - 1]  # coming from left

    # Print the grid
    print("Grid of number of paths (bottom-left start):")
    for row in dp:
        print(' '.join(f"{cell:3}" for cell in row))

    print(f"\nNumber of paths from bottom-left to top-right: {dp[n - 1][m - 1]}")
    return dp[n - 1][m - 1]


# Example usage
n = 4
m = 5
grid_paths_top_left(n, m)
