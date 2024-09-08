"""
Problem statement:
Given a list of bombs, where the range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.
The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb,
whereas ri denotes the radius of its range.
You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.
Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.

Example:
Input: bombs = [[2,1,3],[6,1,4]]
Output: 2

Input: bombs = [[1,1,5],[10,10,5]]
Output: 1

Input: bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
Output: 5

Input: bombs = [[4,4,3],[4,4,3]]
Output: 2
"""
from typing import List, Tuple
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(set)

    def add(self, u: int, v: int):
        """Adds edge from u to v"""
        self.graph[u].add(v)

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        max_count = 1
        graph = Graph()

        # Build connections
        for i, bomb1 in enumerate(bombs):
            for j in range(i+1, len(bombs)):
                bomb2 = copy.deepcopy(bombs[j])
                if self.is_in_range(bomb1, bomb2):
                    graph.add(i, j)
                if self.is_in_range(bomb2, bomb1):
                    graph.add(j, i)
        # Count no. of bombs that detonate
        for i in range(len(bombs)):
            count = BFS(src=i, graph=graph.graph)
            max_count = max(max_count, count)
        return max_count

    def is_in_range(self, 
                    b1: Tuple[int, int, int], 
                    b2: Tuple[int, int, int]
                   ) -> bool:
        """
        Returns True if b2 lies in b1’s range. 
        B1 will denotate b2, if edge exists between b1 and b2.
        """
        if ((b1[0] - b2[0]) ** 2) + ((b1[1] - b2[1]) ** 2) <= (b1[2] ** 2):
            return True
        return False

def BFS(src: int, graph: Graph):
    visited = set()
    queue = deque()
    queue.append(src)

    while (queue):
        node = queue.popleft()
        visited.add(node)
        for nbr in graph[node]:
            if nbr not in visited:
                queue.append(nbr)

    return len(visited)
