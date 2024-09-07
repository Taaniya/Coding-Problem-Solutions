"""
Problem statement: 
----------------------------------------------------
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

E.g., 
1. Input: nums = [2,7,11,15], target = 9
Output: [0,1]

2. Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
-----------------------------------------------------
"""

import collections

class Solution:    
    def twoSum(self, nums, target):
        lookup = collections.defaultdict(set)
        for i,num in enumerate(nums):
            lookup[num].add(i)             # map num and its index
            complement = target - num
            if complement in lookup:
                for comp_id in lookup[complement]:
                    if comp_id != i:
                        return [i,comp_id]
        return []

    def find_indices_pair_sum(arr: List[int], target: int) -> Tuple[int, int]:
        """
        Time & space complexity - O(n)
        """
        num_index_map = {}    # map array elements to indices
    
        for ind1, num1 in enumerate(arr):
            num_index_map[num1] = ind1
            diff = target - num1
            if ((ind2 := num_index_map.get(diff)) is not None) and (ind1 != ind2):
                # only check if not None to avoid failing if valid index returned is zero
                return ind1, ind2
        return -1, -1

        
