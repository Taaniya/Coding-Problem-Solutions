"""
Problem statement: 
There are n nodes in a social network labeled from 0 to n - 1. Given an array logs where logs[i] = [timestampi, xi, yi] indicates that xi and yi will be connected at the time timestampi.
Connection is symmetric & irrespective of distance / path length between 2 nodes. 

Return the earliest time for which every person gets connected with every other person directly or indirectly. 
If there is no such earliest time, return -1.

Example: 
Input: logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6
Output: 20190301

------------------------------------------
Approach -
This is solved using disjoint set union below, where union is performed by size.
Following mappings are maintained -
parent - to map every graph vertex with its parent vertex (also referred as set representative)
set_size - maps every parent vertex (set representative) to the count of members in its set

As the flow begins, for every new edge created between any 2 vertices, if the 2 are not already in the same set, the sets associated with the 
2 vertices are combined by union and setting a common parent for the two.

The moment, when all the vertices get associated with the same parent / set, the graph becomes a single connected component. 
This marks the time when every person get connected with every other person.

"""
from collections import defaultdict
import copy

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        graph = Graph(n)
        logs = sorted(logs, key=lambda ts: ts[0])          # sort logs w.r.t timestamp to maintain chronology
        for log in logs:
            graph.add_edge(log[1], log[2])
            if len(graph.visited) == n:                    # only check for full connectivity once all vertices have been added in graph
                if graph.is_single_connected_component():
                    return log[0]
        return -1

class Graph():
    def __init__(self, v: int) -> None:
        self.v = v           # no. of vertices
        self.vertices = defaultdict(list)
        self.parent = {}
        self.set_size = {}       # key parent node, val - no. of child nodes
        self.visited = {}

    def add_edge(self, u: int, v: int) -> None:
        self.vertices[u].append(v)
        self.visited[u] = 1       # mark people added to graph
        self.visited[v] = 1
        self.set_parent(u, v)
            
    def is_single_connected_component(self) -> bool:
        """
        Iterates through each vertex and finds its set membership in set of vertices in a 
        connected component.All vertices have the same parent if the graph forms a single 
        connected component, otherwise not.
        """
        prev_parent = self.find_parent(0)
        for i in range(1, self.v):
            parent = self.find_parent(i)
            if parent != prev_parent:
                return False
        return True  

    def parent_union(self, u: int, v: int) -> None:
        """ Perform union operation on disjoint set to set common parent for u & v nodes.
        """
        p_u = self.find_parent(u)
        p_v = self.find_parent(v)
        neighbors = []
        if self.set_size[p_u] > self.set_size[p_v]:
            self.parent[v] = copy.deepcopy(p_u)      
            self.set_size[p_u] += 1
            self.set_size[p_v] -= 1
            neighbors = self.vertices[v]
            for nbr in neighbors:
                if self.parent[nbr] != self.parent[u]:
                    self.parent_union(nbr, u)
        else:
            self.parent[u] = copy.deepcopy(self.parent[v])
            self.set_size[p_v] += 1
            self.set_size[p_u] -= 1
            neighbors = self.vertices[u]
        
            # update parent of each neighbor of updated node
            for nbr in neighbors:
                if self.parent[nbr] != self.parent[v]:
                    self.parent_union(nbr, v)
                
    def set_parent(self, u: int, v:int) -> None:
        """ Updates parent of nodes with parent with larger size having more no. of nodes linked to it. 
            Calls union on set in case u and v got connected and previously had parents for different
            connected components.
        """ 
        # check parent / membership, combine if needed
        p_u =  self.find_parent(u)
        p_v =  self.find_parent(v)
        if (p_u == -1) & (p_v == -1):
           # both are new vertices to add, set 1 of them as parent of the other
           self.parent[u] = u
           self.parent[v] = u
           self.set_size[u] = 2
        elif p_u == -1:
           self.parent[u] = copy.deepcopy(self.parent[v])
           self.set_size[self.parent[v]] += 1      # increase size of set for parent of v
        elif p_v == -1:
           self.parent[v] = copy.deepcopy(self.parent[u])
           self.set_size[self.parent[u]] += 1      # increase size of set for parent of u
        elif p_u != p_v:         # both have different parents / are from different sets
           self.parent_union(u, v)

    def find_parent(self, u: int) -> int:
        p = self.parent.get(u, -1)
        if p == -1:     # parent not initialized yet
            self.parent[u] = u
            self.set_size[u] = 1
        elif p!= u:
            self.parent[u] = self.find_parent(self.parent[u])    
        return self.parent[u]
