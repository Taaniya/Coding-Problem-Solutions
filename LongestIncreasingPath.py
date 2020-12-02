#!/bin/user/env python
"""
    This solution finds length of the longest increasing path in a matrix containing  
    such that the path contains numbers in the increasing order.
    This solution is implemented using Dynamic programming approach and memoization.
    Problem statement reference:
    https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

    Parameters:
    ------------
    mat : (2D List(int)) Matrix of integers
    
    Returns:
    ------------
    max_length : (int) Length of longest path
    eg. 
    >> mat = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    >> Solution()longestIncreasingPath.(mat)
    >> 4
    Here, mat = [
				  [9,9,4],
				  [6,6,8],
				  [2,1,1]
				] 
    The longest with increasing numbers from 1,2,6,9.    
    """

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        if not m :                     # if matrix has no elements
            return 0
        n = len(matrix[0])
        lookup = dict()
        max_length = 1
        
        def getLength(x, y , mat, lookup):
            nonlocal max_length
            p, q, r, s = -1, -1, -1, -1
            if (x,y) in lookup:
                return lookup[(x,y)]
            if ((x-1) >=0) and (mat[x-1][y] > mat[x][y]):
                p = 1 + getLength(x-1,y,mat,lookup)
            if ((x+1) < m) and ((mat[x+1][y] > mat[x][y])):
                q = 1 + getLength(x+1,y,mat,lookup)
            if ((y-1) >= 0) and ((mat[x][y-1] > mat[x][y])):
                r = 1 + getLength(x,y-1,mat,lookup)
            if ((y+1) < n) and ((mat[x][y+1] > mat[x][y])):
                s = 1 + getLength(x,y+1,mat,lookup)
            
            lookup[(x,y)] = max(1, (max(p, max(q, max(r,s)))))       
            max_length = max(max_length, lookup[(x,y)])
            return lookup[(x,y)]

        for i in range(m):
            for j in range(n):
                if (i,j) not in lookup:
                    _ = getLength(i, j, matrix, lookup)               
        return max_length