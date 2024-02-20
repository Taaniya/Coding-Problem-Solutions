#!/bin/env python

from typing import List

def binary_search(ls: List[float], x: float) -> int:
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


def binary_search(arr: List[float], ele: float) -> int:
    mid_idx = len(arr) // 2          
    st_idx = 0
    end_idx = len(arr) - 1 

    while((mid_idx >= st_idx) & (mid_idx <= end_idx)):
        if ele == arr[mid_idx]:          # found
            return mid_idx
        elif ele < arr[mid_idx]:
            end_idx = mid_idx - 1
            mid_idx = (st_idx + end_idx ) // 2
        elif ele > arr[mid_idx]:
            st_idx = mid_idx + 1
            mid_idx = (st_idx + end_idx ) // 2
    return -1             # not found 
