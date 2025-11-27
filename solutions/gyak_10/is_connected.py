def is_connected(graph):
    visited = set()
    nodes = list(graph.keys())
    dfs(graph, nodes[0], visited)
    return len(visited) == len(nodes)
