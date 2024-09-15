#!/usr/bin/env python
"""
Problem statement - 
To find the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order.
The elements forming longest subsequence need not necessarily be contiguous in given sequence.

Approach - 
Can be solved with DP with memoization by traversing through elements of given array and computing LIS for each element i by comparing it with 
elements previously visited i-2, i-3......, 3, 2, 1, 0. Result of LIS for each element is cached as we proceed with subsequent elements in the array.

Cases :
Example 1 - [2, 4, 1, 5, 9,7, 10]
Example 2 - [7, 7, 7, 7]
Example 3 - [6, 7, 8, 1, 2, 14, 15, 16]
Example 3 has 2 LIS before 14. one subsequence = 6,7,8 and another 1,2.

Steps - 
LIS is computed for element current_idx by comparing it with previous element as past_idx. If arr[past_idx] < arr[current_idx], then current element could
either be only larger than element at past_idx (14 > 2), or there could another longer LIS ending at another element in the past (14 > 8 for subsequence [6,7,8]). 
Thus, finally LIS is computed as max of LIS w.r.t previous element and also in comparison with other elements in the past.

LIS is maintained globally (single global_max value across all elements in given array) and locally for every element in the array. local_max. This value is 
cached in memoization approach.

The time complexity of below implementation is - O(n^2) (traversing through element - O(n) * O(n-1) comparing with n-1 elements in the past)
Space complexity - O(n)   (to recurse for comparison till the 1st element in past)

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
        Find length of longest increasing subsequence using Dynamic Programming - Memoization.
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

