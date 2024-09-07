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

from collections import deque

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
            max_len = max(max_len, subarray_len)
            
            prev_ele = nums[i]    # update head of previous subarray

# Alternative solution
import bisect

# Below is an optimal algorithm to solve given problem as shared in below link
# https://youtu.be/tkXKAJ7jNGo?si=mbpM7hr9Laqs1j5v
# Time complexity - O(nlogn)
class Solution:
    def max_subarray(self, nums: List[int]):
        """
        Approach - 
        possible - Maintains a list of tuple holding contiguous elements from the end of given array as negated values in increasing order. The tuple holds the 
        elements and their index in given array.
        best - holds the current longest length of semi-decreasing array so far.
        """
        N = len(nums)
        INF = float('inf')
        best = 0

        possible = [(-INF, N)]
        for index in range(N-1, -1, -1):
            x = nums[index]

            sindex = bisect.bisect_left(possible, (-x, INF))
            if 0 <= sindex < len(possible):
                best = max(best, possible[sindex][1] - index + 1)

            if -x > possible[-1][0]:
                possible.append((-x, index))

        return best


        def max_subarray_v2(self, nums: List[int]):
            """
            Another alternative version similar to above, but hopefully easier to understand.

            Approach - 
            Since the desired subarray has 1st element strictly greater than the last element, we start with traversing the given array 
            from the end to start. While visiting elements from end, we store smallest element seen so far in a list - possible.
            This way 'possible' holds these elements in an increasing order and any new smallest element is added in the beginning. 
            The elements are stored as tuple to also maintain their index in given array.

            For every element in given array, it's position in the sorted array - possible is identified using bisec_left. If its index is
            identified in the middle of elements in collection, it's deduced to be greater than atleast 1 element seen so far. Thus we compute the 
            distance between index of current element and the element in possible which currently lies at identified index to get length of this 
            semi-decreasing array. The longest length for a given element is return as the final answer.

            Time complexity - O(nlogn) (involves single for loop (O(n)) and bisect_left (O(logn)) for every element during an iteration. 
            Space complexity - O(n)
            """
            N = len(nums)
            INF = float('inf')
            best = 0
            possible = deque()
            possible.appendleft((INF, N))
            local_max = {}
            for index in range(N-1, -1, -1):
                x = nums[index]
                sindex = bisect.bisect_left(possible, x, key=lambda r: r[0])
                if 0 < sindex < len(possible):
                    local_max[(x, index)] = possible[sindex-1][1] - index + 1
                    best = max( best, local_max[(x, index)])
    
                if x < possible[0][0]:
                    possible.appendleft((x, index))
        return best
