#! /usr/bin/env python

import sys
from collections import defaultdict
from typing import Tuple, List
import heapq


class Graph():
    def __init__(self):
        self.graph = defaultdict(set)
        self.v = 0

    def addEdge(self, u, v, w):
        '''Adds an edge from u to v with edge weight w. '''
        self.graph[u].add((v, w))
        self.v = len(self.graph)

    def dijkstra(self, src):
        """
        - Implements Dijkstra's algorithm to compute shortest path from a source node to all other nodes in the graph
        represented as edglist.
        - This implementation uses min-Priority queue using Binary Heap and calls three priority queue operations
        insert, extract-min & decrease-key (implicit while relaxing).
        - Min-heap based priority queue is used to maintain distances of each graph vertex from the given source vertex.

        Parameters:
        --------------
        src - index of source node
        Returns:
        --------------
        dist - list of distances of each node of graph from the source node
        eg.
        >> graph = Graph()
        >> graph.addEdge(0,1,4)
            graph.addEdge(0,3,3)
            graph.addEdge(1,0,4)
            graph.addEdge(1,2,7)
            graph.addEdge(1,4,2)
            graph.addEdge(2,1,7)
            graph.addEdge(2,4,5)
            graph.addEdge(3,0,3)
            graph.addEdge(3,4,5)
            graph.addEdge(4,3,5)
            graph.addEdge(4,1,2)
            graph.addEdge(4,2,5)
        >> graph.dijkstra(0)
           [0, 4, 11, 3, 6]
        """
        unvisited_queue = []
        visited = set()
        dist = []  # hold shortest distance from source for each node in the graph
        source_nbrs = dict([(v_id, dist) for v_id, dist in self.graph[src]])

        # Step 1: Initialize priority queue with distance of each vertex from given source
        for v_id in range(0, self.v):
            if v_id != src:
                if v_id in source_nbrs:  # if vertices are directly forming any edge with src, include their distance from source
                    v_id_dist = source_nbrs[v_id]
                    dist.append(v_id_dist)
                    heapq.heappush(unvisited_queue, (v_id_dist, v_id))
                else:
                    # initialize shortest distance from source as infinite for vertices not directly connected to source
                    dist.append(sys.maxsize)
                    heapq.heappush(unvisited_queue, (sys.maxsize, v_id))
            else:
                heapq.heappush(unvisited_queue, (0, src))
                dist.append(0)

        # Step 2: Perform BFS traversal & update and find shortest distance for each vertex from source along the way
        while unvisited_queue:
            min_node = heapq.heappop(unvisited_queue)
            visited.add(min_node)
            for nbr, w in self.graph[min_node]:
                if nbr not in visited:
                    new_dist = w + dist[min_node]
                    if new_dist < dist[nbr]:
                        # update shortest distance from source / update priority
                        self.decrease_key((dist[nbr], nbr), new_dist)
                        dist[nbr] = new_dist
        return dist


    def decrease_key(self, vertex: Tuple, new_dist: int, pqueue: List[Tuple[int, int]]):
        pqueue.remove(vertex)
        dist, v_id = vertex
        heapq.heappush(pqueue, (new_dist, v_id))


if __name__ == "__main__":
    graph = Graph()
    graph.addEdge(0, 1, 4)
    graph.addEdge(0, 3, 3)
    graph.addEdge(1, 0, 4)
    graph.addEdge(1, 2, 7)
    graph.addEdge(1, 4, 2)
    graph.addEdge(2, 1, 7)
    graph.addEdge(2, 4, 5)
    graph.addEdge(3, 0, 3)
    graph.addEdge(3, 4, 5)
    graph.addEdge(4, 3, 5)
    graph.addEdge(4, 1, 2)
    graph.addEdge(4, 2, 5)
    print(graph.dijkstra(0))
