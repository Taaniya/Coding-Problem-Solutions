#!/bin/env python

from collections import defaultdict, deque

class Graph():
    def __init__(self, v):
        self.graph = defaultdict(set)
        self.v = v

    def addEdge(self, u, v):
        self.graph[u].add(v)

    def BFS(self, src):
        """
        Performs breadth first traversal for directed unweighted graph represented as edgelist and using queue to 
        keep track of vertices yet to be explored.
        """
        queue = deque()               # performs enqueue and dequeue in O(1) time.
        visited = [0]*self.v
        queue.append(src)
        i = 1
        visited[src] = i
        
        while queue:
            current = queue.popleft()
            for nbr in self.graph[current]:
                i += 1
                if not visited[nbr]:
                    queue.append(nbr)
                    visited[nbr] = i                
        return visited


if __name__ == "__main__":
    graph = Graph(5)
    graph.addEdge(0,1)
    graph.addEdge(1,2)
    graph.addEdge(0,3)
    graph.addEdge(1,4)
    graph.addEdge(4,2)
    graph.addEdge(3,4)
    print(graph.BFS(0))
    
