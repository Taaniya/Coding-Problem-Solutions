#! /user/bin/env python

def findMax(items, weights, w):
    """
    Solution for 0/1 Knapsack problem implemented using Dynamic Programming approach and memoization.
    
    Parameters:
    -------------
    items : List(int), list of integers representing items
    weights : List(int), list of weights corresponding to each item
    w : (int) weight capacity of knapsack
    
    Returns:
    -------------
    maximum : (int), Maximum value of subset of items with total weight <= weight capacity.
    
    eg.
    >> findMax([2,3,5,7],[2,4,6,8],10)
    >> 9
    
    """
    # key-value pairs where key is a tuple(size,total value)
    lookup = dict()
    maximum = 0         # maximum total weight
    
    def isPresent(size,k,total):
        nonlocal maximum
        # key = (size,total)
        key = (size,k)
        
        if key in lookup:
            return lookup[key]
        if size == 0:
            if k <= w:
                maximum = max(maximum, total)
                lookup[key] = total
            else:
                lookup[key] = 0
            return lookup[key]
        elif k > w:
            return 0
        maximum = max(maximum, total)
        # Either an item is included in the optimal subset or it's not.
        # We'll try both and cache the boolean result whether 
        # the total weight <= weight capacity
        inc = isPresent(size-1, k+weights[size-1], total+items[size-1])
        exc = isPresent(size-1, k, total)
        lookup[key] = max(inc, exc)
        return   lookup[key]
    
    _ = isPresent(len(items),0,0)
    return maximum
