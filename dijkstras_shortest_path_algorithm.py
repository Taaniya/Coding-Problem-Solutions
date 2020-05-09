#! /usr/bin/env python

import sys
import math

class MinHeap():
    def __init__(self):
        self.queue = []
        self.pos = {}         # Indices of nodes in queue       
    def qsize(self): return len(self.queue)
    def par(self, i): return  math.floor((i-1)/2)
    def left(self, i): return 2*i + 1
    def right(self, i): return 2*i + 2
    def insert(self, tup):
        self.queue.append(tup)         # insert in the end
        self.pos[tup[1]] = self.qsize() - 1
        self.decrease_key((self.pos[tup[1]], tup[1]), tup[0])    # move to a suitable position w.r.t. priority
    def swap(self, idx1, idx2):
        '''swaps tuples at given indices'''
        node1 = self.queue[idx1][1]
        node2 = self.queue[idx2][1]
        self.queue[idx1], self.queue[idx2] = self.queue[idx2], self.queue[idx1]
        self.pos[node1], self.pos[node2] = idx2, idx1
    def min_heapify(self, i):
        lc = self.left(i)
        rc = self.right(i)
        if (lc < self.qsize()) and (self.queue[lc][0] < self.queue[i][0]):
            minimum = lc   
        else:
            minimum = i
        if (rc < self.qsize()) and (self.queue[rc][0] < self.queue[minimum][0]):
            minimum = rc
        if i!=minimum:
            self.swap(i, minimum)
    def decrease_key(self, tup, pr):
        idx = self.pos[tup[1]]        # Get current position in queue
        # update priority and then move it to position w.r.t priority
        self.queue[idx] = (pr, tup[1])
        while (idx > 0) and (self.queue[self.par(idx)][0] > pr) : 
            self.swap(idx, self.par(idx))
            idx = self.par(idx)
    def extract_min(self):
        if self.qsize() != 0 :
            min_node = self.queue[0][1]
            self.queue[0] = self.queue[self.qsize() - 1]
            del self.queue[self.qsize() - 1]
            self.min_heapify(0)
            del self.pos[min_node]
            return min_node
        else:
            print("heap is empty")
 

class Graph():
    def __init__(self, graph, v):
        self.graph = graph
        self.v = v
        
    def dijkstra(self, src):
        """
        Implements Dijkstra's algorithm to compute shortest path from a source node to all other nodes in the graph
        represented as adjacency matrix. This implementation uses Priority queue using Binary Heap.
        Parameters:
        --------------
        src - index of source node
        Returns:
        --------------
        dist - list of distances of each node of graph from the source node    
        eg.
        >> adj = [[1,4,0,3,0],
                   [4,1,7,0,2],
                   [0,7,1,0,5],
                   [3,0,0,1,5],
                   [0,2,5,5,1]] 
        >> graph = Graph(graph=adj, v=5)
        >> graph.dijkstra(0)
           [0, 4, 11, 3, 6]
        """
        unvisited = MinHeap()        
        dist = []
        for v_id in range(0, self.v):
            if v_id != src:
                dist.append(sys.maxsize)
                unvisited.insert((sys.maxsize, v_id))
            else:
                unvisited.insert((0, src))
                dist.append(0)
        while unvisited.queue:
            min_node = unvisited.extract_min()
            for node_dist,node in unvisited.queue:
                w = self.graph[min_node][node] 
                new_dist = w + dist[min_node]
                if (w > 0) and (new_dist < node_dist):
                    unvisited.decrease_key((node_dist, node), new_dist)
                    dist[node] = new_dist 
        return dist
