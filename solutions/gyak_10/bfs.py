from collections import deque

def bfs(graph, start):
    visited = set()
    q = deque([start])
    visited.add(start)

    while q:
        node = q.popleft()
        print(node, end=" ")

        for neigh in graph[node]:
            if neigh not in visited:
                visited.add(neigh)
                q.append(neigh)
