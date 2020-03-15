#!/usr/bin/env python

def getLis(arr):
    """
    Find length of longest increasing subsequence using Dynamic Programming - Memoization
    
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
        size = len(arr)
        if size == 1:
            return 1
        
        else:
            for j in range(size - 1 ):
                if not done[j]:
                    memo[j] = lis(arr[:j+1])
                    done[j] = 1
                    maximum = max(maximum, memo[j])

                if arr[size-1] > arr[j]:
                    memo[size-1] = max( memo[j] + 1, memo[size-1])
                    maximum = max(maximum, memo[size-1])
        
        done[size-1] = 1        
        return memo[size-1]
    _ = lis(arr)
    return maximum

