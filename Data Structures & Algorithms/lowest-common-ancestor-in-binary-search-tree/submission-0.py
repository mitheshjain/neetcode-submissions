# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            # If both p and q are greater than root, LCA is in right
            if p.val > root.val and q.val > root.val:
                root = root.right
            # If both p and q are less than root, LCA is in left
            elif p.val < root.val and q.val < root.val:
                root = root.left
            # We found the split point!
            else:
                return root
                    
                    