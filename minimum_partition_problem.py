#! /usr/bin/env python

import copy

""" 
Problem statement - To divide a given set of positive integers into 2 subsets such that 
the absolute difference between the sum is minimum and returns this difference. 
A brute force approach is to use a recursive function to find all possible combinations of 
array elements to form 2 sets & find the optimal solution with minimum difference in the sums of 2 sets.
we start by including elements from the given array one by one and we either include it in set 1 or 
set 2. 

The recursion tree of an example if illustrated in this repo. 
The time complexity of such approach is O(2^n).

This function below, implements the solution with dynamic programming approach. Closely looking at the
recursion tree shows that many function calls are repetitive - overlapping subroblems & each recursion can be
solved optimally. Also, since the order of selecting the elements of given array doesn't matter, we see that 
the 2 halves of the recursion tree are symmetric. We can memoize computations performed during one choice 
of including an element for set 1 & look it up when we come across a choice of including the same element in 
the set 2.

Here, each subproblem is uniquely identified by the index of last array element & sum of elements in a partition.
On obtaining a result of a subproblem, this function memoizes it w.r.t sum of both partitions 
(idx, s1) & (idx, s2) separately to avoid recomputations. 
However, the lookup is made w.r.t (idx & s1) only & not s2 to stay consistent.
"""

def get_min_partition_diff(s, s1, s2, lookup=None):
  """
  Parameters:
  ----------------------
  s : list of positive integers
  s1 : sum of integers in subset 1
  s2 : sum of integers in subset 2
  lookup : dictionary data structure holding precomputed values of difference for a tuple of (n,s1) as key
  
  Returns:
  ----------------------
  (int) Minimum difference between 2 subsets
  eg. 
  >> get_min_partition_diff([10,25,15,5,20], 0, 0)
  >> 5
  >>
  where,
  subset 1 : [15, 25]
  subset 2 : [10,5, 20]
  >>
  >> get_min_partition_diff([3, 5, 7], 0, 0)
  >> 1
  >> get_min_partition_diff([3, 1, 4, 2, 2, 1], 0, 0)
  >> 1
  >> get_min_partition_diff([ 1, 6, 11, 5 ], 0, 0)
  >> 1
  >> get_min_partition_diff([1,1,1, 1,2], 0, 0)
  >> 1

  Reference:
    https://www.techiedelight.com/minimum-sum-partition-problem/
  """
  if lookup is None:
    lookup = {}
  
  # deduce the index of last element in given list of integers
  idx = len(s) - 1
  
  # when all the elements are included in either s1 or s2, return the difference of their sums
  if idx < 0:
    return abs(s1 - s2)

  # uniquely identify each subpoblem with idx of last integer & sum of elements in s1
  key = (idx, s1)

  if key in lookup:
    return lookup[key]

  if key not in lookup:
    # Either add the last integer of list in s1 or add it into s2 & recurse for remaining elements
    # Gather partition difference for both scenarios & choose the minimum of the 2
    d1 = get_min_partition_diff(s[:-1], s1 + s[idx], s2, lookup)
    d2 = get_min_partition_diff(s[:-1], s1, s2 + s[idx], lookup)
    lookup[key] = min(d1, d2)
    lookup[(idx, s2)] = copy.deepcopy(lookup[key])          # Perform memoization for both s1 & s2   
  
  return lookup[key]
