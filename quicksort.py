#! /user/bin/env python

"""
This solution implements quick sort algorithm with randomized partitioning technique 
to choose pivot in order to obtain good average-case performance over all inputs.

For results of analysis of its performance with & without randomized version, check
out the quick sort analysis notebook in this repository.
"""

import copy
import random 

def partition(a, first, last, randomize):
  """
  Chooses a pivot and divides given array into 2 sub arrays such that elements in sub array 1 
  is <= pivot and those in 2nd sub array are > pivot. The elements within the sub array may be unsorted
  in the output of this function. Sub sequently, the recursive to quicksort performs sorting of elements in each 
  sub array, each time placing the pivot at an appropriate position in the array.
  """
  # Returns index with which to partition. O(n)
  if randomize:    
    r_index = random.randint(first, last)
    a[r_index], a[last] = swap(a[r_index], a[last])

  pivot = copy.deepcopy(a[last])  
  i = first - 1
  for j in range(first, last):
    if a[j] <= pivot:
      i += 1               # increment i until a[j] > pivot
      a[i], a[j] = swap(a[i], a[j])
    # else, continue. i.e., increment j until a[j] <= pivot is encountered
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
