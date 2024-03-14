#!/usr/bin/env python
"""
Problem statement - 
To find the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order.
The elements forming longest subsequence need not necessarily be contiguous in given sequence.

The time complexity of below implementation is - O(n^2)
Space complexity - O(n)

"""
from typing import List

def getLis(arr: List[int]) -> int:
    """
    Find length of longest increasing subsequence using Dynamic Programming - Memoization.
    Parameters :
    -------------------
    arr = List(int)
    
    Returns :
    -------------------
    maximum = int 
    eg.
    >>> getLis([10, 22, 9, 33, 21, 50, 41, 60])
    >>> 5
    
    >>> getLis([10, 22, 33, 15, 5, 50])
    >>> 4

    >> getLis([0,1,0,3,2,3])
    >> 4

    >> getLis([4])
    >> 1

    >> getLis([7,7,7,7,7,7,7])
    >> 1
    """      
    size = len(arr)
    memo = [1] * size
    done = [0] * size
    maximum = 0
    
    def lis(current,prev):   
        nonlocal maximum
        if done[current]:
            return memo[current]
        elif prev < 0:
          memo[current] = 1
        else:
            for k in range(current):                
                if arr[current] > arr[k]:
                    memo[current] = max( lis(k,k-1) + 1, memo[current])
        maximum = max(maximum, memo[current])
        done[current] = 1        
        return memo[current]
    
    for i in range(size):
        _ = lis(i, i-1)
        
    return maximum


from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Time complexity of below implementation - O(n^2)

        eg.
        >>> getLis([10, 22, 9, 33, 21, 50, 41, 60])
        >>> 5
        
        >>> getLis([10, 22, 33, 15, 5, 50])
        >>> 4
    
        >> getLis([0,1,0,3,2,3])
        >> 4
    
        >> getLis([4])
        >> 1
    
        >> getLis([7,7,7,7,7,7,7])
        >> 1
        
        >> Solution().lengthOfLIS([0])
        >> 0

        >> >> Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6])
        >> 6
        """
        global_max = 1
        local_max = 1
        lis = [1 for _ in range(len(nums))]

        def _lis(current_idx: int, past_idx: int) -> int:
            # base case
            if past_idx == 0:
                if nums[current_idx] > nums[past_idx]:
                  lis[current_idx] = 2
                else:
                   lis[current_idx] = 1
            elif past_idx < 0:
                lis[current_idx] = 1
            elif nums[current_idx] > nums[past_idx]:
                lis[current_idx] = max(1+lis[past_idx], _lis(current_idx, past_idx-1))
            else:
                lis[current_idx] = _lis(current_idx, past_idx-1)
            return lis[current_idx]

        if len(nums) > 1:
            # call _lis iteratively
            for i in range(1, len(nums)):
                local_max = _lis(i, i-1)
                if local_max > global_max:
                    global_max = local_max
        return global_max

