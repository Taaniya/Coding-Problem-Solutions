#! /user/bin/env python

"""
This solution implements quick sort algorithm using normal partitioning technique 
to choose pivot as well as with randomized technique, in order to obtain good average-case 
performance over all inputs.

For results of analysis of its performance with & without randomized version, check
out the quick sort analysis notebook in this repository.
"""

import copy
import random 

def partition(a, first, last, randomize):
  # Returns index with which to partition. O(n)
  if randomize:    
    r_index = random.randint(first, last)
    a[r_index], a[last] = swap(a[r_index], a[last])

  pivot = copy.deepcopy(a[last])  
  i = first - 1
  for j in range(first, last):
    if a[j] <= pivot:
      i += 1
      a[i], a[j] = swap(a[i], a[j])
  a[i+1], a[last] = swap(a[i+1], a[last])
  return i + 1

def quicksort(a, first, last, randomize=True):
  """
  E.g., 
    >> arr = [3, 2, 9, 8 , 1, 7, 5]
    >> quicksort(arr, 0, len(arr)-1, randomize=True)
    >> arr
    >> [1, 2, 3, 5, 7, 8, 9]
  """  
  if first < last:       
    q = partition(a, first, last, randomize)              
    quicksort(a, first, q-1)
    quicksort(a, q+1, last)
  return

def swap(a, b):
  return b, a
