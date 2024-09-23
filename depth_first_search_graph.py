#!/bin/env python

from collections import defaultdict

class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(set)
    
    def addEdge(self, u, v):
        self.graph[u].add(v)

    def DFS(self, src):
        '''Performs depth-first search with cycle detection for a directed (or undirected) unweighted graph represented as edgelist format. 
        https://stackoverflow.com/questions/2869647/why-dfs-and-not-bfs-for-finding-cycle-in-graphs
        Time complexity: O(V+E) 
        '''
        visited = [0] * self.v
        in_progress = set()               # nodes currently explored with DFS
        def visitNode(src):
            in_progress.add(src)          
            visited[src] = 1
            for nbr in self.graph[src]:
                if not visited[nbr]:
                    print(f"visited {nbr}")
                    visitNode(nbr)
                elif nbr in in_progress:
                  print(f"cycle detected. node {nbr} is already visited")
            in_progress.remove(src)
            return
        visitNode(src)
        return visited
        
        
if __name__ == "__main__":
    graph = Graph(5)
    graph.addEdge(0,1)
    graph.addEdge(1,2)
    graph.addEdge(0,3)
    graph.addEdge(1,4)
    graph.addEdge(4,2)
    graph.addEdge(3,4)
    print(graph.DFS(0))
