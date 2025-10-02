def max_treasure_with_path(grid):
    n = len(grid)
    m = len(grid[0])

    # DP table for maximum treasure
    dp = [[0] * m for _ in range(n)]
    # Parent table to reconstruct path ('D' for down, 'R' for right)
    parent = [[None] * m for _ in range(n)]

    dp[0][0] = grid[0][0]

    # Fill first row
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
        parent[0][j] = 'R'  # came from left → moved right

    # Fill first column
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
        parent[i][0] = 'D'  # came from top → moved down

    # Fill rest of the grid
    for i in range(1, n):
        for j in range(1, m):
            if dp[i - 1][j] > dp[i][j - 1]:
                dp[i][j] = grid[i][j] + dp[i - 1][j]
                parent[i][j] = 'D'  # came from top → move down
            else:
                dp[i][j] = grid[i][j] + dp[i][j - 1]
                parent[i][j] = 'R'  # came from left → move right

    # Reconstruct path as moves
    moves = []
    i, j = n - 1, m - 1
    while i != 0 or j != 0:
        move = parent[i][j]
        moves.append(move)
        if move == 'D':
            i -= 1
        else:
            j -= 1
    moves.reverse()

    # Print DP table
    print("DP table (max treasure to reach each cell):")
    for row in dp:
        print(' '.join(f"{cell:3}" for cell in row))

    print("\nMoves to collect maximum treasure:")
    print(moves)

    return dp[n - 1][m - 1], moves


# Example usage
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

max_val, moves = max_treasure_with_path(grid)
print(f"\nMaximum treasure: {max_val}")
