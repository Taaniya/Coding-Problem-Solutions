#!/bin/user/env python

def findLongestPath(mat):
    """
    This function finds length of the longest path in a square matrix containing unique integers 
    such that the path contains numbers in the increasing order with a difference of 1.
    This solution is implemented using Dynamic programming approach and memoization.
    Problem statement reference:
    https://www.geeksforgeeks.org/find-the-longest-path-in-a-matrix-with-given-constraints/
    Parameters:
    ------------
    mat : (2D List(int)) Matrix of integers
    
    Returns:
    ------------
    max : (int) Length of longest path
    eg. 
    >> mat = [[10, 11, 3], [5, 2, 1], [6, 7, 8]]
    >> findLongestPath(mat)
    >> 4
    Here, mat = [[10, 11,  3],
               [ 5,  2,  1],
               [ 6,  7,  8]]
    The longest with increasing numbers with difference 1 is from 5,6,7,8.
    
    >> mat = [[2,1],[3,1]]
    >> findLongestPath(mat)
    >> 3
    Path - 1, 2, 3 
    >> mat = [[1, 2, 5], [4, 3, 0], [5, 6, 7]]
    >> findLongestPath(mat)
    >> 7
    """
    lookup = dict()
    maximum = 1
    
    def getLength(x, y , mat, lookup):
        m = len(mat)
        n = len(mat[0])
        nonlocal maximum
        if (x,y) in lookup:
            return lookup[(x,y)]
        if ((x-1) >=0) and ((mat[x-1][y] - mat[x][y]) == 1):
            lookup[(x,y)] = 1 + getLength(x-1,y,mat,lookup)
        elif ((x+1) < m) and ((mat[x+1][y] - mat[x][y]) == 1):
            lookup[(x,y)] = 1 + getLength(x+1,y,mat,lookup)
        elif ((y-1) >= 0) and ((mat[x][y-1] - mat[x][y]) == 1):
            lookup[(x,y)] = 1 + getLength(x,y-1,mat,lookup)
        elif ((y+1) < n) and ((mat[x][y+1] - mat[x][y]) == 1):
            lookup[(x,y)] = 1 + getLength(x,y+1,mat,lookup)
        else:
            lookup[(x,y)] = 1       
        maximum = max(maximum,lookup[(x,y)])
        return lookup[(x,y)]
    
    order = len(mat)
    for i in range(order):
        for j in range(order):
            if (i,j) not in lookup:
                _ = getLength(i,j,mat,lookup)
    return maximum
