# Shortest Path - Dijkstra
# - dist[v]: best known distance to each vertex
# - pq: vertices waiting to be processed, ordered by current best distance
# - Each time we relax edges, we potentially push smaller distances into the heap
# - Outdated heap entries are ignored automatically

import heapq

def dijkstra(graph, start):
    dist = {v: float('inf') for v in graph.adj}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for (v, w) in graph.adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    return dist

# Dijkstra fails when there is a negative weight edge

g = WeightedGraph()
g.adj = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', -3)],
    'C': [('A', 4), ('B', -3)]
}

print(dijkstra(g, 'A'))
# Output: {'A': 0, 'B': 1, 'C': 4}  <-- WRONG
