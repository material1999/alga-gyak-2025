def shortest_path(graph, start, goal):
    from collections import deque
    q = deque([start])
    visited = {start: None}  # store parent

    while q:
        node = q.popleft()
        if node == goal:
            break
        for neigh in graph[node]:
            if neigh not in visited:
                visited[neigh] = node
                q.append(neigh)

    if goal not in visited:
        return None

    # reconstruct path
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = visited[cur]
    return path[::-1]
