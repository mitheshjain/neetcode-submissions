# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        def count(node,maxVal):
            if not node:
                return 0
            if node.val>=maxVal:
                res=1
            else:
                res=0
            maxVal=max(node.val,maxVal)
            res += count(node.left,maxVal)

            res +=count(node.right,maxVal)
            return res
        res=count(root,root.val)
        return res
