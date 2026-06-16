# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        maxVal=-101
        result=0
        def dfs(node,currMax):
            if not node:
                return 0
            if node.val>=currMax:
                result=1
            else:
                result =0
            newMax=max(currMax,node.val)
            return result + dfs(node.left, newMax) + dfs(node.right, newMax)
        return dfs(root,maxVal)
