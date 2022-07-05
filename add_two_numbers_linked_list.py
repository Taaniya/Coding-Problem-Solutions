#!/bin/env python

"""
Problem statement - Given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order (least significant digit at head) and each of their nodes contain a single digit. Add the two numbers 
and return it as a linked list.

Time complexity = max(m,n) where m, n are length of lists l1 & l2 and the algorithms iterate through the longest list
Space complexity = Length of the resulting list containing the sum is of maximum length = max(m,n) + 1, where is for carry.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        result = node = None
        carry = 0
        def add(a, b, carry):
            total = a + b + carry
            c = 0
            if total >= 10:
                total %= 10
                c = 1
            return total, c
            
        while (l1 is not None) and (l2 is not None):
            value, carry = add(l1.val, l2.val, carry)
            if node is None:
                result = node = ListNode(value)       
            else:
                node.next = ListNode(value)
                node = node.next
            l1 = l1.next
            l2 = l2.next

        llist = l1 if l1 is not None else l2
        while llist is not None:     # traverse through remaining list if other has ended
            value, carry = add(llist.val, carry, 0)
            node.next = ListNode(value)
            node = node.next
            llist = llist.next             
        if carry:                    # add remaining carry in result if present 
            node.next = ListNode(carry)
        return result
 
 

if __name__ == "__main__":
  # Examples
  # l1 = [1] , l2 = [7,3] => [8,3] => 1 + 37 = 38  
  # l1 = [0] , l2 = [7,3] => [7,3] => 0 + 37 = 37
  # l1 = [3] , l2 = [7,3] => [0,4] => 3 + 37 = 40
  # l1 = [8,9] ,l2 = [2] => [0,0,1] => 98 + 2 = 100
    l1 = ListNode(8)
    l1.next = ListNode(9)
    l2 = ListNode(2)
    sol = Solution()
    result_list = sol.addTwoNumbers(l1, l2)
    while result_list is not None:
        print(result_list.val)
        result_list = result_list.next
