#!/user/bin/env python

def findSubset(arr, total):
    """
    Given a set of non-negative integers, and a value sum, determine if there is a subset 
    of the given set with sum equal to given sum.
    
    This solution is solved using Dynamic Programming approach and memoization.
    Parameters:
    --------------
    arr : List(int) 
    total : (int) desired sum
    
    eg.
    >> findsubset([1, 2, 4, 3],6)
    >> True
    
    >> findsubset([1, 2, 5, 8],0)
    >> True
    
    """
    lookup = dict()
    
    def isPresent(arr, sum):
        n = len(arr)
        key = (n,sum)
        if (n == 0) or (total == 0) :
            return sum == total

        elif key in lookup:
            return lookup[key]

        elif sum == total:
            return True

        elif sum > total:
            return False

        else:
            # Either include last element into consideration or we don't
            lookup[key] = isPresent(arr[:n-1], sum + arr[n-1])
            
            # only if a subset adding upto total is still not found, try finding it further
            if not lookup[key]:
                lookup[key] = isPresent(arr[:n-1], sum)           
        return lookup[key]
    found = isPresent(arr,0)
    return found
    
