#! /bin/usr/bin/env python
"""
This script contains implementation of edit distance for 2 strings s1, s2, where |s1|=m & |s2|=n, with 3 different approaches.
The time complexity of these algorithms by normal recursion can be O(3 ^ m) and m < n. We make atleast m recursion calls and further recur thrice in every call.
Using memoized recursion, the time complexity is total no. of unique subproblems. Each subproblem cost O(1).
In worst case the two strings are be completely different. It has best case complextity O(1) when the 2 strings are identical.

Time complexity with memoized recursion is O(m*n).
Space complexity - O(m*n).
"""

from functools import lru_cache

count = 0
def editD(a, b, m, n, ed=None):
    """
    Computes edit distance between 2 strings using Dynamic Programming with memoization.
    This function uses an array for memoization.
    Parameters:
    ---------------------
    a : string 1
    b : string 2
    m : lentgh of string 1
    n : length of string 2
    ed : array in memory to store result of sub problems
    
    Returns:
    ---------------------
    Edit distance between string 1 and string 2.
    
    eg.
    >> editD("cut","cutter",3,6)
    >> 3
    
    >> editD("sunday","saturday",6,8)
    >> 3
    """
    global count
    
    if ed is None:
        ed = [[None for j in range(n)] for i in range(m)]
        
    if a[:m] == b[:n]:
        return 0

    if m == 0 :
        return n

    if n == 0 :
        return m

    if ed[m-1][n-1] is not None:
        return ed[m-1][n-1]
    
    elif a[m-1] == b[n-1]:                      # compare last characters
        ed[m-1][n-1] = editD(a, b, m-1, n-1)

    else:
        ed[m-1][n-1] =  1 + min(editD(a, b, m, n-1, ed), editD(a, b, m-1, n, ed), editD(a,b , m-1 ,n-1, ed))
        count += 1
    return ed[m-1][n-1]


dist = {}
def findEditDistance(s1, s2):
    """ This function uses dictionary for memoization.
    eg.
    >> findEditDistance("cut","cutter")
    >> 3
    """
    if dist.get((s1, s2), None):
	return dist[(s1, s2)]
    elif s1 == s2:                                 # equal strings 
      return 0
    elif s1 == "":
        return len(s2)
    elif s2 == "":
	return len(s1)
    elif s1[-1:] == s2[-1:]:                       # compare last characters
        return findEditDistance(s1[:-1], s2[:-1])
    else:
        dist[(s1, s2)] = 1 + min(findEditDistance(s1[:-1], s2) , findEditDistance(s1, s2[:-1]), findEditDistance(s1[:-1], s2[:-1]))
        return dist[(s1, s2)]


@lru_cache(maxsize=100)
def computeED(s1,s2):
    """ This function uses LRU cache for memoization. 
    eg.
    >> computeED("cut","cutter")
    >> 3
    """
    if s1 == s2:
      return 0
    elif s1 == "":
	return len(s2)
    elif s2 == "":
        return len(s1)
    elif s1[-1:] == s2[-1:]:                                # compare last characters
        return computeED(s1[:-1], s2[:-1])
    else:
        return 1 + min(computeED(s1[:-1], s2) , computeED(s1, s2[:-1]), computeED(s1[:-1], s2[:-1]))
 
    
