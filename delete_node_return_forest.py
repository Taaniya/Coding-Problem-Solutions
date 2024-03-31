"""
Problem statement: 
Given the root of a binary tree, each node in the tree has a distinct value.
After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
Return the roots of the trees in the remaining forest. You may return the result in any order.

Approach:
Traverse the tree in level order (BFS) and while visiting each node check whether current node & its nodes
have to be deleted.
Time complexity - O(V+E)
"""

from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        roots = []                        # list of root nodes of disjoint trees
        queue = deque()
        queue.append((root, False))       # initialize with Parent flag false for root
        _delete_list = set(to_delete)     

        # Traverse with BFS
        while(queue):
            node, has_parent  = queue.popleft()      
            if (node.val not in _delete_list) and (not has_parent):
                roots.append(node)

            if node.val in _delete_list:
                child_has_parent = False
            else:
                child_has_parent = True

            if node.left:
                queue.append((node.left, child_has_parent))
                if node.left.val in _delete_list:
                    node.left = None
        
            if node.right:
                queue.append((node.right, child_has_parent))
                if node.right.val in _delete_list:
                    node.right = None
            
        return roots
