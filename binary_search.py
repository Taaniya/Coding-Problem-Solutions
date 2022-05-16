#!/bin/env python

def binary_search(ls, x):
  """ This function performs binary search for a given element in given array
  sorted in ascending order. 
  Time complexity - O(logn)
  """
  low, high = 0, len(ls) - 1
  mid = low + (high - low) // 2     # we write this instead of (low + high) // 2 
  old_mid = None                    # to avoid integer overflow
  found = False

  if x >= ls[0] and x <= ls[high]:
    while (mid != old_mid):
      if x == ls[mid]:
        return mid
      elif x == ls[high]:
        return high
      if x < ls[mid]:
        high = mid
      else:
       low = mid
      old_mid = mid
      mid = low + (high-low) // 2
  return -1
