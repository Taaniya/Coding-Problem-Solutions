"""
Problem statement:
Given the root of a binary tree, find the number of nodes where the value of the node is equal to the average of the values in its subtree.
- The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
- A subtree of root is a tree consisting of root and all of its descendants.

E.g.,
Input: root = [4,8,5,0,1,null,6]   (Level order traversal)
Output: 5

Input: root = [1]
Output: 1
"""

import math 
from typing import Tuple

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def explore_substree(root: TreeNode) -> Tuple[int, int, int]:
            """
            Explores a node and return num nodes and the weighted sum in its subtree by DFS.
            Also returns no. of nodes having value equal to avg of the values of all nodes
            in its subtree.
            All leaf nodes will have value equal to avg of all node values in the subtree.
            """
            num_left_nodes = 0
            num_right_nodes = 0
            weighted_sum = 0
            num_nodes_equal_avg_val = 0

            if root.left:
                num_left_nodes, left_weighted_sum, num_n_eq_avg = explore_substree(root.left)
                weighted_sum += left_weighted_sum
                if num_n_eq_avg:
                    num_nodes_equal_avg_val += num_n_eq_avg
        
            if root.right:
                num_right_nodes, right_weighted_sum, num_n_eq_avg = explore_substree(root.right)
                weighted_sum += right_weighted_sum
                if num_n_eq_avg:
                    num_nodes_equal_avg_val += num_n_eq_avg
            
            weighted_sum += root.val
            avg = int(math.floor(weighted_sum / (num_right_nodes + num_left_nodes + 1)))
            
            if avg == root.val:
                num_nodes_equal_avg_val += 1

            return num_right_nodes + num_left_nodes + 1, weighted_sum, num_nodes_equal_avg_val
            
        _, _, num_nodes_eq_avg = explore_substree(root)
        return num_nodes_eq_avg

        
