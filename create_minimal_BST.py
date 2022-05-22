#!/bin/env python

""" This script implements the solution to problem, where given a sorted (increasing order) array with unique elements, 
implement an algorithm to create a binary search tree with minimal height.

This problem is solved with divide and conquer approach. Since an inorder traversal of a BST results in a sorted array,
it indicates that the middle element of array is root of the BST. Similarly, the elements in the left half of array represent the left
subtree and those on the right, represent the right subtree.

Divide: We find the middle of array & insert it to form the root of current subtree. O(Logn) for insertion
Conquer: We recursively perform the above step to solve for 2 subproblems - 2 halves of given array. 2T(n/2) , 
where T(n) is running time of a problem of size n
Combine: Since the elements are inserted in place, no more work is done to combine the results of subarrays.

Overall time complexity - 2T(n/2) + O(logn)
"""

import math

class BSTNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
     
def insert(root, val):
  if root is None:
     root = BSTNode(val) 
  elif val < root.data:
     root.left = insert(root.left, val)
  elif val > root.data:
     root.right = insert(root.right, val)
  elif val == root.data:
    print(f"Node with given data already exists. Can't insert duplicates. val={val}, root.data {root.data}")
  return root

def preorder(root):
  if root is not None:
    print(root.data)
    preorder(root.left)
    preorder(root.right)
  return

def inorder(root):
  if root is not None:
    inorder(root.left)
    print(root.data)
    inorder(root.right)
  return

def postorder(root):
  if root is not None:
    postorder(root.left)
    postorder(root.right)
    print(root.data)
  return

def createBalancedBST(arr, root):
  if len(arr):
    root_id = len(arr) // 2                                     
    root = insert(root, arr[root_id])                           
    _ = createBalancedBST(arr[:root_id], root)                                               
    _ = createBalancedBST(arr[root_id + 1: ], root)
    return root
  
if __name__ == "__main__":
  treenode = createBalancedBST([3, 5, 6, 8, 10, 12, 13], None)
  
  # Traverse the tree to verify
  print("\nInorder traversal")
  inorder(treenode)
  print("\nPreorder traversal")
  preorder(treenode)
  print("\nPostorder traversal")
  postorder(treenode)
