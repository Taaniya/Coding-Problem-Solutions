#!/usr/bin/env python

def getLis(arr):
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
    """      
    size = len(arr)
    memo = [1] * size
    done = [0] * size
    maximum = 1
    
    def lis(i,j):   
        nonlocal maximum
        if done[i]:
            return memo[i]
        elif j < 0:
            return 1
        else:
            for j in range(i):                
                if arr[i] > arr[j]:
                    memo[i] = max( lis(j,j-1) + 1, memo[i])
        maximum = max(maximum, memo[i])
        done[i] = 1        
        return memo[i]
    
    for i in range(size):
        _ = lis(i, i-1)
        
    return maximum
