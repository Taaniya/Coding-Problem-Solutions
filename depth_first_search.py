#!/bin/env python

from collections import defaultdict

class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(set)
    
    def addEdge(self, u, v):
        self.graph[u].add(v)

    def DFS(self, src):
        '''Performs depth first search for a directed unweighted graph represented as edglist format.'''
        visited = [0]*self.v
        i = 1
        def visitNode(src):
            nonlocal i 
            visited[src] = i
            for nbr in self.graph[src]:
                if not visited[nbr]:
                    i += 1
                    visitNode(nbr)
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
