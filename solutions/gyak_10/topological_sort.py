def topo_sort(graph):
    visited = set()
    order = []

    def dfs(u):
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                dfs(v)
        order.append(u)

    for node in graph:
        if node not in visited:
            dfs(node)

    return order[::-1]
