"""
Problem statement:
Given an integer array, find the length of the longest semi-decreasing subarray of. Return 0 if there are no such subarrays.
A subarray is a contiguous non-empty sequence of elements within an array.
A non-empty array is semi-decreasing if its first element is strictly greater than its last element.

E.g., input nums = [7,6,5,4,3,2,1,6,10,11]
Output: 8
Due to subarray - [7,6,5,4,3,2,1,6]

E.g., input nums = [57,55,50,60,61,58,63,59,64,60,63]
Output: 6
Due to subarray [61,58,63,59,64,60]

E.g., input nums = [1,2,3,4]
Output: 0
There is no decreasing sub array.
"""

class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        prev_ele = float('-inf')
        max_len = 0

        for i in range(len(nums)):
            if nums[i] <= prev_ele:
                continue
            last_ele_index = i-1

            for j in range(len(nums) -1, i, -1):          # check from end of list (right) till i (left)
                if nums[j] < nums[i]:
                    last_ele_index = j
                    break
            subarray_len = last_ele_index - i + 1         # length of longest subarray beginning with i
            if subarray_len > max_len:
                max_len = subarray_len
            
            prev_ele = nums[i]    # update head of previous subarray

        return max_len        
