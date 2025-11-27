from collections import deque

def path_exists(graph, start, goal):
    q = deque([start])
    visited = set([start])

    while q:
        node = q.popleft()
        if node == goal:
            return True
        for neigh in graph[node]:
            if neigh not in visited:
                visited.add(neigh)
                q.append(neigh)

    return False
