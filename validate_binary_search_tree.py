"""
Problem statement: 
----------------------------------------------------
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

E.g., 
1. root = [2,1,3] (Elements mentioned in BFS (or Level Order) traversal form, where root is 2, followed by left child 1 and right child 3. Expected O/P - True
2. root = [5,1,4,null,null,3,6]. Expected output - False
3. [120,70,140,50,100,130,160,20,55,75,110,119,135,150,200]. Expected output - False

Solution - 
-----------------------------------------------------
Note that many internal left child of right subtrees should be > the ancestors of its parent, while being < its parent.
Similarly, the right child of a parent in left sub tree should be < the ancestors of its parent. 
Overall, every child node will have a max_val or a min_val constraint or both. 

In the below solution, max_val holds the max limit for a right child in left sub tree, 
while min_val holds the min limit for a left child in a right sub tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def _check_bst_validity(parent, min_val=None, max_val=None) -> bool:
            if parent.left:
                if parent.left.val >= parent.val:
                    return False
                elif min_val:
                    if parent.left.val <= min_val:
                        return False

                # validate left subtree
                _is_valid = _check_bst_validity(parent.left, 
                                             max_val=parent.val, 
                                             min_val=min_val )
                if not _is_valid:
                    return False           
                
            if parent.right:
                if parent.right.val <= parent.val:
                    return False
                if max_val:
                    if parent.right.val >= max_val:
                        return False
                        
                # validate right sub tree
                _is_valid = _check_bst_validity(parent.right,
                                            max_val=max_val, 
                                            min_val=parent.val)
                     
                if not _is_valid:
                    return False
            
            return True
        
        is_valid = _check_bst_validity(root, None, None)
        return is_valid
