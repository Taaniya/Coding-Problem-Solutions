#!/bin/env python

"""
Problem statement - The car manufacturer Honda holds their distribution system in the form of a tree (not necessarily binary). 
The root is the company itself, and every node in the tree represents a car distributor that receives cars from the 
parent node and ships them to its children nodes. The leaf nodes are car dealerships that sell cars direct to consumers. 
In addition, every node holds an integer that is the cost of shipping a car to it.

Solution: 
if the root is also a leaf, the best Sales Path, is simply the value in the node itself. This is the base case for the solution. 

If the root has children, then the minimal Sales Path is also a minimal path from the root’s child. Thus, if we already know the 
minimal cost for the root’s children, then the minimal cost for the root is simply the minimum of the values for its children plus the value 
stored in the root itself.

Time complexity = O(n). Each node in the tree is visited atmost once with recursion.
Space complexity = Maxium O(n) sapce for the stack to hold recursive calls.
"""

import sys
import copy

class Node:
  def __init__(self, cost: int):
    self.cost = cost
    self.children = []
       
def findMinimalPath(root: Node) -> int:
  if not len(root.children):
    min_cost = root.cost
  else:
    min_cost = sys.maxsize

  for child in root.children:         
    cost = child.cost + findMinimalPath(child)
    if cost < min_cost:
      min_cost = copy.deepcopy(cost)
  return min_cost      

def printTree(root: Node) -> None:
  print(f"\nNode:{root.cost}")
  for child in root.children:
    print(f"child node: {child.cost}")
    printTree(child)
  
  if not root.children:
    print(f"Node {root.cost} is leaf.")
  return


if __name__ == "__main__":
  root = Node(0)
  five = Node(5)
  three = Node(3)
  two = Node(2)
  zero = Node(0)
  one = Node(1)
  six = Node(6)

  six.children = [Node(1) , Node(5)]
  zero.children = [Node(10)]
  one.children = [Node(1)]
  five.children = [Node(4)]

  two.children = [one]
  three.children = [two, zero]

  root.children = [five, six, three]
  print(f"sales path length from root: {findMinimalPath(root)}")

  root.children = [five, two]
  print(f"sales path length from root: {findMinimalPath(root)}")

  print(f"sales path length from leaf node 10: {findMinimalPath(Node(10))}")

  printTree(root)
