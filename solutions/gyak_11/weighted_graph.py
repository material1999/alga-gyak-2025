##### adjacency list #####

class WeightedGraph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v, w):
        self.adj.setdefault(u, []).append((v, w))
        self.adj.setdefault(v, []).append((u, w))   # remove if directed

##### adjacency matrix #####

class WeightedMatrixGraph:
    def __init__(self, n, directed=False):
        self.n = n
        self.directed = directed
        self.mat = [[float('inf')] * n for _ in range(n)]

        # zero diagonal
        for i in range(n):
            self.mat[i][i] = 0

    def add_edge(self, u, v, w):
        self.mat[u][v] = w
        if not self.directed:
            self.mat[v][u] = w
