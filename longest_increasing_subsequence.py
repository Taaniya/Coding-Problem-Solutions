#!/usr/bin/env python
"""
Problem statement - 
To find the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order.
The elements forming longest subsequence need not necessarily be contiguous in given sequence.

The time complexity of below implementation is - O(n^2)
Space complexity - O(n)

"""
from typing import List

def getLis(arr: List[int]) -> int:
    """
    Find length of longest increasing subsequence using Dynamic Programming - Memoization.
    Parameters :
    -------------------
    arr = List(int)
    
    Returns :
    -------------------
    maximum = int 
    eg.
    >>> getLis([10, 22, 9, 33, 21, 50, 41, 60])
    >>> 5
    
    >>> getLis([10, 22, 33, 15, 5, 50])
    >>> 4

    >> getLis([0,1,0,3,2,3])
    >> 4

    >> getLis([4])
    >> 1

    >> getLis([7,7,7,7,7,7,7])
    >> 1
    """      
    size = len(arr)
    memo = [1] * size
    done = [0] * size
    maximum = 0
    
    def lis(current,prev):   
        nonlocal maximum
        if done[current]:
            return memo[current]
        elif prev < 0:
          memo[current] = 1
        else:
            for k in range(current):                
                if arr[current] > arr[k]:
                    memo[current] = max( lis(k,k-1) + 1, memo[current])
        maximum = max(maximum, memo[current])
        done[current] = 1        
        return memo[current]
    
    for i in range(size):
        _ = lis(i, i-1)
        
    return maximum
