#!/bin/env python
""" 
Topological sorting problem statement: 
Given a directed acyclic graph (DAG), find a linear ordering of vertices 
such that for all edges (v, w), v precedes w in the ordering.
"""

import collections

class Graph():
    def __init__(self, v):
        self.graph = collections.defaultdict(set)
        self.v = v

    def addEdge(self, u, v):
        self.graph[u].add(v)

    def doTopologicalSort(self):
        """
        Implements Topological sort for a directed graph represented in edglist format.
        The algorithm begins with computing in-degress of all vertices, taking O(V)*O(N) = O(E) time.
        It uses a dictionary to keep track of vertices with 0 in-degree, thus taking O(1) time for finding 
        the next vertex with 0 in-degree. During topological sorting, for each vertex with 0 in-degree it updates its adjacent vertices'
        in-degrees, taking O(E). The overall time complexity is thus O(E) + O(E) ~ O(E).
        
        Refernces:
        https://courses.cs.washington.edu/courses/cse326/03wi/lectures/RaoLect20.pdf
        """
        # Find in-degree of all vertices
        indegrees = [0] * self.v 
        # Maintain 2 separate sets containing vertices with 0 indegree and those with atleast 1 indegree
        deg_dist = collections.defaultdict(set)
        tsort = []
        # Add all vertices to the set with 0 degree initially
        deg_dist[0].update(i for i in range(self.v))
        
        # Update in-degrees of vertices and the set they belong to
        for u in range(self.v):
            for nbr in self.graph[u]:                
                # Handling nodes u with no outgoing or incoming edges, i.e no neighbours
                if nbr is not None:
                    if indegrees[nbr] == 0:
                        deg_dist[0].remove(nbr)
                        deg_dist[1].add(nbr)
                    indegrees[nbr] += 1
                    
        # Begin traversal
        for _ in range(self.v):      
            if not len(deg_dist[0]):
                # If there is no vertex with 0 in-degree
                print("graph has cycles")
                break
            node = deg_dist[0].pop()
            tsort.append(node)
            for nbr in self.graph[node]:         
                if nbr is not None:
                    indegrees[nbr] -= 1
                    if indegrees[nbr] == 0:
                        deg_dist[0].add(nbr)
                        deg_dist[1].remove(nbr)
        return tsort

if __name__ == "__main__":
    graph = Graph(6)
    graph.addEdge(0,1)
    graph.addEdge(1,2)
    graph.addEdge(2,3)
    graph.addEdge(0,3)
    graph.addEdge(2,4)
    graph.addEdge(3,4)
    graph.addEdge(5,None)
    print(graph.doTopologicalSort())
