# CSES - Movie Festival
# https://cses.fi/problemset/task/1629/

# Read input
n = int(input())
movies = []

for _ in range(n):
    a, b = map(int, input().split())
    movies.append((a, b))

# Sort movies by ending time (greedy step)
movies.sort(key=lambda x: x[1])

# Select movies
count = 0
last_end = -1

for start, end in movies:
    if start >= last_end:
        count += 1
        last_end = end

# Output the maximum number of movies
print(count)
