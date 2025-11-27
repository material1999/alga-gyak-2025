# adjacency matrix
n = 5
graph = [[0]*n for _ in range(n)]
graph[0][1] = 1
graph[2][4] = 1



# adjacency list
graph = {
    0: [1],
    1: [2, 3],
    2: [],
    3: [4],
    4: []
}


# Operation             Adjacency Matrix	    Adjacency List
# Space	                      O(V²)	                O(V + E)
# Check edge(u, v)	          O(1)	                O(deg(u))
# Iterate neighbors	          O(V)	                O(deg(u))
# Best for	              Dense graphs	          Sparse graphs