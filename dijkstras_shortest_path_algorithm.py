#! /usr/bin/env python

import sys
import math
from collections import defaultdict
from typing import Tuple

class MinHeap():
    def __init__(self):
        self.queue = []       # maintains nodes as tuple (<priority>, <node_id>)
        self.pos = {}         # Indices of nodes in queue       
        
    def qsize(self): 
        return len(self.queue)
        
    def par(self, i): 
        """Returns i's parent node"""
        return  math.floor((i-1)/2)
        
    def left(self, i): 
        return 2*i + 1
    
    def right(self, i): 
        return 2*i + 2
        
    def insert(self, tup: Tuple[int, int]) -> None:
        """
        Paremeters:
        tup: tuple holding priority of node & its unique id.
        """
        self.queue.append(tup)         # insert in the end
        self.pos[tup[1]] = self.qsize() - 1
        self.decrease_key((self.pos[tup[1]], tup[1]), tup[0])    # move to a suitable position w.r.t. priority
        # self.bubble_up(tup, current_idx=self.pos[tup[1]])
        
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
            
    def decrease_key(self, tup: Tuple[int, int], pr: int) -> None:
        """
        Moves the node from its current position in the heap to an appropriate position 
        w.r.t given priority `pr`.
        
        Paremeters:
        ------------------------
        tup: tuple holding current index of node, and unique id of node.
        pr: priority of this node
        """
        idx = self.pos[tup[1]]        # Get current position in queue
        
        self.queue[idx] = (pr, tup[1])
        while (idx > 0) and (self.queue[self.par(idx)][0] > pr) : 
            self.swap(idx, self.par(idx))
            idx = self.par(idx)
        # self.bubble_up(node=self.queue[idx], current_idx=idx)
            
    def extract_min(self):
        """ Extracts 1st element (smallest) from the min_heap. Swaps it with the last element in the heap.
        Calls min_heapify to move this element to its appropriate position in the heap to restore
        min-heap property.
        """
        if self.qsize() != 0 :
            min_node = self.queue[0][1]
            self.queue[0] = self.queue[self.qsize() - 1]
            del self.queue[self.qsize() - 1]
            self.min_heapify(0)
            # self.bubble_down(0)
            del self.pos[min_node]
            return min_node
        else:
            print("heap is empty")

    def bubble_down(self, i):
        """
        Used by extract-min methods after removing min value and replacing it with largest element from the end.
        """
        lc = self.left(i)
        rc = self.right(i)

        if (lc < self.qsize()) and (self.queue[lc][0] < self.queue[i][0]):
            minimum = lc
        else:
            minimum = i
        if (rc < self.qsize()) and (self.queue[rc][0] < self.queue[minimum][0]):
            minimum = rc
        if i != minimum:
            self.swap(i, minimum)
            self.bubble_down(minimum)
        else:
            # Heap invariant is satisfied
            return

    def bubble_up(self, node: Tuple[int, int], current_idx: int) -> None:
        """
        To be used by insert & decrease_key() method for a node when its priority (distance from source) decreases
        """
        pr = node[0]
        parent_idx = self.par(current_idx)
        while (parent_idx > 0) and (pr < self.queue[parent_idx][0]):
                self.swap(current_idx, parent_idx)
                current_idx = copy.deepcopy(parent_idx)
                parent_idx = self.par(current_idx)

class Graph():
    def __init__(self):
        self.graph = defaultdict(set)
        self.v = 0
        
    def addEdge(self, u, v, w):
        '''Adds an edge from u to v with edge weight w. '''
        self.graph[u].add((v,w))
        self.v = len(self.graph)
        
    def dijkstra(self, src):
        """
        Implements Dijkstra's algorithm to compute shortest path from a source node to all other nodes in the graph
        represented as edglist. This implementation uses min-Priority queue using Binary Heap and calls three priority queue operations
        insert, extract-min & decrease-key (implicit while relaxing).
        
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
        unvisited = MinHeap()        
        visited = set()
        dist = []      # hold shortest distance from source for each node in the graph
        for v_id in range(0, self.v):
            if v_id != src:
                # initialize shortest distance from source as infinite
                dist.append(sys.maxsize)
                unvisited.insert((sys.maxsize, v_id))
            else:
                unvisited.insert((0, src))
                dist.append(0)
        # Perform BFS traversal
        while unvisited.queue:
            min_node = unvisited.extract_min()
            visited.add(min_node)
            for nbr,w in self.graph[min_node]:
                new_dist = w + dist[min_node]
                if new_dist < dist[nbr]:
                    # update shortest distance from source / update priority
                    unvisited.decrease_key((dist[nbr], nbr), new_dist)    
                    dist[nbr] = new_dist 
        return dist
