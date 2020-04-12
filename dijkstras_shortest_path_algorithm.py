#! /usr/bin/env python

import sys

class Graph():
    def __init__(self,vertices):
        self.v = vertices
        self.graph = [[0] * vertices] * vertices
    
    def dijkstra(self, src):
        """
        Implements Dijkstra's algorithm to compute shortest path from a source node to all other nodes in the graph
        represented as adjacency matrix.
        Parameters:
        --------------
        src - index of source node
        Returns:
        --------------
        dist - list of distances of each node of graph from the source node
        eg.
        >> g = Graph(5)
        >> g.graph = [[0, 6, 0, 1, 0],
                       [6, 0, 5, 2, 2],
                       [0, 5, 0, 0, 5],
                       [1, 2, 0, 0, 1],
                       [0, 2, 5, 1, 0]]
        >> g.dijkstra(0)
          [0, 3, 7, 1, 2]
        """
        dist = [sys.maxsize] * self.v
        dist[src] = 0
        visited = [False] * self.v
        
        def computeDist(node):
            if not visited[node]:
                min_dist = sys.maxsize
                min_node = node
                visited[node] = True
                
                # For each neigbour of given node, compute their distance from the source node
                for nbr,w in enumerate(self.graph[node]):
                    if (visited[nbr] == False) and (w > 0):
                        dist[nbr] = min(dist[nbr], w + dist[node])
                        if dist[nbr] < min_dist:
                            min_dist = dist[nbr]
                            min_node = nbr
                # Recursively visit the next node closest to the source
                computeDist(min_node)   
        computeDist(src)
        
        return dist
