#!/bin/env python

"""
Given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers 
and return it as a linked list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        head = node = None
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
                head = node = ListNode(value)       
            else:
                node.next = ListNode(value)
                node = node.next
            l1 = l1.next
            l2 = l2.next

        llist = l1 if l1 is not None else l2
        while llist is not None:
            value, carry = add(llist.val, carry, 0)
            node.next = ListNode(value)
            node = node.next
            llist = llist.next             
        if carry == 1:
            node.next = ListNode(carry)
        return head
    
