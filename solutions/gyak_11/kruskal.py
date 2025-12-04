# Minimum Spanning Tree - Kruskal Algorithm
# sorts edges and repeatedly chooses the smallest edge that doesn’t make a cycle

# Disconnected graph:
# Works across all components.
# Produces a minimum spanning forest (one MST per component).

# disjoint set union
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True

def kruskal(n, edges):
    dsu = DSU(n)
    mst = []
    total = 0

    edges = sorted(edges)

    for w, u, v in edges:
        if dsu.union(u, v):
            mst.append((u, v, w))
            total += w

    return mst, total

