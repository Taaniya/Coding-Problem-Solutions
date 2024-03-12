#! /user/bin/env python

"""
Problem statement- 
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 
i.e., given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items 
respectively.You cannot break an item, either pick the complete item or don’t pick it (0-1 property).
"""
import copy

def findMaxSet(items, weights, cp):
  """
  Solution for 0/1 Knapsack problem implemented using Dynamic Programming with tabulation.
  A row & column of zeros in the beginning to set up default values in the dp array.
  
  Time and space complexity - O(n * w)
  Reference - https://www.youtube.com/watch?v=zRza99HPvkQ   

  Parameters:
  -------------
  items : List(int), list of integers representing items
  weights : List(int), list of weights corresponding to each item
  w : (int) weight capacity of knapsack
  
  Returns:
  -------------
  maximum : (int), Maximum value of subset of items with total weight <= weight capacity.
  eg.
    >> findMaxSet([5,7, 2,3],[6,8,2,4],15)
    >> 12
    >>
    >> findMaxSet([1, 2, 5, 6],[2, 3, 4, 5],8)
    >> 8

  """
  dp = [[0 for col in range(cp+1)] for row in range(len(items)+1)]
  items = [0] + items
  weights = [0] + weights

  for i in range(len(dp)):
    for w in range(len(dp[0])):
      if ((w == 0) or (i == 0)):
        dp[i][w] = 0
      elif weights[i] <= w:
        # Either an item is included in the optimal subset or it's not. 
        # We choose max of the 2 resulting choices
        # w - weights[i] = remaining capacity of knapsack if item i with weight w[i] is added 
        # dp[i-1][w-weights[i]] = total value till (i-1)th item
        dp[i][w] = max(items[i] + dp[i-1][w-weights[i]] , dp[i-1][w])
      else: 
        # When current item's weight > capacity
        # use same value as previous row (i.e. prev item) for same weight column
        dp[i][w] = copy.deepcopy(dp[i-1][w])
  return dp[len(items)-1][cp]
