def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")

    for neigh in graph[start]:
        if neigh not in visited:
            dfs(graph, neigh, visited)
