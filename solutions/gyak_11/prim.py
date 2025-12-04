# Minimum Spanning Tree - Prim Algorithm
# builds the MST from a starting vertex, always selecting the minimum-weight outgoing edge

# Disconnected graph:
# - You pick a starting vertex.
# - You get an MST only for the component containing that vertex.

import heapq

def prim(graph, start):
    visited = set()
    mst_edges = []
    pq = []  # (weight, u, v)

    visited.add(start)
    for (v, w) in graph.adj[start]:
        heapq.heappush(pq, (w, start, v))

    total = 0

    while pq:
        w, u, v = heapq.heappop(pq)
        if v in visited:
            continue

        visited.add(v)
        mst_edges.append((u, v, w))
        total += w

        for (to, wt) in graph.adj[v]:
            if to not in visited:
                heapq.heappush(pq, (wt, v, to))

    return mst_edges, total
