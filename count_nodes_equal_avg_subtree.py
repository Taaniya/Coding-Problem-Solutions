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
            Explores a node and return num nodes and the weighted sum in its subtree by post-order traversal, a variant of DFS.
            Also returns no. of nodes having value equal to avg of the values of all nodes
            in its subtree.
            All leaf nodes will have value equal to avg of all node values in the subtree.


            Time complexity - O(n) , where n is the total no. of nodes in the tree, since every node is visited only once/
            Space complexity - O(h) for a balanced tree - best case, where h is the height of the tree. 
                           In worst case, for a skewed tree, height may also be as many as the total 
                           no. of nodes in the tree.
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

##############################################################################################################################
# Alternative implementation with different TreeNode structure to hold all info rather than returning the calculation by each 
# recursive call
##############################################################################################################################
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.subtree_size = 1          # no. of nodes in subtree including root
        self.total_subtree_val = 0     # Total value of all nodes in this subtree including root
        self.num_node_eq_avg_val = 0   # no. of nodes in subtree whose value equals the avg of values of all nodes in its subtree


class Solution:
    def average_of_subtree(self, root: TreeNode) -> int:
        def explore_subtree(root: TreeNode) -> None:
            """
            Explores a node and computes num nodes and the weighted sum in its subtree by post-order traversal, a variant
            of DFS. This calculation is done bottom up using DFS from leaf node to the root of the tree.
            
            Updates intermediate info for each node for its subtree including - no. of nodes having value equal to
            avg of the values of all nodes in a subtree, weighted sum of value of all nodes in subtree & subtree size.
            All leaf nodes will have value equal to avg of all node values in the subtree.
            The root of tree will hold above information for the entire tree.
            
            Time complexity - O(n) , where n is the total no. of nodes in the tree, since every node is visited only once/
            Space complexity - O(h) for a balanced tree - best case, where h is the height of the tree.
                           In worst case, for a skewed tree, height may also be as many as the total
                           no. of nodes in the tree.
            """
            num_left_nodes = 0
            num_right_nodes = 0
            weighted_sum = 0
            num_nodes_equal_avg_val = 0

            if root.left:
                explore_subtree(root.left)
                num_left_nodes = root.left.subtree_size
                left_weighted_sum = root.left.total_subtree_val
                num_n_eq_avg = root.left.num_node_eq_avg_val
                weighted_sum += left_weighted_sum
                if num_n_eq_avg:
                    num_nodes_equal_avg_val += num_n_eq_avg

            if root.right:
                explore_subtree(root.right)
                num_right_nodes = root.right.subtree_size
                right_weighted_sum = root.right.total_subtree_val
                num_n_eq_avg = root.right.num_node_eq_avg_val
                weighted_sum += right_weighted_sum
                if num_n_eq_avg:
                    num_nodes_equal_avg_val += num_n_eq_avg

            weighted_sum += root.val
            sub_tree_size = num_right_nodes + num_left_nodes + 1
            avg = int(math.floor(weighted_sum / sub_tree_size))

            if avg == root.val:
                num_nodes_equal_avg_val += 1

            # update root
            root.total_subtree_val = weighted_sum
            root.subtree_size = sub_tree_size
            root.num_node_eq_avg_val = num_nodes_equal_avg_val

            return

        explore_subtree(root)
        return root.num_node_eq_avg_val


if __name__ == "__main__":
     node0 = TreeNode(0)
     node1 = TreeNode(1)
     node6 = TreeNode(6)
     node8 = TreeNode(8, left=node0, right=node1)
     node5 = TreeNode(5, right=node6)
     root = TreeNode(4, left=node8, right=node5)
     sol = Solution().averageOfSubtree(root)
     print(sol)     # 5
