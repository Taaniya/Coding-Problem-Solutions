#!/usr/bin/env python

def getLis(arr):
    """
    Find length of longest increasing subsequence.
    
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
    maximum = 1
    memo = [1] * (len(arr))
    done = [0] * (len(arr))

    def lis(arr):   
        nonlocal maximum
        n = len(arr)
        if len(arr) == 1:
            return 1
        
        for j in range(len(arr) - 1 ):
            if not done[j]:
                memo[j] = lis(arr[:j+1])
                done[j] = 1
                maximum = max(maximum, memo[j])
                
            if arr[n-1] > arr[j]:
                memo[n-1] = max( memo[j] + 1, memo[n-1])
                maximum = max(maximum, memo[n-1])
        
        done[n-1] = 1        
        return memo[n-1]
    _ = lis(arr)
    return maximum

