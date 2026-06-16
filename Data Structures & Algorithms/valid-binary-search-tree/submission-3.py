# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.prev = float('-inf')
        
        def in_order(node):
            if not node:
                return True
            
            # Check left subtree
            if not in_order(node.left):
                return False
            
            # Check current node value against previous
            if node.val <= self.prev:
                return False
            self.prev = node.val
            
            # Check right subtree
            return in_order(node.right)
            
        return in_order(root)
