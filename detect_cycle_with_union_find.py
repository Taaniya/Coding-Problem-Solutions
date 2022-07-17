#!/bin/env python
# Problem statement

import collections

class Graph():
    def __init__(self, v):
        self.graph = collections.defaultdict(set)
        self.v = v
        
    def addEdge(self, u, v):
        self.graph[u].add(v)

    def findParent(self, u, parent):
        if parent[u] == -1:
            return u
        else:
            parent[u] = self.findParent(parent[u], parent)
            return parent[u]
            
    def union(self,u, u_parent, v_parent, parent):
        # Add the v's parent as child of u's parent (graphically)
        if parent[v_parent] == -1:
            parent[v_parent] = u
        else:
            parent[v_parent] = u_parent
        return parent
        
    def detectCycle(self):
        # A negative value denotes a parent node of the tree represnting a disjoint set
        self.parent = [-1] * self.v
        has_cycle = False

        # Go through all edges     
        for u in self.graph.keys():
            for v in self.graph[u]:
                u_parent = self.findParent(u, self.parent)
                v_parent = self.findParent(v, self.parent)
                if u_parent == v_parent:
                    return True
                else:
                    self.parent = self.union(u, u_parent, v_parent, self.parent)
        return False

if __name__ == "__main__":
    graph = Graph(8)
    graph.addEdge(0,2)
    graph.addEdge(2,3)
    # graph.addEdge(3,1)
    graph.addEdge(1,0)
    graph.addEdge(1,4)
    graph.addEdge(4,6)
    graph.addEdge(6,7)
    graph.addEdge(7,5)
    # graph.addEdge(5,4)
    graph.detectCycle()
