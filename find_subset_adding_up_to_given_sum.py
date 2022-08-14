#! /user/bin/env python
"""
This script implements solution to subset sum problem using 2 approaches. 
Recursive approach with Time complexity O(2^n)
Dynamic programmic approach with memoization using tabulation with Time complexity O(n^2). Given below.
"""

def findSubset(arr, total):
    """
    Given a set of non-negative integers, and a value sum, determine if there is a subset 
    of the given set with sum equal to given sum.
    
    To find the subsets adding up to a value requires a brute force approach finds all possible combinations 
    of elements & for each combination, checks whether their sum == total.
    Now, the total no. of combinations of n unique no.s is 2^n

    nC0 + nC1 + ...... + nCn = 2^n

    One of the worst cases is that the last combination of elements equal to total is discovered in the end 
    of recursion or when target value is > all elements combined (This can be avoided by a 1 step of linear ordered 
    time check to compare the sum of all current set of elements with total and can stop early if so).

    Hence, for this approach, time & space complexity for worst case = O(2^n)  ( exponential)
    This solution is solved using Dynamic Programming approach and memoization.
    Parameters:
    --------------
    arr : List(int) 
    total : (int) desired sum
    
    eg.
    >> findSubset([4, 11, 7, 5], 12)
    >> {(3, 5): True, (4, 0): True}
    >> 2
    >> True

      # worst case. When subset found in the end.
    >> findSubset( [12, 3, 4, 1], 12)
    >> {(1, 8): False, (2, 5): False, (1, 5): False, (3, 1): False, (1, 4): False, (2, 1): False, (1, 1): False, (4, 0): True, (1, 7): False, (2, 4): False, (3, 0): True, (1, 3): False, (2, 0): True, (1, 0): True}
    >> 14
    >> True

    >> findSubset( [7, 5, 4, 11], 12)
    >> {(3, 11): False, (2, 11): False, (1, 11): False, (4, 0): True, (1, 9): False, (2, 4): False, (1, 4): False, (3, 0): True, (1, 5): True, (2, 0): True}
    >> 10
    >> True

       # worst case. When all the elements donot sum upto total
    >> findSubset( [2, 3, 4, 1], 12)
    >> {(1, 8): False, (2, 5): False, (1, 5): False, (3, 1): False, (1, 4): False, (2, 1): False, (1, 1): False, (4, 0): False, (1, 7): False, (2, 4): False, (3, 0): False, (1, 3): False, (2, 0): False, (1, 0): False}
    >> 14
    >> False
    
      # best case. 1st elements compared is equal to target
    >> findSubset([8, 1, 2, 6], 6)
    >> {(4, 0): True}
    >> 1
    >> True
    """
    lookup = dict()
    
    def isPresent(arr, sum):
        n = len(arr)
        key = (n,sum)
        
        if sum == total:
          return True

        if (n == 0) :
            return False

        elif key in lookup:
            return lookup[key]

        elif sum > total:
            return False

        else:
            # Either include last element into consideration or we don't
            lookup[key] = isPresent(arr[:-1], sum + arr[-1])
            
            # only if a subset adding upto total is still not found, try finding it further
            if not lookup[key]:
                lookup[key] = isPresent(arr[:-1], sum)           
        return lookup[key]
    found = isPresent(arr,0)
    print(lookup)
    print(len(lookup))
    return found


import copy 

def findSubset(arr, total):
  """
  Subset sum problem implemented using Dynamic Programming approach and memoization with tabulation
  A row & column of zeros in the beginning to set up default values in the dp array.
  
  Time and space complexity - O(n^2)
  Reference - https://www.youtube.com/watch?v=zRza99HPvkQ   
  (This can be solved with similar approach as knapsack problem)

  
  Returns:
  -------------
  maximum : (int), Maximum value of subset of items with total sum <= given total
  E.g., 
    >> findSubset([4, 11, 7, 5], 12)
    >> True
    >> findSubset( [12, 3, 4, 1], 12)
    >> True
    >> findSubset( [7, 5, 4, 11], 12)
    >> True
    >> findSubset( [2, 3, 4, 1], 12)
    >> False
  """
  dp = [[0 for col in range(total+1)] for row in range(len(arr)+1)]
  arr = [0] + arr
  subset_found = False

  for i in range(len(dp)):
    if not subset_found:
      for w in range(len(dp[0])):
        if ((w == 0) or (i == 0)):
          dp[i][w] = 0
        elif arr[i] <= w:
          # Either an item is included in the optimal subset or it's not. 
          # We choose max of the 2 resulting choices
          # w - arr[i] = remaining sum if array element i is added 
          # dp[i-1][w-arr[i]] = total value till (i-1)th element
          dp[i][w] = max(arr[i] + dp[i-1][w-arr[i]] , dp[i-1][w])
        else: 
          # When current element value > total
          # use same value as previous row (i.e. prev array element) for same sum column
          dp[i][w] = copy.deepcopy(dp[i-1][w])
        if dp[i][w] == total:                # stop early if subset summing upto total found
          subset_found = True
          break
  
  return subset_found
