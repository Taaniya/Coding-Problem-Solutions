#!/bin/env python

""" Problem statement - Find all subsets of a given set.
The total no. of subsets of a given set of n elements is sum of combinations of set elements in different sizes - r
= Nc0 + Nc1 + Nc2 + ..... + Ncn = 2^n

This implmementation maintains a list of all possible subsets initializing it with an empty set.
It finds all subsets by iterating over individual elements of given input set and 
updates the list in every iteration. In every iteration for an element in  input set, it adds the element 
in existing subsets in the subset_list maintained while retaining them originally as well. 
The inner loop takes O(2^n) time.

Time & space complexity: O(n2^n)
"""

import copy
def find_all_subset(S):
  """
  E.g., 
  >> subsets_ls = find_all_subset({5})
  >> print(subsets_ls)
  >> [set(), {5}]
  >> print(len(subsets_ls))
  >> 2

  >> subsets_ls = find_all_subset({5, 6})
  >> print(subsets_ls)
  >> [set(), {5}, {6}, {5, 6}]
  >> print(len(subsets_ls))
  >> 4

  >> subsets_ls = find_all_subset({5,6,7,8})
  >> print(subsets_ls)
  >> [set(), {8}, {5}, {8, 5}, {6}, {8, 6}, {5, 6}, {8, 5, 6}, {7}, {8, 7}, {5, 7}, {8, 5, 7}, {6, 7}, {8, 6, 7}, {5, 6, 7}, {8, 5, 6, 7}]
  >> print(len(subsets_ls))
  >> 16

  """
  subset_ls = []                  # list containing all possible subset
  subset_ls.append(set())         # add empty set
  for num in S:                   
    ls_temp = copy.deepcopy(subset_ls)       # create temporary list with updated subsets
    for subset in subset_ls:
      subset_cp = copy.deepcopy(subset)
      subset_cp.add(num)
      ls_temp.append(subset_cp) 
    subset_ls = copy.deepcopy(ls_temp)       # update origian subset list
  return subset_ls


if __name__ == "__main__":
  subsets_ls = find_all_subset({5, 6 })
  print(subsets_ls)
  print(len(subsets_ls))
