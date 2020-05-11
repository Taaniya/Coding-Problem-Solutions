#!/bin/env python

def floyd_warshall(adj):
    """Computes all pairs shortest path using Floyw-Warshall algorithm and returns the updated graph adjacency matrix."""
    v = len(adj)
    for k in range(v):
        for i in range(v):
            if i!=k:
                for j in range(v):
                    if (j!= k):
                        adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

    return adj
    
if __name__ == "__main__":
    adj = [[0,3,99999,7],
           [8,0,2,99999],
           [5,99999,0,1],
           [2,99999,99999,0]]
    print(floyd_warshall(adj))
